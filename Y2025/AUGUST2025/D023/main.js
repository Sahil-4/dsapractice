/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumSum = function (grid) {
  const rotate90 = (grid) => {
    const M = grid.length;
    const N = grid[0].length;

    const rotated = Array.from({ length: N }, () => new Array(M).fill(0));
    for (let i = 0; i < M; i++) {
      for (let j = 0; j < N; j++) {
        rotated[j][M - i - 1] = grid[i][j];
      }
    }

    return rotated;
  };

  const minimumArea = (grid, ri, R, ci, C) => {
    let [maxCol, minCol] = [-1001, 1000];
    let [maxRow, minRow] = [-1001, 1000];

    for (let r = ri; r < R; r++)
      for (let c = ci; c < C; c++) {
        if (grid[r][c] !== 1) continue;
        [maxCol, minCol] = [Math.max(maxCol, c), Math.min(minCol, c)];
        [maxRow, minRow] = [Math.max(maxRow, r), Math.min(minRow, r)];
      }

    return (maxCol - minCol + 1) * (maxRow - minRow + 1);
  };

  let result = Number.MAX_SAFE_INTEGER;

  const helper = (grid) => {
    const M = grid.length;
    const N = grid[0].length;

    // case 1 & 2
    for (let ri = 1; ri < M; ri++) {
      for (let ci = 1; ci < N; ci++) {
        const topLeft = minimumArea(grid, 0, ri, 0, ci);
        const topRight = minimumArea(grid, 0, ri, ci, N);
        const bottom = minimumArea(grid, ri, M, 0, N);
        result = Math.min(result, topLeft + topRight + bottom);

        const top = minimumArea(grid, 0, ri, 0, N);
        const bottomLeft = minimumArea(grid, ri, M, 0, ci);
        const bottomRight = minimumArea(grid, ri, M, ci, N);
        result = Math.min(result, top + bottomLeft + bottomRight);
      }
    }

    // case 3
    for (let ri1 = 1; ri1 < M; ri1++) {
      for (let ri2 = ri1 + 1; ri2 < M; ri2++) {
        const top = minimumArea(grid, 0, ri1, 0, N);
        const middle = minimumArea(grid, ri1, ri2, 0, N);
        const bottom = minimumArea(grid, ri2, M, 0, N);
        result = Math.min(result, top + middle + bottom);
      }
    }
  };

  helper(grid);
  helper(rotate90(grid));

  return result;

  // Complexity analysis
  // Time : O(2 * ((M * N * M * N) + (M * M * M * N))) + O(M * N)
  // Space : O(MN)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3197. Find the Minimum Area to Cover All Ones II - https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/description/?envType=daily-question&envId=2025-08-23

  console.log(
    minimumSum([
      [1, 0, 1],
      [1, 1, 1],
    ])
  );
  console.log(
    minimumSum([
      [1, 0, 1, 0],
      [0, 1, 0, 1],
    ])
  );
};

/**
 * @param {number[]} arr
 * @param {number} k
 * @returns {number}
 */
class Solution2 {
  findPages(arr, k) {
    // code here
    if (arr.length < k) return -1;

    // binary search on answer

    // output range
    let low = Math.max(...arr);
    let high = arr.reduce((acc, e) => acc + e, 0);

    let ans = high;

    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      if (this.isPossibleDistribution(arr, k, mid)) {
        ans = mid;
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    return ans;

    // Complexity analysis
    // Time : O(Log(SUM(arr) - MAX(Arr)) * N)
    // Space : O(1)
  }

  isPossibleDistribution(arr, k, maxPages) {
    let students = 1;

    for (let i = 0, pages = 0; i < arr.length; i++) {
      if (pages + arr[i] <= maxPages) pages += arr[i];
      else (pages = arr[i]), students++;
    }

    return students <= k;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Allocate Minimum Pages - https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

  const s2 = new Solution2();
  console.log(s2.findPages([12, 34, 67, 90], 2));
  console.log(s2.findPages([12, 34, 67, 90], 4));
  console.log(s2.findPages([12, 34, 67, 90], 1));
  console.log(s2.findPages([12, 34, 67, 90], 5));
};

(() => {
  // Day 23 of August 2025

  p1();

  p2();
})();
