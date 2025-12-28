/**
 * @param {number[]} nums
 * @return {number[]}
 */
var largestDivisibleSubset = function (nums) {
  // Modified version of LIS (longest increasing subseq)

  // copy input
  const arr = [...nums];
  const N = arr.length;

  // sort copied input
  arr.sort((a, b) => a - b);

  const dp = new Array(N).fill(1);
  const path = new Array(N).fill(0);

  for (let index = 0; index < N; index++) {
    path[index] = index;

    for (let prev = 0; prev < index; prev++) {
      if (arr[index] % arr[prev] == 0 && dp[index] < dp[prev] + 1) {
        dp[index] = dp[prev] + 1;
        path[index] = prev;
      }
    }
  }

  let lsubset = [];

  let l_index = dp.reduce((acc, _, i) => (dp[i] > dp[acc] ? i : acc), 0);

  lsubset.push(arr[l_index]);

  while (path[l_index] != l_index) {
    l_index = path[l_index];
    lsubset.push(arr[l_index]);
  }

  return lsubset;

  // Complexity analysis
  // Time : O(N*LOG(N)) + O(N*N) + O(N) + O(N)
  // Space : O(3N) for memory
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 368. Largest Divisible Subset - https://leetcode.com/problems/largest-divisible-subset/description/?envType=daily-question&envId=2025-04-06

  console.log(largestDivisibleSubset([1, 2, 3]));
  console.log(largestDivisibleSubset([1, 2, 4, 8]));
  console.log(largestDivisibleSubset([8, 4, 2, 1]));
  console.log(largestDivisibleSubset([1]));
  console.log(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]));
  console.log(largestDivisibleSubset([1462280116]));
};

// User function Template for javascript
/**
 * @param {number} V
 * @param {number[][]} adj
 * @returns {number[]}
 */
class Problem2 {
  topoSort(V, edges) {
    // code here
    // return this.topoSort_dfs(V, edges);
    return this.topoSort_bfs(V, edges);
  }

  topoSort_dfs(V, edges) {
    const output = [];
    const visited = new Array(V).fill(false);
    const adj = Array.from({ length: V }, () => new Array());
    for (let [u, v] of edges) {
      adj[u].push(v);
    }

    const _dfs = (u) => {
      visited[u] = true;

      for (let v of adj[u]) {
        if (visited[v]) continue;
        _dfs(v);
      }

      output.push(u);
    };

    for (let v = 0; v < V; v++) {
      if (visited[v]) continue;
      _dfs(v);
    }

    output.reverse();
    return output;

    // Complexity analysis
    // Time : O(E) + O(V + E)
    // Space : O(V) + O(V+E) + O(V)
  }

  topoSort_bfs(V, edges) {
    const output = [];
    const indegree = new Array(V).fill(0);
    const adj = Array.from({ length: V }, () => new Array());

    for (let [u, v] of edges) {
      adj[u].push(v);
      indegree[v]++;
    }

    const queue = [];
    for (let v = 0; v < V; v++) {
      if (indegree[v] == 0) {
        queue.push(v);
      }
    }

    while (queue.length) {
      const u = queue.shift();

      output.push(u);

      for (let v of adj[u]) {
        if (--indegree[v] == 0) {
          queue.push(v);
        }
      }
    }

    return output;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Topological sort - https://www.geeksforgeeks.org/problems/topological-sort/1

  console.log(
    new Problem2().topoSort(4, [
      [3, 0],
      [1, 0],
      [2, 0],
    ]),
  );
  console.log(
    new Problem2().topoSort(6, [
      [1, 3],
      [2, 3],
      [4, 1],
      [4, 0],
      [5, 0],
      [5, 2],
    ]),
  );
};

(() => {
  // Day 6 of April 2025

  p1();

  p2();
})();
