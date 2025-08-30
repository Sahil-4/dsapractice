/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  // for every row, col and subgrid of 3x3
  // verify all values should be unique if value is in [1-9]

  const N = 9;

  const verify = (r, c, rn, cn) => {
    const set = new Set();
    for (let i = r; i < rn; i++) {
      for (let j = c; j < cn; j++) {
        if (board[i][j] === ".") continue;
        if (set.has(board[i][j])) return false;
        set.add(board[i][j]);
      }
    }

    return true;
  };

  for (let i = 0; i < 9; i++) {
    // ith row
    if (!verify(i, 0, i + 1, N)) return false;

    // ith col
    if (!verify(0, i, N, i + 1)) return false;

    // sub grid (sri,sci)
    let sri = Math.floor(i / 3) * 3;
    let sci = (i % 3) * 3;
    if (!verify(sri, sci, sri + 3, sci + 3)) return false;
  }

  return true;

  // Complexity analysis
  // Time : O(N * 2N) + O(N * N)
  // Space : O(N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 36. Valid Sudoku - https://leetcode.com/problems/valid-sudoku/description/?envType=daily-question&envId=2025-08-30

  console.log(
    isValidSudoku([
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
  console.log(
    isValidSudoku([
      ["8", "3", ".", ".", "7", ".", ".", ".", "."],
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
  console.log(
    isValidSudoku([
      ["5", "3", ".", ".", "5", ".", ".", ".", "."],
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
 * @param {number[][]} mat
 * @returns {number}
 */
class Solution2 {
  celebrity(mat) {
    // code here

    // return this.bruteForce(mat);
    return this.optimal(mat);
  }

  optimal(mat) {
    // mat[][] = [
    // [1, 1, 0],
    // [0, 1, 0],
    // [0, 1, 1]]
    // people = [0, 1, 2]
    // possibility if ith person being celebrity
    // mat[i][j] == 0 && mat[j][i] == 1
    // but
    // if mat[i][j] == 1 && mat[j][i] == 1
    // or mat[i][j] == 0 && mat[j][i] == 0
    // neither i nor j can be celebrity
    // for every person i, we just check with its remaining neighbour
    // after this we have to verify the last person for celebrity

    const N = mat.length;

    const stack = new Array();
    for (let i = 0; i < N; i++) stack.push(i);

    let celebrity = -1;

    while (stack.length) {
      if (stack.length === 1) {
        celebrity = stack.pop();
        break;
      }

      let personA = stack.pop();
      let personB = stack.pop();

      if (mat[personA][personB] == 0 && mat[personB][personA] == 1) {
        stack.push(personA);
      } else if (mat[personA][personB] == 1 && mat[personB][personA] == 0) {
        stack.push(personB);
      }
    }

    // verify
    for (let personB = 0; personB < N && celebrity !== -1; personB++) {
      if (celebrity === personB) continue;
      if (mat[celebrity][personB] === 1) celebrity = -1;
      if (mat[personB][celebrity] === 0) celebrity = -1;
    }

    return celebrity;

    // Complexity analysis
    // Time : O(3N)
    // Space : O(N)
  }

  bruteForce(mat) {
    // mat[][] = [
    // [1, 1, 0],
    // [0, 1, 0],
    // [0, 1, 1]]
    // how many people know ith (incoming) = [0, 0, 0] initially all 0
    // how many people ith knows (outgoing) = [0, 0, 0] initially all 0
    // n = 3
    // [1, 3, 1]
    // [2, 1, 2]
    // celebrity = 1

    const N = mat.length;

    if (N === 1) return 0;

    const incoming = new Array(N).fill(0);
    const outgoing = new Array(N).fill(0);

    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        if (mat[i][j] === 1) {
          incoming[j]++;
          outgoing[i]++;
        }
      }
    }

    for (let i = 0; i < N; i++) {
      if (incoming[i] === N && outgoing[i] === 1) return i;
    }

    return -1;

    // Complexity analysis
    // Time : O(N * N) + O(N)
    // Space : O(2N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks The Celebrity Problem - https://www.geeksforgeeks.org/problems/the-celebrity-problem/1

  const s2 = new Solution2();
  console.log(
    s2.celebrity([
      [1, 1, 0],
      [0, 1, 0],
      [0, 1, 1],
    ])
  );
  console.log(
    s2.celebrity([
      [1, 1],
      [1, 1],
    ])
  );
  console.log(s2.celebrity([[1]]));
};

(() => {
  // Day 30 of August 2025

  p1();

  p2();
})();
