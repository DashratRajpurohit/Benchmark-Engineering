#!/usr/bin/env python3
"""Turn the raw `olympus` downloads in .raw/ into problems/<slug>/ folders and README.md.

Usage: python3 tools/build.py            (run tools/sync.sh first to refresh .raw/)
"""
import csv
import datetime
import json
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / ".raw"
OUT = ROOT / "problems"
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
FILES = ["task.md", "Dockerfile", "test.patch", "solution.patch", "metadata.json", "Makefile"]


def ts(ms):
    return datetime.datetime.fromtimestamp(ms / 1000, IST) if ms else None


def day(ms):
    t = ts(ms)
    return t.strftime("%Y-%m-%d") if t else ""


def clean_title(title):
    return re.sub(r"https?://\S+", "", title or "").strip() or "Untitled problem draft"


def slug(p):
    repo = (p.get("repoKey") or (p.get("latestVersion") or {}).get("githubRepoUrl") or "").rstrip("/")
    repo = repo.split("/")[-1].lower() if repo else "no-repo"
    words = re.findall(r"[a-z0-9]+", clean_title(p["title"]).lower())[:6]
    return f"{repo}-{'-'.join(words)}-{p['_id'][:8]}"


def repo_name(p):
    url = (p.get("latestVersion") or {}).get("githubRepoUrl") or ""
    m = re.search(r"github\.com/([^/]+/[^/]+?)(?:\.git)?/?$", url)
    return m.group(1) if m else (p.get("repoKey") or "")


def stage(p):
    s = p["status"]
    if s == "accepted":
        return "accepted"
    if s in ("finalizing_review", "pending_review", "in_review"):
        return "in review" if s != "finalizing_review" else "approved (finalizing)"
    if p.get("archived"):
        return "archived"
    return "draft"


def key_date(p):
    """Acceptance date for accepted/approved work, else the last draft edit, else creation."""
    if p["status"] in ("accepted", "finalizing_review"):
        return p.get("managerVerdictAt") or p.get("currentStatusEnteredAt") or p["_creationTime"]
    return p.get("lastDraftEditedAt") or p["_creationTime"]


def is_empty(raw_dir):
    return not any((raw_dir / f).exists() and (raw_dir / f).stat().st_size for f in ("test.patch", "solution.patch", "Dockerfile")) \
        and not ((raw_dir / "task.md").exists() and (raw_dir / "task.md").stat().st_size)


