class ConnectedComponents {
  constructor(n) {
    this.parent = new Array(n);
    this.connections = new Array(n);

    for (let i = 0; i < n; i++) {
      this.parent[i] = i;
      this.connections[i] = 1;
    }
  }

  connect(u, v) {
    let u_par = this.getParent(u);
    let v_par = this.getParent(v);

    this.parent[u_par] = v_par;

    this.connections[u]++;
    this.connections[v]++;
  }

  getParent(u) {
    if (this.parent[u] == u) return u;
    return (this.parent[u] = this.getParent(this.parent[u]));
  }

  getConnections(u) {
    return this.connections[u];
  }
}

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countCompleteComponents = function (n, edges) {
  const dsu = new ConnectedComponents(n);

  // make components
  for (let edge of edges) {
    const [u, v] = edge;
    dsu.connect(u, v);
  }

  // collect components
  const compoMap = new Map();
  for (let i = 0; i < n; i++) {
    let parent_i = dsu.getParent(i);

    if (!compoMap.has(parent_i)) {
      compoMap.set(parent_i, new Array());
    }

    compoMap.get(parent_i).push(dsu.getConnections(i));
  }

  let completeComponents = 0;

  const isComplete = (arr) => {
    return arr.reduce((acc, e) => acc & (e == arr.length), true);
  };

  compoMap.forEach((value) => {
    if (isComplete(value)) {
      completeComponents++;
    }
  });

  return completeComponents;

  // Complexity analysis
  // Time : O(N) + O(E) + O(N) + O(N)
  // Space : O(3N) dsu + components map
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2685. Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/description/?envType=daily-question&envId=2025-03-22

  console.log(countCompleteComponents(6, [[0, 1],[0, 2],[1, 2],[3, 4]]));
  console.log(countCompleteComponents(6, [[0, 1],[0, 2],[1, 2],[3, 4],[3, 5]]));
  console.log(countCompleteComponents(3, [[1,0],[2,0]]));
  console.log(countCompleteComponents(4, [[2,0],[2,1],[3,0],[3,1]]));
};

/**
 * @param number[] arr
 * @returns number
 */

class Problem2 {
  maxValue(arr) {
    // code here

    // take 0th element or (n-1)th element

    const n = arr.length;

    return Math.max(this.findMaxSum([...arr].splice(0, n - 1)), this.findMaxSum([...arr].splice(1, n)));
  }

  findMaxSum(arr) {
    // code here

    // return this.recursion(arr, -1);

    // const n = arr.length;
    // const memo = new Array(n+1).fill(-1);
    // return this.memoize(arr, 0, memo);

    return this.tabulation(arr);
  }

  recursion(arr, i) {
    if (i >= arr.length) return 0;

    let not_pick = this.recursion(arr, i + 1);
    let pick = i == -1 ? 0 : arr[i] + this.recursion(arr, i + 2);

    return Math.max(not_pick, pick);

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) stack space
  }

  memoize(arr, i, memo) {
    if (i > arr.length) return 0;

    if (memo[i] != -1) return memo[i];

    let not_pick = this.memoize(arr, i + 1, memo);
    let pick = i == 0 ? 0 : arr[i - 1] + this.memoize(arr, i + 2, memo);

    return (memo[i] = Math.max(not_pick, pick));

    // Complexity analysis
    // Time : O(2*N)
    // Space : O(N) stack space + O(N) memory
  }

  tabulation(arr) {
    const n = arr.length;
    const memo = new Array(n + 3).fill(0);

    for (let i = n; i >= 0; i--) {
      let not_pick = memo[i + 1];
      let pick = i == 0 ? 0 : arr[i - 1] + memo[i + 2];
      memo[i] = Math.max(not_pick, pick);
    }

    return memo[0];

    // Complexity analysis
    // Time : O(N)
    // Space : O(N) memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Stickler Thief II - https://www.geeksforgeeks.org/problems/house-robber-ii/1

  console.log(new Problem2().maxValue([2, 3, 2]));
  console.log(new Problem2().maxValue([1, 2, 3, 1]));
  console.log(new Problem2().maxValue([2, 2, 3, 1, 2]));
};

(() => {
  // Day 22 of March 2025

  p1();

  p2();
})();
