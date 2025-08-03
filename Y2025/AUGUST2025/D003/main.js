/**
 * @param {number[][]} fruits
 * @param {number} startPos
 * @param {number} k
 * @return {number}
 */
var maxTotalFruits = function (fruits, startPos, k) {
  const N = fruits.length;

  const lowerBound = (key) => {
    // lowerBound = greater then equal to key
    let low = 0;
    let high = N;

    while (low < high) {
      let mid = Math.floor((low + high) / 2);

      if (fruits[mid][0] >= key) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }

    return low;
  };

  const upperBound = (key) => {
    // upperBound = greater then key
    let low = 0;
    let high = N;

    while (low < high) {
      let mid = Math.floor((low + high) / 2);

      if (fruits[mid][0] > key) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }

    return low;
  };

  const prefixSum = new Array(N);
  prefixSum[0] = fruits[0][1];
  for (let i = 1; i < N; i++) {
    prefixSum[i] = fruits[i][1] + prefixSum[i - 1];
  }

  let maxFruits = 0;

  for (let d = 0; d <= Math.floor(k / 2); d++) {
    const remainK = k - 2 * d;

    // case 1 : move left, then right
    let leftPosition = startPos - d;
    let rightPosition = startPos + remainK;

    let leftIndex = lowerBound(leftPosition);
    let rightIndex = upperBound(rightPosition) - 1;

    if (leftIndex <= rightIndex) {
      const total = prefixSum[rightIndex] - (leftIndex > 0 ? prefixSum[leftIndex - 1] : 0);
      maxFruits = Math.max(maxFruits, total);
    }

    // case 2 : move right, then left
    leftPosition = startPos - remainK;
    rightPosition = startPos + d;

    leftIndex = lowerBound(leftPosition);
    rightIndex = upperBound(rightPosition) - 1;

    if (leftIndex <= rightIndex) {
      const total = prefixSum[rightIndex] - (leftIndex > 0 ? prefixSum[leftIndex - 1] : 0);
      maxFruits = Math.max(maxFruits, total);
    }
  }

  return maxFruits;

  // Complexity analysis
  // Time : O(N) + O((K/2) * (4 * Log(N)))
  // Space : O(N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2106. Maximum Fruits Harvested After at Most K Steps - https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/description/?envType=daily-question&envId=2025-08-03

  console.log(
    maxTotalFruits(
      [
        [2, 8],
        [6, 3],
        [8, 6],
      ],
      5,
      4
    )
  );
  console.log(
    maxTotalFruits(
      [
        [0, 9],
        [4, 1],
        [5, 7],
        [6, 2],
        [7, 4],
        [10, 9],
      ],
      5,
      4
    )
  );
  console.log(
    maxTotalFruits(
      [
        [0, 3],
        [6, 4],
        [8, 5],
      ],
      3,
      2
    )
  );
};

/**
 * @param {number[][]} mat
 * @param {number[][]} opr
 * @returns {number[][]}
 */
class Solution2 {
  applyDiff2D(mat, opr) {
    // code here

    // return this.brute(mat, opr);

    return this.optimal(mat, opr);
  }

  optimal(mat, opr) {
    // opr[][] = [[2, 0, 0, 1, 1], [-1, 1, 0, 2, 2]]
    // [1 2 3]
    // [1 1 0]
    // [4 -2 2]
    // difference array operations - !INDEX_OUT_OF_BOUND ahead
    // diff[r1][c1] += v;
    // diff[r2 + 1][c1] -= v;
    // diff[r1][c2 + 1] -= v;
    // diff[r2 + 1][c2 + 1] += v;
    // difference array (after q = 0)
    // [+2 +0 -2]
    // [+0 +0 +0]
    // [-2 +0 +2]
    // difference array (after q = 1)
    // [+2 +0 -2]
    // [-1 +0 +0]
    // [-2 +0 +2]
    // built - row wise prefix sum
    // [+2 +2 +0]
    // [-1 -1 -1]
    // [-2 -2 +0]
    // built - col wise prefix sum
    // [+2 +2 +0]
    // [+1 +1 -1]
    // [-1 -1 -1]
    // final output
    // [1+2 2+2 3+0]
    // [1+1 1+1 0-1]
    // [4-1 -2-1 2-1]
    // final output
    // [3 4 3]
    // [2 2 -1]
    // [3 -3 1]

    const N = mat.length;
    const M = mat[0].length;

    // build difference array
    const diff = Array.from({ length: N }, () => new Array(M).fill(0));
    for (let [v, r1, c1, r2, c2] of opr) {
      diff[r1][c1] += v;
      if (r2 + 1 < N) diff[r2 + 1][c1] -= v;
      if (c2 + 1 < M) diff[r1][c2 + 1] -= v;
      if (r2 + 1 < N && c2 + 1 < M) diff[r2 + 1][c2 + 1] += v;
    }

    // row wise prefix sum
    for (let r = 0; r < N; r++) {
      for (let c = 1; c < M; c++) {
        diff[r][c] += diff[r][c - 1];
      }
    }

    // col wise prefix sum
    for (let c = 0; c < M; c++) {
      for (let r = 1; r < N; r++) {
        diff[r][c] += diff[r - 1][c];
      }
    }

    const cmat = Array.from({ length: N }, () => new Array(M));
    // compute final output
    for (let r = 0; r < N; r++) {
      for (let c = 0; c < M; c++) {
        cmat[r][c] = mat[r][c] + diff[r][c];
      }
    }

    return cmat;

    // Complexity analysis
    // Time : O(Q) + O(4 * (N * M))
    // Space : O(N * M)
  }

  brute(mat, opr) {
    // opr[][] = [[2, 0, 0, 1, 1], [-1, 1, 0, 2, 2]]
    // [1 2 3]
    // [1 1 0]
    // [4 -2 2]
    // after first operation
    // [3 4 3]
    // [3 3 0]
    // [4 -2 2]
    // after second operation
    // [3 4 3]
    // [2 2 -1]
    // [3 -3 1]
    const cmat = JSON.parse(JSON.stringify(mat));

    for (let [v, r1, c1, r2, c2] of opr) {
      for (let r = r1; r <= r2; r++) {
        for (let c = c1; c <= c2; c++) {
          cmat[r][c] += v;
        }
      }
    }

    return cmat;

    // Complexity analysis
    // Time : O(Q * N * M)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks 2D Difference Array - https://www.geeksforgeeks.org/problems/2-d-difference-array/1

  const s2 = new Solution2();
  console.log(
    s2.applyDiff2D(
      [
        [1, 2, 3],
        [1, 1, 0],
        [4, -2, 2],
      ],
      [
        [2, 0, 0, 1, 1],
        [-1, 1, 0, 2, 2],
      ]
    )
  );
};

(() => {
  // Day 3 of August 2025

  p1();

  p2();
})();
