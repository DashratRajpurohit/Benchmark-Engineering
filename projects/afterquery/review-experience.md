# Maintainer review experience — 87 completed reviews

[AfterQuery overview](README.md)

The authenticated dashboard showed **87 completed reviews on November 19, 2026**. This page summarizes the work without publishing other authors' prompts, implementations, hidden tests, identities, or private review decisions.

## What I examine

| Review area | Practical work |
|---|---|
| Prompt and implementation alignment | Trace requested behavior into code and verify that blockers follow from the stated contract |
| Behavioral grading | Check that tests distinguish correct behavior from plausible incomplete fixes without requiring one implementation |
| Regression safety | Separate new fail-to-pass behavior from existing pass-to-pass compatibility checks |
| Reference calibration | Compare golden and alternative solutions with the unchanged baseline and negative controls |
| Agent trajectories | Read attempts to identify the actual failure path, assumptions, and interactions with the environment |
| Environment integrity | Investigate dependency, resource, command, and timeout failures before attributing them to model capability |
| Adversarial robustness | Consider whether superficial changes can earn reward while missing requested behavior |
| Final judgment | Relate current evidence to the live checklist and mergeability, rather than treating a badge as the full review |

## Engineering themes

The review work spans API compatibility, optional schema fields, state transitions, database access patterns, migration behavior, concurrency, security boundaries, resource usage, and build environments. It develops the ability to switch between a product-level requirement and the specific behavior the verifier observes.

For performance-related work, I examine whether the measurement captures the intended resource or operation and whether unrelated environment variability can change the verdict. For compatibility work, I check the existing contract before treating preserved behavior as a defect.

## Evidence discipline

A historical failed attempt and a current passing revision are different pieces of evidence. I attach findings to the relevant version or run and explain the concrete impact and correction.

Missing logs and conflicting reports remain unresolved until investigated. They do not establish a pass or a failure on their own. This distinction matters when benchmark decisions affect both task authors and the agents being evaluated.

The aggregate count is verified; this portfolio does not invent 87 public case studies or claim that every reviewed task was approved.
