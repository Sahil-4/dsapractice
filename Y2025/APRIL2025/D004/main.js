//  * Definition for a binary tree node.
function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

const solve1 = () => {
  const getDeepestLeaves = (root) => {
    let deepestLeaves = [];
    let queue = [];
    queue.push(root);

    while (queue.length > 0) {
      const N = queue.length;
      deepestLeaves = [];

      for (let i = 0; i < N; i++) {
        const node = queue.shift();

        deepestLeaves.push(node);

        if (node.left) {
          isLeaf = false;
          queue.push(node.left);
        }
        if (node.right) {
          isLeaf = false;
          queue.push(node.right);
        }
      }

      if (isLeaf) break;
    }

    return deepestLeaves;

    // Complexity analysis (worst case only for finding deepest leaves)
    // Time : O(N)
    // Space : O(W) queue memory
  };

  const getPath = (root, leaf, path) => {
    if (!root) return false;

    if (root.val == leaf.val) {
      path.push(root);
      return true;
    }

    let left = getPath(root.left, leaf, path);
    let right = getPath(root.right, leaf, path);

    if (left || right) {
      path.push(root);
      return true;
    }

    return false;

    // Complexity analysis (worst case only for finding the path)
    // Time : O(N)
    // Space : O(N) stack
  };

  if (!root.left && !root.right) return root;

  // Approach -
  // Find the set of Deepest nodes
  // Then find the LCA of these nodes
  // finally return the LCA

  // for finding deepest nodes
  // use level order traversal
  // then for each of deepest nodes
  // find their paths
  // then using P pointers find the last common node in their paths

  const deepestLeaves = getDeepestLeaves(root);
  const deepestLeavesPath = deepestLeaves.map((leaf) => {
    const path = [];
    getPath(root, leaf, path);
    path.reverse();
    return path;
  });

  // holds lca node
  let LCA = null;

  // number of leaf nodes
  const L = deepestLeavesPath.length;
  // length shortest path
  let mplen = deepestLeavesPath.reduce((acc, path) => Math.min(acc, path.length), deepestLeavesPath[0].length);

  // compare ith node of path and if they are same for all make it LCA
  for (let i = 0; i < mplen; i++) {
    let check = true;
    let node = deepestLeavesPath[0][i]; // ith node in path (from root)

    for (let j = 0; j < L; j++) {
      check = check && node.val == deepestLeavesPath[j][i].val;
    }

    if (!check) break;

    LCA = node;
  }

  return LCA;

  // Complexity analysis (worst case only for finding deepest leaves)
  // Time : O(LN*H) for finding LCA at the end
  // Space : O(2LN) for storing deepest nodes & path
};

const solve2 = (root) => {
  // single dfs (compute height + gauranteed node lca)

  const _dfs = (node) => {
    if (!node) return [0, null]; // [height, lca]

    let left = _dfs(node.left);
    let right = _dfs(node.right);

    if (left[0] == right[0]) {
      return [left[0] + 1, node];
    } else if (left[0] > right[0]) {
      return [left[0] + 1, left[1]];
    } else {
      return [right[0] + 1, right[1]];
    }
  };

  return _dfs(root)[1];

  // To understand this approach
  // - check multiple binary trees
  // - check their deepest leaf nodes
  // - now understand this,
  // - if nodeX has same height on left and right,
  // - nodeX will have same number of deepest leaf nodes
  // - and for those leaf nodes nodeX will be the LCA
  // But what if height is not same on left, and right
  // - then deepest node will be on the side where height is more
  // - and LCA also
};

/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var lcaDeepestLeaves = function (root) {
  // return solve1(root);
  return solve2(root);
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1123. Lowest Common Ancestor of Deepest Leaves - https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/?envType=daily-question&envId=2025-04-04

  const root = TreeNode(1);
  console.log(lcaDeepestLeaves(root));
};

// User function Template for javascript
/**
 * @param {number} V
 * @param {number[][]} adj
 * @returns {boolean}
 */
class Problem2 {
  isCycle(V, edges) {
    // Code here

    // create adjacency list
    const adj = Array.from({ length: V }, () => new Array());
    for (let [u, v] of edges) {
      // undirected edge
      adj[u].push(v); // u -> v
      adj[v].push(u); // v -> u
    }

    let result = false; // final output
    const visited = new Array(V).fill(false); // mark visited vertices

    for (let i = 0; i < V; i++) {
      // if visited - no need to perform traversal
      if (visited[i]) continue;

      // perform traversal
      result = this._dfs(adj, i, -1, visited);

      // if output is true break
      if (result) break;
    }

    // finally return output
    return result;
  }

  _dfs(adj, curr, parent, visited) {
    // mark curr as visited
    visited[curr] = true;

    // explore ajacent nodes
    for (let v of adj[curr]) {
      if (v == parent) {
        // skip v -> u, take only u -> v
        continue;
      } else if (visited[v]) {
        // if we came here again - its a cycle
        return true;
      } else {
        // explore this vertex
        if (this._dfs(adj, v, curr, visited)) {
          // return true if traversing this node return cycle
          return true;
        }
      }
    }

    // no cycle found till now
    return false;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Undirected Graph Cycle - https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

  console.log(
    new Problem2().isCycle([
      [0, 1],
      [0, 2],
      [1, 2],
      [2, 3],
    ]),
  );
  console.log(
    new Problem2().isCycle([
      [0, 1],
      [1, 2],
      [2, 3],
      [3, 0],
    ]),
  );
  console.log(
    new Problem2().isCycle([
      [0, 1],
      [1, 2],
      [2, 3],
    ]),
  );
};

(() => {
  // Day 4 of April 2025

  p1();

  p2();
})();
