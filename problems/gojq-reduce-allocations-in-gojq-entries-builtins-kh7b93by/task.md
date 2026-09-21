Make the to_entries, from_entries and with_entries builtins substantially cheaper in memory allocations without changing anything observable.

As a guide, from_entries on a list of 100 entries should make under 110 allocations and to_entries on a 100-key object under 420, and with_entries should benefit from both.

Behaviour must stay exactly the same for every kind of input and every error: the same results in the same order and the same error messages. That includes arrays accepted by to_entries, objects accepted by from_entries, entries that spell their key or value as key, Key, name, Name, value or Value, entries whose key is null or false, and inputs that are not objects or arrays at all. Results must not share mutable state with the input.

Add regression tests for the new behaviour alongside the existing tests.
