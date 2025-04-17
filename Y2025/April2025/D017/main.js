/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countPairs = function (nums, k) {
  const N = nums.length;
  let count = 0;

  const solution1 = () => {
    for (let i = 0; i < N; i++) {
      for (let j = i + 1; j < N; j++) {
        if (nums[i] != nums[j]) continue;
        if ((i * j) % k != 0) continue;
        count++;
      }
    }

    // Complexity analysis
    // Time : O(N^2)
    // Space : O(1)
  };

  const solution2 = () => {
    // stores element -> [indices where element occurred]
    const occurrenceMap = new Map();

    for (let i = 0; i < N; i++) {
      const prevIndices = occurrenceMap.get(nums[i]) || [];

      prevIndices.forEach((index) => {
        count += (index * i) % k == 0;
      });

      occurrenceMap.set(nums[i], [...prevIndices, i]);
    }

    // Complexity analysis
    // Time : O(N * X), X = max freq of any element
    // Space : O(N)
  };

  // solution1();
  solution2();

  return count;
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2176. Count Equal and Divisible Pairs in an Array - https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/?envType=daily-question&envId=2025-04-17

  console.log(countPairs([3, 1, 2, 2, 2, 1, 3], 2));
  console.log(countPairs([1, 2, 3, 4], 1));
};

class MinHeap {
  constructor() {
    this.heap = [];
  }

  push([dist, node]) {
    this.heap.push([dist, node]);
    this._bubbleUp(this.heap.length - 1);
  }

  pop() {
    const min = this.heap[0];
    const end = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = end;
      this._sinkDown(0);
    }
    return min;
  }

  _bubbleUp(index) {
    const element = this.heap[index];
    while (index > 0) {
      const parentIdx = Math.floor((index - 1) / 2);
      const parent = this.heap[parentIdx];
      if (element[0] >= parent[0]) break;
      this.heap[index] = parent;
      this.heap[parentIdx] = element;
      index = parentIdx;
    }
  }

  _sinkDown(index) {
    const length = this.heap.length;
    const element = this.heap[index];

    while (true) {
      let leftIdx = 2 * index + 1;
      let rightIdx = 2 * index + 2;
      let swap = null;

      if (leftIdx < length) {
        if (this.heap[leftIdx][0] < element[0]) {
          swap = leftIdx;
        }
      }

      if (rightIdx < length) {
        if (
          (swap === null && this.heap[rightIdx][0] < element[0]) ||
          (swap !== null && this.heap[rightIdx][0] < this.heap[leftIdx][0])
        ) {
          swap = rightIdx;
        }
      }

      if (swap === null) break;

      this.heap[index] = this.heap[swap];
      this.heap[swap] = element;
      index = swap;
    }
  }

  isEmpty() {
    return this.heap.length === 0;
  }
}

class Problem2 {
  dijkstra(u, v, V, adj) {
    const dist = new Array(V).fill(Number.MAX_SAFE_INTEGER);
    dist[u] = 0;

    const pq = new MinHeap();
    pq.push([0, u]);

    while (!pq.isEmpty()) {
      const [_d, _u] = pq.pop();

      if (_d > dist[_u]) continue;

      for (let [_v, _w] of adj[_u]) {
        // ignore direct connection between src and dest
        if ((_u === u && _v === v) || (_u === v && _v === u)) continue;

        if (dist[_v] > dist[_u] + _w) {
          dist[_v] = dist[_u] + _w;
          pq.push([dist[_v], _v]);
        }
      }
    }

    return dist[v];
  }

  findMinCycle(V, edges) {
    // code here
    const adj = Array.from({ length: V }, () => new Array());
    for (let [u, v, w] of edges) {
      adj[u].push([v, w]);
    }

    let minCycle = Number.MAX_SAFE_INTEGER;

    for (let [u, v, w] of edges) {
      const _dist = this.dijkstra(u, v, V, adj);

      if (_dist != Number.MAX_SAFE_INTEGER) {
        minCycle = Math.min(minCycle, _dist + w);
      }
    }

    return minCycle;

    // Complexity analysis
    // Time : O(E) + O(E * V * LOG(E))
    // Space : O(V + E) + V
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Minimum Weight Cycle - https://www.geeksforgeeks.org/problems/minimum-weight-cycle/1

  console.log(
    new Problem2().findMinCycle(5, [
      [0, 1, 2],
      [1, 2, 2],
      [1, 3, 1],
      [1, 4, 1],
      [0, 4, 3],
      [2, 3, 4],
    ]),
  );
  console.log(
    new Problem2().findMinCycle(5, [
      [0, 1, 3],
      [1, 2, 2],
      [0, 4, 1],
      [1, 4, 2],
      [1, 3, 1],
      [3, 4, 2],
      [2, 3, 3],
    ]),
  );
};

(() => {
  // Day 17 of April 2025

  p1();

  p2();
})();
