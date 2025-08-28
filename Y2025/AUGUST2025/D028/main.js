/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var sortMatrix = function (grid) {
  const comparatorASCE = (a, b) => a <= b;
  const comparatorDESC = (a, b) => a >= b;

  // function to sort a range
  const sort = (mat, ri, ci, N, comparator) => {
    for (let i = 0; i < N; i++) {
      let smi = i;
      for (let j = i; j < N; j++) {
        if (comparator(mat[ri + j][ci + j], mat[ri + smi][ci + smi])) smi = j;
      }
      [mat[ri + i][ci + i], mat[ri + smi][ci + smi]] = [
        mat[ri + smi][ci + smi],
        mat[ri + i][ci + i],
      ];
    }
  };

  // copy input for output
  const cgrid = JSON.parse(JSON.stringify(grid));
  const N = cgrid.length;

  // [0][0] -> DESC
  sort(cgrid, 0, 0, N - 0, comparatorDESC);
  for (let i = 1; i < N; i++) {
    // [0][i] ASCE & [i][0] DESC
    sort(cgrid, 0, i, N - i, comparatorASCE);
    sort(cgrid, i, 0, N - i, comparatorDESC);
  }

  return cgrid;

  // Complexity analysis
  // Time : O(2 * N * N * N)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3446. Sort Matrix by Diagonals - https://leetcode.com/problems/sort-matrix-by-diagonals/description/?envType=daily-question&envId=2025-08-28

  console.log(
    sortMatrix([
      [1, 7, 3, 5],
      [9, 8, 2, 4],
      [4, 5, 6, 7],
      [1, 4, 3, 2],
    ])
  );
  console.log(
    sortMatrix([
      [1, 7, 3],
      [9, 8, 2],
      [4, 5, 6],
    ])
  );
  console.log(
    sortMatrix([
      [0, 1],
      [1, 2],
    ])
  );
  console.log(sortMatrix([[1]]));
  console.log(
    sortMatrix([
      [21, 61, 39, 71, 11, 71, 75, 17, 96, 23],
      [58, 49, 90, 81, 93, 10, 51, 88, 77, 48],
      [23, 66, 40, 83, 8, 87, 93, 40, 48, 48],
      [34, 22, 100, 36, 98, 61, 7, 84, 2, 40],
      [71, 76, 1, 89, 65, 24, 97, 11, 41, 95],
      [53, 58, 39, 95, 65, 53, 54, 53, 39, 43],
      [93, 46, 61, 93, 52, 39, 60, 68, 16, 60],
      [31, 16, 74, 97, 26, 10, 26, 0, 64, 50],
      [10, 66, 79, 84, 50, 0, 1, 21, 60, 89],
      [82, 53, 62, 45, 50, 50, 15, 91, 20, 100],
    ])
  );
};

/**
 * @param {number[]} arr
 * @param {number} k
 * @returns {number}
 */
class Solution2 {
  maxOnes(arr, k) {
    // code here
    // arr[] = [1, 0, 1], k = 1
    // classic sliding window and two pointer problem

    let llen = 0;

    for (let l = 0, r = 0, N = arr.length; r < N; r++) {
      while (arr[r] === 0 && k < 1 && l <= r) {
        if (arr[l] === -1) {
          arr[l] = 0;
          k++;
        }
        l++;
      }

      if (arr[r] === 0 && k > 0) {
        arr[r] = -1;
        k--;
      }

      llen = Math.max(llen, r - l + 1);
    }

    for (let i = 0; i < arr.length; i++) {
      if (arr[i] === -1) arr[i] = 0;
    }

    return llen;

    // Complexity analysis
    // Time : O(2N) + O(N)
    // Space : O(1) in-place modification
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Maximize Number of 1's - https://www.geeksforgeeks.org/problems/maximize-number-of-1s0905/1

  const s2 = new Solution2();
  console.log(s2.maxOnes([1, 0, 1], 1));
  console.log(s2.maxOnes([1, 0, 0, 1, 0, 1, 0, 1], 2));
  console.log(s2.maxOnes([1, 1], 2));
  console.log(s2.maxOnes([0, 0], 0));
  console.log(s2.maxOnes([1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1], 12));
  console.log(s2.maxOnes([1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1], 0));
};

(() => {
  // Day 28 of August 2025

  p1();

  p2();
})();
