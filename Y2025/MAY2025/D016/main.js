/**
 * @param {string[]} words
 * @param {number[]} groups
 * @return {string[]}
 */
var getWordsInLongestSubsequence = function (words, groups) {
  // calculate hamming distance of two strings 
  const hammingDistance_1 = (a, b) => {
    if (a.length !== b.length) return false;

    for (let i = 0, d = 0; i < a.length; i++) {
      if (a[i] != b[i]) d++;
      if (d > 1) return false;
    }

    return true;
  };

  // input length 
  const N = words.length;

  const dp = new Array(N).fill(1); // longest subseq length ending at i 
  const parent = new Array(N).fill(-1);

  // length of longest subseq found 
  let lslen = 1;
  // index of last found member of longest subseq 
  let lsidx = 0;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < i; j++) {
      // if satisfy given condition 
      if (groups[j] != groups[i] && hammingDistance_1(words[j], words[i])) {
        if (dp[j] + 1 > dp[i]) {
          // update length of longest subseq found at index i 
          dp[i] = dp[j] + 1;
          parent[i] = j;

          // update length and index of longest subseq found 
          if (lslen < dp[i]) {
            lslen = dp[i];
            lsidx = i;
          }
        }
      }
    }
  }

  const output = [];

  while (lsidx != -1) {
    output.push(words[lsidx]);
    lsidx = parent[lsidx];
  }

  output.reverse();

  return output;

  // Complexity analysis 
  // Time : O(2N) + O(N*N*L) + O(2N) 
  // Space : O(2N) + O(N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2901. Longest Unequal Adjacent Groups Subsequence II - https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/description/?envType=daily-question&envId=2025-05-16 

  console.log(["bab", "dab", "cab"], [1, 2, 2]);
  console.log(["a", "b", "c", "d"], [1, 2, 3, 4]);
  console.log(["d", "c", "b", "a"], [1, 2, 3, 4]);
  console.log(["d"], [1]);
};

class MinHeap {
  constructor() {
    this.heap = [];
  }

  push(item) {
    this.heap.push(item);
    this._bubbleUp();
  }

  pop() {
    if (this.size() === 1) return this.heap.pop();
    const top = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._bubbleDown();
    return top;
  }

  top() {
    return this.heap[0];
  }

  size() {
    return this.heap.length;
  }

  _bubbleUp() {
    let idx = this.heap.length - 1;
    const element = this.heap[idx];
    while (idx > 0) {
      let parentIdx = Math.floor((idx - 1) / 2);
      let parent = this.heap[parentIdx];
      if (element[0] >= parent[0]) break;
      this.heap[idx] = parent;
      idx = parentIdx;
    }
    this.heap[idx] = element;
  }

  _bubbleDown() {
    let idx = 0;
    const length = this.heap.length;
    const element = this.heap[0];

    while (true) {
      let leftIdx = 2 * idx + 1;
      let rightIdx = 2 * idx + 2;
      let swap = null;

      if (leftIdx < length && this.heap[leftIdx][0] < element[0]) {
        swap = leftIdx;
      }
      if (
        rightIdx < length &&
        this.heap[rightIdx][0] < (swap === null ? element[0] : this.heap[leftIdx][0])
      ) {
        swap = rightIdx;
      }

      if (swap === null) break;
      this.heap[idx] = this.heap[swap];
      idx = swap;
    }
    this.heap[idx] = element;
  }
}

/**
 * @param {number[][]} arr
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */

class Problem2 {
  findSmallestRange(nums) {
    // code here

    const k = nums.length;
    const pq = new MinHeap();

    let maxEl = -Infinity;
    for (let i = 0; i < k; i++) {
      pq.push([nums[i][0], i, 0]); // [element, listIdx, idx]
      maxEl = Math.max(maxEl, nums[i][0]);
    }

    let resultRange = [-1000000, 1000000];

    while (pq.size() > 0) {
      const [minEl, listIdx, idx] = pq.pop();

      if (maxEl - minEl < resultRange[1] - resultRange[0]) {
        resultRange = [minEl, maxEl];
      }

      if (idx + 1 < nums[listIdx].length) {
        const nextElement = nums[listIdx][idx + 1];
        pq.push([nextElement, listIdx, idx + 1]);
        maxEl = Math.max(maxEl, nextElement);
      } else {
        break;
      }
    }

    return resultRange;

    // Complexity analysis 
    // Time : O(N * K * log(K)) 
    // Space : O(K) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Smallest range in K lists - https://www.geeksforgeeks.org/problems/find-smallest-range-containing-elements-from-k-lists/1 

  console.log(new Problem2().findSmallestRange([[4, 7, 9, 12, 15], [0, 8, 10, 14, 20], [6, 12, 16, 30, 50]]));
  console.log(new Problem2().findSmallestRange([[1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [2, 3, 5, 7, 11]]));
};


(() => {
  // Day 16 of May 2025

  p1();

  p2();
})();
