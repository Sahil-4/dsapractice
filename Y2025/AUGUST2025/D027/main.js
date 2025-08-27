/**
 * @param {number[][]} grid
 * @return {number}
 */
var lenOfVDiagonal = function (grid) {
  // movement rules
  const cellRule = [
    [1, 1],
    [1, -1],
    [-1, -1],
    [-1, 1],
  ];

  // grid dimensions
  const N = grid.length;
  const M = grid[0].length;

  // traverse grid and find length of longest path
  const traverse = (r, c, dir, el = 2, flag = true) => {
    // base conditions
    // check in current cell is invalid
    if (r < 0 || r >= N || c < 0 || c >= M || grid[r][c] !== el) return 0;

    // update next element [2, 0, 2, 0, ...]
    const nel = 2 - el;
    const [nr, nc] = cellRule[dir];
    let nextCount = traverse(r + nr, c + nc, dir, nel, flag);

    if (flag) {
      const ndir = (dir + 1) % 4;
      const [nr, nc] = cellRule[ndir];
      nextCount = Math.max(nextCount, traverse(r + nr, c + nc, ndir, nel, false));
    }

    return 1 + nextCount;
  };

  let longestDiagonalSegmentV = 0;

  // start traversal from beginning
  for (let r = 0; r < N; r++) {
    for (let c = 0; c < M; c++) {
      if (grid[r][c] !== 1) continue;

      longestDiagonalSegmentV = Math.max(longestDiagonalSegmentV, 1 + traverse(r + 1, c + 1, 0));
      longestDiagonalSegmentV = Math.max(longestDiagonalSegmentV, 1 + traverse(r + 1, c - 1, 1));
      longestDiagonalSegmentV = Math.max(longestDiagonalSegmentV, 1 + traverse(r - 1, c - 1, 2));
      longestDiagonalSegmentV = Math.max(longestDiagonalSegmentV, 1 + traverse(r - 1, c + 1, 3));
    }
  }

  return longestDiagonalSegmentV;

  // Complexity analysis
  // Time : O(N * M * 4 * D)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3459. Length of Longest V-Shaped Diagonal Segment - https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/description/?envType=daily-question&envId=2025-08-27

  console.log(
    lenOfVDiagonal([
      [2, 2, 1, 2, 2],
      [2, 0, 2, 2, 0],
      [2, 0, 1, 1, 0],
      [1, 0, 2, 2, 2],
      [2, 0, 0, 2, 2],
    ])
  );
  console.log(
    lenOfVDiagonal([
      [2, 2, 2, 2, 2],
      [2, 0, 2, 2, 0],
      [2, 0, 1, 1, 0],
      [1, 0, 2, 2, 2],
      [2, 0, 0, 2, 2],
    ])
  );
  console.log(
    lenOfVDiagonal([
      [1, 2, 2, 2, 2],
      [2, 2, 2, 2, 0],
      [2, 0, 0, 0, 0],
      [0, 0, 2, 2, 2],
      [2, 0, 0, 2, 0],
    ])
  );
  console.log(lenOfVDiagonal([[1]]));
};

/**
 * @param {number[]} arr
 * @returns {number}
 */
class Solution2 {
  countTriangles(arr) {
    // code here
    // Dry Run
    // arr[] = [4, 6, 3, 7]
    // 3 4 6 7
    // (3,4) -> 1 possible third sides
    // (3,6) -> 1 possible third sides
    // (4,6) -> 1 possible third sides
    // arr[] = [3, 4, 5, 6, 7]
    // 3 4 5 6 7
    // (3,4) -> 2 possible third sides (index 4 - index 1 - 1)
    // (3,5) -> 2 possible third sides (index 5 - index 2 - 1)
    // (3,6) -> 1 possible third sides (index 5 - index 3 - 1)
    // (3,7) X
    // (4,5) -> 2 possible third sides (index 5 - index 2 - 1)
    // (4,6) -> 1 possible third sides (index 5 - index 3 - 1)
    // (4,7) X
    // (5,6) -> 1 possible third sides (index 5 - index 3 - 1)

    // Logic :
    // for first two sides use two nested for loops (i for Size1, j for Side2)
    // and for third size use binary search
    // find index of element >= SUM(Side1 + Side2) say k
    // countOfThirdSides = k - j - 1
    // increment count of triangles by countOfThirdSides

    const N = arr.length;
    arr.sort((a, b) => a - b); // !MODIFYING INPUT

    let trianglesCount = 0;

    for (let i = 0; i < N - 2; i++) {
      for (let j = i + 1; j < N - 1; j++) {
        const sum = arr[i] + arr[j]; // side1 + side2
        const countOfThirdSides = Math.max(this._binarySearch(arr, N, sum) - j - 1, 0);
        trianglesCount += countOfThirdSides;
      }
    }

    return trianglesCount;

    // Complexity analysis
    // Time : O(N * Log(N)) + O(N * N * Log(N))
    // Space : O(N)
  }

  _binarySearch(arr, N, key) {
    let low = 0;
    let high = N - 1;

    let ans = N;

    while (low <= high) {
      const mid = Math.floor((low + high) / 2);

      if (arr[mid] >= key) {
        ans = mid;
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    return ans;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Count the number of possible triangles - https://www.geeksforgeeks.org/problems/count-possible-triangles-1587115620/1

  const s2 = new Solution2();
  console.log(s2.countTriangles([4, 6, 3, 7, 5]));
  console.log(s2.countTriangles([4, 6, 3, 7]));
  console.log(s2.countTriangles([10, 21, 22, 100, 101, 200, 300]));
  console.log(s2.countTriangles([1, 2, 3]));
  console.log(s2.countTriangles([28, 4, 33, 38, 0, 45]));
};

(() => {
  // Day 27 of August 2025

  p1();

  p2();
})();
