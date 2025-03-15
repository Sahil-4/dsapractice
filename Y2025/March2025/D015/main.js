/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minCapability = function (nums, _k) {
  const n = nums.length;

  const memoize = (k, i, memo) => {
    if (k == 0) return 0;
    if (i >= n) return Infinity;

    if (memo[i][k] != -1) return memo[i][k];

    const not_take = memoize(k, i + 1, memo);
    const take = Math.max(nums[i], memoize(k - 1, i + 2, memo));

    return (memo[i][k] = Math.min(not_take, take));

    // Complexity analysis
    // Time : O(2*N*K)
    // Space : O(N) stack space + O(N*K) memory
  };

  const _binary_search = () => {
    const isRobbingPossible = (mid) => {
      let houses = 0;

      for (let i = 0; i < n; i++) {
        if (nums[i] <= mid) {
          houses++;
          i++;
        }
      }

      return houses >= _k;
    };

    let low = 1;
    let high = nums.reduce((acc, e) => acc + e, 0);
    let ans = 0;

    while (low <= high) {
      const mid = Math.floor(low + (high - low) / 2);

      if (isRobbingPossible(mid)) {
        ans = mid;
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    return ans;

    // Complexity analysis
    // Time : O(LOG(HIGH) * N)
    // Space : O(1)
  };

  // const memo = Array.from({ length: n }, () => new Array(_k+1).fill(-1));
  // return memoize(_k, 0, memo);

  return _binary_search();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2560. House Robber IV - https://leetcode.com/problems/house-robber-iv/description/?envType=daily-question&envId=2025-03-15

  console.log(minCapability([2, 3, 5, 9], 2));
  console.log(minCapability([2, 7, 9, 3, 1], 2));
};

/**
 * @param {number[]} coins
 * @param {number} sum
 * @returns {number}
 */
class Problem2 {
  minCoins(coins, sum) {
    // your code here
    if (this.countWays(coins, sum) == 0) return -1;
    this.tsum = sum;

    // return this.recursion(coins, sum, 0);

    // const n = coins.length;
    // const memo = Array.from({ length: n }, () => new Array(sum+1).fill(-1));
    // return this.recursion(coins, sum, 0, memo);

    return this.tabulation(coins, sum);
  }

  recursion(coins, sum, i, memo) {
    if (i >= coins.length) {
      if (sum == 0) return 0;
      return this.tsum;
    }

    if (memo && memo[i][sum] != -1) return memo[i][sum];

    let option1 = this.recursion(coins, sum, i + 1, memo);
    let option2 = sum < coins[i] ? this.tsum : 1 + this.recursion(coins, sum - coins[i], i, memo);

    const output = Math.min(option1, option2);
    if (memo && memo[i][sum] != -1) memo[i][sum] = output;

    return output;

    // Complexity analysis
    // Time : O(2*N*SUM)
    // Space : O(N) stack space + O(N*SUM) memory
  }

  tabulation(coins, tsum) {
    const n = coins.length;
    let next = new Array(tsum + 1).fill(tsum);

    // base case
    next[0] = 0;

    for (let i = n - 1; i >= 0; i--) {
      let curr = new Array(tsum + 1).fill(0);

      for (let sum = 0; sum <= tsum; sum++) {
        let option1 = next[sum];
        let option2 = sum < coins[i] ? tsum : 1 + curr[sum - coins[i]];

        const output = Math.min(option1, option2);
        curr[sum] = output;
      }

      next = curr;
    }

    return next[tsum];

    // Complexity analysis
    // Time : O(N*SUM)
    // Space : O(N*SUM) memory
  }

  countWays(coins, tsum) {
    const n = coins.length;
    let next = new Array(tsum + 1).fill(0);

    // base case
    next[0] = 1;

    for (let i = n - 1; i >= 0; i--) {
      let curr = new Array(tsum + 1).fill(0);
      for (let sum = 0; sum <= tsum; sum++) {
        let op1 = next[sum];
        let op2 = sum < coins[i] ? 0 : curr[sum - coins[i]];

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
  // Problem 2 : POTD Geeksforgeeks Coin Change (Minimum Coins) - https://www.geeksforgeeks.org/problems/number-of-coins1824/1

  console.log(new Problem2().minCoins([9, 6, 5, 1], 19));
};

(() => {
  // Day 15 of March 2025

  p1();

  p2();
})();
