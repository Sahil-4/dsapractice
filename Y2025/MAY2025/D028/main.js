/**
 * @param {number[][]} edges1
 * @param {number[][]} edges2
 * @param {number} k
 * @return {number[]}
 */
var maxTargetNodes = function (edges1, edges2, k) {
  // number of nodes in tree 1 and tree 2 
  const N = edges1.length + 1;
  const M = edges2.length + 1;

  // build adjacency list 
  const adj1 = Array.from({ length: N }, () => new Array());
  for (let [u, v] of edges1) {
    adj1[u].push(v);
    adj1[v].push(u);
  }
  const adj2 = Array.from({ length: M }, () => new Array());
  for (let [u, v] of edges2) {
    adj2[u].push(v);
    adj2[v].push(u);
  }

  const countNodesAtDistanceK = (adj, ui, visited, k) => {
    if (k === 0) return 1;
    if (k < 0) return 0;

    visited.add(ui);
    let count = 1;

    for (let vi of adj[ui]) {
      if (!visited.has(vi)) {
        count += countNodesAtDistanceK(adj, vi, visited, k - 1);
      }
    }

    return count;
  };

  // count target nodes in tree 1 
  const tree1 = new Array(N).fill(0);
  for (let i = 0; i < N; i++) {
    const visited = new Set();
    tree1[i] = countNodesAtDistanceK(adj1, i, visited, k);
  }

  // for tree 2 
  const tree2 = new Array(M).fill(0);
  for (let i = 0; i < M; i++) {
    const visited = new Set();
    tree2[i] = countNodesAtDistanceK(adj2, i, visited, k - 1);
  }

  let maxi = Math.max(...tree2);
  const answer = tree1.map((e) => e + maxi);

  return answer;

  // Complexity analysis 
  // Time : O(N) + O(M) + O(N * (N + N)) + O(M * (M + M)) 
  // Space : O(N + N) + O(M + M) + O(N) + O(M) + O(N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3372. Maximize the Number of Target Nodes After Connecting Trees I - https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/description/?envType=daily-question&envId=2025-05-28 

  {
    const edges1 = [[0, 1], [0, 2], [2, 3], [2, 4]];
    const edges2 = [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]];
    const k = 2;
    console.log(maxTargetNodes(edges1, edges2, k));
  }
  {
    const edges1 = [[0, 1], [0, 2], [0, 3], [0, 4]];
    const edges2 = [[0, 1], [1, 2], [2, 3]];
    const k = 1;
    console.log(maxTargetNodes(edges1, edges2, k));
  }
};

/**
 * @param {number[][]} mat
 * @returns {boolean}
 */

class Problem2 {
  ValidCorner(mat) {
    // Code here

    // return this.brute(mat);

    return this.better(mat);
  }

  better(mat) {
    // check column pair in every row 
    // if same pair found in any other row, 
    // we can make a rectangle using these four points 
    // we will use a set to store column pairs 

    const N = mat.length;
    const M = mat[0].length;

    const s = new Set();

    for (let r = 0; r < N; r++) {
      for (let cleft = 0; cleft < M - 1; cleft++) {
        if (mat[r][cleft] !== 1) continue;

        for (let cright = cleft + 1; cright < M; cright++) {
          if (mat[r][cright] !== 1) continue;

          let key = `${cleft}.${cright}`;
          if (s.has(key)) return true;
          s.add(key);
        }
      }
    }

    return false;

    // Complexity analysis 
    // Time : O(N * (M * M)) 
    // Space : O(N * M) 
  }

  brute(mat) {
    // check every submatrix 
    // use recursion 

    this.N = mat.length;
    this.M = mat[0].length;
    this.mat = mat;

    let flag = false;

    for (let i = 0; i < this.N && !flag; i++) {
      for (let j = 0; j < this.M && !flag; j++) {
        if (mat[i][j] !== 1) continue;
        const memo = Array.from({ length: this.N }, () => new Array(this.M).fill(-1));
        flag = this.memoization([i, j], [i, j], memo);
      }
    }

    return flag;

    // Complexity analysis 
    // Time : O((N * M) * (N * M)) 
    // Space : O(N * M) memory + O(N + M) stack 
  }

  memoization([topLeftRow, topLeftCol], [bottomRightRow, bottomRightCol], memo) {
    if (bottomRightRow >= this.N || bottomRightCol >= this.M) {
      return false;
    }

    if (memo[bottomRightRow][bottomRightCol] != -1) {
      return memo[bottomRightRow][bottomRightCol];
    }

    if (this.mat[bottomRightRow][bottomRightCol] === 1 && bottomRightRow !== topLeftRow && bottomRightCol !== topLeftCol) {
      let [topRightRow, topRightCol] = [topLeftRow, bottomRightCol];
      let [bottomLeftRow, bottomLeftCol] = [bottomRightRow, topLeftCol];

      if (this.mat[topRightRow][topRightCol] === 1 && this.mat[bottomLeftRow][bottomLeftCol] === 1) {
        return true;
      }
    }

    let op1 = this.memoization([topLeftRow, topLeftCol], [bottomRightRow, bottomRightCol + 1], memo);
    let op2 = this.memoization([topLeftRow, topLeftCol], [bottomRightRow + 1, bottomRightCol + 1], memo);
    let op3 = this.memoization([topLeftRow, topLeftCol], [bottomRightRow + 1, bottomRightCol], memo);

    return memo[bottomRightRow][bottomRightCol] = (op1 || op2 || op3);
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Find rectangle with corners as 1 - https://www.geeksforgeeks.org/problems/find-rectangle-with-corners-as-1--141631/1 

  const mat = [
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1]
  ];
  console.log(new Problem2().ValidCorner(mat));
};


(() => {
  // Day 28 of May 2025

  p1();

  p2();
})();
