/**
 * @param {number[]} arr
 * @return {boolean}
 */
var threeConsecutiveOdds = function (arr) {
  // if (arr.length < 3) return false;

  for (let i = 1; i < arr.length - 1; i++) {
    // const check = [arr[i], arr[i-1], arr[i+1]].reduce((acc, e) => (acc && (e & 1)), true);
    const check = (arr[i] & 1) && (arr[i - 1] & 1) && (arr[i + 1] & 1);
    if (check) return true;
  }

  return false;

  // Complexity analysis 
  // Time : O(N) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1550. Three Consecutive Odds - https://leetcode.com/problems/three-consecutive-odds/?envType=daily-question&envId=2025-05-11 

  console.log(threeConsecutiveOdds([2, 6, 4, 1]));
  console.log(threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]));
  console.log(threeConsecutiveOdds([1, 3]));
  console.log(threeConsecutiveOdds([1, 3, 5]));
  console.log(threeConsecutiveOdds([1]));
};

class MinHeap {
  constructor() {
    this.heap = [];
  }

  push(key) {
    this.heap.push(key);
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

  top() {
    return this.heap[0];
  }

  _bubbleUp(index) {
    const element = this.heap[index];
    while (index > 0) {
      const parentIdx = Math.floor((index - 1) / 2);
      const parent = this.heap[parentIdx];
      if (element >= parent) break;
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
        if (this.heap[leftIdx] < element) {
          swap = leftIdx;
        }
      }

      if (rightIdx < length) {
        if (
          (swap === null && this.heap[rightIdx] < element) ||
          (swap !== null && this.heap[rightIdx] < this.heap[leftIdx])
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

  size() {
    return this.heap.length;
  }
}

// User function Template for javascript
class Problem2 {
  // Function to find the kth largest element in the given array.
  kthLargest(arr, k) {
    // return this.brute(arr, k);

    return this.optimal(arr, k);
  }

  optimal(arr, k) {
    const heap = new MinHeap();

    for (let i = 0; i < arr.length; i++) {
      let sum = 0;

      for (let j = i; j < arr.length; j++) {
        sum += arr[j];

        if (heap.size() >= k) {
          if (sum > heap.top()) {
            heap.pop();
            heap.push(sum);
          }
        } else {
          heap.push(sum);
        }
      }
    }

    return heap.top();

    // Complexity analysis 
    // Time : O((N*N) * Log(k)) 
    // Space : O(k) 
  }

  brute(arr, k) {
    const sums = [];

    for (let i = 0; i < arr.length; i++) {
      let sum = 0;

      for (let j = i; j < arr.length; j++) {
        sum += arr[j];
        sums.push(sum);
      }
    }

    sums.sort((a, b) => b - a);

    return sums[k - 1];

    // Complexity analysis 
    // Time : O(N*N) + O((N*N) * Log(N*N)) 
    // Space : O(N*N) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks K-th Largest Sum Contiguous Subarray - https://www.geeksforgeeks.org/problems/k-th-largest-sum-contiguous-subarray/1 

  console.log(new Problem2().kthLargest("2 5 1 7 1 5".split(" "), 1));
  console.log(new Problem2().kthLargest("2 5 1 7 1 5".split(" "), 2));
  console.log(new Problem2().kthLargest("2 5 1 7 1 5".split(" "), 5));
  console.log(new Problem2().kthLargest("2 6 4 1".split(" "), 3));
  console.log(new Problem2().kthLargest("3 2 1".split(" "), 2));
};


(() => {
  // Day 11 of May 2025

  p1();

  p2();
})();
