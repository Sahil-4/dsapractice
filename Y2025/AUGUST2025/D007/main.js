/**
 * @param {number[][]} fruits
 * @return {number}
 */
var maxCollectedFruits = function (fruits) {
  const N = fruits.length;

  const isValidCell = (x, y) => x >= 0 && x < N && y >= 0 && y < N;

  const player1Traversal = () => {
    let sum = 0;
    for (let i = 0; i < N; i++) sum += fruits[i][i];
    return sum;
  };

  const player2_n_3Traversal = () => {
    const dp = fruits.map((fruit_row) => fruit_row.map((fruit_cell) => fruit_cell));

    if (N === 2) return dp[0][N - 1] + dp[N - 1][0];
    if (N === 3) return dp[0][N - 1] + dp[1][N - 1] + dp[N - 1][0] + dp[N - 1][1];

    for (let i = N - 2; i > 1; i--) {
      for (let j = i + 1; j < N; j++) {
        let x = i - 1;
        for (let y = j - 1; y <= j + 1; y++) {
          if (isValidCell(x, y)) {
            dp[x][y] = Math.max(dp[x][y], fruits[x][y] + dp[i][j]);
            dp[y][x] = Math.max(dp[y][x], fruits[y][x] + dp[j][i]);
          }
        }
      }
    }

    const p2 = dp[0][N - 1] + Math.max(dp[1][N - 1], dp[1][N - 2]);
    const p3 = dp[N - 1][0] + Math.max(dp[N - 1][1], dp[N - 2][1]);
    return p2 + p3;
  };

  let player1 = player1Traversal();
  let player2_n_3 = player2_n_3Traversal();

  return player1 + player2_n_3;

  // Complexity analysis
  // Time : O(N) + O(N * N)
  // Space : O(N * N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3363. Find the Maximum Number of Fruits Collected - https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/description/?envType=daily-question&envId=2025-08-07

  console.log(
    maxCollectedFruits([
      [1, 2, 3, 4],
      [5, 6, 8, 7],
      [9, 10, 11, 12],
      [13, 14, 15, 16],
    ])
  );
  console.log(
    maxCollectedFruits([
      [1, 1],
      [1, 1],
    ])
  );
  console.log(
    maxCollectedFruits([
      [1, 2, 3, 4, 7],
      [5, 7, 6, 8, 7],
      [9, 10, 7, 11, 12],
      [13, 2, 14, 15, 16],
      [6, 8, 7, 2, 1],
    ])
  );
};

/**
 * @param {string} arr
 * @returns {number}
 */
class Solution2 {
  minDifference(arr) {
    // code here
    // ["12:30:15", "12:30:45"]
    // [45015, 45045]
    // ["00:00:01", "23:59:59", "00:00:05"]
    // [1, 86399, 5]

    // maximum "23:59:59" = 86,399
    // minimum "00:00:00" = 0

    const toSeconds = (ts) => {
      const segments = ts.split(":").map(Number);
      return segments[0] * 60 * 60 + segments[1] * 60 + segments[2];
    };
    const secondsArray = arr.map(toSeconds);
    secondsArray.sort((a, b) => a - b);

    const T = 86399;
    const N = arr.length;

    let minDiff = T;
    for (let i = 1; i < N; i++) {
      minDiff = Math.min(minDiff, Math.abs(secondsArray[i] - secondsArray[i - 1]));
    }
    minDiff = Math.min(minDiff, Math.abs(T - secondsArray[N - 1] + 1 + secondsArray[0]));

    return minDiff;

    // Complexity analysis
    // Time : O(N) + O(N * Log(N)) + O(N)
    // Space : O(N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Difference Check - https://www.geeksforgeeks.org/problems/difference-check/1

  const s2 = new Solution2();
  console.log(s2.minDifference(["12:30:15", "12:30:45"]));
  console.log(s2.minDifference(["00:00:01", "23:59:59", "00:00:05"]));
};

(() => {
  // Day 7 of August 2025

  p1();

  p2();
})();
