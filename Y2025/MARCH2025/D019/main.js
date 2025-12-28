/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function (nums) {
  const n = nums.length;
  let ans = 0;

  const flip_1_0 = (arr, i, j) => {
    for (i; i < j; i++) {
      arr[i] = arr[i] == 1 ? 0 : 1;
    }
  };

  let i = 0;
  while (i <= n - 3) {
    if (nums[i] == 0) {
      flip_1_0(nums, i, i + 3);
      ans++;
    }

    i++;
  }

  let check = nums.reduce((acc, e) => acc && e != 0, true);
  return check ? ans : -1;

  // Complexity analysis
  // Time : O(N^2) ~
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3191. Minimum Operations to Make Binary Array Elements Equal to One I - https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/?envType=daily-question&envId=2025-03-19

  console.log(minOperations([1, 0, 1, 0, 1, 0]));
  console.log(minOperations([0, 1, 0, 1, 0, 1]));
  console.log(minOperations([1, 0, 0, 1, 1, 0, 1, 1, 1]));
  console.log(minOperations([0, 0, 0]));
  console.log(minOperations([1, 1, 1]));
  console.log(minOperations([1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]));
};

class Problem2 {
  maxProfit(prices, k) {
    // code here

    // return this.recursion(prices, k, 0, false);

    // const n = prices.length;
    // const memo = Array.from({ length: n+1 }, () => {
    //     return Array.from({ length: 2 }, () => new Array(k+1).fill(-1));
    // });
    // return this.memoize(prices, k, 0, false, memo);

    // return this.tabulation(prices, k);

    return this.optimised(prices, k);
  }

  recursion(prices, k, i, bought) {
    if (i >= prices.length) return 0;

    if (bought) {
      let not_sell = this.recursion(prices, k, i + 1, bought);
      let sell = prices[i] + this.recursion(prices, k - 1, i + 1, false);

      return Math.max(not_sell, sell);
    } else {
      let not_buy = this.recursion(prices, k, i + 1, bought);
      let buy = 0;
      if (k > 0) {
        buy = -prices[i] + this.recursion(prices, k, i + 1, true);
      }

      return Math.max(not_buy, buy);
    }

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) stack
  }

  memoize(prices, k, i, bought, memo) {
    if (i >= prices.length) return 0;

    if (memo[i][Number(bought)][k] != -1) return memo[i][Number(bought)][k];

    if (bought) {
      let not_sell = this.memoize(prices, k, i + 1, bought, memo);
      let sell = prices[i] + this.memoize(prices, k - 1, i + 1, false, memo);

      return (memo[i][Number(bought)][k] = Math.max(not_sell, sell));
    } else {
      let not_buy = this.memoize(prices, k, i + 1, bought, memo);
      let buy = 0;
      if (k > 0) {
        buy = -prices[i] + this.memoize(prices, k, i + 1, true, memo);
      }

      return (memo[i][Number(bought)][k] = Math.max(not_buy, buy));
    }

    // Complexity analysis
    // Time : O(2*N*2*K)
    // Space : O(N) stack + O(N*2*K) memory
  }

  tabulation(prices, _k) {
    const n = prices.length;
    const memo = Array.from({ length: n + 1 }, () => {
      return Array.from({ length: 2 }, () => new Array(_k + 1).fill(0));
    });

    for (let i = n - 1; i >= 0; i--) {
      for (let k = 0; k <= _k; k++) {
        let not_sell = memo[i + 1][1][k];
        let sell = prices[i] + memo[i + 1][0][k - 1];
        memo[i][1][k] = Math.max(not_sell, sell);

        let not_buy = memo[i + 1][0][k];
        let buy = k > 0 ? -prices[i] + memo[i + 1][1][k] : 0;
        memo[i][0][k] = Math.max(not_buy, buy);
      }
    }

    return memo[0][0][_k];

    // Complexity analysis
    // Time : O(N*_K)
    // Space : O(N*2*_K)
  }

  optimised(prices, _k) {
    const n = prices.length;
    let next = Array.from({ length: 2 }, () => new Array(_k + 1).fill(0));

    for (let i = n - 1; i >= 0; i--) {
      let curr = Array.from({ length: 2 }, () => new Array(_k + 1).fill(0));

      for (let k = 0; k <= _k; k++) {
        let not_sell = next[1][k];
        let sell = prices[i] + next[0][k - 1];
        curr[1][k] = Math.max(not_sell, sell);

        let not_buy = next[0][k];
        let buy = k > 0 ? -prices[i] + next[1][k] : 0;
        curr[0][k] = Math.max(not_buy, buy);
      }

      next = curr;
    }

    return next[0][_k];

    // Complexity analysis
    // Time : O(N*_K)
    // Space : O(2*2*_K)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Stock Buy and Sell – Max K Transactions Allowed - https://www.geeksforgeeks.org/problems/maximum-profit4657/1

  console.log(new Problem2().maxProfit([10, 22, 5, 80], 2));
  console.log(new Problem2().maxProfit([20, 580, 420, 900], 3));
  console.log(new Problem2().maxProfit([100, 90, 80, 50, 25], 1));
};

(() => {
  // Day 19 of March 2025

  p1();

  p2();
})();
