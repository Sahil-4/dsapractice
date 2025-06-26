/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubsequence = function (s, k) {
  const N = s.length;

  let blength = 0;
  let p = 1;

  for (let i = N - 1; i >= 0; i--) {
    if (s[i] === '0') {
      blength++;
    } else if (p <= k) {
      k -= p;
      blength++;
    }

    if (p <= k) p <<= 1;
  }

  return blength;

  // Complexity analysis 
  // Time : O(N) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2311. Longest Binary Subsequence Less Than or Equal to K - https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/description/?envType=daily-question&envId=2025-06-26 

  console.log(longestSubsequence("1001010", 5));
  console.log(longestSubsequence("00101001", 1));
};

/**
 * @param {string} s
 * @param {number} k
 * @returns {number}
 */
class Problem2 {
  minValue(s, k) {
    // code here
    const frequency = new Array(26).fill(0);

    for (let c of s) frequency[this.c2i(c)]++;

    let stringValue = frequency.reduce((acc, e) => (acc + (e * e)), 0);

    while (k > 0) {
      const mi = this.getMaximum(frequency);

      stringValue -= (frequency[mi] * frequency[mi]);
      frequency[mi]--;
      stringValue += (frequency[mi] * frequency[mi]);

      k--;
    }

    return stringValue;

    // Complexity analysis 
    // Time : O(N) + O(26) + O(K * 26) 
    // Space : O(26) 
    // NOTE : this solution can be further optimised using heap 
    // and adding a base case for k === s.length 
  }

  getMaximum(frequency) {
    let mi = 0;
    for (let i = 0; i < 26; i++) {
      if (frequency[i] > frequency[mi]) mi = i;
    }

    return mi;
  };

  c2i(c) {
    const i = c.charCodeAt(0) - 'a'.charCodeAt(0);
    return i;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Game with String - https://www.geeksforgeeks.org/problems/game-with-string4100/1 

  const s = new Problem2();
  console.log(s.minValue("abbccc", 2));
  console.log(s.minValue("aaab", 2));
  console.log(s.minValue("abbbccc", 2));
  console.log(s.minValue("abbbcccddd", 3));
};


(() => {
  // Day 26 of June 2025

  p1();

  p2();
})();
