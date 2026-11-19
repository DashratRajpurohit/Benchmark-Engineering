# Four approved AfterQuery tasks

[AfterQuery overview](README.md) · [Complete task catalogue](task-catalog.md)

All four statuses below were **Approved** in the live author dashboard on **November 19, 2026**. Descriptions are portfolio summaries, not copies of private task prompts or grading specifications.

## one-file-build — reproducible standalone Python delivery

**Problem:** A command-line application needed a distributable single-file build while retaining its established invocation behavior.

**Engineering work:** Package application code into a self-contained Python zipapp; preserve CLI and module entry points; make output reproducible despite incidental filesystem metadata; handle supported runtime requirements and exclude build debris.

**What the evaluation exercises:** Build reproducibility, packaging boundaries, backward compatibility, and useful failure behavior.

**Outcome:** Approved. This task demonstrates build and toolchain engineering beyond a successful local invocation.

## yard-writes-one-commit — atomic batch operations

**Problem:** Inventory operations involving multiple writes needed consistent transaction boundaries and reliable behavior when part of a batch failed.

**Engineering work:** Coordinate batch updates around one commit, preserve established CLI behavior, and account for rollback, retry behavior, and filesystem output alongside database state.

**What the evaluation exercises:** Transaction design, error recovery, data integrity, state management, and compatibility with existing workflows.

**Outcome:** Approved. This task demonstrates reasoning across database effects and user-visible output rather than isolated function behavior.

## one-seat-per-week — reservation consistency

**Problem:** A company should not obtain conflicting reservations for the same weekly advertising slot, including under overlapping or concurrent requests.

**Engineering work:** Enforce the reservation invariant across multiweek booking, cancellation, ownership, hold expiry, and independent advertising categories.

**What the evaluation exercises:** Concurrency, atomicity, authorization boundaries, and compatibility with existing booking rules.

**Outcome:** Approved. This task demonstrates translating a product rule into a reliable state transition.

## submitted-links-web-only — safe URL handling

**Problem:** User-provided links needed consistent web-only validation, including data already stored before validation was strengthened.

**Engineering work:** Validate HTTP(S) URLs and hosts at input boundaries, preserve valid submitted values, and prevent unsafe legacy links from becoming active links or published unsafe output.

**What the evaluation exercises:** Input validation, security, backward compatibility, and consistent behavior across data ingestion and presentation.

**Outcome:** Approved. This task demonstrates following a security requirement through the full data lifecycle.

## Shared authoring contribution

Across these tasks, my work combines repository investigation, implementation, behavioral test design, calibration patches, and validation iteration. Approval is the verified platform outcome; it does not imply that a patch was merged into an upstream repository.
