# Benchmark design and long-horizon evaluation

[Back to portfolio](../README.md)

My work focuses on repository-level software tasks where an agent must investigate unfamiliar code, make a coherent change, preserve existing behavior, and demonstrate correctness through tools and tests.

## From engineering problem to evaluation task

1. **Investigate the repository.** Reproduce the behavior, identify public interfaces and invariants, and understand the existing test and build environment.
2. **Define the behavioral contract.** Explain the intended outcome and relevant constraints without prescribing incidental implementation details.
3. **Build a reference implementation.** Keep the change scoped and verify compatibility and failure behavior.
4. **Design meaningful grading.** Exercise observable outcomes, edge cases, and plausible shortcuts; keep regression checks distinct from newly fixed behavior.
5. **Calibrate the verifier.** Test the unchanged baseline, reference solution, an alternative valid solution, and a plausible incorrect implementation.
6. **Run realistic verification.** Account for dependency setup, resource ownership, command timeouts, repeatability, and the execution environment.
7. **Audit agent attempts.** Inspect trajectories and failure evidence to distinguish engineering difficulty from ambiguous requirements or environment defects.
8. **Revise with evidence.** Recheck the affected contract and report the exact status reached: local verification, dry run, validation, or approval.

## Why long-horizon tasks need more than a final test result

A repository task can require coordinated changes across code, tests, configuration, and data handling. An agent may make a locally plausible edit that violates an invariant elsewhere, or lose an earlier constraint while pursuing a later failure.

I examine the sequence of investigation, implementation, debugging, and verification. Useful questions include whether the agent identified the real boundary, preserved previous requirements, and used test evidence to correct its approach.

Examples from my work include atomic operations spanning database and filesystem effects, reservation rules spanning concurrent requests, and build reproducibility across incidental environmental differences.

## Relation to reinforcement learning

Reliable task specifications and executable evaluators can supply useful correctness signals for software-agent evaluation and reinforcement-learning workflows. My documented role is engineering and reviewing those tasks and evaluation signals. This portfolio does not claim ownership of model training infrastructure or measured improvements in a trained model.

## What I aim to make reliable

| Property | Design approach |
|---|---|
| Correctness | Check observable behavior and relevant invariants |
| Fairness | Accept distinct valid implementations |
| Discrimination | Reject an unchanged baseline and meaningful incorrect controls where new behavior is required |
| Reproducibility | Control environmental assumptions and execution budgets |
| Compatibility | Preserve explicitly retained interfaces and existing behavior |
| Interpretability | Make failures actionable and connect them to the stated requirement |
