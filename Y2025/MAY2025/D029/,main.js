/**
 * @param {number[][]} edges1
 * @param {number[][]} edges2
 * @return {number[]}
 */
var maxTargetNodes = function (edges1, edges2) {
  const dfs = (ui, upi, adj, markings, oddEvenCount) => {
    oddEvenCount[0] += (markings[ui] === 0); // increment even count 
    oddEvenCount[1] += (markings[ui] === 1); // increment odd count 

    for (let vi of adj[ui]) {
      if (vi == upi) continue;
      markings[vi] = markings[ui] === 0 ? 1 : 0;
      dfs(vi, ui, adj, markings, oddEvenCount);
    }
  };

  const getAdjacencyList = (edges, V) => {
    const adj = Array.from({ length: V }, () => new Array());
    for (let [u, v] of edges) {
      adj[u].push(v);
      adj[v].push(u);
    }
    return adj;
  };

  // number of nodes in tree 1 and tree 2 
  const N = edges1.length + 1;
  const M = edges2.length + 1;

  // build adjacency list 
  const adj1 = getAdjacencyList(edges1, N);
  const adj2 = getAdjacencyList(edges2, M);

  // marking nodes odd (1) or even (0) in tree 1 
  const tree1 = new Array(N).fill(-1);
  const tree1EvenOddCount = [0, 0];
  tree1[0] = 0;

  // dfs call for tree 1 
  dfs(0, -1, adj1, tree1, tree1EvenOddCount);

  // marking nodes odd (1) or even (0) in tree 2 
  const tree2 = new Array(M).fill(-1);
  const tree2EvenOddCount = [0, 0];
  tree2[0] = 0;

  // dfs call for tree 2 
  dfs(0, -1, adj2, tree2, tree2EvenOddCount);

  // build answer 
  const answer = new Array(N).fill(0);
  const maxi = Math.max(...tree2EvenOddCount);
  for (let i = 0; i < N; i++) {
    let mark = tree1[i];
    answer[i] = maxi + (mark === 0 ? tree1EvenOddCount[0] : tree1EvenOddCount[1]);
  }

  return answer;

  // Complexity analysis 
  // Time : O(4N + 3M) 
  // Space : O(3N + 3M) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3373. Maximize the Number of Target Nodes After Connecting Trees II - https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/description/?envType=daily-question&envId=2025-05-29 

  console.log(maxTargetNodes([[0, 1], [0, 2], [2, 3], [2, 4]], [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]));
  console.log(maxTargetNodes([[0, 1], [0, 2], [0, 3], [0, 4]], [[0, 1], [1, 2], [2, 3]]));
};

/*
class Node{
    constructor(data){
        this.data = data;
        this.left = null;
        this.right = null;
    }
} */

/**
 * @param {Node} root
 * @return {number}
 */

class Problem2 {
  sumOfLongRootToLeafPath(root) {
    // code here

    let [msum] = this.dfs(root);

    return msum;

    // Complexity analysis 
    // Time: O(N) 
    // Space: O(N) 
  }

  dfs(root) {
    if (!root) return [0, 0];

    let [leftsum, leftlevel] = this.dfs(root.left);
    let [rightsum, rightlevel] = this.dfs(root.right);

    let out = [0, 0];

    if (leftlevel === rightlevel) {
      out = [Math.max(leftsum, rightsum) + root.data, leftlevel + 1];
    } else if (leftlevel > rightlevel) {
      out = [leftsum + root.data, leftlevel + 1];
    } else {
      out = [rightsum + root.data, rightlevel + 1];
    }

    return out;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Sum of nodes on the longest path - https://www.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1 

  const root = {
    data: 4,
    left: {
      data: 2,
      left: {
        data: 7,
        left: null,
        right: null,
      },
      right: {
        data: 1,
        left: {
          data: 6,
          left: null,
          right: null,
        },
        right: null,
      },
    },
    right: {
      data: 5,
      left: {
        data: 2,
        left: null,
        right: null,
      },
      right: {
        data: 3,
        left: null,
        right: null,
      },
    },
  };
  console.log(new Problem2().sumOfLongRootToLeafPath(root));
};


(() => {
  // Day 29 of May 2025

  p1();

  p2();
})();
