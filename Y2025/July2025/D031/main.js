/**
 * @param {number[]} arr
 * @return {number}
 */
var subarrayBitwiseORs = function (arr) {
  let result = new Set();
  let curr = new Set();
  let prev = new Set();

  for (const el of arr) {
    for (const orVal of prev) {
      result.add(orVal | el);
      curr.add(orVal | el);
    }

    result.add(el);
    curr.add(el);
    prev = new Set([...curr]);

    curr.clear();
  }

  return result.size;

  // Complexity anlaysis
  // Time : O(N * 32)
  // Space : O(32)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 898. Bitwise ORs of Subarrays - https://leetcode.com/problems/bitwise-ors-of-subarrays/description/?envType=daily-question&envId=2025-07-31

  console.log(subarrayBitwiseORs([0]));
  console.log(subarrayBitwiseORs([1, 1, 2]));
  console.log(subarrayBitwiseORs([1, 2, 4]));
};

/**
 * @param {number[][]} intervals
 * @param {number} k
 * @returns {number}
 */
class Solution2 {
  powerfulInteger(intervals, k) {
    // code here

    // return this.brute(intervals, k);
    return this.optimal(intervals, k);
  }

  optimal(intervals, k) {
    // modified difference array technique
    // not storing all keys, but only edges
    // this helps reducing space and time a lot

    // frequency map for counting of values occurrence
    const map = new Map();
    let keys = new Set();

    // build difference array map
    for (const [startI, endI] of intervals) {
      map.set(startI, (map.get(startI) || 0) + 1);
      map.set(endI + 1, (map.get(endI + 1) || 0) - 1);
      keys.add(startI);
      keys.add(endI + 1);
    }

    // sort all keys
    keys = new Array(...keys).sort((a, b) => a - b);

    let ans = -1;
    let prefixSum = 0;

    // find optimal answer
    for (const key of keys) {
      const val = map.get(key);

      if (val >= 0) {
        prefixSum += val;
        if (prefixSum >= k) ans = key;
      } else {
        if (prefixSum >= k) ans = key - 1;
        prefixSum += val;
      }
    }

    return ans;

    // Complexity analysis
    // Time : O(N) + O(N * Log(N)) + O(N)
    // Space : O(2N)
  }

  brute(intervals, k) {
    // can be solved using difference array technique
    // n = 3, intervals[][] = [[1, 3], [4, 6], [3, 4]], k = 2
    // minVal = 1, maxVal = 7;
    // differenceArray = [1, 0, 1, 0, -1. 0, -1];
    // valCount = [1, 1, 2, 2, 1. 1, 0];

    // n = 5, intervals[][] = [[16, 21], [5, 8], [12, 17], [17, 29], [9, 24]], k = 3
    // range = [5, 30]
    // darr = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, -1, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, -1]
    // count = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0]

    // find range
    const range = [1000000000, 0];
    for (const [startI, endI] of intervals) {
      range[0] = Math.min(range[0], startI);
      range[1] = Math.max(range[1], endI);
    }

    // create difference array
    const T = range[1] - range[0] + 1;
    const darr = new Array(T + 1).fill(0);

    // build difference array
    for (const [startI, endI] of intervals) {
      darr[startI - range[0]]++;
      darr[endI - range[0] + 1]--;
    }

    // count array - utilise darr for count

    // count number of occurrence of each value
    for (let i = 1; i <= T; i++) {
      darr[i] += darr[i - 1];
    }

    // find the answer
    for (let i = T; i >= 0; i--) {
      if (darr[i] >= k) return i + range[0];
    }

    return -1;

    // Complexity analysis
    // Time : O(N) + O(N) + O(T) + O(T)
    // Space : O(T)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Powerful Integer - https://www.geeksforgeeks.org/problems/powerfull-integer--170647/1

  const s2 = new Solution2();
  console.log(
    s2.powerfulInteger(
      [
        [1, 3],
        [4, 6],
        [3, 4],
      ],
      2
    )
  );
  console.log(
    s2.powerfulInteger(
      [
        [1, 4],
        [12, 45],
        [3, 8],
        [10, 12],
      ],
      3
    )
  );
  console.log(
    s2.powerfulInteger(
      [
        [16, 21],
        [5, 8],
        [12, 17],
        [17, 29],
        [9, 24],
      ],
      3
    )
  );
};

(() => {
  // Day 31 of July 2025

  p1();

  p2();
})();
