/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function (ratings) {
  // Approach - 
  // Initially give each child 1 candy (greedy) 
  // now perform two traversals 
  // in first iteration check ith child rating with its left one 
  // if ith child rating is more then left child it should get more candies then left 
  // in second iteration check ith child with its right child 
  // and do same 
  // [1 0 2] - ratings 
  // [1 1 1] - i0 
  // [1 1 2] - i1 
  // [2 1 2] - i2 

  const N = ratings.length;

  const candies = new Array(N).fill(1);

  for (let i = 1; i < N; i++) {
    if (ratings[i] > ratings[i - 1]) {
      candies[i] += candies[i - 1];
    }
  }

  for (let i = N - 2; i >= 0; i--) {
    if (ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1]) {
      candies[i] = candies[i + 1] + 1;
    }
  }

  return candies.reduce((acc, e) => acc + e, 0);

  // Complexity analysis 
  // Time : O(3N) 
  // Space : O(N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 135. Candy - https://leetcode.com/problems/candy/description/?envType=daily-question&envId=2025-06-02 

  console.log(candy([1, 0, 2]));
  console.log(candy([1, 2, 2]));
  console.log(candy([1, 2, 3, 4, 4, 5]));
  console.log(candy([1, 2, 3, 4, 5]));
  console.log(candy([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]));
  console.log(candy([6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 0]));
};

/**
 * @param {number[][]} grid
 * @returns {number}
 */

class Problem2 {
  uniquePaths(grid) {
    // code here
    const n = grid.length;
    const m = grid[0].length;

    // edge case - first cell is blocked 
    if (grid[0][0] === 1) return 0;
    // edge case - last cell is blocked 
    if (grid[n - 1][m - 1] === 1) return 0;

    // const memo = Array.from({ length: n }, () => new Array(m).fill(-1));
    // return this.memoization(grid, 0, 0, memo);

    // return this.tabulation(grid);

    return this.optimised(grid);
  }

  memoization(grid, i, j, memo) {
    const n = grid.length - 1;
    const m = grid[0].length - 1;

    if (i === n && j === m) return 1;
    if (i > n || j > m) return 0;
    if (grid[i][j] === 1) return 0;

    if (memo[i][j] !== -1) return memo[i][j];

    let left = this.memoization(grid, i, j + 1, memo);
    let right = this.memoization(grid, i + 1, j, memo);

    return memo[i][j] = (left + right);

    // Complexity analysis 
    // Time : O(2 * N*M) 
    // Space : O(N*M) memory + O(N+M) stack 
  }

  tabulation(grid) {
    const n = grid.length;
    const m = grid[0].length;

    const memo = Array.from({ length: n + 1 }, () => new Array(m + 1).fill(0));

    for (let i = n - 1; i >= 0; i--) {
      for (let j = m - 1; j >= 0; j--) {
        if ((i === n - 1) && (j === m - 1)) {
          memo[n - 1][m - 1] = 1;
          continue;
        }

        if (grid[i][j] === 1) {
          memo[i][j] = 0;
        } else {
          let left = memo[i][j + 1];
          let right = memo[i + 1][j];

          memo[i][j] = (left + right);
        }
      }
    }

    return memo[0][0];

    // Complexity analysis 
    // Time : O(N*M) 
    // Space : O(N*M) 
  }

  optimised(grid) {
    const n = grid.length;
    const m = grid[0].length;

    let next = new Array(m + 1).fill(0);

    for (let i = n - 1; i >= 0; i--) {
      let curr = new Array(m + 1).fill(0);

      for (let j = m - 1; j >= 0; j--) {
        if ((i === n - 1) && (j === m - 1)) {
          curr[j] = 1;
          continue;
        }

        if (grid[i][j] === 1) {
          curr[j] = 0;
        } else {
          let left = curr[j + 1];
          let right = next[j];

          curr[j] = (left + right);
        }
      }

      next = curr;
    }

    return next[0];

    // Complexity analysis 
    // Time : O(N*M) 
    // Space : O(2M) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Unique Paths in a Grid - https://www.geeksforgeeks.org/problems/unique-paths-in-a-grid--170647/1 

  console.log(new Problem2().uniquePaths([[0, 0, 0]]));
  console.log(new Problem2().uniquePaths([[0, 0, 1]]));
  console.log(new Problem2().uniquePaths([[1, 0, 0]]));
  console.log(new Problem2().uniquePaths([[0, 0, 0], [0, 0, 0], [0, 0, 0]]));
  console.log(new Problem2().uniquePaths([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]));
};


(() => {
  // Day 2 of June 2025

  p1();

  p2();
})();
