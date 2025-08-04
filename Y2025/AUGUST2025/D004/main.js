/**
 * @param {number[]} fruits
 * @return {number}
 */
var totalFruit = function (fruits) {
  const N = fruits.length;

  // maximum number of adjacent trees I can take fruits from (i.e. having only two elements)
  let maxPossibleTrees = 0;

  const basket1 = [null, 0]; // [type, count]
  const basket2 = [null, 0]; // [type, count]

  // helper function to update basket
  // t = type of fruit
  // inc = count to increment (-count to decrement)
  // returns boolean shows able to add fruit in any of the basket or not
  const update = (t, inc) => {
    if (basket1[0] === t) {
      basket1[1] += inc;
    } else if (basket2[0] === t) {
      basket2[1] += inc;
    } else if (basket1[1] === 0) {
      basket1[0] = t;
      basket1[1] += inc;
    } else if (basket2[1] === 0) {
      basket2[0] = t;
      basket2[1] += inc;
    } else {
      return false;
    }
    return true;
  };

  // ! find largest subarray with at most two unique elements
  for (let l = 0, r = 0; r < N; r++) {
    // can I take fruits[r] in any of my basket ?
    while (!update(fruits[r], 1)) {
      // if I cant - I remove fruits from left to right
      update(fruits[l], -1);
      l++;
    }

    // update count of adjacent trees we can pick fruits from
    maxPossibleTrees = Math.max(maxPossibleTrees, r - l + 1);
  }

  return maxPossibleTrees;

  // Complexity analysis
  // Time : O(2N)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 904. Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets/description/?envType=daily-question&envId=2025-08-04

  console.log(totalFruit([1, 2, 1]));
  console.log(totalFruit([0, 1, 2, 2]));
  console.log(totalFruit([1, 2, 3, 2, 2]));
  console.log(totalFruit([1, 2, 3, 1, 2]));
  console.log(totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]));
  console.log(totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]));
};

/**
 * @param {number[][]} mat
 * @return {number}
 */
class Solution2 {
  maxRectSum(mat) {
    // code here
    const N = mat.length;
    const M = mat[0].length;

    let output = -1001;

    for (let cs = 0; cs < M; cs++) {
      const rowSum = new Array(N).fill(0);
      for (let ce = cs; ce < M; ce++) {
        for (let r = 0; r < N; r++) {
          rowSum[r] += mat[r][ce];
        }

        let rowsColSum = 0;
        let maxxRowsColSum = -1001;
        for (let r = 0; r < N; r++) {
          rowsColSum += rowSum[r];
          maxxRowsColSum = Math.max(maxxRowsColSum, rowsColSum);
          if (rowsColSum < 0) rowsColSum = 0;
        }

        output = Math.max(output, maxxRowsColSum);
      }
    }

    return output;

    // Complexity analysis
    // Time : O(M * M * N)
    // Space : O(N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Maximum sum Rectangle - https://www.geeksforgeeks.org/problems/maximum-sum-rectangle2948/1

  const s2 = new Solution2();
  console.log(
    s2.maxRectSum([
      [1, 2, -1, -4, -20],
      [-8, -3, 4, 2, 1],
      [3, 8, 10, 1, 3],
      [-4, -1, 1, 7, -6],
    ])
  );
  console.log(
    s2.maxRectSum([
      [-1, -2],
      [-3, -4],
    ])
  );
};

(() => {
  // Day 4 of August 2025

  p1();

  p2();
})();
