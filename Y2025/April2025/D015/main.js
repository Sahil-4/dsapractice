var goodTriplets_TLE = function (nums1, nums2) {
  const N = nums1.length;

  // element to index map for nums2 array
  const nums2Map = new Map();
  for (let i = 0; i < N; i++) {
    nums2Map.set(nums2[i], i);
  }

  let count = 0;

  // Triplet [X, Y, Z]

  for (let y1 = 1; y1 < N; y1++) {
    let Ey = nums1[y1];
    let y2 = nums2Map.get(Ey);

    let leftCommonElementCounts = 0;
    let rightCommonElementCounts = N - 1 - y2;

    for (let x1 = y1 - 1; x1 >= 0; x1--) {
      let Ex = nums1[x1];
      let x2 = nums2Map.get(Ex);
      if (x2 < y2) leftCommonElementCounts++;
      else rightCommonElementCounts--;
    }

    // possible triplets for this Ey element
    let possibleTriplets = leftCommonElementCounts * rightCommonElementCounts;

    count += possibleTriplets;
  }

  return count;

  // Complexity analysis
  // Time : O(N * N)
  // Space : O(N)
};

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var goodTriplets = function (nums1, nums2) {
  function updateSegmentTree(i, l, r, updateIndex, segmentTree) {
    if (l === r) {
      segmentTree[i] = 1;
      return;
    }

    const mid = l + Math.floor((r - l) / 2);
    if (updateIndex <= mid) {
      updateSegmentTree(2 * i + 1, l, mid, updateIndex, segmentTree);
    } else {
      updateSegmentTree(2 * i + 2, mid + 1, r, updateIndex, segmentTree);
    }

    segmentTree[i] = segmentTree[2 * i + 1] + segmentTree[2 * i + 2];
  }

  function querySegmentTree(queryStart, queryEnd, i, l, r, segmentTree) {
    if (r < queryStart || l > queryEnd) {
      return 0;
    }

    if (l >= queryStart && r <= queryEnd) {
      return segmentTree[i];
    }

    const mid = l + Math.floor((r - l) / 2);

    const left = querySegmentTree(queryStart, queryEnd, 2 * i + 1, l, mid, segmentTree);
    const right = querySegmentTree(queryStart, queryEnd, 2 * i + 2, mid + 1, r, segmentTree);

    return left + right;
  }

  const n = nums1.length;
  const mp = new Map();
  for (let i = 0; i < n; i++) {
    mp.set(nums2[i], i);
  }

  const segmentTree = new Array(4 * n).fill(0);
  let result = 0;

  updateSegmentTree(0, 0, n - 1, mp.get(nums1[0]), segmentTree);

  for (let i = 1; i < n; i++) {
    const idx = mp.get(nums1[i]);
    const leftCommonCount = querySegmentTree(0, idx, 0, 0, n - 1, segmentTree);
    const leftNotCommonCount = i - leftCommonCount;
    const elementsAfterIdxNums2 = n - 1 - idx;
    const rightCommonCount = elementsAfterIdxNums2 - leftNotCommonCount;

    result += leftCommonCount * rightCommonCount;

    updateSegmentTree(0, 0, n - 1, idx, segmentTree);
  }

  return result;
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2179. Count Good Triplets in an Array - https://leetcode.com/problems/count-good-triplets-in-an-array/description/?envType=daily-question&envId=2025-04-15

  console.log(goodTriplets([2, 0, 1, 3], [0, 1, 2, 3]));
  console.log(goodTriplets([4, 0, 1, 3, 2], [4, 1, 0, 2, 3]));
};

// User function Template for javascript

/**
 * Function to implement Bellman Ford
 * @param {number} V
 * @param {number[][]} edges
 * @param {number} src
 * @returns {number[]}
 */

class Solution {
  bellmanFord(V, edges, src) {
    // code here
    const MAX_DISTANCE = 100000000;
    const distances = new Array(V).fill(MAX_DISTANCE);

    distances[src] = 0;

    for (let i = 0; i < V - 1; i++) {
      for (let [u, v, w] of edges) {
        if (distances[u] != MAX_DISTANCE && distances[u] + w < distances[v]) {
          distances[v] = distances[u] + w;
        }
      }
    }

    for (let [u, v, w] of edges) {
      if (distances[u] != MAX_DISTANCE && distances[u] + w < distances[v]) {
        return [-1];
      }
    }

    return distances;

    // Complexity analysis
    // Time : O(V * E)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Bellman-Ford - http://geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

  console.log(
    new Solution().bellmanFord(
      5,
      [
        [1, 3, 2],
        [4, 3, -1],
        [2, 4, 1],
        [1, 2, 1],
        [0, 1, 5],
      ],
      0,
    ),
  );
  console.log(
    new Solution().bellmanFord(
      4,
      [
        [0, 1, 4],
        [1, 2, -6],
        [2, 3, 5],
        [3, 1, -2],
      ],
      0,
    ),
  );
};

(() => {
  // Day 15 of April 2025

  p1();

  p2();
})();
