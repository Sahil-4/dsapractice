/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var countPaths = function (n, roads) {
  if (n == 1) return 1;

  const MODO = 1e9 + 7;

  const start = 0;
  const dest = n - 1;

  // 1. construct graph

  const graph = {};

  for (const road of roads) {
    const [u, v, t] = road;

    if (!graph[u]) graph[u] = [];
    graph[u].push([v, t]);

    if (!graph[v]) graph[v] = [];
    graph[v].push([u, t]);
  }

  // 2. perform dijkstra

  const ways2ReachI = new Array(n).fill(0);
  const timeSrc2I = new Array(n).fill(Infinity);

  ways2ReachI[start] = 1;
  timeSrc2I[start] = 0;

  // [u, t], t = time to reach to u node
  const pq = new PriorityQueue((a, b) => (a[1] <= b[1] ? -1 : 1));
  pq.enqueue([start, 0]); // starting node

  while (!pq.isEmpty()) {
    const [u, t1] = pq.dequeue();

    if (timeSrc2I[u] < t1) continue;

    for (const [v, t2] of graph[u]) {
      // t1 + t2 time to reach v
      if (t1 + t2 < timeSrc2I[v]) {
        timeSrc2I[v] = t1 + t2;
        ways2ReachI[v] = ways2ReachI[u] % MODO;
        pq.enqueue([v, t1 + t2]);
      } else if (t1 + t2 == timeSrc2I[v]) {
        ways2ReachI[v] = (ways2ReachI[v] + ways2ReachI[u]) % MODO;
      }
    }
  }

  return ways2ReachI[dest];

  // Complexity analysis
  // Time : O(E) + O(V+E)
  // Space : O(V+E) + O(2V)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1976. Number of Ways to Arrive at Destination - https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/?envType=daily-question&envId=2025-03-23

  console.log(countPaths(1, []));
  console.log(countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]));
};

/**
 * @param {string} digits
 * @return {number}
 */
class Problem2 {
  countWays(digits) {
    // code here

    // return this.recursion(digits, 0);

    // const n = digits.length;
    // const memo = new Array(n).fill(-1);
    // return this.memoize(digits, 0, memo);

    // return this.tabulation(digits);

    return this.optimised(digits);
  }

  recursion(digits, i) {
    if (i >= digits.length) return 1;
    if (digits[i] == 0) return 0;

    let pick1 = this.recursion(digits, i + 1);
    let pick2 = 0;
    if (i + 2 <= digits.length && digits.substring(i, i + 2) <= 26) pick2 = this.recursion(digits, i + 2);

    return pick1 + pick2;

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) stack space
  }

  memoize(digits, i, memo) {
    if (i >= digits.length) return 1;
    if (digits[i] == 0) return 0;

    if (memo[i] != -1) return memo[i];

    let pick1 = this.memoize(digits, i + 1, memo);
    let pick2 = 0;
    if (i + 2 <= digits.length && digits.substring(i, i + 2) <= 26) {
      pick2 = this.memoize(digits, i + 2, memo);
    }

    return (memo[i] = pick1 + pick2);

    // Complexity analysis
    // Time : O(2*N)
    // Space : O(N) stack space + O(N) memory
  }

  tabulation(digits) {
    const n = digits.length;
    const memo = new Array(n + 2).fill(0);

    // base
    memo[n] = 1;
    memo[n + 1] = 1;

    // recurrence
    for (let i = n - 1; i >= 0; i--) {
      if (digits[i] == "0") {
        memo[i] = 0;
        continue;
      }
      let pick1 = memo[i + 1];
      let pick2 = 0;
      if (i + 2 <= digits.length && digits.substring(i, i + 2) <= 26) {
        pick2 = memo[i + 2];
      }

      memo[i] = pick1 + pick2;
    }

    // return
    return memo[0];
  }

  optimised(digits) {
    const n = digits.length;

    // base
    let next2 = 1;
    let next1 = 1;

    // recurrence
    for (let i = n - 1; i >= 0; i--) {
      let curr = 0;

      if (digits[i] == "0") {
        curr = 0;
      } else {
        let pick1 = next1;
        let pick2 = 0;
        if (i + 2 <= digits.length && digits.substring(i, i + 2) <= 26) {
          pick2 = next2;
        }
        curr = pick1 + pick2;
      }

      next2 = next1;
      next1 = curr;
    }

    // return
    return next1;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Total Decoding Messages - https://www.geeksforgeeks.org/problems/total-decoding-messages1235/1 

  console.log(new Problem2().countWays("12345678910"));
  console.log(new Problem2().countWays("01234567891"));
};

(() => {
  // Day 23 of March 2025

  p1();

  p2();
})();
