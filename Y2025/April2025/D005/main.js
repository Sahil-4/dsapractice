/**
 * @param {number[]} nums
 * @return {number}
 */
var subsetXORSum = function(nums) {
  const N = nums.length;

  // try with recursion 
  // we will take i, XOR value till now, initially 0 
  const recursion = (_index, _XOR) => {
      if (_index >= N) return _XOR;

      // we have two options now, for every _index 
      const not_take = recursion(_index + 1, _XOR);
      const take = recursion(_index + 1, _XOR ^ nums[_index]);

      return (not_take + take);

      // Complexity analysis 
      // Time : O(pow(2,N)) 
      // Space : O(N) stack 
  }

  const iterative = () => {
      let total_XOR = 0;
      const limit = 1 << N; // limit or total subsets 

      // create bit mask 
      // 0 - ...000, 1 - ...001, 2 - ...010, 3 - ...011, and so on 
      for (let mask = 0; mask < limit; mask++) {
          let XOR = 0;

          // take ith elements if ith bit is set 
          for (let i = 0; i < N; i++) {
              if ((mask >> i) & 1) {
                  XOR ^= nums[i];
              }
          }

          total_XOR += XOR;
      }

      return total_XOR;

      // Complexity analysis 
      // Time : O(pow(2,N) * N) 
      // Space : O(1) 
  };

  // return recursion(0, 0);
  return iterative();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1863. Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/?envType=daily-question&envId=2025-04-05 

  console.log(subsetXORSum([5,1,6]));
  console.log(subsetXORSum([3,4,5,6,7,8]));
};

class DSU {
  constructor(t) {
    this.parent = new Array(t);
    this.size = new Array(t);
    for (let i = 0; i < t; i++) {
      this.parent[i] = i;
      this.size[i] = 1;
    }
  }

  findParent(u) {
    if (this.parent[u] == u) return u;
    return (this.parent[u] = this.findParent(this.parent[u]));
  }

  union(u, v) {
    const u_parent = this.findParent(u);
    const v_parent = this.findParent(v);

    if (u_parent == v_parent) return;

    if (this.size[u_parent] >= this.size[v_parent]) {
      this.parent[v_parent] = u_parent;
      this.size[u_parent] += this.size[v_parent];
    } else {
      this.parent[u_parent] = v_parent;
      this.size[v_parent] += this.size[u_parent];
    }
  }
}

// User function Template for javascript
/**
 * @param {string[][]} grid
 * @returns {number}
 */
class Problem2 {
  numIslands(grid) {
    // code here
    // simply find number of components
    // assume an island a component
    // if two adjacent cells are having 'L' add it into dsu
    // with its parent as its adjacent cell
    // total cell - N*M
    // cell no - (r * N) + c;

    const _dirs = [
      [-1, -1],
      [-1, 0],
      [-1, +1],
      [0, +1],
      [+1, +1],
      [+1, 0],
      [+1, -1],
      [0, -1],
    ];

    const N = grid.length;
    const M = grid[0].length;
    const cellCount = N * M;

    const dsu = new DSU(cellCount);

    const canMove = (r, c) => {
      if (r < 0 || r >= N) return false;
      if (c < 0 || c >= M) return false;
      if (grid[r][c] != "L") return false;
      return true;
    };

    for (let r = 0; r < N; r++) {
      for (let c = 0; c < M; c++) {
        if (grid[r][c] == "L") {
          const cellP = r * M + c;

          // connect adjacent 'L' nodes
          for (let [rp, cp] of _dirs) {
            const nr = r + rp;
            const nc = c + cp;

            const cellU = nr * M + nc;

            if (canMove(nr, nc)) {
              dsu.union(cellP, cellU);
            }
          }
        }
      }
    }

    let count = 0;
    for (let r = 0; r < N; r++) {
      for (let c = 0; c < M; c++) {
        if (grid[r][c] == "L") {
          const cellP = r * M + c;
          if (dsu.findParent(cellP) == cellP) {
            count++;
          }
        }
      }
    }

    return count;

    // Complexity analysis
    // Time : O(NM) dsu building + O(NM) grid lookup and connect cells + O(NM) count components
    // Space : O(2NM) dsu + O(NM) visited + O(N|M) stack
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Find the number of islands - https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1

  console.log(
    new Problem2().numIslands([
      ["L", "L", "W", "W", "W"],
      ["W", "L", "W", "W", "L"],
      ["L", "W", "W", "L", "L"],
      ["W", "W", "W", "W", "W"],
      ["L", "W", "L", "L", "W"],
    ]),
  );
  console.log(
    new Problem2().numIslands([
      ["W", "L", "L", "L", "W", "W", "W"],
      ["W", "W", "L", "L", "W", "L", "W"],
    ]),
  );
};

(() => {
  // Day 5 of April 2025

  p1();

  p2();
})();
