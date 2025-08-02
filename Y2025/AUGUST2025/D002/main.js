const min = Math.min;
const abs = Math.abs;

/**
 * @param {number[]} basket1
 * @param {number[]} basket2
 * @return {number}
 */
var minCost = function (basket1, basket2) {
  const N = basket1.length;

  let gmin = 1e9;
  const map = new Map();
  for (let i = 0; i < N; i++) {
    map.set(basket1[i], (map.get(basket1[i]) || 0) + 1);
    map.set(basket2[i], (map.get(basket2[i]) || 0) - 1);
    gmin = min(gmin, basket1[i]);
    gmin = min(gmin, basket2[i]);
  }

  const redistributions = new Array();
  for (const [fruitCost, frequency] of map) {
    let count = abs(frequency);
    if (count & 1) return -1;
    count /= 2;
    while (count--) redistributions.push(fruitCost);
  }

  redistributions.sort((a, b) => a - b);

  let cost = 0;
  let swap = 0;

  for (let i = 0, gmin_2 = gmin * 2; i < redistributions.length / 2; i++) {
    if (redistributions[i] <= gmin_2) {
      cost += redistributions[i];
      swap += 2;
    }
  }

  cost += (redistributions.length - swap) * gmin;

  return cost;

  // Complexity analysis
  // Time : O(N) + O(2N) + O(N * Log(N)) + O(N/2)
  // Space : O(N) + O(N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2561. Rearranging Fruits - https://leetcode.com/problems/rearranging-fruits/description/?envType=daily-question&envId=2025-08-02

  console.log(minCost([4, 2, 2, 2], [1, 4, 1, 2]));
  console.log(minCost([2, 3, 4, 1], [3, 2, 5, 1]));
};

class Solution2 {
  longestSubarray(arr, k) {
    // Code Here
    // arr[] = [1, 2, 3, 4, 1], k = 2
    // inc[] = [-1, -1, 1, 1, -1]
    // psum[] = [0, -1, -2, -1, 0, -1]
    // arr[] = [1, 2, 3, 4], k = 2
    // psum[] = [0, -1, -2, -1, 0]
    // arr[] = [1, 2, 3], k = 2
    // psum[] = [-1, -2, -1]

    const N = arr.length;

    const prefixSumMap = new Map();
    let prefixSum = 0;
    let llen = 0;

    prefixSumMap.set(prefixSum, -1);

    for (let i = 0; i < N; i++) {
      prefixSum += arr[i] > k ? 1 : -1;

      if (prefixSum > 0) {
        llen = Math.max(llen, i - 0 + 1);
      }

      if (prefixSumMap.has(prefixSum - 1)) {
        llen = Math.max(llen, i - prefixSumMap.get(prefixSum - 1));
      }

      if (!prefixSumMap.has(prefixSum)) {
        prefixSumMap.set(prefixSum, i);
      }
    }

    return llen;

    // Complexity analysis
    // Time : O(N)
    // Space : O(N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Longest Subarray with Majority Greater than K - https://www.geeksforgeeks.org/problems/longest-subarray-with-majority-greater-than-k/1

  const s2 = new Solution2();
  console.log(s2.longestSubarray([1, 2, 3, 4, 1], 2));
  console.log(s2.longestSubarray([1, 2, 3, 4], 2));
  console.log(s2.longestSubarray([1, 2, 3], 2));
};

(() => {
  // Day 2 of August 2025

  p1();

  p2();
})();
