/**
 * @param {number[]} arr
 * @return {number}
 */
var findLucky = function (arr) {
  const frequency = new Map();

  for (let i = 0; i < arr.length; i++) {
    const e = arr[i];
    const ef = (frequency.get(e) || 0) + 1;
    frequency.set(e, ef);
  }

  let lucky = -1;

  for (const [e, ef] of frequency) {
    if (e === ef) lucky = Math.max(lucky, e);
  }

  return lucky;

  // Complexity analysis
  // Time : O(2N)
  // Space : O(N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1394. Find Lucky Integer in an Array - https://leetcode.com/problems/find-lucky-integer-in-an-array/description/?envType=daily-question&envId=2025-07-05

  console.log(findLucky([2, 2, 3, 4])); // 2
  console.log(findLucky([1, 2, 2, 3, 3, 4])); // -1
  console.log(findLucky([2, 2, 2, 3, 3])); // 3
};

/**
 * @param {number[]} arr
 * @returns {number[]}
 */
class Solution2 {
  maxSum(arr) {
    // code here
    // arr = [4, 3, 5, 1]
    // sarr = [4, 3], score = (3 + 4) = 7
    // sarr = [4, 3, 5], score = (3 + 4) = 7
    // sarr = [4, 3, 5, 1], score = (1 + 3) = 4
    // sarr = [3, 5], score = (3 + 5) = 8
    // sarr = [3, 5, 1], score = (1 + 3) = 4
    // sarr = [5, 1], score = (1 + 5) = 6

    // this is maximum adjacent elements sum

    const fn = ([pe, out], ce) => [ce, Math.max(out, pe + ce)];
    return arr.reduce(fn, [0, 0])[1];

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Max Score from Subarray Mins - https://www.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/1

  const s2 = new Solution2();
  console.log(s2.maxSum([4, 3, 5, 1])); // 8
  console.log(s2.maxSum([1, 2, 3, 4])); // 6
  console.log(s2.maxSum([1, 2, 3, 4, 5])); // 8
};

(() => {
  // Day 5 of July 2025

  p1();

  p2();
})();
