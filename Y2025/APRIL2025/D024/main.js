/**
 * @param {number[]} nums
 * @return {number}
 */
var countCompleteSubarrays = function (nums) {
  const N = nums.length;
  const t_unique = nums.reduce((acc, e) => acc.add(e) && acc, new Set()).size;

  let completeSubarraysCount = 0;

  const map = new Map();

  for (let l = 0, r = 0; r < N; r++) {
    if (!map.has(nums[r])) map.set(nums[r], 0);
    map.set(nums[r], map.get(nums[r]) + 1);

    while (map.keys().toArray().length === t_unique) {
      completeSubarraysCount += (N - r);

      map.set(nums[l], map.get(nums[l]) - 1);
      if (map.get(nums[l]) === 0) map.delete(nums[l]);

      l++;
    }
  }

  return completeSubarraysCount;

  // Complexity analysis 
  // Time : O(2N) 
  // Space : O(N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2799. Count Complete Subarrays in an Array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/?envType=daily-question&envId=2025-04-24 

  console.log(countCompleteSubarrays([1, 3, 1, 2, 2]));
  console.log(countCompleteSubarrays([5, 5, 5, 5]));
  console.log(countCompleteSubarrays([5]));
  console.log(countCompleteSubarrays([5, 5]));
  console.log(countCompleteSubarrays([5, 2]));
  console.log(countCompleteSubarrays([5, 2, 1]));
};

// User function Template for javascript
/**
 * @param {number[]} arr
 * @returns {number}
 */

class Problem2 {
  getSingle(arr) {
    // code here
    let ones = 0, twos = 0;

    for (let n of arr) {
      ones = (ones ^ n) & ~twos;
      twos = (twos ^ n) & ~ones;
    }

    return ones;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Unique Number III - https://www.geeksforgeeks.org/problems/find-element-occuring-once-when-all-other-are-present-thrice/1 

  console.log(new Problem2().getSingle([1, 10, 1, 1]));
  console.log(new Problem2().getSingle([3, 2, 1, 34, 34, 1, 2, 34, 2, 1]));
};

(() => {
  // Day 24 of April 2025

  p1();

  p2();
})();
