/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function (nums) {
  // Observation 1 : maximum possible bitwise AND of an array,
  // is the maximum number present in the array
  // as the maximum number present in the array ensures that
  // the most significant bit is set
  // minimum possible output can be 1, in case there is only one largest element
  // maximum answer can be size of subarray in which all elements are equal to largest element
  // HINT : from here problem becomes,
  // Find the longest subarray containing only element K,
  // K is the largest element in given array

  const N = nums.length;

  const maxAND = Math.max(...nums);
  let length = 1;

  // find subarray with continious element "maxAND"
  for (let l = 0, r = 0; r < N; ) {
    // this starting cant give maximum and value of subarray
    if (nums[r] !== maxAND) {
      r++;
      continue;
    }

    // move left pointer - left pointer is start of subarray
    l = r;
    // move right pointer - right pointer is end of subarray
    while (r < N && nums[l] === nums[r]) r++;

    // calculate length of subarray and update longest subarray length
    length = Math.max(length, r - l);
  }

  return length;

  // Complexity analysis
  // Time : O(2N)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2419. Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/?envType=daily-question&envId=2025-07-30

  console.log(longestSubarray([1, 2, 3, 3, 2, 2]));
  console.log(longestSubarray([1, 2, 3, 4]));
  console.log(longestSubarray([1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]));
  console.log(longestSubarray([1, 2, 2, 2, 1, 1, 6, 1, 2, 2, 2, 2, 2, 2, 2]));
};

class Solution2 {
  cntSubarrays(arr, k) {
    // code here
    // arr[] = [10, 2, -2, -20, 10], k = -10
    // prefixSum = [0, 10, 12, 10, -10, 0] replace with int variable and optimise with map for count
    // needToRemove = [INV, 20, 22, 20, 0, 10]
    // count = [0, 0, 0, 0, 1, 2]
    // total = 3

    const N = arr.length;

    let count = 0;
    let prefixSum = 0;
    const prefixSumCount = new Map();
    prefixSumCount.set(0, 1);

    for (let i = 0; i < N; i++) {
      prefixSum += arr[i];
      let needToRemove = prefixSum - k;
      count += prefixSumCount.get(needToRemove) || 0;
      prefixSumCount.set(prefixSum, (prefixSumCount.get(prefixSum) || 0) + 1);
    }

    return count;

    // Complexity analysis
    // Time : O(N)
    // Space : O(N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Subarrays with sum K - https://www.geeksforgeeks.org/problems/subarrays-with-sum-k/1

  const s2 = new Solution2();
  console.log(s2.cntSubarrays([10, 2, -2, -20, 10], -10));
  console.log(s2.cntSubarrays([9, 4, 20, 3, 10, 5], 33));
  console.log(s2.cntSubarrays([1, 3, 5], 0));
};

(() => {
  // Day 30 of July 2025

  p1();

  p2();
})();
