/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countSymmetricIntegers = function (low, high) {
  let count = 0;

  const brute = () => {
    for (let i = low; i <= high; i++) {
      const numStr = String(i);
      const len = numStr.length;

      // odd length
      if (len & 1) continue;

      const left = numStr.substring(0, len / 2).split("");
      const right = numStr.substring(len / 2).split("");

      const leftSum = left.reduce((acc, e) => acc + +e, 0);
      const rightSum = right.reduce((acc, e) => acc + +e, 0);

      if (leftSum === rightSum) count++;
    }

    // Complexity analysis
    // Time : O(N * len(N))
    // Space : O(1) + some strings
    // N = high - low + 1
  };

  const optimal = () => {
    const _low = 10;
    const _high = 9999;

    for (let i = Math.max(_low, low); i <= Math.min(_high, high); i++) {
      if (i >= 10 && i <= 99 && i % 11 == 0) {
        count++;
      } else if (i >= 1000 && i <= 9999) {
        const d1 = Math.floor(i / 1000);
        const d2 = Math.floor(i / 100) % 10;
        const d3 = Math.floor(i / 10) % 10;
        const d4 = Math.floor(i / 1) % 10;

        const leftSum = d1 + d2;
        const rightSum = d3 + d4;

        if (leftSum === rightSum) count++;
      }
    }

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  };

  // brute();
  optimal();

  return count;
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2843. Count Symmetric Integers - https://leetcode.com/problems/count-symmetric-integers/description/?envType=daily-question&envId=2025-04-11

  console.log(countSymmetricIntegers(1, 100));
  console.log(countSymmetricIntegers(1200, 1230));
  console.log(countSymmetricIntegers(1, 10000));
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
  // Returns shortest distances from src to all other vertices
  dijkstra(V, edges, src) {
    // code here

    // build adjacency list
    const adj = Array.from({ length: V }, () => new Array());
    for (let [u, v, w] of edges) adj[u].push([v, w]);

    const distance = new Array(V).fill(Infinity);
    const mh = new MinHeap(); // [w, v]

    distance[src] = 0; // src -> src

    mh.push([0, src]);

    while (mh.size() > 0) {
      const [w, u] = mh.pop();

      if (distance[u] > w) continue;

      for (let [_v, _w] of adj[u]) {
        if (w + _w < distance[_v]) {
          distance[_v] = w + _w;
          mh.push([w + _w, _v]);
        }
      }
    }

    return distance;

    // Complexity analysis
    // Time : O(E) + O(V) + O(V + E * LOG(V))
    // Space : O(V+E) + O(V) + O(E)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Dijkstra Algorithm - https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

  {
    const args = [
      3,
      [
        [0, 1, 1],
        [1, 2, 3],
        [0, 2, 6],
      ],
      2,
    ];
    console.log(new Problem2().dijkstra(...args));
  }
  {
    const args = [
      5,
      [
        [0, 1, 4],
        [0, 2, 8],
        [1, 4, 6],
        [2, 3, 2],
        [3, 4, 10],
      ],
      0,
    ];
    console.log(new Problem2().dijkstra(...args));
  }
  {
    const args = [
      3,
      [
        [0, 1, 1],
        [1, 2, 3],
        [0, 2, 6],
      ],
      0,
    ];
    console.log(new Problem2().dijkstra(...args));
  }
};

(() => {
  // Day 11 of April 2025

  p1();

  p2();
})();
