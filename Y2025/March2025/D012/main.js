var last_neg = function (arr) {
  let low = 0;
  let high = arr.length - 1;

  let ans = -1;

  while (low <= high) {
    const mid = Math.floor(low + (high - low) / 2);

    if (arr[mid] < 0) {
      ans = mid;
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return ans;
};

var first_pos = function (arr) {
  let low = 0;
  let high = arr.length - 1;

  let ans = -1;

  while (low <= high) {
    const mid = Math.floor(low + (high - low) / 2);

    if (arr[mid] > 0) {
      ans = mid;
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }

  return ans;
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumCount = function (nums) {
  const solve1 = () => {
    return nums.reduce(
      (acc, e) => {
        if (e > 0) acc.pos++;
        else if (e < 0) acc.neg++;

        acc.max = Math.max(acc.pos, acc.neg);

        return acc;
      },
      { pos: 0, neg: 0, max: 0 },
    ).max;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  };

  var solve2 = () => {
    const n = nums.length;

    // index of last element less then equal to -1
    let lelte_i = last_neg(nums);
    // index of first element greater then equal to 1
    let fegte_i = first_pos(nums);

    // count of negative & positive numbers
    const neg = 1 + lelte_i;
    const pos = fegte_i == -1 ? 0 : n - fegte_i;

    // return whichever is max
    return Math.max(neg, pos);

    // Complexity analysis
    // Time : O(2 * Log(N))
    // Space : O(1)
  };

  // return solve1();
  return solve2();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2529. Maximum Count of Positive Integer and Negative Integer - https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/?envType=daily-question&envId=2025-03-12

  console.log(maximumCount([-2, -1, -1, 1, 2, 3]));
  console.log(maximumCount([-3, -2, -1, 0, 0, 1, 2]));
  console.log(maximumCount([5, 20, 66, 1314]));
  console.log(maximumCount([-3, -2, -1]));
};

/**
 * @param {number[]} cost
 * @returns {number}
 */
class Problem2 {
  minCostClimbingStairs(cost) {
    // Write your code here

    // return this.recursion(cost, -1);

    // const n = cost.length;
    // const memo = new Array(n).fill(-1);
    // return this.memoize(cost, -1, memo);

    // return this.tabulation(cost);

    return this.optimised(cost);
  }

  recursion(cost, i) {
    if (cost.length <= i) return 0;

    let op1 = this.recursion(cost, i + 1);
    let op2 = this.recursion(cost, i + 2);

    let out = Math.min(op1, op2);

    if (i != -1) out += cost[i];

    return out;

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) stack space
  }

  memoize(cost, i, memo) {
    if (cost.length <= i) return 0;

    if (i != -1 && memo[i] != -1) return memo[i];

    let op1 = this.memoize(cost, i + 1, memo);
    let op2 = this.memoize(cost, i + 2, memo);

    let out = Math.min(op1, op2);

    if (i != -1) {
      memo[i] = out += cost[i];
    }

    return out;

    // Complexity analysis
    // Time : O(2*N)
    // Space : O(N) stack space + O(N) memory space
  }

  tabulation(cost) {
    const n = cost.length;
    const memo = new Array(n + 2).fill(0);

    for (let i = n - 1; i >= 0; i--) {
      memo[i] = Math.min(memo[i + 1], memo[i + 2]) + cost[i];
    }

    return Math.min(memo[0], memo[1]);

    // Complexity analysis
    // Time : O(N)
    // Space : O(N) memory space
  }

  optimised(cost) {
    const n = cost.length;

    let next2 = 0;
    let next = 0;

    for (let i = n - 1; i >= 0; i--) {
      let curr = Math.min(next, next2) + cost[i];
      next2 = next;
      next = curr;
    }

    return Math.min(next2, next);

    // Complexity analysis
    // Time : O(N)
    // Space : O(2) memory space
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Min Cost Climbing Stairs - https://www.geeksforgeeks.org/problems/min-cost-climbing-stairs/1

  console.log(new Problem2().minCostClimbingStairs([10, 15, 20]));
  console.log(new Problem2().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]));
};

(() => {
  // Day 12 of March 2025

  p1();

  p2();
})();
