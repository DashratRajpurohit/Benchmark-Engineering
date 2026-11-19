# Shipd Quest Olympus

[Back to portfolio](../../README.md)

My Shipd Quest Olympus work develops repository-based coding challenges for evaluating software agents. It combines problem investigation, reference implementations, tests, environment preparation, and analysis of evaluation attempts.

The catalogue below preserves the **October 24, 2026 repository snapshot** in a concise form. It records **5 accepted tasks**, **1 approved task still finalizing**, **6 drafts**, and **18 archived entries**. Four archived entries were empty drafts, so the snapshot contains 26 substantive entries, including two separate attempts on one Zoekt topic. These are historical statuses, not a claim that all work remains in the same state today.

## Accepted work

| Project | Engineering problem | Skills demonstrated |
|---|---|---|
| Ristretto | Correct cache cost accounting and callback behavior around update rejection and deletion races | Concurrency, resource accounting, lifecycle invariants |
| NSQ | Combine per-node statistics without mutating the original node results | Data ownership, aggregation correctness, regression testing |
| NSQ | Handle deferred message operations safely during channel shutdown | Lifecycle management, error handling, messaging correctness |
| rqlite | Expose the actual types of returned query values | SQL result semantics, API compatibility, mixed-type data |
| Zoekt | Preserve indexed data when multiple inputs share a repository name | Indexing integrity, CLI behavior, regression diagnosis |

Acceptance dates in the snapshot range from September 7 to October 13, 2026. These are task-platform acceptances; they are not claims of upstream merged changes.

## Other authored work in the snapshot

| Status on October 24 | Project | Topic |
|---|---|---|
| Approved, finalizing | NSQ | Discovery cleanup and malformed-input handling |
| Draft | M3 | Time-modifier consistency across query engines |
| Draft | Olric | Data handoff when a cluster member leaves |
| Draft | Bleve | Range-facet counts and readable facet values |
| Draft | Ristretto | Enforcing a changed cache cost limit |
| Draft | Watermill | Deduplication behavior after handler failure |
| Draft | Mailpit | Bulk operations on large mailboxes |
| Archived | TiDB | Partial privilege revocation |
| Archived | TiDB | XML query functions |
| Archived | GMQTT | Message expiry, aliases, wills, and session takeover |
| Archived | Headlamp | Refreshing watchers and cached clients after configuration changes |
| Archived | Sift | Previewing indexing work |
| Archived | gojq | Allocation reductions in entry operations |
| Archived | rqlite | Exposing a write's Raft index |
| Archived | rqlite | Closed-queue behavior in change-data capture |
| Archived | Zoekt | Partial failures when reading Git objects — two separate attempts |
| Archived | rqlite | Recovering a database connection after replacement failure |
| Archived | rqlite | Filtering columns in change-data-capture events |
| Archived | Zerolog | Named custom log levels |
| Archived | gojq | Context-aware extension functions |
| Archived | Various | Four empty exploratory drafts, excluded from substantive work |

## Later development

Local work records after the snapshot include NSQ authentication-cache expiry, per-channel in-flight limits, administration notifications, Ripes instruction-set work, and further M3 and Olric iteration. These topics are development activity; no additional acceptance is claimed here without refreshed platform evidence.

## What this work shows

The accepted work concentrates on Go systems where seemingly small changes affect ownership, concurrency, storage, and lifecycle rules. Drafts and archived investigations also show the task-selection process: a useful benchmark must have a coherent contract, meaningful difficulty, and a fair verifier.

This summary omits hidden grading artifacts, raw evaluation traces, and private platform records. Existing archive files elsewhere in the repository are outside the scope of this documentation update.
