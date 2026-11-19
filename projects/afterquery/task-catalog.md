# AfterQuery task catalogue

[AfterQuery overview](README.md)

## Live dashboard snapshot — November 19, 2026

| Task | Area | Observed status |
|---|---|---|
| one-file-build | Python packaging and reproducible CLI delivery | Approved |
| yard-writes-one-commit | Transactional batch writes and failure recovery | Approved |
| one-seat-per-week | Concurrent weekly reservation consistency | Approved |
| submitted-links-web-only | URL validation and safe handling of legacy data | Approved |
| transactional-web-build | Build pipeline consistency | Failed |
| reproducible-release-bundle | Reproducible release packaging | Failed |
| merchant-scoped-user-cache | Cache scoping and isolation | Failed |
| job-alert-seen-once | Notification state and repeat handling | Failed |

“Failed” records the platform status at the evidence date. It is not an accepted result, even when parts of local verification passed.

## Additional local and historical work

| Task | Scope | Evidence and boundary |
|---|---|---|
| streaming-tape-query | Go streaming query refactor with compatibility, resource ownership, and error propagation | Local bundle and verification prepared November 18, 2026; no platform approval claimed |
| subscription-filter-regex-match | Subscription filtering and regular-expression matching | Historical rejection followed by local revision; no later approval verified |

This catalogue covers the named submissions and substantive local bundles identified in the available records. Empty or discarded exploratory drafts are not counted as completed tasks.

## Lessons carried into later work

Separate tests that should fail before the change from tests that preserve existing behavior. Passing compatibility tests on the unchanged repository is expected; describing them as newly fixed tests creates misleading evaluation evidence.

Budget verification commands against the actual overall time allowance. Measure reference, alternative, baseline, and negative-control behavior independently. A successful local check or dry run does not replace full platform validation or human approval.
