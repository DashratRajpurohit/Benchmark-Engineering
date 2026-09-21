Add a read-only preview of what the next index run would do to a corpus. For each file the corpus scans to, report whether it would be added, modified relative to what was indexed before, or skipped because its contents are not text. For something the extraction cache remembers that the corpus no longer scans to, report it as removed. The preview must not write anything to disk or publish anything.

The preview must agree with what the real index run would do, including for a file the corpus already held before the corpus's own configuration changed. The result must be deterministic: the same corpus and the same prior state always give the same list in the same order.

Do not depend on the package that wires the command-line operations together, because that package will depend on the new one.

Interface:
- A new package internal/plan exporting type Change struct { Rel string; Kind string }, where Kind is exactly one of "added", "modified", "removed", "skipped: binary", and func Compute(cfg core.Config) ([]Change, error).
- A new method func (a App) Plan(root string) ([]plan.Change, error) on the existing App type, following the pattern of its other methods: resolve the corpus configuration from root, delegate, and wrap any error with the operation name.
