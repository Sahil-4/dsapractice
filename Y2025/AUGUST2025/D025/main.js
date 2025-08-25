/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var findDiagonalOrder = function (mat) {
  // start point = [0][0]
  // direction rules :
  // on up [r - 1][c + 1]
  // on down [r + 1][c - 1]
  // traversal logic :
  // print current cell
  // move to next cell as per direction rules
  // if next cell is invalid,
  //      if direction is up
  //      move to next col, or next row
  //      if direction is down
  //      move to next row, or prev col
  // if no next cell is valid break the loop

  const M = mat.length;
  const N = mat[0].length;

  const traversalOutput = new Array();

  const currCell = { r: 0, c: 0 };
  let currDirection = 1; // 1 : UP, 0 : DOWN

  const invalidCell = (r, c) => r < 0 || r >= M || c < 0 || c >= N;

  while (true) {
    // put current element in output
    traversalOutput.push(mat[currCell.r][currCell.c]);

    // move to next cell
    if (currDirection) {
      // UP [r - 1][c + 1] // no direction change
      // UP [r + 0][c + 1] // direction change
      // UP [r + 1][c + 0] // direction change
      if (!invalidCell(currCell.r - 1, currCell.c + 1)) {
        currCell.r -= 1;
        currCell.c += 1;
      } else if (!invalidCell(currCell.r + 0, currCell.c + 1)) {
        currCell.r += 0;
        currCell.c += 1;
        currDirection = !currDirection;
      } else {
        currCell.r += 1;
        currCell.c += 0;
        currDirection = !currDirection;
      }
    } else {
      // DOWN [r + 1][c - 1] // no direction change
      // DOWN [r + 1][c + 0] // direction change
      // DOWN [r + 0][c + 1] // direction change
      if (!invalidCell(currCell.r + 1, currCell.c - 1)) {
        currCell.r += 1;
        currCell.c -= 1;
      } else if (!invalidCell(currCell.r + 1, currCell.c + 0)) {
        currCell.r += 1;
        currCell.c += 0;
        currDirection = !currDirection;
      } else {
        currCell.r += 0;
        currCell.c += 1;
        currDirection = !currDirection;
      }
    }

    if (invalidCell(currCell.r, currCell.c)) {
      break;
    }
  }

  return traversalOutput;

  // Complexity analysis
  // Time : O(N * M)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 498. Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/description/?envType=daily-question&envId=2025-08-25

  console.log(
    findDiagonalOrder([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ])
  );
  console.log(
    findDiagonalOrder([
      [1, 2],
      [3, 4],
    ])
  );
  console.log(
    findDiagonalOrder([
      [1, 2, 3, 4],
      [5, 6, 7, 8],
    ])
  );
  console.log(
    findDiagonalOrder([
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
    ])
  );
  console.log(findDiagonalOrder([[1], [2], [3], [4]]));
  console.log(
    findDiagonalOrder([
      [1, 5],
      [2, 6],
      [3, 7],
      [4, 8],
    ])
  );
  console.log(
    findDiagonalOrder([
      [1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10],
      [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20],
    ])
  );
  console.log(
    findDiagonalOrder([
      [1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10],
      [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20],
      [21, 22, 23, 24, 25],
    ])
  );
};

/**
 * @param {number[]} arr
 * @param {number} k
 * @returns {number}
 */
class Solution2 {
  maximizeMedian(arr, k) {
    // code here
    // 1, 3, 6, 4, 2
    // [1, 2, 3, 4, 6]
    // 3 4 6 (op = 10)
    // 4 4 6 (op = 9)
    // 4 5 6 (op = 8)
    // 5 5 6 (op = 7)
    // 5 6 6 (op = 6)
    // 6 6 6 (op = 5)
    // 6 6 7 (op = 4)
    // 6 7 7 (op = 3)
    // 7 7 7 (op = 2)
    // 7 7 8 (op = 1)
    // 7 8 8 (op = 0)
    // median = 7
    // brute force : keep priority queue with median elements and its all right neighbours
    // perform operations k times
    // take out smallest element increment it by one
    // put incremented element back to priority queue
    // but this will take k * log(n) which is not efficient for this problem constraint
    // key observaton :
    // we need to increment mid to N - 1 elements
    // we can increment them by 0, to K
    // so min median can be element + 0, and maximum can be element + K
    // now we can use this as search space and perform binary search algorithm to find the output

    return this.binarySearchVersion(arr, k);
  }

  binarySearchVersion(arr, k) {
    arr.sort((a, b) => a - b);
    let n = arr.length;

    // compute initial median floor if even length
    let iniMedian = arr[Math.floor(n / 2)];
    if (n % 2 === 0) {
      iniMedian += arr[n / 2 - 1];
      iniMedian = Math.floor(iniMedian / 2);
    }

    let low = iniMedian,
      high = iniMedian + k;
    let bestMedian = iniMedian;

    // binary search to find maximum
    // achievable median
    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      if (this.isPossible(arr, mid, k)) {
        bestMedian = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return bestMedian;
  }

  // check if we can make the median at least
  // 'target' using at most 'k' operation
  isPossible(arr, target, k) {
    let n = arr.length;

    if (n % 2 === 1) {
      // for odd-sized array, consider elements from
      // middle to end
      for (let i = Math.floor(n / 2); i < n; ++i) {
        if (arr[i] < target) k -= target - arr[i];

        if (k < 0) break;
      }
    } else {
      // for even-sized array, handle two middle
      // elements separately
      if (arr[n / 2] <= target) {
        k -= target - arr[n / 2];
        k -= target - arr[n / 2 - 1];
      } else {
        k -= 2 * target - (arr[n / 2] + arr[n / 2 - 1]);
      }
      // process remaining elements to the right
      for (let i = n / 2 + 1; i < n; ++i) {
        if (arr[i] < target) k -= target - arr[i];

        if (k < 0) break;
      }
    }

    return k >= 0;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Maximize median after doing k addition operation - https://www.geeksforgeeks.org/problems/maximize-median-after-doing-k-addition-operation/1

  const s2 = new Solution2();
  console.log(s2.maximizeMedian([1, 3, 4, 5], 3));
  console.log(s2.maximizeMedian([1, 3, 6, 4, 2], 10));
};

(() => {
  // Day 25 of August 2025

  p1();

  p2();
})();
