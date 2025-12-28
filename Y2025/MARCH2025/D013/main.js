/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number}
 */
var minZeroArray = function (nums, queries) {
  const N = nums.length;
  const Q = queries.length;

  const solve1 = function () {
    let k = 0;

    for (const query of queries) {
      // break if all e became zeroes
      let flag = true;
      for (let i = 0; i < N; i++) {
        if (nums[i] != 0) flag = false;
      }
      if (flag) break;

      // or reduce in this range
      const [li, ri, vali] = query;
      for (let i = li; i <= ri; i++) {
        nums[i] -= Math.min(nums[i], vali);
      }

      // increment k
      k++;
    }

    let flag = true;
    for (let i = 0; i < N; i++) {
      if (nums[i] != 0) flag = false;
    }

    return flag ? k : -1;

    // Complexity analysis
    // Time : O(Q*2N)
    // Space : O(1)
  };

  var differenceArray = function (q) {
    const diff = new Array(N).fill(0);

    for (let i = 0; i <= q; i++) {
      const [li, ri, vali] = queries[i];

      diff[li] += vali;
      if (ri + 1 < N) diff[ri + 1] -= vali;
    }

    let csum = 0;
    for (let i = 0; i < N; i++) {
      csum += diff[i];
      diff[i] = csum;

      if (nums[i] > diff[i]) {
        return false;
      }
    }

    return true;
  };

  var solve2 = function () {
    // if already zero
    if (nums.reduce((acc, e) => acc + e, 0) == 0) return 0;

    // run queries
    for (let q = 0; q < Q; q++) {
      if (differenceArray(q)) {
        return q + 1;
      }
    }

    // not possible to make array zero
    return -1;

    // Complexity analysis
    // Time : O(Q*(Q + N))
    // Space : O(N)
  };

  var solve3 = function () {
    // if already zero
    if (nums.reduce((acc, e) => acc + e, 0) == 0) return 0;

    // run queries - using binary search
    let low = 0;
    let high = Q - 1;
    let ans = -1;

    while (low <= high) {
      const mid = Math.floor(low + (high - low) / 2);

      if (differenceArray(mid)) {
        ans = mid + 1;
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    // not possible to make array zero
    return ans;

    // Complexity analysis
    // Time : O(Log(Q) * (Q + N))
    // Space : O(N)
  };

  // return solve1();
  // return solve2();
  return solve3();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3356. Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/description/?envType=daily-question&envId=2025-03-13

  console.log(minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]]));
  console.log(minZeroArray([4,3,2,1], [[1,3,2],[0,2,1]]));
  console.log(minZeroArray([8,4], [[0,1,5],[1,1,5],[1,1,3],[1,1,4],[0,0,3],[1,1,4],[0,1,2],[1,1,3],[1,1,1]]));
};

/**
 * @param {number} capacity
 * @param {number[]} val
 * @param {number[]} wt
 * @returns {number}
 */
class Problem2 {
  // Function to return max value that can be put in knapsack of capacity.
  knapSack(capacity, val, wt) {
    // code here
    // return this.recursion(capacity, val, wt, 0);

    // const memo = new Map();
    // return this.memoize(capacity, val, wt, 0, memo);

    // return this.tabulation(capacity, val, wt);

    return this.optimised(capacity, val, wt);
  }

  recursion(W, val, wt, i) {
    if (i == val.length) return 0;

    let op1 = this.recursion(W, val, wt, i + 1);
    let op2 = 0;
    if (W >= wt[i]) op2 = val[i] + this.recursion(W - wt[i], val, wt, i + 1);

    return Math.max(op1, op2);

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) stack
  }

  memoize(W, val, wt, i, memo) {
    if (i == val.length) return 0;

    if (memo.has(W) && memo.get(W).has(i)) return memo.get(W).get(i);

    let op1 = this.memoize(W, val, wt, i + 1, memo);
    let op2 = 0;
    if (W >= wt[i]) op2 = val[i] + this.memoize(W - wt[i], val, wt, i + 1, memo);

    if (!memo.has(W)) {
      memo.set(W, new Map());
    }

    memo.get(W).set(i, Math.max(op1, op2));

    return memo.get(W).get(i);

    // Complexity analysis
    // Time : O(2*N*N)
    // Space : O(N) stack + O(W*N) memory
  }

  tabulation(capacity, val, wt) {
    const n = val.length;
    const memo = Array.from({ length: n + 1 }, () => new Array(capacity + 1).fill(0));

    for (let W = 0; W <= capacity; W++) {
      for (let i = n - 1; i >= 0; i--) {
        let op1 = memo[i + 1][W];
        let op2 = 0;
        if (W >= wt[i]) op2 = val[i] + memo[i + 1][W - wt[i]];

        memo[i][W] = Math.max(op1, op2);
      }
    }

    return memo[0][capacity];

    // Complexity analysis
    // Time : O(W*N)
    // Space : O(W*N) memory
  }

  optimised(capacity, val, wt) {
    const n = val.length;
    let next = new Array(capacity + 1).fill(0);

    for (let i = n - 1; i >= 0; i--) {
      let curr = new Array(capacity + 1).fill(0);

      for (let W = 0; W <= capacity; W++) {
        let op1 = next[W];
        let op2 = 0;
        if (W >= wt[i]) op2 = val[i] + next[W - wt[i]];

        curr[W] = Math.max(op1, op2);
      }

      next = curr;
    }

    return next[capacity];

    // Complexity analysis
    // Time : O(W*N)
    // Space : O(W*N) memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks 0 - 1 Knapsack Problem - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

  console.log(new Problem2().knapSack(4, [6, 3, 8, 6, 9, 8, 2, 4, 10, 9], [2, 1, 3, 1, 4, 1, 2, 2, 5, 7]));
  console.log(new Problem2().knapSack(5, [10, 40, 30, 50], [5, 4, 2, 3]));
};

(() => {
  // Day 13 of March 2025

  p1();

  p2();
})();
