/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minSum = function (nums1, nums2) {
  const getSumAndZeroCount = ([sum, zeroes], e) => [sum + e, zeroes + (e == 0)];

  const [sum1, zero1] = nums1.reduce(getSumAndZeroCount, [0, 0]);
  const [sum2, zero2] = nums2.reduce(getSumAndZeroCount, [0, 0]);

  const boundSum1 = (sum1 + zero1);
  const boundSum2 = (sum2 + zero2);

  if (boundSum1 < boundSum2 && zero1 == 0) return -1;
  if (boundSum2 < boundSum1 && zero2 == 0) return -1;

  return Math.max(boundSum1, boundSum2);

  // Complexity analysis 
  // Time : O(N) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros - https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description/?envType=daily-question&envId=2025-05-10 

  console.log(minSum([3, 2, 0, 1, 0], [6, 5, 0]));
  console.log(minSum([2, 0, 2, 0], [1, 4]));
};

//Back-end complete function Template for javascript
class Problem2 {
  longestSubarray(arr, k) {
    // Code Here
    const N = arr.length;

    let llen = 0;
    let psum = 0;

    const prefixSumMap = new Map();

    prefixSumMap.set(0, -1);

    for (let i = 0; i < N; i++) {
      psum += (arr[i] > k) ? +1 : -1;

      if (psum > 0) {
        llen = i + 1;
      }

      if (prefixSumMap.has(psum - 1)) {
        llen = Math.max(llen, i - prefixSumMap.get(psum - 1));
      }

      if (!prefixSumMap.has(psum)) {
        prefixSumMap.set(psum, i);
      }
    }

    return llen;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Longest Subarray with Majority Greater than K - https://www.geeksforgeeks.org/problems/longest-subarray-with-majority-greater-than-k/1 

  console.log(new Problem2().longestSubarray("1 2 3 4 1".split(" "), 2));
  console.log(new Problem2().longestSubarray("1 2 3 2 1".split(" "), 5));
  console.log(new Problem2().longestSubarray("1 2 3 2 1".split(" "), 0));
  console.log(new Problem2().longestSubarray("11 60 26 7 44 30 18 29 10 72 3 4 49 77 23 21 20 34 20 99 21 70 9 74 41".split(" "), 35));
};


(() => {
  // Day 10 of May 2025

  p1();

  p2();
})();
