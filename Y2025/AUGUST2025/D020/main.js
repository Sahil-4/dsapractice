/**
 * @param {number[][]} matrix
 * @return {number}
 */
var countSquares = function (matrix) {
  const M = matrix.length;
  const N = matrix[0].length;

  const dp = Array.from({ length: M }, () => new Array(N).fill(0));

  for (let c = 0; c < N; c++) dp[0][c] = matrix[0][c];
  for (let r = 0; r < M; r++) dp[r][0] = matrix[r][0];

  for (let r = 1; r < M; r++)
    for (let c = 1; c < N; c++) {
      if (matrix[r][c] !== 1) continue;
      const bound = Math.min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]);
      dp[r][c] = matrix[r][c] + bound;
    }

  let sum = 0;
  for (let r = 0; r < M; r++) for (let c = 0; c < N; c++) sum += dp[r][c];
  return sum;

  // Complexity analysis
  // Time : O(2 * N * M)
  // Space : O(N * M)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1277. Count Square Submatrices with All Ones - https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/?envType=daily-question&envId=2025-08-20

  console.log(
    countSquares([
      [0, 1, 1, 1],
      [1, 1, 1, 1],
      [0, 1, 1, 1],
    ])
  );
  console.log(
    countSquares([
      [1, 0, 1],
      [1, 1, 0],
      [1, 1, 0],
    ])
  );
};

/**
 * @param {number[][]} mat
 * @param {number} x
 * @returns {boolean}
 */
class Solution2 {
  searchMatrix(mat, x) {
    // code here
    // PROBLEM : search in sorted rotated array
    // using binary search

    const N = mat.length;
    const M = mat[0].length;

    const getRCE = (cell) => {
      // return mat[r][c];
      // cell = ri * M + ci;
      const r = Math.floor(cell / M);
      const c = Math.floor(cell % M);
      return mat[r][c];
    };

    // search space
    let low = 0; // [0][0]
    let high = N * M - 1; // [N - 1][M - 1]

    while (low <= high) {
      const mid = Math.floor((low + high) / 2);

      const midE = getRCE(mid);

      if (midE === x) return true;

      const lowE = getRCE(low);
      const highE = getRCE(high);

      // to shrink search space
      // first find which side is sorted
      // then use that side to check which side x may lie

      if (lowE <= midE) {
        // low to mid is sorted
        if (lowE <= x && x <= midE) {
          high = mid - 1;
        } else {
          low = mid + 1;
        }
      } else {
        // mid to high is sorted
        if (midE <= x && x <= highE) {
          low = mid + 1;
        } else {
          high = mid - 1;
        }
      }
    }

    return false;

    // Complexity analysis
    // Time : O(Log(NM))
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Search in fully rotated sorted 2D matrix - https://www.geeksforgeeks.org/problems/search-in-fully-rotated-sorted-2d-matrix/1

  const s2 = new Solution2();
  console.log(
    s2.searchMatrix(
      [
        [6, 7, 8],
        [9, 1, 2],
        [3, 4, 5],
      ],
      10
    )
  );
  console.log(
    s2.searchMatrix(
      [
        [7, 8, 9, 10],
        [11, 12, 13, 1],
        [2, 3, 4, 5],
      ],
      3
    )
  );
  console.log(
    s2.searchMatrix(
      [[16, 17, 18][(19, 20, 21)][(1, 2, 3)][(4, 5, 6)][(7, 8, 9)][(10, 11, 12)][(13, 14, 15)]],
      25
    )
  );
};

(() => {
  // Day 20 of August 2025

  p1();

  p2();
})();
