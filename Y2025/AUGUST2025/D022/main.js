/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumArea = function (grid) {
  // find min and max row and col in which 1 appeared
  // then find width and height of rectangle
  // width = maxCol - minCol + 1
  // height = maxRow - minRow + 1
  // then find area
  // ar = width * height
  // return area 'ar'
  // Logic behind solution : find the edges that contains all ones (exactly what problem has asked)

  const R = grid.length;
  const C = grid[0].length;

  let [maxCol, minCol] = [-1001, 1000];
  let [maxRow, minRow] = [-1001, 1000];

  for (let r = 0; r < R; r++) {
    for (let c = 0; c < C; c++) {
      if (grid[r][c] === 1) {
        [maxCol, minCol] = [Math.max(maxCol, c), Math.min(minCol, c)];
        [maxRow, minRow] = [Math.max(maxRow, r), Math.min(minRow, r)];
      }
    }
  }

  const width = maxCol - minCol + 1;
  const height = maxRow - minRow + 1;
  const ar = width * height;

  return ar;

  // Complexity analysis
  // Time : O(R * C)
  // Space : O(4)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3195. Find the Minimum Area to Cover All Ones I - https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description/?envType=daily-question&envId=2025-08-22

  console.log(
    minimumArea([
      [0, 1, 0],
      [1, 0, 1],
    ])
  );
  console.log(
    minimumArea([
      [1, 0],
      [0, 0],
    ])
  );
  console.log(
    minimumArea([
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [1, 0, 0, 1],
    ])
  );
  console.log(
    minimumArea([
      [0, 1, 1, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [1, 0, 0, 1],
    ])
  );
  console.log(
    minimumArea([
      [0, 0, 1, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [1, 0, 0, 1],
    ])
  );
};

/**
 * @param {number[][]} mat
 * @returns {number}
 */
class Solution2 {
  median(mat) {
    // code here
    // first solution :
    // use merge n sorted array (of size m)
    // to produce a larger array of n * m elements
    // then return the middle index
    // another solution :
    // use binary search on output
    // [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
    // output can only be within [1, 9]
    // and whatever will be the output it will have (((N * M) - 1) / 2) elements on left and right
    // perform binary search on output range [1, 9] (min(mat), max(mat))
    // for each mid find how many elements are on its left
    // shrink the search space as
    // if count <= requiredCount : update low = mid + 1
    // else update high = mid - 1
    // at the end return low
    // initial search space
    // [1, 2, 3, 3, 5, 6, 6, 9, 9]
    // after first iteration
    // suppose mid = 5
    // count of elements <= 5 is 5
    // required count = 4
    // since count > requiredCount → high = mid - 1
    // search space becomes [1, 2, 3, 3, 5]
    // next iteration mid = 2
    // count of elements <= 2 is 2
    // required count = 4
    // since count <= requiredCount → low = mid + 1
    // search space becomes [3, 3, 5]
    // next iteration mid = 3
    // count of elements <= 3 is 4
    // required count = 4
    // since count <= requiredCount → low = mid + 1
    // search space becomes [5]
    // low = 5, high = 5, loop ends
    // answer = low = 5
    // now how to find count efficiently ?
    // we have n sorted rows on each row we can easily apply binary search
    // we will use binary search to find first index where element is just greater then given mid val
    // this index is count of element <= mid in this row
    // repeat this for all rows and sum up all indices
    // and finally return the count

    // dimensions
    const N = mat.length;
    const M = mat[0].length;

    const requiredCount = (N * M - 1) / 2;

    // search space
    let low = 2001;
    let high = -2001;
    for (let r = 0; r < N; r++) {
      low = Math.min(low, mat[r][0]);
      high = Math.max(high, mat[r][M - 1]);
    }

    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      if (this.count(mat, N, M, mid) <= requiredCount) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return low;

    // Complexity analysis
    // Time : O(Log(max(mat) - min(mat)) * (N * Log(M)))
    // Space : O(1)
  }

  count(mat, N, M, mid) {
    let cnt = 0;
    for (let r = 0; r < N; r++) {
      cnt += this.upperBound(mat[r], M, mid);
    }
    return cnt;
  }

  upperBound(arr, M, val) {
    let low = 0;
    let high = M - 1;
    let ans = M;

    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      if (arr[mid] > val) {
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
  // Problem 2 : POTD Geeksforgeeks Median in a row-wise sorted Matrix - https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1

  const s2 = new Solution2();
  console.log(
    s2.median([
      [1, 3, 5],
      [2, 6, 9],
      [3, 6, 9],
    ])
  );
  console.log(
    s2.median([
      [2, 4, 9],
      [3, 6, 7],
      [4, 7, 10],
    ])
  );
  console.log(s2.median([[3], [4], [8]]));
};

(() => {
  // Day 22 of August 2025

  p1();

  p2();
})();
