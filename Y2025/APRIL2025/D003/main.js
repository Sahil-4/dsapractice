/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTripletValue = function (nums) {
  // greedy approach
  // (nums[i] - nums[j]) * nums[k]
  // maximize nums[k], and (nums[i] - nums[j]) tp get largest possible value
  // maximize nums[i], and minimize nums[j] to get largest possible difference

  const N = nums.length;

  let maxValue = 0;
  let maxElement = 0;
  let maxDiff = 0;

  for (let i = 0; i < N; i++) {
    maxValue = Math.max(maxValue, maxDiff * nums[i]);
    maxDiff = Math.max(maxDiff, maxElement - nums[i]);
    maxElement = Math.max(maxElement, nums[i]);
  }

  return maxValue;

  // Complexity analysis
  // Time : O(N)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2874. Maximum Value of an Ordered Triplet II - https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/description/?envType=daily-question&envId=2025-04-03

  console.log(maximumTripletValue([12, 6, 1, 2, 7]));
  console.log(maximumTripletValue([1, 10, 3, 4, 19]));
  console.log(maximumTripletValue([1, 2, 3]));
};

/**
 * @param {number[][]} mat
 * @returns {number}
 */
class Problem2 {
  orangesRotting(mat) {
    // code here
    const N = mat.length;
    const M = mat[0].length;

    // possible movements t, l, b, r
    const _dirs = [
      [-1, 0],
      [0, +1],
      [+1, 0],
      [0, -1],
    ];

    // check if index valid
    const isValidIndex = (r, c) => {
      if (r >= 0 && r < N && c >= 0 && c < M) return true;
      return false;
    };

    // copy given grid
    const copyGrid = Array.from({ length: N }, () => new Array(M));
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        copyGrid[i][j] = mat[i][j];
      }
    }

    // stores time to rot any orange in cell
    const timeGrid = Array.from({ length: N }, () => new Array(M));
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        timeGrid[i][j] = mat[i][j] == 1 ? Infinity : 0;
      }
    }

    // bfs
    const stack = [];

    // add all starting points [x, y, t] in stack
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        if (copyGrid[i][j] == 2) {
          stack.push([i, j, 0]);
        }
      }
    }

    // start rotting oranges
    while (stack.length > 0) {
      const [x, y, t] = stack.shift();

      for (let [ni, nc] of _dirs) {
        const [nx, ny, nt] = [x + ni, y + nc, t + 1];

        if (isValidIndex(nx, ny) && copyGrid[nx][ny] != 0 && timeGrid[nx][ny] > nt) {
          copyGrid[nx][ny] = 2;
          timeGrid[nx][ny] = nt;
          stack.push([nx, ny, nt]);
        }
      }
    }

    // check if any orange is not rotten - return -1
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        if (copyGrid[i][j] == 1) return -1;
      }
    }

    // maximum time to rot any orange defines min time to rot all oranges
    // find it
    let mtime = 0;

    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        mtime = Math.max(mtime, timeGrid[i][j]);
      }
    }

    return mtime;

    // Complexity analysis
    // Time : O(6 * N*M)
    // Space : O(3 * N*M)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Rotten Oranges - https://www.geeksforgeeks.org/problems/rotten-oranges2536/1

  console.log(
    new Problem2().orangesRotting([
      [0, 1, 2],
      [0, 1, 2],
      [2, 1, 1],
    ]),
  );
  console.log(new Problem2().orangesRotting([[2, 2, 0, 1]]));
  console.log(
    new Problem2().orangesRotting([
      [2, 2, 2],
      [0, 2, 0],
    ]),
  );
};

(() => {
  // Day 3 of April 2025

  p1();

  p2();
})();
