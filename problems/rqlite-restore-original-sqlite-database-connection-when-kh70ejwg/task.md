SwappableDB.Swap hot-swaps the SQLite file backing a database connection. If the replacement database at the given path fails to open, the caller is left with a SwappableDB that has no working database at all.

Fix Swap so a failed open leaves the original database intact and usable. Only discard the original database's files once the replacement has actually opened successfully, and clean up any files used to make the recovery possible. Swap should still report the failure that caused the fallback.

This needs to hold for both the main database file and its WAL and SHM files, and for whatever driver and foreign-key/WAL settings the original database was opened with.
