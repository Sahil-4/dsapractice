/**
 * @param {number} n
 * @param {number} x
 * @return {number}
 */
var numberOfWays = function (n, x) {
  // n = 10, x = 2
  // 1^2, 2^2, 3^2, 4^2
  // n = 4, x = 1
  // 1^1, 2^1, 3^1, 4^1

  const MODO = 1000000007;

  const powers = new Array();
  for (let i = 1; ; i++) {
    let power = Math.pow(i, x);
    powers.push(power);
    if (power > n) break;
  }

  const memoization = (num, i, memo) => {
    if (num === 0) return 1;
    if (powers[i - 1] > num) return 0;

    if (memo[num][i] !== -1) return memo[num][i];

    let skip = memoization(num - 0, i + 1, memo);
    let take = num >= powers[i - 1] ? memoization(num - powers[i - 1], i + 1, memo) : 0;

    memo[num][i] = (skip + take) % MODO;

    return memo[num][i];

    // Complexity analysis
    // Time : O(2 * Num * PN)
    // Space : O(Num * PN)
  };

  const tabulation = () => {
    const PN = powers.length;
    const memo = Array.from({ length: n + 1 }, () => new Array(PN + 1).fill(0));

    // base case
    for (let i = 0; i <= PN; i++) memo[0][i] = 1;

    for (let num = 1; num <= n; num++) {
      for (let i = PN - 1; i >= 1; i--) {
        let skip = memo[num][i + 1];
        let take = num >= powers[i - 1] ? memo[num - powers[i - 1]][i + 1] : 0;
        memo[num][i] = (skip + take) % MODO;
      }
    }

    return memo[n][1];

    // Complexity analysis
    // Time : O(Num * PN)
    // Space : O(Num * PN)
  };

  const space_optimised = () => {
    const PN = powers.length;
    let next = new Array(n + 1).fill(0);
    next[0] = 1;

    for (let i = PN - 1; i >= 1; i--) {
      let curr = new Array(n + 1).fill(0);
      curr[0] = 1;
      for (let num = 1; num <= n; num++) {
        let skip = next[num];
        let take = num >= powers[i - 1] ? next[num - powers[i - 1]] : 0;
        curr[num] = (skip + take) % MODO;
      }

      next = curr;
    }

    return next[n];

    // Complexity analysis
    // Time : O(Num * PN)
    // Space : O(2 * Num)
  };

  // const PN = powers.length;
  // const memo = Array.from({ length: n + 1 }, () => new Array(PN).fill(-1));
  // return memoization(n, 1, memo);

  // return tabulation();
  return space_optimised();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2787. Ways to Express an Integer as Sum of Powers - https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/description/?envType=daily-question&envId=2025-08-12

  console.log(numberOfWays(1, 1));
  console.log(numberOfWays(10, 1));
  console.log(numberOfWays(300, 1));
  console.log(numberOfWays(300, 5));
};

/**
 * @param {number[]} prices
 * @param {number} k
 * @returns {number[]}
 */
class Solution2 {
  minMaxCandy(prices, k) {
    // code here
    // prices[] = [3, 2, 1, 4], k = 2
    // [1, 2, 3, 4]

    const arr = [...prices].sort((a, b) => a - b);
    const N = arr.length;

    const output = [0, 0];

    let lowBuy = 0;
    let lowFree = N - 1;

    let highBuy = N - 1;
    let highFree = 0;

    while (lowBuy <= lowFree && highBuy >= highFree) {
      output[0] += arr[lowBuy];
      lowBuy++;
      lowFree -= k;

      output[1] += arr[highBuy];
      highBuy--;
      highFree += k;
    }

    return output;

    // Complexity analysis
    // Time : O(N) + O(N * Log(N)) + O(N)
    // Space : O(N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Shop in Candy Store - https://www.geeksforgeeks.org/problems/shop-in-candy-store1145/1

  const s2 = new Solution2();
  console.log(s2.minMaxCandy([3, 2, 1, 4], 2));
  console.log(s2.minMaxCandy([3, 2, 1, 4, 5], 4));
};

(() => {
  // Day 12 of August 2025

  p1();

  p2();
})();
