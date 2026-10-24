# Shipd Olympus portfolio (private)

Every challenge I have authored for Shipd's Quest Olympus (Datacurve), pulled from the platform with the `olympus` CLI. **Private: `test.patch` and `solution.patch` are the hidden grader and must never be published.**

Refresh: `tools/sync.sh` (downloads every problem into `.raw/`, rebuilds `problems/` and this README).

| Status | Date | Challenge | Repo | Lang | Quality | Runs |
|---|---|---|---|---|---|---|
| accepted | 2026-10-13 | [ShouldUpdate rejection and Del races corrupt cost accounting and double-fire OnExit](problems/ristretto-shouldupdate-rejection-and-del-races-corrupt-kh73wyvb/) | dgraph-io/ristretto | go | 2.67 | Orion 1/4 (80K) |
| accepted | 2026-10-12 | [Merge per-node nsqd stats without corrupting each node's own entry](problems/nsq-merge-per-node-nsqd-stats-without-kh79v71n/) | nsqio/nsq | go | 2.33 | Orion 1/6 (93K) |
| accepted | 2026-10-02 | [Reject deferred publish/requeue on an exiting nsqd channel](problems/nsq-reject-deferred-publish-requeue-on-an-kh73twmg/) | nsqio/nsq | go | 2.67 | 2/10 (old pool) |
| accepted | 2026-09-25 | [Report the actual type of every returned value with a vtypes query option](problems/rqlite-report-the-actual-type-of-every-kh70aw6y/) | rqlite/rqlite | go | 2.67 | 2/10 (old pool) |
| accepted | 2026-09-07 | [zoekt-index and zoekt-git-index: shared repository names silently lose data across positional inputs](problems/zoekt-zoekt-index-and-zoekt-git-index-kh74mg7a/) | sourcegraph/zoekt | go | 2.67 | 2/10 (old pool) |
| approved (finalizing) | 2026-10-22 | [nsqlookupd keeps dead ephemeral entries and trusts malformed input](problems/nsq-nsqlookupd-keeps-dead-ephemeral-entries-and-kh7d3ses/) | nsqio/nsq | go | 2.67 | Nova 0/4 (463K), Orion 1/6 (62K), Vega 0/4 (109K) |
| draft | 2026-10-24 | [Make M3 Query's two PromQL engines agree on time modifiers](problems/m3-make-m3-query-s-two-promql-kh7et34f/) | m3db/m3 | go | 2.33 | Nova 0/4 (1606K), Orion 0/4 (145K), Vega 0/8 (324K) |
| draft | 2026-10-23 | [Hand off a member's data when it leaves the cluster](problems/olric-hand-off-a-member-s-data-kh7bg0m7/) | olric-data/olric | go |  | 2/2 (old pool) |
| draft | 2026-10-23 | [Count documents in range facets and show readable values in number and date term facets](problems/bleve-count-documents-in-range-facets-and-kh75xq28/) | blevesearch/bleve | go |  | Nova 0/1 (1180K), Orion 1/1 (119K) |
| draft | 2026-10-19 | [Cache ignores MaxCost when the limit is lowered or a stored entry grows](problems/ristretto-cache-ignores-maxcost-when-the-limit-kh77xja1/) | dgraph-io/ristretto | go |  | Nova 0/1 (774K), Orion 4/4 (103K) |
| draft | 2026-10-17 | [Deduplicator drops redelivered messages when the handler fails](problems/watermill-deduplicator-drops-redelivered-messages-when-the-kh78qm7a/) | threedotslabs/watermill | go |  |  |
| draft | 2026-10-13 | [Bulk delete and mark-read break on large mailboxes](problems/mailpit-bulk-delete-and-mark-read-break-kh7827r4/) | axllent/mailpit | go |  | 2/2 (old pool) |
| archived | 2026-10-21 | Untitled problem draft (empty, `kh70yws8`) | m3db/m3 | go |  |  |
| archived | 2026-10-21 | [Support MySQL partial revokes](problems/tidb-support-mysql-partial-revokes-kh7cvwtt/) | pingcap/tidb | go |  |  |
| archived | 2026-10-19 | [Add the MySQL XML functions ExtractValue() and UpdateXML()](problems/tidb-add-the-mysql-xml-functions-extractvalue-kh7fg6br/) | pingcap/tidb | go |  |  |
| archived | 2026-10-17 | [Follow the MQTT spec for expiry, aliases, wills and takeover](problems/gmqtt-follow-the-mqtt-spec-for-expiry-kh7aybze/) | drmagice/gmqtt | go |  |  |
| archived | 2026-10-05 | [Reload cluster watchers and evict cached clients when a request-supplied kubeconfig changes](problems/headlamp-reload-cluster-watchers-and-evict-cached-kh71yy7a/) | kubernetes-sigs/headlamp | go | 1.33 | Orion 0/2 (181K) |
| archived | 2026-09-24 | Untitled problem draft (empty, `kh7fv354`) | dgraph-io/badger | go |  |  |
| archived | 2026-09-21 | [Preview the next index run](problems/sift-preview-the-next-index-run-kh70tx1v/) | kenxpx/sift | go |  |  |
| archived | 2026-09-21 | [Reduce allocations in gojq entries builtins](problems/gojq-reduce-allocations-in-gojq-entries-builtins-kh7b93by/) | itchyny/gojq | go |  |  |
| archived | 2026-09-20 | [Add an rqlite_raft_index() SQL function that exposes the Raft log index of a write](problems/rqlite-add-an-rqlite-raft-index-sql-kh75ta7m/) | rqlite/rqlite | go |  |  |
| archived | 2026-09-20 | [CDC FIFO queue's HasNext blocks forever when called after the queue is closed](problems/rqlite-cdc-fifo-queue-s-hasnext-blocks-kh7essb7/) | rqlite/rqlite | go |  |  |
| archived | 2026-09-19 | [gitindex silently indexes a fraction of the repository when part of the object store is unreadable](problems/zoekt-gitindex-silently-indexes-a-fraction-of-kh7c7stn/) | sourcegraph/zoekt | go |  |  |
| archived | 2026-09-19 | [gitindex silently indexes a fraction of the repository when part of the object store is unreadable](problems/zoekt-gitindex-silently-indexes-a-fraction-of-kh708xbe/) | sourcegraph/zoekt | go |  |  |
| archived | 2026-09-19 | [Restore original SQLite database connection when replacement open fails during hot-swap](problems/rqlite-restore-original-sqlite-database-connection-when-kh70ejwg/) | rqlite/rqlite | go |  |  |
| archived | 2026-09-19 | [Add per-table column filtering to CDC event payloads](problems/rqlite-add-per-table-column-filtering-to-kh79v59g/) | rqlite/rqlite | go | 2.00 | 2/20 (old pool) |
| archived | 2026-09-18 | [Named custom log levels for zerolog](problems/zerolog-named-custom-log-levels-for-zerolog-kh72jsmz/) | rs/zerolog | go |  | 3/3 (old pool) |
| archived | 2026-09-02 | Untitled problem draft (empty, `kh73gw8h`) |  |  |  |  |
| archived | 2026-09-02 | [Context-aware custom functions for gojq](problems/gojq-context-aware-custom-functions-for-gojq-kh78k7g1/) | itchyny/gojq | go |  |  |
| archived | 2026-09-01 | Untitled problem draft (empty, `kh70west`) |  |  |  |  |

Date column: acceptance/approval date for accepted work, otherwise the last draft edit.
