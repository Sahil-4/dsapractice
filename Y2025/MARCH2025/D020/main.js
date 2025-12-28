// disjoint set union
class DSU {
  constructor(n) {
    this.parent = new Array(n);
    this.AND = new Array(n);

    // init
    for (let u = 0; u < n; u++) {
      this.parent[u] = u;
      this.AND[u] = -1;
    }
  }

  findParent(u) {
    if (this.parent[u] == u) return u;
    return (this.parent[u] = this.findParent(this.parent[u]));
  }

  union(u, v, w) {
    let u_par = this.findParent(u);
    let v_par = this.findParent(v);

    this.parent[v_par] = u_par;

    this.updateAND(u_par, v_par, w);
  }

  updateAND(u, v, w) {
    this.AND[u] = this.AND[u] & this.AND[v] & w;
  }

  getAND(u) {
    return this.AND[this.findParent(u)];
  }
}

/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[][]} query
 * @return {number[]}
 */
var minimumCost = function (N, edges, query) {
  const QN = query.length;
  const answer = new Array(QN).fill(-1);

  const dsu = new DSU(N);

  for (let edge of edges) {
    const [u, v, w] = edge;
    dsu.union(u, v, w);
  }

  for (let i = 0; i < QN; i++) {
    const [s, t] = query[i];
    if (dsu.findParent(s) == dsu.findParent(t)) {
      answer[i] = dsu.getAND(s);
    }
  }

  return answer;

  // Complexity analysis
  // Time : O(E * 4a) + O(QN * 4a)
  // Space : O(2N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3108. Minimum Cost Walk in Weighted Graph - https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/description/?envType=daily-question&envId=2025-03-20

  console.log(minimumCost(3, [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], [[1,2]]));
  console.log(minimumCost(3, [[1,0,4],[0,2,5],[0,2,3],[0,2,14],[0,2,12],[2,0,14],[0,2,4]], [[2,1]]));
};

class Problem2 {
  maxProfit(prices) {
    // code here

    const n = prices.length;
    const _k = 2;

    // return this.recursion(prices, _k, 0, 0);

    // const memo = Array.from({ length: n }, () => {
    //     return Array.from({ length: 2 }, () => new Array(_k+1).fill(-1));
    // });
    // return this.memoize(prices, _k, 0, 0, memo);

    // return this.tabulation(prices, _k);

    return this.optimised(prices, _k);
  }

  recursion(prices, k, i, bought) {
    if (i >= prices.length) return 0;

    if (bought) {
      let not_sell = this.recursion(prices, k, i + 1, bought);
      let sell = prices[i] + this.recursion(prices, k - 1, i + 1, false);

      return Math.max(not_sell, sell);
    } else {
      let not_buy = this.recursion(prices, k, i + 1, bought);
      let buy = 0;
      if (k > 0) {
        buy = -prices[i] + this.recursion(prices, k, i + 1, true);
      }

      return Math.max(not_buy, buy);
    }

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) stack
  }

  memoize(prices, k, i, bought, memo) {
    if (i >= prices.length) return 0;

    if (memo[i][Number(bought)][k] != -1) return memo[i][Number(bought)][k];

    if (bought) {
      let not_sell = this.memoize(prices, k, i + 1, bought, memo);
      let sell = prices[i] + this.memoize(prices, k - 1, i + 1, false, memo);

      return (memo[i][Number(bought)][k] = Math.max(not_sell, sell));
    } else {
      let not_buy = this.memoize(prices, k, i + 1, bought, memo);
      let buy = 0;
      if (k > 0) {
        buy = -prices[i] + this.memoize(prices, k, i + 1, true, memo);
      }

      return (memo[i][Number(bought)][k] = Math.max(not_buy, buy));
    }

    // Complexity analysis
    // Time : O(2*N*2*K)
    // Space : O(N) stack + O(N*2*K) memory
  }

  tabulation(prices, _k) {
    const n = prices.length;
    const memo = Array.from({ length: n + 1 }, () => {
      return Array.from({ length: 2 }, () => new Array(_k + 1).fill(0));
    });

    for (let i = n - 1; i >= 0; i--) {
      for (let k = 0; k <= _k; k++) {
        let not_sell = memo[i + 1][1][k];
        let sell = prices[i] + memo[i + 1][0][k - 1];
        memo[i][1][k] = Math.max(not_sell, sell);

        let not_buy = memo[i + 1][0][k];
        let buy = k > 0 ? -prices[i] + memo[i + 1][1][k] : 0;
        memo[i][0][k] = Math.max(not_buy, buy);
      }
    }

    return memo[0][0][_k];

    // Complexity analysis
    // Time : O(N*_K)
    // Space : O(N*2*_K)
  }

  optimised(prices, _k) {
    const n = prices.length;
    let next = Array.from({ length: 2 }, () => new Array(_k + 1).fill(0));

    for (let i = n - 1; i >= 0; i--) {
      let curr = Array.from({ length: 2 }, () => new Array(_k + 1).fill(0));

      for (let k = 0; k <= _k; k++) {
        let not_sell = next[1][k];
        let sell = prices[i] + next[0][k - 1];
        curr[1][k] = Math.max(not_sell, sell);

        let not_buy = next[0][k];
        let buy = k > 0 ? -prices[i] + next[1][k] : 0;
        curr[0][k] = Math.max(not_buy, buy);
      }

      next = curr;
    }

    return next[0][_k];

    // Complexity analysis
    // Time : O(N*_K)
    // Space : O(2*2*_K)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Stock Buy and Sell – Max 2 Transactions Allowed - https://www.geeksforgeeks.org/problems/buy-and-sell-a-share-at-most-twice/1

  console.log(new Problem2().maxProfit([10, 22, 5, 75, 65, 80]));
  console.log(new Problem2().maxProfit([2, 30, 15, 10, 8, 25, 80]));
};

(() => {
  // Day 20 of March 2025

  p1();

  p2();
})();
