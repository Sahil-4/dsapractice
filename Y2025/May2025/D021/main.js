/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {
  const M = matrix.length;
  const N = matrix[0].length;

  // find zero cells 
  // mark 0 to first col of impacted row and first row of impacted col 
  // revisit matrix 
  // check 0th col and 0th row of its row and col 
  // if anyone is zero make the cell zero 

  // edge case for first row and first col 
  let frow = fcol = false;
  for (let c = 0; c < N && !frow; c++) frow = (matrix[0][c] === 0);
  for (let r = 0; r < M && !fcol; r++) fcol = (matrix[r][0] === 0);

  for (let r = 0; r < M; r++) {
    for (let c = 0; c < N; c++) {
      if (matrix[r][c] === 0) {
        matrix[r][0] = 0;
        matrix[0][c] = 0;
      }
    }
  }

  for (let r = 1; r < M; r++) {
    for (let c = 1; c < N; c++) {
      if (matrix[r][0] === 0 || matrix[0][c] === 0) {
        matrix[r][c] = 0;
      }
    }
  }

  for (let c = 1; c < N && frow; c++) matrix[0][c] = 0;
  for (let r = 1; r < M && fcol; r++) matrix[r][0] = 0;

  // Complexity analysis 
  // Time : O(2 * (N + M)) +  O(2 * (M * N)) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/?envType=daily-question&envId=2025-05-21 

  console.log(setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]));
  console.log(setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]));
};


/**
 * @param {number} m
 * @param {number} n
 * @param {number} k
 * @returns {number}
 */

class Problem2 {
  kthSmallest(m, n, k) {
    // code here

    const ltk = (e) => {
      // tells how many elements are smalles then e 
      let c = 0;

      // i = number of table 
      for (let i = 1; i <= m; i++) {
        c += Math.min(Math.floor(e / i), n);
      }

      return c;
    };

    // search space 
    let low = 1;
    let high = m * n;

    // binary search 
    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      if (ltk(mid) < k) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return low;

    // Complexity analysis 
    // Time : O(Log(M * N) * M) 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Kth Smallest Number in Multiplication Table - https://www.geeksforgeeks.org/problems/kth-smallest-number-in-multiplication-table/1 

  console.log(new Problem2().kthSmallest(5, 5, 4));
  console.log(new Problem2().kthSmallest(1000, 1000, 100));
  console.log(new Problem2().kthSmallest(1000, 1000, 1000));
  console.log(new Problem2().kthSmallest(3000, 3000, 1000));
};


(() => {
  // Day 21 of May 2025

  p1();

  p2();
})();
