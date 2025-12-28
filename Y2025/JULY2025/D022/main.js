/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumUniqueSubarray = function (nums) {
  // "Maximum sum of contiguous subarray without repeating elements"

  let msum = 0;

  const set = new Set();

  for (let l = 0, r = 0, sum = 0; r < nums.length; r++) {
    while (set.has(nums[r])) {
      set.delete(nums[l]);
      sum -= nums[l];
      l++;
    }

    set.add(nums[r]);
    sum += nums[r];

    msum = Math.max(msum, sum);
  }

  return msum;

  // Complexity analysis
  // Time : O(2N), considering TC : O(1) for set operations
  // Space : O(N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1695. Maximum Erasure Value - https://leetcode.com/problems/maximum-erasure-value/description/?envType=daily-question&envId=2025-07-22

  console.log(maximumUniqueSubarray([4, 2, 4, 5, 6]));
  console.log(maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]));
  console.log(maximumUniqueSubarray([5, 2, 1, 3, 4, 4]));
};

/**
 * @param {number[]} arr
 * @returns {number}
 */
class Solution2 {
  missingNumber(arr) {
    // code here
    // Naive solution :
    // sort the given array
    // traverse sorted array using two pointers
    // one pointer for index on arr, another pointer to point to positive integer
    // if (arr[p1] <= 0) p1++ // we have to skip all negatives
    // else if arr[p1] != p2 return p2;
    // else p2++;
    // This will take O(N * Log(N)) time and O(N) space
    // Optimal solution :
    // init an array of length N + 1, named positives initially all value false
    // traverse given array arr,
    // for e of arr
    // if (e <= 0) continue;
    // else positives[e] = true;
    // at last traverse positives from i = 1 till i = N
    // if positives[i] === false return i

    const N = arr.length + 1;
    const positives = new Array(N).fill(false);

    for (const e of arr) {
      if (e <= 0) continue;
      positives[e] = true;
    }

    for (let mi = 1; mi < N; mi++) {
      if (!positives[mi]) return mi;
    }

    return N;

    // Complexity analysis
    // Time : O(2N)
    // Space : O(N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Smallest Positive Missing - https://www.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1

  const s2 = new Solution2();
  console.log(s2.missingNumber([2, -3, 4, 1, 1, 7]));
  console.log(s2.missingNumber([5, 3, 2, 5, 1]));
  console.log(s2.missingNumber([-8, 0, -1, -4, -3]));
  console.log(s2.missingNumber([0, 1, -1, -2, 5]));
  console.log(s2.missingNumber([0]));
  console.log(s2.missingNumber([0, 5]));
};

(() => {
  // Day 22 of July 2025

  p1();

  p2();
})();
