/**
 * @param {number} n
 * @return {boolean}
 */
var checkPowersOfThree = function (n) {
  function solve1(n) {
    // calculate maximum possible power
    let mpower = 0;
    while (Math.pow(3, mpower) <= n) {
      mpower++;
    }

    // decrease n by its power (power should be distinct)
    while (n > 0) {
      if (n >= Math.pow(3, mpower)) {
        n -= Math.pow(3, mpower);
      }

      // duplicate power
      if (n >= Math.pow(3, mpower)) {
        return false;
      }

      // reduce power
      mpower--;
    }

    return true;

    // Complexity analysis
    // Time : O(log3(N))
    // Space : O(1)
  }

  function solve2(n) {
    while (n >= 3) {
      let bit = n % 3;
      if (bit == 2) return false;
      n = Math.floor(n / 3);
    }
    return n != 2;

    // Complexity analysis
    // Time : O(log3(N))
    // Space : O(1)
  }

  function solve3(n, p) {
    if (n == 0) return true;
    if (Math.pow(3, p) > n) return false;

    let not_take = solve3(n, p + 1);
    let take = solve3(n - Math.pow(3, p), p + 1);

    return not_take || take;

    // Complexity analysis
    // Time : O(2^log3(N))
    // Space : O(1)
  }

  // return solve1(n);
  // return solve2(n);
  return solve3(n, 0);
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1780. Check if Number is a Sum of Powers of Three - https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/?envType=daily-question&envId=2025-03-04

  console.log(checkPowersOfThree(0));
  console.log(checkPowersOfThree(1));
  console.log(checkPowersOfThree(3));
  console.log(checkPowersOfThree(8));
  console.log(checkPowersOfThree(12));
  console.log(checkPowersOfThree(18));
};

function lis(arr) {
  // code here
  function recursion(arr, index, prev) {
    if (arr.length === index) return 0;

    let not_take = recursion(arr, index + 1, prev);
    let take = 0;
    if (prev === -1 || arr[prev] < arr[index]) take = 1 + recursion(arr, index + 1, index);

    return Math.max(not_take, take);

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) stack
  }

  function memoization(arr, index, prev, memo) {
    if (arr.length === index) return 0;

    if (memo[index][prev + 1] !== -1) {
      return memo[index][prev + 1];
    }

    let not_take = memoization(arr, index + 1, prev, memo);
    let take = 0;
    if (prev === -1 || arr[prev] < arr[index]) {
      take = 1 + memoization(arr, index + 1, index, memo);
    }

    return (memo[index][prev + 1] = Math.max(not_take, take));

    // Complexity analysis
    // Time : O(2*N*N)
    // Space : O(N) stack + O(N*N) memory
  }

  function tabulation(arr) {
    const n = arr.length;
    let memo = new Array(n + 1).fill(new Array(n + 1).fill(0));

    for (let index = n - 1; index >= 0; index--) {
      for (let prev = index - 1; prev >= -1; prev--) {
        let not_take = memo[index + 1][prev + 1];
        let take = 0;
        if (prev === -1 || arr[prev] < arr[index]) {
          take = 1 + memo[index + 1][index + 1];
        }

        memo[index][prev + 1] = Math.max(not_take, take);
      }
    }

    return memo[0][0];

    // Complexity analysis
    // Time : O(N*N)
    // Space : O(N) stack + O(N*N) memory
  }

  function optimised(arr) {
    const n = arr.length;
    let next = new Array(n + 1).fill(0);

    for (let index = n - 1; index >= 0; index--) {
      let curr = new Array(n + 1).fill(0);

      for (let prev = index - 1; prev >= -1; prev--) {
        let not_take = next[prev + 1];
        let take = 0;
        if (prev === -1 || arr[prev] < arr[index]) {
          take = 1 + next[index + 1];
        }

        curr[prev + 1] = Math.max(not_take, take);
      }

      next = curr;
    }

    return next[0];

    // Complexity analysis
    // Time : O(N*N)
    // Space : O(N) stack + O(N*N) memory
  }

  // return recursion(arr, 0, -1);

  // const n = arr.length;
  // let memo = new Array(n).fill(new Array(n+1).fill(-1));
  // return memoization(arr, 0, -1, memo);

  // return tabulation(arr);

  return optimised(arr);
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Longest Increasing Subsequence - https://www.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1

  console.log(lis([5, 8, 3, 7, 9, 1]));
  console.log(lis([9, 8, 7, 6, 5, 4, 3, 2, 1]));
  console.log(lis([1, 2, 3, 5, 6, 7, 8, 9, 20]));
};

(() => {
  // Day 4 of March 2025

  p1();

  p2();
})();
