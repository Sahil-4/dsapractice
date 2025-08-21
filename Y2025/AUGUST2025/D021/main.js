/**
 * @param {number[][]} mat
 * @return {number}
 */
var numSubmat = function (mat) {
  const M = mat.length; // number of rows
  const N = mat[0].length; // number of cols

  // dp[i][j] = height of consecutive 1's ending at cell (i, j)
  const dp = Array.from({ length: M }, () => new Array(N).fill(0));

  // build heights row by row
  for (let i = 0; i < M; i++) {
    for (let j = 0; j < N; j++) {
      if (mat[i][j] === 1) {
        dp[i][j] = i > 0 ? dp[i - 1][j] + 1 : 1;
      }
    }
  }

  let count = 0;

  // now for each row, count submatrices ending at (i, j)
  for (let i = 0; i < M; i++) {
    for (let j = 0; j < N; j++) {
      if (dp[i][j] === 0) continue; // no 1's ending here

      let minHeight = dp[i][j]; // tracking min height while moving left

      // extend leftward from (i, j) to (i, 0)
      for (let k = j; k >= 0; k--) {
        if (dp[i][k] === 0) break; // can't extend beyond a zero

        minHeight = Math.min(minHeight, dp[i][k]);
        count += minHeight;
      }
    }
  }

  return count;

  // Complexity analysis:
  // Time: O(M * N^2)
  // Space: O(M * N) for dp matrix
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1504. Count Submatrices With All Ones - https://leetcode.com/problems/count-submatrices-with-all-ones/description/?envType=daily-question&envId=2025-08-21

  console.log(
    numSubmat([
      [1, 0, 1],
      [1, 1, 0],
      [1, 1, 0],
    ])
  );
  console.log(
    numSubmat([
      [0, 1, 1, 0],
      [0, 1, 1, 1],
      [1, 1, 1, 0],
    ])
  );
};

/**
 * @param {number[]} arr
 * @param {number} k
 * @returns {number}
 */
class Solution2 {
  maxMinDiff(arr, k) {
    // code here
    // arr[] = [2, 6, 2, 5], k = 3
    // arr[] = [2, 2, 5, 6]
    // [2, 5, 6]
    // out = 1 (6 - 5)
    // minimum possible difference between any two numbers can be 0
    // maximum possible difference between any two numbers can be the maximum number itself
    // IDEA :
    // sort the array (for checking difference between two elements efficiently - just requred adjacent)
    // get min and max possible diff as search space
    // perform binary search on this
    // we have to maximize this differene
    // for each difference we will have to
    // check whether we are able to take k elements or not
    // such that difference is <= given difference

    const N = arr.length;
    const nums = [...arr].sort((a, b) => a - b);

    // check if able to take k elements with difference less then equal to diff
    const isValid = (diff) => {
      let elementsCount = 1;

      for (let i = 1, prev = 0; i < N; i++) {
        if (nums[i] - nums[prev] >= diff) {
          elementsCount += 1;
          prev = i;
        }
      }

      return elementsCount >= k;
    };

    // search space
    let low = 0;
    let high = nums[N - 1];
    let ans = 0;

    // binary search
    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      if (isValid(mid)) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return ans;

    // Complexity analysis
    // Time : O(N) + O(N * Log(N)) + O(N) + O(Log(Max(Arr)) * N)
    // Space : O(N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Maximize the minimum difference between k elements - https://www.geeksforgeeks.org/problems/maximize-the-minimum-difference-between-k-elements/1

  const s2 = new Solution2();
  console.log(s2.maxMinDiff([2, 6, 2, 5], 3));
  console.log(s2.maxMinDiff([1, 4, 9, 0, 2, 13, 3], 4));
};

(() => {
  // Day 21 of August 2025

  p1();

  p2();
})();
