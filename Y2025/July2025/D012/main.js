/**
 * @param {number} n
 * @param {number} firstPlayer
 * @param {number} secondPlayer
 * @return {number[]}
 */
var earliestAndLatest = function (n, firstPlayer, secondPlayer) {
  const F = Array.from({ length: 30 }, () =>
    Array.from({ length: 30 }, () => new Array(30).fill(0))
  );
  const G = Array.from({ length: 30 }, () =>
    Array.from({ length: 30 }, () => new Array(30).fill(0))
  );

  const dp = (n, f, s) => {
    if (F[n][f][s]) {
      return [F[n][f][s], G[n][f][s]];
    }
    if (f + s === n + 1) {
      return [1, 1];
    }

    // F(n,f,s)=F(n,n+1-s,n+1-f)

    if (f + s > n + 1) {
      const [x, y] = dp(n, n + 1 - s, n + 1 - f);
      F[n][f][s] = x;
      G[n][f][s] = y;
      return [x, y];
    }

    let earliest = Infinity;
    let latest = -Infinity;
    const n_half = Math.floor((n + 1) / 2);
    if (s <= n_half) {
      // On the left or in the middle
      for (let i = 0; i < f; i++) {
        for (let j = 0; j < s - f; j++) {
          const [x, y] = dp(n_half, i + 1, i + j + 2);
          earliest = Math.min(earliest, x);
          latest = Math.max(latest, y);
        }
      }
    } else {
      // s on the right
      const s_prime = n + 1 - s;
      const mid = Math.floor((n - 2 * s_prime + 1) / 2);
      for (let i = 0; i < f; i++) {
        for (let j = 0; j < s_prime - f; j++) {
          const [x, y] = dp(n_half, i + 1, i + j + mid + 2);
          earliest = Math.min(earliest, x);
          latest = Math.max(latest, y);
        }
      }
    }

    F[n][f][s] = earliest + 1;
    G[n][f][s] = latest + 1;
    return [F[n][f][s], G[n][f][s]];
  };

  // F(n,f,s) = F(n,s,f)
  if (firstPlayer > secondPlayer) {
    [firstPlayer, secondPlayer] = [secondPlayer, firstPlayer];
  }
  const [earliest, latest] = dp(n, firstPlayer, secondPlayer);
  return [earliest, latest];

  // Complexity analysis
  // Time : O(N^4 * Log(N))
  // Space : O(2 * (30 ^ 3))
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1900. The Earliest and Latest Rounds Where Players Compete - https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/description/?envType=daily-question&envId=2025-07-12

  console.log(earliestAndLatest(11, 2, 4));
  console.log(earliestAndLatest(5, 1, 5));
};

/**
 * @param {number[][]} mat
 * @return {number}
 */
class Solution2 {
  maxGold(mat) {
    // code here
    // [
    // [1, 3, 3],
    // [2, 1, 4],
    // [0, 6, 4]
    // ]
    // 12 ton

    const N = mat.length;
    const M = mat[0].length;
    let mx = 0;

    // for (let si = 0; si < N; si++) {
    //   const memory = Array.from({ length: N }, () => new Array(M).fill(-1));
    //   let res = this.memoized(mat, si, 0, memory);
    //   mx = Math.max(mx, res);
    // }

    // mx = this.tabulation(mat);
    mx = this.optimised(mat);

    return mx;
  }

  recursion(matrix, cr, cc) {
    if (cc >= matrix[0].length) return 0;
    if (cr < 0 || cr >= matrix.length) return 0;

    let op1 = this.recursion(matrix, cr + 1, cc + 1);
    let op2 = this.recursion(matrix, cr + 0, cc + 1);
    let op3 = this.recursion(matrix, cr - 1, cc + 1);

    return matrix[cr][cc] + Math.max(op1, op2, op3);

    // Complexity analysis
    // Time : O(R * 3^C)
    // Space : O(C) stack space
  }

  memoized(matrix, cr, cc, memory) {
    if (cc >= matrix[0].length) return 0;
    if (cr < 0 || cr >= matrix.length) return 0;

    if (memory[cr][cc] !== -1) return memory[cr][cc];

    let op1 = this.memoized(matrix, cr + 1, cc + 1, memory);
    let op2 = this.memoized(matrix, cr + 0, cc + 1, memory);
    let op3 = this.memoized(matrix, cr - 1, cc + 1, memory);

    return (memory[cr][cc] = matrix[cr][cc] + Math.max(op1, op2, op3));

    // Complexity analysis
    // Time : O(R * (3 * R * C))
    // Space : O(R * C) stack space + O(R * R * C) memory
  }

  tabulation(matrix) {
    const N = matrix.length;
    const M = matrix[0].length;

    const memory = Array.from({ length: N }, () => Array.from({ length: M }, () => 0));
    for (let ri = 0; ri < N; ri++) {
      memory[ri][M - 1] = matrix[ri][M - 1];
    }

    for (let cc = M - 2; cc >= 0; cc--) {
      for (let cr = N - 1; cr >= 0; cr--) {
        let op1 = cr < N - 1 ? memory[cr + 1][cc + 1] : 0;
        let op2 = memory[cr + 0][cc + 1];
        let op3 = cr > 0 ? memory[cr - 1][cc + 1] : 0;

        memory[cr][cc] = matrix[cr][cc] + Math.max(op1, op2, op3);
      }
    }

    let res = Math.max(...memory.map((mr) => mr[0]));
    return res;

    // Complexity analysis
    // Time : O(N * M) + O(N * M) + O(N)
    // Space : O(N * M) memory
  }

  optimised(matrix) {
    const N = matrix.length;
    const M = matrix[0].length;

    let next = Array.from({ length: N }, (_, k) => matrix[k][M - 1]);

    for (let cc = M - 2; cc >= 0; cc--) {
      let curr = new Array(N);

      for (let cr = N - 1; cr >= 0; cr--) {
        let op1 = cr < N - 1 ? next[cr + 1] : 0;
        let op2 = next[cr + 0];
        let op3 = cr > 0 ? next[cr - 1] : 0;

        curr[cr] = matrix[cr][cc] + Math.max(op1, op2, op3);
      }

      next = curr;
    }

    let res = Math.max(...next);
    return res;

    // Complexity analysis
    // Time : O(N) + O(N * M) + O(N)
    // Space : O(N * 2) memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Gold Mine Problem - https://www.geeksforgeeks.org/problems/gold-mine-problem2608/1

  const s2 = new Solution2();
  console.log(
    s2.maxGold([
      [1, 3, 3],
      [2, 1, 4],
      [0, 6, 4],
    ])
  );
  console.log(
    s2.maxGold([
      [1, 3, 1, 5],
      [2, 2, 4, 1],
      [5, 0, 2, 3],
      [0, 6, 1, 2],
    ])
  );
  console.log(
    s2.maxGold([
      [1, 3, 3],
      [2, 1, 4],
      [0, 7, 5],
    ])
  );
};

(() => {
  // Day 12 of July 2025

  p1();

  p2();
})();
