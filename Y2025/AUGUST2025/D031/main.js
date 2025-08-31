/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function (board) {
  // i will try possible options to put at cell [r][c]
  // possible options = [1-9]
  // if i can put e at [r][c], i will and move to next cell
  // this will be recursive solution

  const N = 9;

  const canIPut = (e, r, c) => {
    for (let i = 0; i < 9; i++) {
      if (board[r][i] === e) return false;
      if (board[i][c] === e) return false;
    }

    let sri = Math.floor(r / 3) * 3;
    let sci = Math.floor(c / 3) * 3;
    for (let i = sri; i < sri + 3; i++) {
      for (let j = sci; j < sci + 3; j++) {
        if (board[i][j] === e) return false;
      }
    }

    return true;
  };

  const recursion = (r, c) => {
    if (r >= N) return true;
    if (c >= N) return recursion(r + 1, 0);
    if (board[r][c] !== ".") return recursion(r, c + 1);

    for (let e = 1; e <= 9; e++) {
      if (!canIPut(String(e), r, c)) continue;

      board[r][c] = String(e);
      const check = recursion(r, c + 1);
      if (check) return true;
      board[r][c] = ".";
    }

    return false;
  };

  return recursion(0, 0);

  // Complexity analysis
  // Time : O(N ^ N)
  // Space : O(N * N) stack space
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 37. Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/?envType=daily-question&envId=2025-08-31

  console.log(
    solveSudoku([
      ["5", "3", ".", ".", "7", ".", ".", ".", "."],
      ["6", ".", ".", "1", "9", "5", ".", ".", "."],
      [".", "9", "8", ".", ".", ".", ".", "6", "."],
      ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
      ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
      [".", "6", ".", ".", ".", ".", "2", "8", "."],
      [".", ".", ".", "4", "1", "9", ".", ".", "5"],
      [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ])
  );
};

/**
 * @param {number[]} arr
 * @returns {number}
 */
class Solution2 {
  maxWater(arr) {
    // code here
    // clarifications
    // water will be stored between two lines
    // water will not be stored above the lines
    // say arr[] = [1, 5]
    // water will be stored between 1 and 5 height line
    // and the maximum amount of water we can store here will be 1
    // if we store more then 1 water that will overflow from 1 height line
    // difference between these lines is 1 hence 1 * 1 unit water
    // if I want to collect maximum amount water
    // I will have to find two largest and farthest lines
    // use two pointers (for farthest)
    // update pointer, whichever element is low

    const N = arr.length;

    let maxxWater = 0;

    let l = 0;
    let r = N - 1;

    while (l < r) {
      const [ai, ae] = [l, arr[l]];
      const [bi, be] = [r, arr[r]];

      const water = Math.abs(ai - bi) * Math.min(ae, be);
      maxxWater = Math.max(maxxWater, water);

      if (ae < be) l++;
      else r--;
    }

    return maxxWater;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Container With Most Water - https://www.geeksforgeeks.org/problems/container-with-most-water0535/1

  const s2 = new Solution2();
  console.log(s2.maxWater([2, 5, 1]));
  console.log(s2.maxWater([1, 5]));
  console.log(s2.maxWater([1]));
  console.log(s2.maxWater([1, 5, 4, 3]));
  console.log(s2.maxWater([3, 1, 2, 4, 5]));
  console.log(s2.maxWater([2, 1, 8, 6, 4, 6, 5, 5]));
};

(() => {
  // Day 31 of August 2025

  p1();

  p2();
})();
