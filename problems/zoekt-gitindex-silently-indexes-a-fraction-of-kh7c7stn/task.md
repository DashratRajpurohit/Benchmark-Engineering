When gitindex walks a commit's tree to decide which files to index, a subtree it cannot read is treated the same as reaching the end of the tree.

A repository cloned with `git clone --shared` has most of its objects living only in the origin repository's object store, reached through git's alternates mechanism. Indexing such a clone should index every file reachable from the requested branch, including files that only exist via an alternate object store.

Fix the walk so it cannot mistake an unreadable part of the tree for having finished normally: if any part of the tree cannot be read for a reason other than genuinely reaching the end, indexing should fail with an error. Separately, make sure a `git clone --shared` style repository indexes completely and correctly.
