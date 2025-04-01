/**
 * @param {number[][]} questions
 * @return {number}
 */
var mostPoints = function (questions) {
  const N = questions.length;

  const recursion = (index) => {
    if (index >= N) return 0;

    let not_pick = recursion(index + 1);
    let pick = recursion(index + questions[index][1] + 1) + questions[index][0];

    return Math.max(not_pick, pick);

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) stack space
  };

  const memoize = (index, memo) => {
    if (index >= N) return 0;

    if (memo[index] != -1) return memo[index];

    let not_pick = memoize(index + 1, memo);
    let pick = memoize(index + questions[index][1] + 1, memo) + questions[index][0];

    return (memo[index] = Math.max(not_pick, pick));

    // Complexity analysis
    // Time : O(2*N)
    // Space : O(N) stack space + O(N) memory
  };

  const tabulation = () => {
    const memo = new Array(N + 1).fill(0);

    for (let index = N - 1; index >= 0; index--) {
      let not_pick = memo[index + 1];
      let mindex = index + questions[index][1] + 1;
      let pick = (mindex <= N ? memo[mindex] : 0) + questions[index][0];

      memo[index] = Math.max(not_pick, pick);
    }

    return memo[0];

    // Complexity analysis
    // Time : O(N)
    // Space : O(N) memory
  };

  // return recursion(0);
  // return memoize(0, new Array(N).fill(-1));
  return tabulation();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2140. Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/description/?envType=daily-question&envId=2025-04-01

  console.log(mostPoints([[3,2],[4,3],[4,4],[2,5]]));
  console.log(mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]));
};

/**
 * @param {number[][]} adj
 * @returns {number[]}
 */
class Problem2 {
  // Function to return a list containing the DFS traversal of the graph.
  dfs(adj) {
    // code here
    const start = 0;

    const output = [];

    this._dfs(adj, start, new Set(), output);

    return output;
  }

  _dfs(adj, curr, visited, output) {
    output.push(curr); // add into output
    visited.add(curr); // mark it visited

    for (let neighbour of adj[curr]) {
      if (visited.has(neighbour)) continue;

      // explore neighbour is not visited
      this._dfs(adj, neighbour, visited, output);
    }

    // Complexity analysis
    // Time : O(V + 2E)
    // Space : O(V) stack space + O(V) visited set memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks DFS of Graph - https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

  console.log(new Problem2().dfs([[2, 3, 1], [0], [0, 4], [0], [2]]));
  console.log(new Problem2().dfs([[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]));
};

(() => {
  // Day 1 of April 2025
  // Day 91st of 2025

  p1();

  p2();
})();
