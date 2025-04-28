/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countSubarrays = function (nums, k) {
  let count = 0;

  for (let l = 0, r = 0, sum = 0; r < nums.length; r++) {
    sum += nums[r];

    let score = ((sum) * (r - l + 1));

    while (score >= k) {
      sum -= nums[l];
      score = ((sum) * (r - l));
      l++;
    }

    count += (r - l + 1);
  }

  return count;

  // Complexity analysis 
  // Time : O(2N) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2302. Count Subarrays With Score Less Than K - https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description/?envType=daily-question&envId=2025-04-28 

  console.log(countSubarrays([2, 1, 4, 3, 5], 10));
  console.log(countSubarrays([1, 1, 1], 5));
  console.log(countSubarrays([1, 1, 1], 10));
};

// User function Template for javascript

/**
 * @param {Node} root
 * @returns {number}
 */

class Node {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}

class Problem2 {
  // Function to return the maximum sum of non-adjacent nodes.
  getMaxSum(root) {
    // your code here

    const memo = new Map();
    return this.dfs_solution(root, memo);
  }

  dfs_solution(root, memo) {
    if (!root) return 0;

    if (memo.has(root)) return memo.get(root);

    // do not select this node 
    let option_1 = 0 + (this.dfs_solution(root.left, memo) + this.dfs_solution(root.right, memo));

    // select this node 
    let option_2 = root.data;
    option_2 += (this.dfs_solution(root.left?.left, memo) + this.dfs_solution(root.left?.right, memo));
    option_2 += (this.dfs_solution(root.right?.left, memo) + this.dfs_solution(root.right?.right, memo));

    memo.set(root, Math.max(option_1, option_2));
    return memo.get(root);

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(H) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Maximum sum of Non-adjacent nodes - https://www.geeksforgeeks.org/problems/maximum-sum-of-non-adjacent-nodes/1 

  const root = {
    data: 8,
    left: {
      data: 4,
      left: null,
      right: null,
    },
    right: {
      data: 5,
      left: null,
      right: null,
    }
  };
  console.log(new Problem2().getMaxSum(root));
};

(() => {
  // Day 28 of April 2025

  p1();

  p2();
})();
