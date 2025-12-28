/**
 * @param {number[]} candies
 * @param {number} k
 * @return {number}
 */
function maximumCandies(candies, k) {
  const isDistributionPossible = function (minCandies) {
    let childs = 0;
    for (let i = 0; i < candies.length && childs < k; i++) {
      childs += Math.floor(candies[i] / minCandies);
    }

    return childs >= k;
  };

  let ans = 0;
  let low = 1;
  let high = candies.reduce((acc, e) => Math.max(acc, e), -1);

  while (low <= high) {
    const mid = Math.floor(low + (high - low) / 2);

    if (isDistributionPossible(mid)) {
      ans = mid;
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return ans;

  // Complexity analysis
  // Time : O(Log(HIGH) * N), HIGH = MAX(ARR)
  // Space : O(1)
}

const p1 = () => {
  // Problem 1 : POTD Leetcode 2226. Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/?envType=daily-question&envId=2025-03-14

  console.log(maximumCandies([5, 8, 6], 3));
  console.log(maximumCandies([1, 3], 1));
  console.log(maximumCandies([1, 3], 2));
  console.log(maximumCandies([1, 3], 3));
};

class Problem {
  count(coins, sum) {
    // code here
    // return this.recursion(coins, sum, 0);

    // const n = coins.length;
    // const memo = Array.from({ length: n }, () => new Array(sum+1).fill(-1));
    // return this.memoize(coins, sum, 0, memo);

    // return this.tabulation(coins, sum);

    return this.optimised(coins, sum);
  }

  recursion(coins, sum, i) {
    if (i >= coins.length) return sum == 0;

    let op1 = this.recursion(coins, sum, i + 1);
    let op2 = 0;
    if (sum >= coins[i]) op2 = this.recursion(coins, sum - coins[i], i);

    return op1 + op2;

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) stack space
  }

  memoize(coins, sum, i, memo) {
    if (i >= coins.length) return sum == 0;

    if (memo[i][sum] != -1) return memo[i][sum];

    let op1 = this.memoize(coins, sum, i + 1, memo);
    let op2 = 0;
    if (sum >= coins[i]) op2 = this.memoize(coins, sum - coins[i], i, memo);

    return (memo[i][sum] = op1 + op2);

    // Complexity analysis
    // Time : O(2*N*Sum)
    // Space : O(N) stack space + O(N*Sum) memory
  }

  tabulation(coins, tsum) {
    const n = coins.length;
    const memo = Array.from({ length: n + 1 }, () => new Array(tsum + 1).fill(0));

    // base case
    memo[n][0] = 1;

    for (let i = n - 1; i >= 0; i--) {
      for (let sum = 0; sum <= tsum; sum++) {
        let op1 = memo[i + 1][sum];
        let op2 = 0;
        if (sum >= coins[i]) op2 = memo[i][sum - coins[i]];

        memo[i][sum] = op1 + op2;
      }
    }

    return memo[0][tsum];

    // Complexity analysis
    // Time : O(N*Sum)
    // Space : O(N*Sum) memory
  }

  optimised(coins, tsum) {
    const n = coins.length;
    let next = new Array(tsum + 1).fill(0);

    // base case
    next[0] = 1;

    for (let i = n - 1; i >= 0; i--) {
      let curr = new Array(tsum + 1).fill(0);
      for (let sum = 0; sum <= tsum; sum++) {
        let op1 = next[sum];
        let op2 = 0;
        if (sum >= coins[i]) op2 = curr[sum - coins[i]];

        curr[sum] = op1 + op2;
      }

      next = curr;
    }

    return next[tsum];

    // Complexity analysis
    // Time : O(N*Sum)
    // Space : O(2*Sum) memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Coin Change (Count Ways) - https://www.geeksforgeeks.org/problems/coin-change2448/1

  console.log(new Problem().count([1, 2, 3], 4));
  console.log(new Problem().count([11, 12, 13, 14, 15], 1000));
};

(() => {
  // Day 14 of March 2025

  p1();

  p2();
})();
