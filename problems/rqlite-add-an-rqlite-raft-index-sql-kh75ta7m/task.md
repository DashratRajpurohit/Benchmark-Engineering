rqlite can report the Raft index of a write through the `raft_index` query parameter, but the data itself has no way to record it. Add a SQL function, `rqlite_raft_index()`, that takes no arguments and returns an integer.

While a write is applied, the function returns the index of the Raft log entry that carries the request. Every statement in the request, including those in a transaction, and anything those statements set off, such as a trigger body, sees that same value. It is the value `raft_index` reports for that request. A value stored by a write must be identical on every node, and must be reproduced exactly when log entries are replayed during node recovery. One node's indexes must never appear on another, even when several nodes run in the same process.

The function must also work in reads. A strong read sees the index of the log entry that carries the read. A read at any other consistency level sees the index of the latest log entry its node has applied.

It must be usable through `/db/execute`, `/db/query` and `/db/request`.