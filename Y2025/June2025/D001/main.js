/**
 * @param {number} n
 * @param {number} limit
 * @return {number}
 */
var distributeCandies = function (n, limit) {
  const brute = () => {
    let count = 0;

    for (let i = 0; i <= Math.min(n, limit); i++) {
      for (let j = 0; j <= Math.min(n - i, limit); j++) {
        // for k (or child 3)
        let s = n - i - j;
        if (s >= 0 && s <= limit) count++;
      }
    }

    return count;

    // Complexity analysis 
    // Time : O(N^2) 
    // Space : O(1) 
  };

  const better = () => {
    let count = 0;

    const l2 = limit * 2;

    for (let i = 0; i <= Math.min(n, limit); i++) {
      let s = n - i; // remaining candies for other 2 childs 

      // limit will exceed 
      if (s > l2) continue;

      // maximum candies that now can be given to child 2, and 3 
      let pmax = Math.min(limit, s);
      // minimum candies that now can be given to child 2, and 3 
      let pmin = Math.max(s - limit, 0);

      // number of ways (valid) to distribute n candies 
      // if child 1 gets i candies 
      // and child 2, 3 gets distributed s candies 
      count += pmax - pmin + 1;
    }

    return count;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) 
  };

  const optimal = () => {
    // combinatrics - inclusion and exclusion principle 

    const combination = (n, r) => {
      if (n < 0) return 0;
      return ((n * (n - 1)) / r);
    };

    // total possible distributions 
    const t = combination(n + 2, 2);

    // total invalid distributions 
    const c1 = 3 * combination(n - limit + 1, 2); // one children gets more then limit candies 
    const c2 = 3 * combination(n - (limit + 1) * 2 + 2, 2); // two children gets more then limit candies 
    const c3 = combination(n - 3 * (limit + 1) + 2, 2); // three children gets more then limit candies 

    // total valid distributions 
    const valids = t - c1 + c2 - c3;

    return valids;

    // Complexity analysis 
    // Time : O(1) 
    // Space : O(1) 
  };

  // return brute();
  // return better();
  return optimal();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2929. Distribute Candies Among Children II  - https://leetcode.com/problems/distribute-candies-among-children-ii/description/?envType=daily-question&envId=2025-06-01 

  console.log(distributeCandies(5, 2));
  console.log(distributeCandies(3, 3));
};

/**
 * @param {number[][]} mat1
 * @param {number[][]} mat2
 * @param {number} x
 * @returns {number}
 */

class Problem2 {
  countPairs(mat1, mat2, x) {
    // code here

    // return this.solve1(mat1, mat2, x);

    return this.solve2(mat1, mat2, x);
  }

  solve2(mat1, mat2, x) {
    let n = mat1.length;
    let N = n * n - 1;

    let count = 0;

    let i = 0;
    let j = N;

    while (i <= N && j >= 0) {
      let indexA = [Math.floor(i / n), i % n];
      let indexB = [Math.floor(j / n), j % n];

      let a = mat1[indexA[0]][indexA[1]];
      let b = mat2[indexB[0]][indexB[1]];

      if (a + b === x) {
        count++;
        i++;
        j--;
      } else if (a + b < x) {
        i++;
      } else {
        j--;
      }
    }

    return count;

    // Complexity analysis 
    // Time : O(2 * N*N) 
    // Space : O(1) 
  }

  solve1(mat1, mat2, x) {

    const N = mat1.length;

    let count = 0;

    const seen = new Set();
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        seen.add(mat1[i][j]);
      }
    }

    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        let need = x - mat2[i][j];
        if (seen.has(need)) {
          count++;
        }
      }
    }

    return count;

    // Complexity analysis 
    // Time : O(N*N) + (N*N * Log(N*N)) 
    // Space : O(N*N) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Count pairs Sum in matrices - https://www.geeksforgeeks.org/problems/count-pairs-sum-in-matrices4332/1 

  {
    const mat1 = [[1, 5, 6], [8, 10, 11], [15, 16, 18]];
    const mat2 = [[2, 4, 7], [9, 10, 12], [13, 16, 20]];
    const x = 21;

    console.log(new Problem2().countPairs(mat1, mat2, x));
  }

  {
    const mat1 = [[1, 2], [3, 4]];
    const mat2 = [[4, 5], [6, 7]];
    const x = 10;

    console.log(new Problem2().countPairs(mat1, mat2, x));
  }
};


(() => {
  // Day 1 of June 2025

  p1();

  p2();
})();
