/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var colorTheGrid = function (m, n) {
  let MODO = 1000000007;

  // Step 1 : generate column states 
  const columnState = [];
  const buildColumnStates = (state, i, prev) => {
    if (i === m) {
      columnState.push([...state]);
      return;
    }

    for (let color of ["R", "G", "B"]) {
      if (color === prev) continue;
      state.push(color);
      buildColumnStates(state, i + 1, color);
      state.pop();
    }
  };

  // call to generate column states 
  buildColumnStates([], 0, "$");

  const memo = Array.from({ length: n + 1 }, () => new Array(columnState.length + 1).fill(-1));

  // Step 3 : calculate number of ways to color cells 
  const solve = (remaining, prev) => {
    if (remaining === 0) {
      // zero columns left 
      return 1;
    }

    if (memo[remaining][prev] !== -1) {
      return memo[remaining][prev];
    }

    let ways = 0;

    const prevCol = columnState[prev];

    for (let i = 0; i < columnState.length; i++) {
      if (i === prev) continue;

      let valid = true;
      const currCol = columnState[i];

      for (let r = 0; r < m && valid; r++) {
        valid = valid && (prevCol[r] !== currCol[r]);
      }

      if (valid) {
        ways = (ways + solve(remaining - 1, i)) % MODO;
      }
    }

    return memo[remaining][prev] = ways;
  };

  // Step 2 : call solve function for different startings and count ways 
  let ways = 0;

  for (let i = 0; i < columnState.length; i++) {
    ways = (ways + solve(n - 1, i)) % MODO;
  }

  return ways;

  // Complexity analysis 
  // Time : O(3^M) + O(S * S) 
  // Space : O(S) + O(N * S) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1931. Painting a Grid With Three Different Colors - https://leetcode.com/problems/painting-a-grid-with-three-different-colors/description/?envType=daily-question&envId=2025-05-18 

  console.log(colorTheGrid(1, 1));
  console.log(colorTheGrid(1, 2));
  console.log(colorTheGrid(5, 5));
  console.log(colorTheGrid(5, 20));
  console.log(colorTheGrid(5, 50));
  console.log(colorTheGrid(5, 1000));
};

/**
 * @param {Node} root
 * @returns {number[]}
 */
/*
class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
} */

class Problem2 {
  findSpiral(root) {
    // code here

    let output = [];

    let deque = [];
    let level = 0;
    if (root) deque.push(root);

    while (deque.length) {
      let N = deque.length;

      for (let i = 0; i < N; i++) {
        let node = (level & 1) ? deque.shift() : deque.pop();
        output.push(node.data);

        if (level) {
          if (node.left) deque.push(node.left);
          if (node.right) deque.push(node.right);
        } else {
          if (node.right) deque.unshift(node.right);
          if (node.left) deque.unshift(node.left);
        }
      }

      level = !level;
    }

    return output;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(W) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Level Order in spiral form - https://www.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1 

  const root = {
    data: 1,
    left: {
      data: 2,
      left: {
        data: 7,
        left: null,
        right: null,
      },
      right: {
        data: 6,
        left: null,
        right: null,
      },
    },
    right: {
      data: 3,
      left: {
        data: 5,
        left: null,
        right: null,
      },
      right: {
        data: 4,
        left: null,
        right: null,
      },
    },
  };

  console.log(new Problem2().findSpiral(root));
};


(() => {
  // Day 18 of May 2025

  p1();

  p2();
})();
