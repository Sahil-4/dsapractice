/**
 * @param {number[][]} dominoes
 * @return {number}
 */
var numEquivDominoPairs = function (dominoes) {
  // if there are n similar items 
  // we can form n(n-1) / 2 pairs 

  // just count frequency of dominoes [min(a, b), max(a, b)]
  // then count pairs 

  const map = new Map();
  for (let [a, b] of dominoes) {
    let mn = Math.min(a, b);
    let mx = Math.max(a, b);

    let key = `${mn}${mx}`;

    if (!map.has(key)) map.set(key, 0);

    map.set(key, map.get(key) + 1);
  }

  let pairsCount = 0;
  for (let [k, v] of map) {
    pairsCount += ((v * (v - 1)) / 2);
  }

  return pairsCount;

  // Complexity analysis 
  // Time : O(2N) 
  // Space : O(N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1128. Number of Equivalent Domino Pairs - https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/?envType=daily-question&envId=2025-05-04 

  console.log(numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]));
  console.log(numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]));
};

// User function Template for javascript

/**
 * @param {string} s
 * @return {number}
 */

class Problem2 {
  findSubString(str) {
    // code here
    const freq = new Map();
    for (let char of str) freq.set(char, 0);

    let mlen = str.length;

    const validWindow = () => {
      for (let [k, v] of freq) {
        if (v == 0) return false;
      }
      return true;
    };

    for (let l = 0, r = 0; r < str.length; r++) {
      freq.set(str[r], freq.get(str[r]) + 1);

      while (validWindow()) {
        mlen = Math.min(mlen, r - l + 1);
        freq.set(str[l], freq.get(str[l]) - 1);
        l++;
      }
    }

    return mlen;

    // Complexity analysis 
    // Time : O(N) + O(N * N) 
    // Space : O(N) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Smallest distinct window - https://www.geeksforgeeks.org/problems/smallest-distant-window3132/1 

  console.log(new Problem2().findSubString("geeksforgeeks"));
  console.log(new Problem2().findSubString("aaab"));
  console.log(new Problem2().findSubString("aabcbcdbca"));
  console.log(new Problem2().findSubString("abcdefghijklmnopqrstuvwxyz"));
};

(() => {
  // Day 4 of April 2025

  p1();

  p2();
})();
