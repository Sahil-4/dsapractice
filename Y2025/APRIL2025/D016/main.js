/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countGood = function (nums, k) {
  const N = nums.length;
  let count = 0;

  const freqMap = new Map();
  let pairs = 0;
  let l = (r = 0);

  while (r < N) {
    const prevFreq = freqMap.get(nums[r]) || 0;
    freqMap.set(nums[r], prevFreq + 1);
    pairs += prevFreq;

    while (pairs >= k) {
      count += N - r;

      freqMap.set(nums[l], freqMap.get(nums[l]) - 1);
      pairs -= freqMap.get(nums[l]);

      l++;
    }

    r++;
  }

  return count;
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2537. Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/?envType=daily-question&envId=2025-04-16

  console.log(countGood(([1, 1, 1, 1, 1], 10)));
  console.log(countGood(([3, 1, 4, 3, 2, 2, 4], 2)));
};

// User function template for javascript
/**
 * @param {number[][]} matrix
 * @returns {number}
 */

class Problem2 {
  floydWarshall(dist) {
    // code here
    /**
     * Floyd Warshall
     * Simple brute force algorithm to find distance from each node to all other nodes
     *
     * to find distance from ui to vi we take an intermediatory ki
     * and go from ui to ki and then ki to vi
     * this will be the distance from ui to vi
     *
     * we will have a adjacency matrix
     * where matrix[i][j] is weight of edge from i to j
     *
     * to find shortest distance between each pair of node
     * we take a src, a destination and an intermediatory
     * for (interm) for (src) for (dest)
     * distance[src][dest] = MIN(distance[src][dest], distance[src][interm] + distance[interm][dest])
     */

    const V = dist.length;

    for (let m = 0; m < V; m++) {
      for (let u = 0; u < V; u++) {
        for (let v = 0; v < V; v++) {
          const _distance = dist[u][m] + dist[m][v];
          if (dist[u][v] > _distance) {
            dist[u][v] = _distance;
          }

          if (u == v) dist[u][v] = 0;
        }
      }
    }

    return dist;

    // Complexity analysis
    // Time : O(V) + O(V^3)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Floyd Warshall - https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1

  console.log(
    new Problem2().floydWarshall([
      [0, -1, , 5, 100000000],
      [6, 0, , 5, 1],
      [1, 5, , 0, 100000000],
      [6, 100000000, , 2, 0],
    ]),
  );
  console.log(
    new Problem2().floydWarshall([
      [0, 1, 43],
      [1, 0, 6],
      [-1, -1, 0],
    ]),
  );
};

(() => {
  // Day 16 of April 2025

  p1();

  p2();
})();
