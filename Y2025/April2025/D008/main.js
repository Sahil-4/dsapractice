/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function (nums) {
  const N = nums.length;

  const solve1 = () => {
    // build freq map
    const freq = new Map();
    for (let num of nums) {
      if (!freq.has(num)) freq.set(num, 0);
      freq.set(num, freq.get(num) + 1);
    }

    let oprs = 0;
    let i = 0;

    // traverse the array and remove elements from array ultil we got unique values
    while (N - i > 0 && freq.keys().toArray().length != N - i) {
      for (let it = i; it < Math.min(i + 3, N); it++) {
        freq.set(nums[it], freq.get(nums[it]) - 1);
        if (freq.get(nums[it]) == 0) freq.delete(nums[it]);
      }

      oprs++;
      i += 3;
    }

    return oprs;

    // Complexity analysis
    // Time : O(2N)
    // Space : O(N)
  };

  const solve2 = () => {
    const t = 128;
    const seen = new Array(t).fill(false);

    for (let i = N - 1; i >= 0; i--) {
      if (seen[nums[i]]) {
        return Math.floor(i / 3) + 1;
      }

      seen[nums[i]] = true;
    }

    return 0;

    // Complexity analysis
    // Time : O(N)
    // Space : O(128)
  };

  // return solve1();
  return solve2();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3396. Minimum Number of Operations to Make Elements in Array Distinct - https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description/?envType=daily-question&envId=2025-04-08

  console.log(minimumOperations([1, 2, 3, 4, 2, 3, 3, 5, 7]));
  console.log(minimumOperations([4, 5, 6, 4, 4]));
  console.log(minimumOperations([6, 7, 8, 9]));
  console.log(minimumOperations([1, 2, 2, 1, 1]));
};

class DSU {
  constructor(V) {
    this.parent = new Array(V).fill(null);
    this.size = new Array(V).fill(null);
    for (let i = 0; i < V; i++) {
      this.parent[i] = i;
      this.size[i] = 1;
    }
  }

  union(u, v) {
    let u_par = this.getParent(u);
    let v_par = this.getParent(v);

    if (u_par == v_par) return;

    if (this.size[u_par] >= this.size[v_par]) {
      this.parent[v_par] = u_par;
      this.size[u_par] += this.size[v_par];
    } else {
      this.parent[u_par] = v_par;
      this.size[v_par] += this.size[u_par];
    }
  }

  getParent(u) {
    if (this.parent[u] == u) return u;
    return (this.parent[u] = this.getParent(this.parent[u]));
  }
}

class Problem2 {
  isBridge(V, edges, c, d) {
    // code here

    const dsu = new DSU(V);

    for (let [u, v] of edges) {
      if (u == c && v == d) continue;
      if (u == d && v == c) continue;
      dsu.union(u, v);
    }

    return dsu.getParent(c) != dsu.getParent(d);

    // Complexity analysis
    // Time : O(E * 4A) + 2*4A
    // Space : O(2V) by dsu
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Bridge edge in a graph - https://www.geeksforgeeks.org/problems/bridge-edge-in-graph/1

  {
    const args = [
      4,
      [
        [0, 1],
        [1, 2],
        [3, 4],
        [0, 2],
      ],
      0,
      2,
    ];
    console.log(new Problem2().isBridge(...args));
  }
  {
    const args = [
      5,
      [
        [1, 0],
        [1, 2],
        [2, 0],
        [0, 3],
        [3, 4],
      ],
      0,
      2,
    ];
    console.log(new Problem2().isBridge(...args));
  }
};

(() => {
  // Day 8 of April 2025

  p1();

  p2();
})();
