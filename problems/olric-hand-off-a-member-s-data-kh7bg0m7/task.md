Calling Shutdown on an Olric member loses the data that member owns. Once it stops, the keys stored on it can no longer be read from the cluster, because nothing moves its partitions to the other members first.

Make Shutdown leave the cluster gracefully. Before the member stops, it has to hand the primary copies it owns over to the members that take over its partitions, and Shutdown may return without an error only after all of them have been handed over. If no other member is left in the cluster, there is nobody to hand them to, and Shutdown stops the member as it does today. Backup copies that the member keeps for other members when ReplicaCount is above 1 are not part of this.

If the context passed to Shutdown ends before all primary copies have been handed over, Shutdown returns an error and the member keeps running in the cluster with the keys it has not handed over yet, so no key is lost and Shutdown can be called again later.

The cluster has to keep working normally while a member leaves. A key must stay readable through the other members at every moment of the hand-off, and a change made to a key during it, for example with Incr, must still be there afterwards. Several members can also leave at the same time, even all of them at once, and none of these Shutdown calls may hang or fail because of the others.
