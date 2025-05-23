/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number[][]} edges
 * @return {number}
 */
var maximumValueSum = function (nums, k, edges) {
  // another solution : includes sorting 
  // make xor of all num in nums 
  // choose most profitable pairs 
  // if no pair possible choose original num 

  let sum = 0;
  let XORCount = 0;
  let minLoss = Number.MAX_SAFE_INTEGER;

  for (let num of nums) {
    if ((num ^ k) > num) {
      XORCount++;
      sum += num ^ k;
    } else {
      sum += num;
    }

    minLoss = Math.min(minLoss, Math.abs(num - (num ^ k)));
  }

  if (XORCount & 1) sum -= minLoss;

  return sum;

  // Complexity analysis 
  // Time : O(N) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3068. Find the Maximum Sum of Node Values - https://leetcode.com/problems/find-the-maximum-sum-of-node-values/description/?envType=daily-question&envId=2025-05-23 

  console.log(maximumValueSum([1, 2, 1], 3, [[0, 1], [0, 2]]));
  console.log(maximumValueSum([2, 3], 7, [[0, 1]]));
  console.log(maximumValueSum([7, 7, 7, 7, 7, 7], 3, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]));
};

class Problem2 {
  noOfWays(m, n, x) {
    // code here

    // 1 2 3 4 5 6 
    // 1 2 3 4 5 6 
    // 1 2 3 4 5 6 
    // [1 5 6], [1 6 5], 
    // [2 4 6], [2 5 5], [2 6 4] 
    // [3 3 6], [3 4 5], [3 5 4], [3 6 3]
    // [4 2 6], [4 3 5], [4 4 4], [4 5 3], [4 6 2] 
    // [5 1 6], [5 2 5], [5 3 4], [5 4 3], [5 5 2], [5 6 1]
    // [6 1 5], [6 2 4], [6 3 3], [6 4 2], [6 5 1] 

    // use recursion - try all combinations 
    // roll n dices one by one 
    // explore all possible combinations (sum of values on dice faces)
    // if sum is equal to x - increment count by 1 

    // const memo = Array.from({ length: n }, () => new Array(x + 1).fill(-1));
    // return this.memoization(n, m, 0, x, memo);

    return this.tabulation(n, m, x);
  }

  // n = number of dices 
  // m = number of faces on each dice 
  // i = current dice 
  // x = required sum 
  memoization(n, m, i, x, memo) {
    if (i === n) return x === 0;

    if (memo[i][x] != -1) return memo[i][x];

    let count = 0;

    for (let v = 1; v <= m; v++) {
      if (v <= x) {
        count += this.memoization(n, m, i + 1, x - v, memo);
      }
    }

    return memo[i][x] = count;

    // Complexity analysis 
    // Time : O(M * N * X) 
    // Space : O(N * X) memory + O(N) stack 
  }

  // n = number of dices 
  // m = number of faces on each dice 
  // x = required sum 
  tabulation(n, m, x) {
    let next = new Array(x + 1).fill(0);
    next[0] = 1;

    for (let i = n - 1; i >= 0; i--) {
      let curr = new Array(x + 1).fill(0);

      for (let _x = 1; _x <= x; _x++) {
        for (let v = 1; v <= m; v++) {
          if (v <= _x) {
            curr[_x] += next[_x - v];
          }
        }
      }

      next = curr;
    }

    return next[x];

    // Complexity analysis 
    // Time : O(M * N * X) 
    // Space : O(2 * X) memory 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Dice throw - https://www.geeksforgeeks.org/problems/dice-throw5349/1 

  console.log(new Problem2(6, 3, 12));
  console.log(new Problem2(2, 3, 6));
  console.log(new Problem2(50, 50, 50));
};


(() => {
  // Day 23 of May 2025

  p1();

  p2();
})();
