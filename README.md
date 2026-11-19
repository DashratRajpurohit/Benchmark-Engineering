# AI Evaluation & Benchmark Engineering Portfolio

**Dashrat Singh Rajpurohit** · Software-agent evaluation · RL task engineering · Long-horizon coding benchmarks

I build repository-based coding tasks and review the evidence used to evaluate software agents. My work connects real engineering problems with clear specifications, reference implementations, behavioral tests, reproducible environments, and careful analysis of agent attempts.

This portfolio brings together my **AfterQuery Gold Maintainer** and **Shipd Quest Olympus** work. My contribution is task engineering and evaluation; the results below describe authored tasks and reviews, not model training runs or upstream merged pull requests.

## At a glance

| Work | Result | Evidence date |
|---|---|---|
| AfterQuery maintainer review | **87 completed reviews** | Live dashboard checked November 19, 2026 |
| AfterQuery task authoring | **4 approved tasks** across Python and TypeScript | Live dashboard checked November 19, 2026 |
| Shipd Quest Olympus | **5 accepted Go tasks** | Repository's October 24, 2026 status snapshot |
| Engineering coverage | Concurrency, transactions, compatibility, security, packaging, distributed systems, and query behavior | Project case studies below |

The two platforms use different status labels. Shipd's separate “approved (finalizing)” entry is not included in its five accepted tasks. Completed reviews are not the same as approvals.

## Explore the work

| Portfolio area | What you will find |
|---|---|
| [AfterQuery Gold Maintainer](projects/afterquery/README.md) | Project overview, authoring responsibilities, and review experience |
| [Four approved task case studies](projects/afterquery/approved-tasks.md) | Problems, engineering work, outcomes, and demonstrated skills |
| [AfterQuery task catalogue](projects/afterquery/task-catalog.md) | Approved work, failed submissions, and local development |
| [87 reviews: methods and judgment](projects/afterquery/review-experience.md) | How I assess correctness, grading fairness, trajectories, and evidence |
| [Shipd Quest Olympus](projects/shipd-olympus/README.md) | Accepted work and a dated catalogue of earlier challenge development |
| [Benchmark design and long-horizon evaluation](methodology/benchmark-design.md) | My workflow from repository investigation to evaluation audit |
| [Skills and evidence](SKILLS.md) | Engineering capabilities mapped to concrete work |

## Selected work

- **Reliable Python delivery:** a standalone CLI build with reproducible packaging and compatible entry points.
- **Atomic inventory operations:** batch writes that commit together and recover cleanly from failure.
- **Concurrent reservations:** enforce a weekly uniqueness rule without breaking multiweek booking behavior.
- **Safe submitted links:** validate web URLs at input boundaries and handle existing unsafe data.
- **Go systems correctness:** cache accounting, message lifecycle safety, query result typing, and search indexing integrity.

## Evidence and maintenance

AfterQuery counts and the eight live task statuses were checked in the authenticated author dashboard on November 19, 2026. Shipd statuses are explicitly dated historical records. Detailed private review records are not reproduced in these portfolio pages.

New documentation contains summaries rather than hidden tests, reference patches, raw trajectories, or other authors' task material. **This documentation update does not remove pre-existing artifacts or their Git history from the repository.**

The legacy `tools/sync.sh` / `tools/build.py` workflow rebuilds the old archive and overwrites this README; it is not a refresh command for this portfolio. Maintain these pages using reviewed summaries and update evidence dates when counts change.

[GitHub profile](https://github.com/DashratRajpurohit)
