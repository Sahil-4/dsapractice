/**
 * @param {number} n
 * @param {number} k
 * @param {number} maxPts
 * @return {number}
 */
var new21Game = function (n, k, maxPts) {
  const P = new Array(n + 1).fill(0.0);
  P[0] = 1.0;

  let probSum = k === 0 ? 0.0 : 1.0;

  for (let i = 1; i <= n; i++) {
    P[i] = probSum / maxPts;
    if (i < k) probSum += P[i];
    if (i - maxPts >= 0 && i - maxPts < k) probSum -= P[i - maxPts];
  }

  let tprobability = 0.0;
  for (let i = k; i <= n; i++) tprobability += P[i];
  return tprobability;

  // Complexity analysis
  // Time : O(2N)
  // Space : O(N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 837. New 21 Game - https://leetcode.com/problems/new-21-game/description/?envType=daily-question&envId=2025-08-17

  console.log(new21Game(10, 1, 10));
  console.log(new21Game(6, 1, 10));
  console.log(new21Game(21, 17, 10));
  console.log(new21Game(0, 0, 1));
};

/**
 * @param {number[]} arr
 * @param {number} x
 * @return {void}
 */
class Solution2 {
  rearrange(arr, x) {
    // code here
    const comparator = (a, b) => Math.abs(a - x) - Math.abs(b - x);
    arr.sort(comparator);
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Sort by Absolute Difference - https://www.geeksforgeeks.org/problems/sort-by-absolute-difference-1587115621/1

  const s2 = new Solution2();
  console.log(s2.rearrange([10, 5, 3, 9, 2], 7));
  console.log(s2.rearrange([1, 2, 3, 4, 5], 6));
};

(() => {
  // Day 17 of August 2025

  p1();

  p2();
})();
