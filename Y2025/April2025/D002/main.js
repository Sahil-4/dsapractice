/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTripletValue = function (nums) {
  const N = nums.length;

  const brute = () => {
    let maxValue = 0;

    for (let i = 0; i < N; i++) {
      for (let j = i + 1; j < N; j++) {
        for (let k = j + 1; k < N; k++) {
          const value = (nums[i] - nums[j]) * nums[k];
          maxValue = Math.max(maxValue, value);
        }
      }
    }

    return maxValue;

    // Complexity analysis
    // Time : O(N^3)
    // Space : O(1)
  };

  const optimal = () => {
    // (nums[i] - nums[j]) * nums[k];
    // --->
    // (highestPossibleDifference) * maxElementj
    // --->
    // (maxElement_i - minElement)

    let maxValue = 0;
    let maxElement = 0;
    let maxDiff = 0;

    for (let i = 0; i < N; i++) {
      maxValue = Math.max(maxValue, maxDiff * nums[i]);
      maxDiff = Math.max(maxDiff, maxElement - nums[i]);
      maxElement = Math.max(maxElement, nums[i]);
    }

    return maxValue;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  };

  // return brute();
  return optimal();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2873. Maximum Value of an Ordered Triplet I - https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/?envType=daily-question&envId=2025-04-02

  console.log(maximumTripletValue([12, 6, 1, 2, 7]));
  console.log(maximumTripletValue([1, 10, 3, 4, 19]));
  console.log(maximumTripletValue([1, 2, 3]));
  console.log(maximumTripletValue([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]));
  console.log(maximumTripletValue([71, 31, 95, 44, 52, 81, 48, 7, 39, 34, 70, 86, 90, 7, 99, 67, 30, 82, 58, 70]));
};

// User function Template for javascript
class Problem2 {
  // Function to return Breadth First Search Traversal of the given graph.
  bfs(adj) {
    // Code here
    const N = adj.length;

    const start = 0;
    const output = [];

    const visited = new Array(N).fill(false);
    const queue = new Array();

    queue.push(0);
    visited[0] = true;

    while (queue.length) {
      const node = queue.shift();

      output.push(node);

      for (let ng of adj[node]) {
        if (visited[ng]) continue;
        queue.push(ng);
        visited[ng] = true;
      }
    }

    return output;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks BFS of graph - https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

  console.log(new Problem2().bfs([[2, 3, 1], [0], [0, 4], [0], [2]]));
  console.log(new Problem2().bfs([[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]));
};

(() => {
  // Day 2 of April 2025

  p1();

  p2();
})();
