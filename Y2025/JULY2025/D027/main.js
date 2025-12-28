/**
 * @param {number[]} nums
 * @return {number}
 */
var countHillValley = function (nums) {
  let count = 0;

  const N = nums.length;

  for (let i = 1; i < N - 1; i++) {
    // skip points which are part of other valley or hills
    while (nums[i] === nums[i + 1]) i++;

    // prev index, next index variables
    let pi = i;
    let ni = i;

    // index of next not equal
    while (ni < N && nums[ni] === nums[i]) ni++;
    // index of prev not equal
    while (pi >= 0 && nums[pi] === nums[i]) pi--;

    // check for hill . ^ .
    if (pi >= 0 && ni < N && nums[pi] < nums[i] && nums[i] > nums[ni]) {
      count++;
    }
    // check for valley ^ . ^
    if (pi >= 0 && ni < N && nums[pi] > nums[i] && nums[i] < nums[ni]) {
      count++;
    }
  }

  return count;

  // Complexity analysis
  // Time : O(N * N)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2210. Count Hills and Valleys in an Array - https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/?envType=daily-question&envId=2025-07-27

  console.log(countHillValley([2, 4, 1, 1, 6, 5]));
  console.log(countHillValley([6, 6, 5, 5, 4, 1]));
  console.log(countHillValley([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]));
  console.log(countHillValley([39, 55, 43, 51, 50, 9, 74, 24, 55, 26, 88, 98, 40, 92, 65, 22, 9]));
  console.log(countHillValley([22, 1, 89, 16, 73, 36, 12, 52, 20, 29, 46, 76, 85, 43, 15, 58, 90]));
};

class Solution2 {
  setMatrixZeroes(mat) {
    // code here

    // return this.sol1(mat);
    return this.sol2(mat);
  }

  sol1(mat) {
    const N = mat.length;
    const M = mat[0].length;

    const zeroRows = [];
    const zeroCols = [];

    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        if (mat[i][j] === 0) {
          zeroRows.push(i);
          zeroCols.push(j);
        }
      }
    }

    for (let r of zeroRows) {
      for (let c = 0; c < M; c++) {
        mat[r][c] = 0;
      }
    }
    for (let c of zeroCols) {
      for (let r = 0; r < N; r++) {
        mat[r][c] = 0;
      }
    }

    return mat;

    // Complexity analysis
    // Time : O(N * M) + O(N * M)
    // Space : O(N + M) + modified input
  }

  sol2(mat) {
    const N = mat.length;
    const M = mat[0].length;

    let C0Zero = false; // first col has zero
    let R0Zero = false; // first row has zero

    for (let r = 0; r < N; r++) C0Zero = C0Zero || mat[r][0] === 0;
    for (let c = 0; c < M; c++) R0Zero = R0Zero || mat[0][c] === 0;

    // marking
    for (let r = 1; r < N; r++) {
      for (let c = 1; c < M; c++) {
        if (mat[r][c] === 0) {
          mat[r][0] = 0;
          mat[0][c] = 0;
        }
      }
    }

    // making zero - inner matrix
    for (let r = 1; r < N; r++) {
      for (let c = 1; c < M; c++) {
        if (mat[r][0] === 0 || mat[0][c] === 0) {
          mat[r][c] = 0;
        }
      }
    }

    // making zero - border matrix
    // make all col of first row zero if it had zero at any col
    for (let c = 0; c < M && R0Zero; c++) mat[0][c] = 0;

    // making zero - border matrix
    // make all row of first col zero if it had zero at any row
    for (let r = 0; r < N && C0Zero; r++) mat[r][0] = 0;

    return mat;

    // Complexity analysis
    // Time : O(N + M) + O(N * M) + O(N * M)
    // Space : O(1) + modified input
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Set Matrix Zeros - https://www.geeksforgeeks.org/problems/set-matrix-zeroes/1

  const s2 = new Solution2();
  console.log(
    s2.setMatrixZeroes([
      [1, -1, 1],
      [-1, 0, 1],
      [1, -1, 1],
    ])
  );
  console.log(
    s2.setMatrixZeroes([
      [0, 1, 2, 0],
      [1, 2, 6, 2],
      [1, 3, 1, 8],
    ])
  );
  console.log(
    s2.setMatrixZeroes([
      [1, 0, 2, 0],
      [1, 2, 6, 2],
      [1, 3, 1, 8],
    ])
  );
};

(() => {
  // Day 27 of July 2025

  p1();

  p2();
})();
