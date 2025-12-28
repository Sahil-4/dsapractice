/**
 * @param {number[][]} board
 * @return {number}
 */
var snakesAndLadders = function (board) {
  const n = board.length;
  const N = (n * n);

  const getCoords = (cell) => {
    let re = n - 1;
    let i = re - Math.floor((cell - 1) / n);
    let j = ((cell - 1) % n);

    if (((i & 1) && (n & 1)) || (!(i & 1) && !(n & 1))) {
      j = re - j;
    }

    return [i, j];
  };

  let start = 1;
  let destination = N;

  let steps = 0;

  let visited = new Array(N + 1).fill(false);
  let queue = [];

  visited[start] = true;
  queue.push(1);

  while (queue.length) {
    let width = queue.length;

    for (let i = 0; i < width; i++) {
      let curr = queue.shift();

      if (curr === destination) return steps;

      for (let n = 1; n <= 6; n++) {
        let next = curr + n;

        if (next > destination) break;
        if (visited[next]) continue;

        let coords = getCoords(next);

        visited[next] = true;

        if (board[coords[0]][coords[1]] != -1) {
          next = board[coords[0]][coords[1]];
        }

        queue.push(next);
      }
    }

    steps++;
  }

  return -1;

  // Complexity analysis 
  // Time : O(N) 
  // Space : O(2N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 909. Snakes and Ladders  - https://leetcode.com/problems/snakes-and-ladders/description/?envType=daily-question&envId=2025-05-31 
 
  console.log(snakesAndLadders([[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]));
  console.log(snakesAndLadders([[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, 36, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]));
  console.log(snakesAndLadders([[-1, -1], [-1, 3]]));
  console.log(snakesAndLadders([[-1, 1, 2, -1], [2, 13, 15, -1], [-1, 10, -1, -1], [-1, 6, 2, 8]]));
  console.log(snakesAndLadders([[-1, -1, 30, 14, 15, -1], [23, 9, -1, -1, -1, 9], [12, 5, 7, 24, -1, 30], [10, -1, -1, -1, 25, 17], [32, -1, 28, -1, -1, 32], [-1, -1, 23, -1, 13, 19]]));
  console.log(snakesAndLadders([[-1, -1, 27, 13, -1, 25, -1], [-1, -1, -1, -1, -1, -1, -1], [44, -1, 8, -1, -1, 2, -1], [-1, 30, -1, -1, -1, -1, -1], [3, -1, 20, -1, 46, 6, -1], [-1, -1, -1, -1, -1, -1, 29], [-1, 29, 21, 33, -1, -1, -1]]));
};

class MaxHeap {
  constructor() {
    this.heap = [];
  }

  // Returns the number of elements in the heap
  size() {
    return this.heap.length;
  }

  // Checks if the heap is empty
  isEmpty() {
    return this.heap.length === 0;
  }

  // Returns the maximum element without removing it
  peek() {
    if (this.isEmpty()) {
      return null;
    }
    return this.heap[0];
  }

  // Adds a new element to the heap
  push(value) {
    this.heap.push(value);
    this._heapifyUp();
  }

  // Removes and returns the maximum element from the heap
  pop() {
    if (this.isEmpty()) {
      return null;
    }
    if (this.size() === 1) {
      return this.heap.pop();
    }

    const max = this.heap[0];
    this.heap[0] = this.heap.pop(); // Move the last element to the root
    this._heapifyDown();
    return max;
  }

  // Helper method to maintain heap property after insertion (bubble up)
  _heapifyUp() {
    let currentIndex = this.heap.length - 1;
    while (currentIndex > 0) {
      let parentIndex = Math.floor((currentIndex - 1) / 2);
      if (this.heap[currentIndex] > this.heap[parentIndex]) {
        // Swap if child is greater than parent
        [this.heap[currentIndex], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[currentIndex]];
        currentIndex = parentIndex;
      } else {
        break; // Heap property satisfied
      }
    }
  }

  // Helper method to maintain heap property after deletion (bubble down)
  _heapifyDown() {
    let currentIndex = 0;
    const lastIndex = this.heap.length - 1;

    while (true) {
      let leftChildIndex = 2 * currentIndex + 1;
      let rightChildIndex = 2 * currentIndex + 2;
      let largestIndex = currentIndex;

      // Check if left child exists and is greater than current largest
      if (leftChildIndex <= lastIndex && this.heap[leftChildIndex] > this.heap[largestIndex]) {
        largestIndex = leftChildIndex;
      }

      // Check if right child exists and is greater than current largest
      if (rightChildIndex <= lastIndex && this.heap[rightChildIndex] > this.heap[largestIndex]) {
        largestIndex = rightChildIndex;
      }

      // If the largest is not the current node, swap and continue
      if (largestIndex !== currentIndex) {
        [this.heap[currentIndex], this.heap[largestIndex]] = [this.heap[largestIndex], this.heap[currentIndex]];
        currentIndex = largestIndex;
      } else {
        break; // Heap property satisfied
      }
    }
  }
};

/**
 * @param {number[][]} matrix
 * @param {number} k
 * @returns {number}
 */

class Problem2 {
  kthSmallest(matrix, k) {
    // code here

    // return this.solve1(matrix, k);

    return this.solve2(matrix, k);
  }

  solve1(matrix, k) {
    // max heap needed 
    // top element will be largest 
    // traverse matrix 
    // if heap is empty put the curr element in heap 
    // else if size is k and top element is greater then curr element 
    // remove top element, andput the curr element in heap 
    // and move to next element 

    const N = matrix.length;

    const heap = new MaxHeap();

    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        if (heap.isEmpty() || heap.size() < k) {
          heap.push(matrix[i][j]);
        } else if (heap.size() === k && heap.peek() > matrix[i][j]) {
          heap.pop();
          heap.push(matrix[i][j]);
        }
      }
    }

    return heap.pop();

    // Complexity analysis 
    // Time : O(N*N * Log(k)) 
    // Space : O(K) 
  }

  solve2(matrix, k) {
    // binary search 
    // matrix[0][0] is 0th or 1st smallest number 
    // matrix[n-1][n-1] is largest number or (n*n)th largest number 
    // answer lies within this range [0, n*n] 
    // use binary search 
    // for every mid check how many smaller numbers are there for it and 
    // if they are exactly k - 1 return it as answer (base) 
    // if they are less then k move low towards right (shrink) 
    // if they are more then k move high towards left (shrink) 

    const n = matrix.length;

    const countSmallerThen = (x) => {
      let count = 0;
      let row = 0;
      let col = n - 1;

      while (row < n && col >= 0) {
        if (matrix[row][col] <= x) {
          count += (col + 1);
          row++;
        } else {
          col--;
        }
      }

      return count;
    };

    let ans = -1;

    // search space 
    let low = matrix[0][0];
    let high = matrix[n - 1][n - 1];

    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      let smallers = countSmallerThen(mid);

      if (smallers < k) {
        low = mid + 1;
      } else {
        ans = mid;
        high = mid - 1;
      }
    }

    return ans;

    // Complexity analysis 
    // Time : O(Log(matrix[n][n]) * n) 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Kth element in Matrix - https://www.geeksforgeeks.org/problems/kth-element-in-matrix/1 

  console.log(new Problem2().kthSmallest([[16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93], [36, 78, 87, 94]], 3));
  console.log(new Problem2().kthSmallest([[10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]], 7));
};


(() => {
  // Day 31 of May 2025

  p1();

  p2();
})();
