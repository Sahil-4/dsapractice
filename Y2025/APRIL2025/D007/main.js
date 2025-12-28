/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function (nums) {
  const N = nums.length;
  const t_sum = nums.reduce((acc, e) => acc + e, 0);

  if (t_sum & 1) return false;

  const _target = Math.floor(t_sum / 2);

  let next = new Array(t_sum + 1).fill(false);

  // base case
  next[0] = true;

  for (let i = N - 1; i >= 0; i--) {
    let curr = new Array(t_sum + 1).fill(false);

    for (let _sum = 1; _sum <= _target; _sum++) {
      let not_pick = next[_sum];
      let pick = _sum >= nums[i] ? next[_sum - nums[i]] : false;

      curr[_sum] = pick || not_pick;
    }

    next = curr;
  }

  return next[_target];

  // Complexity analysis
  // Time : O(N) + O(N * _target)
  // Space : O(2*t_sum)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 416. Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/description/?envType=daily-question&envId=2025-04-07

  console.log(canPartition([1, 2, 3, 5]));
  console.log(canPartition([100, 100, 100, 100, 100, 100, 100, 100, 100, 100]));
};

// User function Template for javascript

/**
 * @param {number} V
 * @param {number[][]} edges
 * @returns {boolean}
 */
class Problem2 {
  // Function to detect cycle in a directed graph.
  isCyclic(V, edges) {
    // code here

    const adj = Array.from({ length: V }, () => new Array());
    const indegree = new Array(V).fill(0);

    for (let [u, v] of edges) {
      adj[u].push(v);
      indegree[v]++;
    }

    let count = 0;
    const queue = new Array();

    for (let i = 0; i < V; i++) {
      if (indegree[i] == 0) {
        count++;
        queue.push(i);
      }
    }

    while (queue.length) {
      const u = queue.shift();

      for (let v of adj[u]) {
        if (--indegree[v] == 0) {
          count++;
          queue.push(v);
        }
      }
    }

    return count != V;

    // Complexity analysis
    // Time : O(E) + O(V) + O(V+E)
    // Space : O(V+E) + O(V)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Directed Graph Cycle - https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

  console.log(new Problem2().isCyclic(4, [[0, 1], [1, 2], [2, 3], [3, 3]]));
  console.log(new Problem2().isCyclic(3, [[0, 1], [1, 2]]));
};

(() => {
  // Day 7 of April 2025

  p1();

  p2();
})();
