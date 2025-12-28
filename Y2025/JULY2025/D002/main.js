/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var possibleStringCount = function (word, k) {
  const MODO = 1000000007;
  const N = word.length;

  const groups = new Array();
  for (let i = 1, count = 1; i <= N; i++, count++) {
    if (i === N || word[i] !== word[i - 1]) {
      groups.push(count);
      count = 0;
    }
  }

  let totalCombinations = groups.reduce((acc, e) => (acc * e) % MODO, 1);
  if (k <= groups.length) return totalCombinations;

  let dp = new Array(k).fill(0);
  dp[0] = 1;

  for (let i = 0; i < groups.length; i++) {
    const dp2 = new Array(k).fill(0);
    const group = groups[i];
    let wsum = 0;

    for (let j = i; j < k; j++) {
      dp2[j] = (dp2[j] + wsum) % MODO;
      wsum = (wsum + dp[j]) % MODO;

      if (j >= group) {
        wsum = (wsum - dp[j - group] + MODO) % MODO;
      }
    }

    dp = dp2;
  }

  const invalidCombinations = dp.reduce((acc, e) => (acc + e) % MODO, 0);
  return (totalCombinations - invalidCombinations + MODO) % MODO;

  // Complexity analysis
  // Time : O(N) + O(N) + O(N * K)
  // Space : O(N) + O(2K)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3333. Find the Original Typed String II - https://leetcode.com/problems/find-the-original-typed-string-ii/description/?envType=daily-question&envId=2025-07-02

  console.log(possibleStringCount("aabbccdd", 7));
  console.log(possibleStringCount("aabbccdd", 8));
  console.log(possibleStringCount("aaabbb", 3));
  console.log(possibleStringCount("aaabbbaaa", 3));
  console.log(possibleStringCount("aabbccdd", 4));
  console.log(possibleStringCount("aa", 2));
  console.log(possibleStringCount("bbbbbyyyyyyyyyyccccccccyyyqqqqhffffhhhhhhhhsswwwwvvvvvlllldddddddddnnnnnnvr", 69));
};

/**
 * @param {number[]} arr
 * @returns {number}
 */
class Problem2 {
  totalElements(arr) {
    // code here
    const K = 2;
    const frequencyMap = new Map();
    let distinct = 0;

    let llen = 0;

    for (let l = 0, r = 0; r < arr.length; r++) {
      // add current window last element
      const e = arr[r];

      // update frequency of element e
      const oldF = frequencyMap.get(e) || 0;
      frequencyMap.set(e, oldF + 1);

      // increment distinct count
      if (oldF === 0) distinct++;

      // remove extra elements
      while (distinct > K) {
        const e = arr[l];

        // update frequency of element e
        const oldF = frequencyMap.get(e) || 0;
        frequencyMap.set(e, oldF - 1);

        // increment distinct count
        if (oldF === 1) distinct--;

        l++;
      }

      // update output
      if (distinct <= K) {
        llen = Math.max(llen, r - l + 1);
      }
    }

    return llen;

    // Complexity analysis
    // Time : O(2N)
    // Space : O(N)
  }
}

const p2 = () => {
  // Problem2 2 : POTD Geeksforgeeks Longest subarray with Atmost two distinct integers - https://www.geeksforgeeks.org/problems/fruit-into-baskets-1663137462/1

  const s = new Problem2();
  console.log(s.totalElements([2, 1, 2]));
  console.log(s.totalElements([2, 1, 3, 3, 3, 3, 2]));
  console.log(s.totalElements([3, 3, 3, 3]));
};

(() => {
  // Day 2 of July 2025

  p1();

  p2();
})();
