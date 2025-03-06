/**
 * @param {number[][]} grid
 * @return {number[]}
 */
function findMissingAndRepeatedValues(grid) {
  function solve1() {
    const glen = grid.length;
    const N = glen * glen;

    let nsum = (N * (N + 1)) / 2;

    let set = new Set();
    let duplicate = 0,
      missing = 0;
    let gsum = 0;

    for (let i = 0; i < glen; i++) {
      for (let j = 0; j < glen; j++) {
        if (set.has(grid[i][j])) {
          duplicate = grid[i][j];
        }
        set.add(grid[i][j]);
        gsum += grid[i][j];
      }
    }

    missing = nsum - (gsum - duplicate);

    return [duplicate, missing];

    // Complexity analysis
    // Time : O(N)
    // Space : O(N)
  }

  function solve2() {
    const glen = grid.length;
    const N = glen * glen;

    let NSum = (N * (N + 1)) / 2; // sum of first N naturals
    let NSqrSum = (N * (N + 1) * (2 * N + 1)) / 6; // sum of first N natural's square
    let GSum = 0; // sum of elements of grid
    let GSqrSum = 0; // sum of square of elements of grid

    for (let i = 0; i < glen; i++) {
      for (let j = 0; j < glen; j++) {
        GSum += grid[i][j];
        GSqrSum += grid[i][j] * grid[i][j];
      }
    }

    const sumDiff = NSum - GSum;
    const sqrDiff = NSqrSum - GSqrSum;
    const sqrDiff2sumDiff = sqrDiff / sumDiff;

    const duplicate = (sqrDiff2sumDiff - sumDiff) / 2;
    const missing = (sqrDiff2sumDiff + sumDiff) / 2;

    return [duplicate, missing];

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

  // return solve1();
  return solve2();
}

const p1 = () => {
  // Problem 1 : POTD Leetcode 2965. Find Missing and Repeated Values - https://leetcode.com/problems/find-missing-and-repeated-values/?envType=daily-question&envId=2025-03-06

  console.log(
    findMissingAndRepeatedValues([
      [1, 3],
      [2, 2],
    ]),
  );
  console.log(
    findMissingAndRepeatedValues([
      [9, 1, 7],
      [8, 9, 2],
      [3, 4, 6],
    ]),
  );
};

function lcs(s1, s2) {
  // code here
  var recursion = function (s1, i1, s2, i2) {
    if (i1 >= s1.length) return 0;
    if (i2 >= s2.length) return 0;

    let op1 = recursion(s1, i1 + 1, s2, i2);
    let op2 = recursion(s1, i1, s2, i2 + 1);
    let op3 = 0;
    if (s1[i1] == s2[i2]) {
      op3 = 1 + recursion(s1, i1 + 1, s2, i2 + 1);
    }

    return Math.max(op1, op2, op3);
  };

  var memoization = function (s1, i1, s2, i2, memo) {
    if (i1 >= s1.length) return 0;
    if (i2 >= s2.length) return 0;

    if (memo[i1][i2] != -1) {
      return memo[i1][i2];
    }

    let op1 = memoization(s1, i1 + 1, s2, i2, memo);
    let op2 = memoization(s1, i1, s2, i2 + 1, memo);
    let op3 = 0;
    if (s1[i1] == s2[i2]) {
      op3 = 1 + memoization(s1, i1 + 1, s2, i2 + 1, memo);
    }

    return (memo[i1][i2] = Math.max(op1, op2, op3));
  };

  // return recursion(s1, 0, s2, 0);

  const n = s1.length;
  const m = s2.length;
  const memo = Array.from({ length: n }, () => new Array(m).fill(-1));
  return memoization(s1, 0, s2, 0, memo);
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Longest Common Subsequence - https://www.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1

  console.log(lcs("abc", "abcd"));
  console.log(lcs("abcd", "abc"));
  console.log(lcs("abc", "abc"));
  console.log(lcs("abc", "acc"));
  console.log(lcs("acc", "abc"));
};

(() => {
  // Day 6 of March 2025

  p1();

  p2();
})();
