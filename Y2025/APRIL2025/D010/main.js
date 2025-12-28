/**
 * @param {number} start
 * @param {number} finish
 * @param {number} limit
 * @param {string} s
 * @return {number}
 */
var numberOfPowerfulInt = function (start, finish, limit, suffix) {
  const solve = (ending) => {
    // deps [ending, suffix, limit]

    // if the end length is smaller then suffix, we cant add suffix anywhere in it
    if (ending.length < suffix.length) return 0;

    let count = 0;

    const trailStr = ending.substring(ending.length - suffix.length);
    const remainLen = ending.length - suffix.length;

    for (let i = 0; i < remainLen; i++) {
      const digit = Number(ending.charAt(i));

      if (digit <= limit) {
        count += digit * Math.pow(limit + 1, remainLen - i - 1);
      } else {
        count += Math.pow(limit + 1, remainLen - i);
        return count;
      }
    }

    // edge case
    if (Number(trailStr) >= Number(suffix)) count += 1;

    return count;
  };

  const _startStr = String(start - 1);
  const finishStr = String(finish);

  return solve(finishStr) - solve(_startStr);

  // Complexity analysis
  // Time : O(X * N) for substrings and string conversions + (N * POW) for Loop and calculating power
  // Space : O(1) + some strings
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2999. Count the Number of Powerful Integers - https://leetcode.com/problems/count-the-number-of-powerful-integers/description/?envType=daily-question&envId=2025-04-10

  console.log(numberOfPowerfulInt(1, 6000, 4, "124"));
  console.log(numberOfPowerfulInt(15, 215, 6, "10"));
  console.log(numberOfPowerfulInt(1000, 2000, 4, "3000"));
};

class MinHeap {
  constructor() {
    this.heap = [];
  }

  push(item) {
    this.heap.push(item);
    this._heapifyUp();
  }

  pop() {
    if (this.size() === 0) return null;
    const top = this.heap[0];
    const end = this.heap.pop();
    if (this.size() > 0) {
      this.heap[0] = end;
      this._heapifyDown();
    }
    return top;
  }

  size() {
    return this.heap.length;
  }

  _heapifyUp() {
    let i = this.heap.length - 1;
    while (i > 0) {
      let parent = Math.floor((i - 1) / 2);
      if (this.heap[i][0] >= this.heap[parent][0]) break;
      [this.heap[i], this.heap[parent]] = [this.heap[parent], this.heap[i]];
      i = parent;
    }
  }

  _heapifyDown() {
    let i = 0;
    const length = this.heap.length;
    while (true) {
      let left = 2 * i + 1;
      let right = 2 * i + 2;
      let smallest = i;

      if (left < length && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
      if (right < length && this.heap[right][0] < this.heap[smallest][0]) smallest = right;

      if (smallest === i) break;
      [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
      i = smallest;
    }
  }
}

// User function Template for javascript
class Problem2 {
  minCost(houses) {
    // code here

    // MCST - Min Cost Spanning Tree

    // Approach - Prim's
    // starting with house or node 0
    // Use min heap to select the edge with min weight or connecting cost
    // Skipping houses or nodes which are already present in MST
    // Repeating this till all nodes are not done

    const V = houses.length;

    // track total cost
    let t_cost = 0;
    // visited nodes - track nodes which are in mst
    const visited = new Set();

    // min heap - [cost, u]
    const minHeap = new MinHeap();

    minHeap.push([0, 0]); // cost = 0, node = 0

    while (minHeap.size() > 0) {
      if (visited.size == V) break;

      const [cost, u] = minHeap.pop();

      if (visited.has(u)) continue;

      visited.add(u);
      t_cost += cost;

      for (let v = 0; v < V; v++) {
        if (visited[v]) continue;
        const dist = this.manhattanDistance(houses[u], houses[v]);
        minHeap.push([dist, v]);
      }
    }

    return t_cost;

    // Complexity analysis
    // Time : O(_E * LOG(_E))
    // Space : O(N) + O(_E)
    // _E = C(2, V)
  }

  manhattanDistance(h1, h2) {
    return Math.abs(h1[0] - h2[0]) + Math.abs(h1[1] - h2[1]);
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Minimum cost to connect all houses in a city - https://www.geeksforgeeks.org/problems/minimum-cost-to-connect-all-houses-in-a-city/1

  {
    const args = [
      [
        [0, 7],
        [0, 9],
        [20, 7],
        [30, 7],
        [40, 70],
      ],
    ];
    console.log(new Problem2().minCost(...args));
  }
  {
    const args = [
      [
        [0, 0],
        [1, 1],
        [1, 3],
        [3, 0],
      ],
    ];
    console.log(new Problem2().minCost(...args));
  }
};

(() => {
  // Day 10 of April 2025

  p1();

  p2();
})();