def write_results(p, dest):
    res = dest / "results"
    res.mkdir(exist_ok=True)
    runs = (p.get("runs") or {})
    crit = dict(runs.get("criteria") or {})
    crit["readiness"] = ((p.get("checks") or {}).get("readiness") or {}).get("criteria")
    (res / "criteria.json").write_text(json.dumps(crit, indent=1) + "\n")
    (res / "aggregate-stats.json").write_text(json.dumps(p.get("aggStats") or {}, indent=1) + "\n")
    reviews = []
    for r in p.get("reviews") or []:
        r = {k: v for k, v in r.items() if k not in ("reviewerImageUrl",)}
        r["submittedAtIST"] = ts(r.get("submittedAt")).isoformat() if r.get("submittedAt") else None
        reviews.append(r)
    (res / "reviews.json").write_text(json.dumps(reviews, indent=1) + "\n")
    cols = ["label", "agent", "agentType", "verdict", "stale", "reEvalRound", "fault", "filesModified",
            "solutionLOC", "agentMessages", "sequenceLength", "executionTimeSeconds", "environmentBlocker", "createdIST", "id"]
    with open(res / "runs.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in sorted(runs.get("agentRuns") or [], key=lambda r: r.get("createdAt") or 0):
            o = r.get("output") or {}
            eb = o.get("environmentBlocker")
            w.writerow([r.get("label"), r.get("taskAgentCodename"), r.get("taskAgentType"), r.get("verdict"),
                        r.get("stale"), r.get("reEvalRound") or "", r.get("fault"), o.get("filesModified"),
                        o.get("solutionLOC"), o.get("agentMessages"), o.get("sequenceLength") or o.get("trajectoryLength"),
                        o.get("executionTimeSeconds"), (eb or {}).get("detected") if isinstance(eb, dict) else eb,
                        ts(r.get("createdAt")).isoformat() if r.get("createdAt") else "", r.get("id")])


def pools_line(p):
    pools = ((p.get("runs") or {}).get("criteria") or {}).get("olympusV2Pools") or {}
    parts = []
    for pool in [pools.get("nova")] + list(pools.get("strong") or []):
        if pool and pool.get("measured"):
            seq = pool.get("avgSequenceLength")
            parts.append(f"{pool['codename']} {pool['passes']}/{pool['measured']}" + (f" ({seq / 1000:.0f}K)" if seq else ""))
    if parts:
        return ", ".join(parts)
    agg = p.get("aggStats") or {}
    return f"{agg.get('passedRuns', 0)}/{agg.get('totalRuns', 0)} (old pool)" if agg.get("totalRuns") else ""


def card(p, sl):
    lv = p.get("latestVersion") or {}
    pay = p.get("payoutBreakdown") or {}
    rows = [
        ("Problem id", f"`{p['_id']}`"),
        ("Status", stage(p) + f" (platform: `{p['status']}`)"),
        ("Repository", f"{lv.get('githubRepoUrl') or p.get('repoKey') or '-'} @ `{lv.get('githubCommitHash') or '-'}`"),
        ("Language / category", f"{p.get('language') or '-'} / {p.get('category') or '-'}"),
        ("Live version", str(lv.get("version", "-"))),
        ("Created", day(p["_creationTime"])),
        ("Last draft edit", day(p.get("lastDraftEditedAt"))),
        ("Submitted", day(p.get("submittedAt"))),
        ("Accepted / approved", day(p.get("managerVerdictAt")) if p.get("managerVerdictAt") else
            (day(p.get("currentStatusEnteredAt")) if p["status"] == "finalizing_review" else "-")),
        ("Quality", f"{p['overallQuality']:.2f}/3 (score {p.get('qualityScore')})" if p.get("overallQuality") else "-"),
        ("Payout", f"{pay['amount']} tokens" if pay.get("amount") else "-"),
        ("Runs", pools_line(p) or "-"),
    ]
    out = [f"# {clean_title(p['title'])}", "", "| | |", "|---|---|"]
    out += [f"| {k} | {v} |" for k, v in rows]
    out += ["", "Files: `task.md` (agent-facing description), `test.patch` (hidden tests + test.sh), "
            "`solution.patch` (reference), `Dockerfile`, `metadata.json`. Platform records in `results/`.", ""]
    return "\n".join(out)


def main():
    problems = []
    for vf in sorted(RAW.glob("*.view.json")):
        p = json.loads(vf.read_text())
        raw_dir = RAW / p["_id"]
        p["_empty"] = is_empty(raw_dir)
        problems.append(p)
    problems.sort(key=key_date)

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    index = []
    for p in problems:
        sl = slug(p)
        if not p["_empty"]:
            dest = OUT / sl
            dest.mkdir()
            for f in FILES:
                src = RAW / p["_id"] / f
                if src.exists():
                    shutil.copy2(src, dest / f)
            write_results(p, dest)
            (dest / "README.md").write_text(card(p, sl))
        index.append((p, sl))

    order = {"accepted": 0, "approved (finalizing)": 1, "in review": 2, "draft": 3, "archived": 4}
    lines = [
        "# Shipd Olympus portfolio (private)",
        "",
        "Every challenge I have authored for Shipd's Quest Olympus (Datacurve), pulled from the platform with the "
        "`olympus` CLI. **Private: `test.patch` and `solution.patch` are the hidden grader and must never be published.**",
        "",
        "Refresh: `tools/sync.sh` (downloads every problem into `.raw/`, rebuilds `problems/` and this README).",
        "",
        "| Status | Date | Challenge | Repo | Lang | Quality | Runs |",
        "|---|---|---|---|---|---|---|",
    ]
    for p, sl in sorted(index, key=lambda x: (order[stage(x[0])], -key_date(x[0]))):
        title = clean_title(p["title"])
        name = f"[{title}](problems/{sl}/)" if not p["_empty"] else f"{title} (empty, `{p['_id'][:8]}`)"
        q = f"{p['overallQuality']:.2f}" if p.get("overallQuality") else ""
        lines.append(f"| {stage(p)} | {day(key_date(p))} | {name} | {repo_name(p)} | "
                     f"{p.get('language') or ''} | {q} | {pools_line(p)} |")
    lines += ["", "Date column: acceptance/approval date for accepted work, otherwise the last draft edit.", ""]
    (ROOT / "README.md").write_text("\n".join(lines))

    # plan for the dated per-challenge commits: slug<TAB>ISO date<TAB>stage<TAB>title
    with open(ROOT / ".raw" / "commit-plan.tsv", "w") as fh:
        for p, sl in index:
            if not p["_empty"]:
                fh.write(f"{sl}\t{ts(key_date(p)).isoformat()}\t{stage(p)}\t{clean_title(p['title'])}\n")


if __name__ == "__main__":
    main()
