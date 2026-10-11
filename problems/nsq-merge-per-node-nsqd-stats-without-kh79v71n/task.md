Stats reported for a particular node, e.g. the per-node e2e latencies should probably be that and not stats on top of whatever channel(s) that first node happened to return. And then maybe have an all-nodes version which would represent the total stats for a cluster?

Combining percentile data, the minimum value should probably be the minimum rather than the current behaviour where it is calculated from the maximums. Percentile data should be consistently ordered. They should probably be in the same order for individual nodes and nsqd (I prefer highest quantile first).

The order of the nodes should probably be consisten across different calls. Should get a not found response for a topic, channel or node once all the nodes that could have it have responded but error for nodes that couldn't be reached. A lookupd that doesn't know about a topic has still answered, so probably a not found. Any topic, channel or node response that's missing some nodes should probably list them in failed_nodes.

The order of clients in channels should probably be consisten. More generally, if I get stats twice and nothing changed, the whole response should probably be the same, not just the client order.
