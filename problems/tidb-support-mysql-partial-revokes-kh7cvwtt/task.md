TiDB follows MySQL 8.4 for accounts and privileges, but it has no support for MySQL's partial revokes.

MySQL has a global system variable partial_revokes that is OFF by default. While it is OFF, revoking a privilege on a single schema (REVOKE ... ON db.*) from an account that holds the privilege only globally (ON *.*) is an error. When it is ON, the same REVOKE succeeds: the account loses that privilege on that schema only, keeps it on every other schema, and keeps its other privileges on that schema. SHOW GRANTS then lists the restriction as a REVOKE line after the account's GRANT line, for example REVOKE INSERT ON `world`.* FROM `u1`@`%`.

Add the partial_revokes variable and this behaviour.
