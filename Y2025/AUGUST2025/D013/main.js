/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function (n) {
  if (n <= 0) return false;

  const sol1 = () => {
    let value = 1;
    while (value < n) value *= 3;
    return value === n;

    // Complexity analysis
    // Time : O(qube_root(N))
    // Space : O(1)
  };

  const sol2 = () => {
    const maxPowerOfThree = 1162261467;
    return n > 0 && maxPowerOfThree % n == 0;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  };

  // return sol1();
  return sol2();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 326. Power of Three - https://leetcode.com/problems/power-of-three/description/?envType=daily-question&envId=2025-08-13

  console.log(isPowerOfThree(-3));
  console.log(isPowerOfThree(-1));
  console.log(isPowerOfThree(0));
  console.log(isPowerOfThree(1));
  console.log(isPowerOfThree(3));
  console.log(isPowerOfThree(15));
  console.log(isPowerOfThree(1054));
};

/**
 * @param {number[]} arr
 * @param {number} k
 * @returns {number}
 */

class Solution2 {
  minSoldiers(arr, k) {
    // code here
    // arr = [3, 5, 6, 7, 9, 10], k = 4
    // [3 % 4, 5 % 4, 6 % 4, 7 % 4, 9 % 4, 10 % 4]
    // [1, 3, 2, 1, 3, 2] => [1,1,2,2,3,3]
    // output = 4

    const fn = (val) => (val % k !== 0 ? k - (val % k) : 0);
    const need = arr.map(fn);
    need.sort((a, b) => a - b);

    let soldiers = 0;
    const NT = Math.abs(arr.length / 2);
    for (let i = 0; i < NT; i++) soldiers += need[i];

    return soldiers;

    // Complexity analysis
    // Time : O(N) + O(N * Log(N)) + O(N/2)
    // Space : O(N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Tywin's War Strategy - https://www.geeksforgeeks.org/problems/tywins-war-strategy0527/1

  const s2 = new Solution2();
  console.log(s2.minSoldiers([5, 6, 3, 2, 1], 2));
  console.log(s2.minSoldiers([3, 5, 6, 7, 9, 10], 4));
  console.log(s2.minSoldiers([1, 1, 1, 1, 1, 14, 14, 14, 14, 14], 5));
};

(() => {
  // Day 13 of August 2025

  p1();

  p2();
})();
