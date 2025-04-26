var __countSubarrays__ = function (nums, minK, maxK) {
  const N = nums.length;
  let count = 0;

  for (let l = 0; l < N; l++) {
    let _min_val = nums[l];
    let _max_val = nums[l];

    for (let r = l; r < N; r++) {
      _min_val = Math.min(_min_val, nums[r]);
      _max_val = Math.max(_max_val, nums[r]);

      if (_min_val === minK && _max_val === maxK) count++;
      if (_min_val < minK || _max_val > maxK) break;
    }
  }

  return count;

  // Complexity analysis 
  // Time : O(N * N) 
  // Space : O(1) 
};

/**
 * @param {number[]} nums
 * @param {number} minK
 * @param {number} maxK
 * @return {number}
 */
var countSubarrays = function (nums, minK, maxK) {
  const N = nums.length;

  let count = 0;

  let min_i = -1;
  let max_i = -1;
  let start_i = 0;

  for (i = 0; i < N; i++) {
    let num = nums[i];

    if (num < minK || num > maxK) {
      min_i = -1;
      max_i = -1;
      start_i = i + 1;
      continue;
    }

    if (num === minK) min_i = i;
    if (num === maxK) max_i = i;

    count += Math.max(0, Math.min(min_i, max_i) - start_i + 1);
  }

  return count;

  // Complexity analysis 
  // Time : O(N) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2444. Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/?envType=daily-question&envId=2025-04-26 

  console.log(countSubarrays([1, 3, 5, 2, 7, 5], 1, 5));
  console.log(countSubarrays([1, 1, 1, 1], 1, 1));
  console.log(countSubarrays([3, 3, 1, 3, 3], 3, 3));
  console.log(countSubarrays([1, 3, 3, 1, 3, 3], 3, 3));
};

// User function Template for javascript

/**
 * @param {Node} root
 * @returns {boolean}
 */

class Node {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}

class Problem2 {
  isHeap(root) {
    // code here

    // Approach - 
    // use level order traversal 
    // return false 
    // - if node level i node value, is not greater then level i+1 node value 
    // - if after encountering null nodes, we encounter non null nodes in further nodes 

    const queue = [];
    let ends = false;

    queue.push(root);

    while (queue.length) {
      const { data, left, right } = queue.shift();

      if (left) {
        if (ends || data <= left.data) return false;
        queue.push(left);
      } else {
        ends = true;
      }

      if (right) {
        if (ends || data <= right.data) return false;
        queue.push(right);
      } else {
        ends = true;
      }
    }

    return true; // valid max heap 

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(W) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Is Binary Tree Heap - https://www.geeksforgeeks.org/problems/is-binary-tree-heap/1 

  const root = {
    data: 100,
    left: {
      data: 50,
      left: null,
      right: null,
    },
    right: null,
  };
  console.log(new Problem2().isHeap(root));
};

(() => {
  // Day 26 of April 2025

  p1();

  p2();
})();