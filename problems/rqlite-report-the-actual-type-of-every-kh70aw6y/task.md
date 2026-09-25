SQLite lets any column hold any value, so declared column types cannot tell a client what it got.

Add an optional `vtypes` parameter to `/db/query`, `/db/execute` and `/db/request`. Results with rows carry a `vtypes` key beside the values, one entry per row: an array holding one of `null`, `integer`, `real`, `text` or `blob` per column, or with `associative` an object keyed by column.

The reported type is how SQLite stores the value, whatever the column declares: a blob in a TEXT column reports `blob`. DATE, DATETIME and TIMESTAMP columns are the exception, reporting `text` for any value, though NULL reports `null`.

Without it, responses must not change. A result with no rows carries none. It works at every consistency level and through a follower. Such a blob must reach the client with its exact bytes, as must text computed from one, such as by CAST, which existing text handling mangles.

Change data capture events always carry them too, under the same rules, as `before_types` and `after_types` keyed by column.

Give the rqlite shell a `.vtypes on|off` setting, off by default. While on it requests the types and shows each value followed by its type in parentheses, in all modes.