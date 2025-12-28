/**
 * @param {number[]} nums
 * @return {number}
 */
var countMaxOrSubsets = function (nums) {
  // problem 1 : find maximum possible "OR" of subset say "maxORSub"
  // problem 2 : count subset with maxORSub "OR" of its elements
  // combined : use cached recursion
  // better : do not combine and use count subset with maxORSub OR Logic with memoization
  // optimizations : use tabulation

  const N = nums.length;

  // maximum possible "OR"
  let maxOR = nums.reduce((acc, num) => acc | num, 0);

  // count of maxOR
  let maxORCount = 0;

  // count subset with given maxOR OR
  const recursion = (index, value) => {
    // value = current path OR
    if (index >= N) return value === maxOR;

    const skip = recursion(index + 1, value);
    const take = recursion(index + 1, value | nums[index]);

    return skip + take;

    // Complexity analysis
    // Time : O(2 ^ N)
    // Space : O(N) stack
  };

  const memoize = (index, value, memo) => {
    // value = current path OR
    if (index >= N) return value === maxOR;

    if (memo[index][value] !== null) return memo[index][value];

    const skip = memoize(index + 1, value, memo);
    const take = memoize(index + 1, value | nums[index], memo);

    return (memo[index][value] = skip + take);

    // Complexity analysis
    // Time : O(2 * N * MaxOR)
    // Space : O(N) stack + O(N * MaxOR)
  };

  const tabulation = () => {
    const memory = Array.from({ length: N + 1 }, () => new Array(maxOR + 1).fill(0));

    memory[N][maxOR] = 1;

    for (let index = N - 1; index >= 0; index--) {
      for (let value = 0; value <= maxOR; value++) {
        const skip = memory[index + 1][value];
        const take = memory[index + 1][value | nums[index]];
        memory[index][value] = skip + take;
      }
    }

    return memory[0][0];

    // Complexity analysis
    // Time : O(N * MaxOR)
    // Space : O(N * MaxOR)
  };

  const optimised = () => {
    let next = new Array(maxOR + 1).fill(0);
    next[maxOR] = 1;

    for (let index = N - 1; index >= 0; index--) {
      let curr = new Array(maxOR + 1).fill(0);

      for (let value = 0; value <= maxOR; value++) {
        const skip = next[value];
        const take = next[value | nums[index]];
        curr[value] = skip + take;
      }

      next = curr;
    }

    return next[0];

    // Complexity analysis
    // Time : O(N * MaxOR)
    // Space : O(2 * MaxOR)
  };

  // maxORCount = recursion(0, 0);
  // const memory = Array.from({ length: N }, () => new Array(maxOR + 1).fill(null));
  // maxORCount = memoize(0, 0, memory);
  // maxORCount = tabulation();
  maxORCount = optimised();

  return maxORCount;
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2044. Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/?envType=daily-question&envId=2025-07-28

  console.log(countMaxOrSubsets([3, 1]));
  console.log(countMaxOrSubsets([2, 2, 2]));
  console.log(countMaxOrSubsets([3, 2, 1, 5]));
};

/**
 * @param {number[][]} mat
 * @returns {number}
 */
class Solution2 {
  balanceSums(mat) {
    // code here
    // find sum or each row, and each col
    // get maximum value out of them
    // this is our boundary,
    // to which we should increase the sum of any row or col
    // !!!!!! next to calculate number of operations !!!!!!!!
    // for this we can just rely on either row or col sum as its a matrix
    // and performing operation on any row will affect any other col
    // this will itself make the other thing (row, or col) balanced
    // just rely on row sum
    // compute row sum
    // calculate how much more its required to make sum of this row to reach boundary
    // do this for every row and sum all of them
    // finally return this sum as output

    const N = mat.length;

    let boundary = 0;
    for (let i = 0; i < N; i++) {
      let rowSum = 0;
      let colSum = 0;

      for (let j = 0; j < N; j++) {
        rowSum += mat[i][j];
        colSum += mat[j][i];
      }

      boundary = Math.max(boundary, rowSum);
      boundary = Math.max(boundary, colSum);
    }

    let operations = 0;
    for (let i = 0; i < N; i++) {
      let rowSum = 0;

      for (let j = 0; j < N; j++) {
        rowSum += mat[i][j];
      }

      operations += boundary - rowSum;
    }

    return operations;

    // Complexity analysis
    // Time : O(N * N) + O(N * N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Make Matrix Beautiful - https://www.geeksforgeeks.org/problems/make-matrix-beautiful-1587115620/1

  const s2 = new Solution2();
  console.log(
    s2.balanceSums([
      [1, 2],
      [3, 4],
    ])
  );
  console.log(
    s2.balanceSums([
      [1, 2, 3],
      [4, 2, 3],
      [3, 2, 1],
    ])
  );
  console.log(
    s2.balanceSums([
      [2, 2, 3, 5, 4],
      [3, 5, 1, 2, 2],
      [5, 4, 3, 2, 5],
      [7, 8, 9, 2, 5],
      [1, 2, 3, 4, 7],
    ])
  );
};

(() => {
  // Day 28 of July 2025

  p1();

  p2();
})();
