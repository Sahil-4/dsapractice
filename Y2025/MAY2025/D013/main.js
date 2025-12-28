/**
 * @param {string} s
 * @param {number} t
 * @return {number}
 */
var lengthAfterTransformations = function (s, t) {
  const MODO = 1e9 + 7;

  let charsFreq = new Array(26).fill(0);

  for (let i = 0; i < s.length; i++) {
    // MODO
    charsFreq[s.charCodeAt(i) - 97] = (charsFreq[s.charCodeAt(i) - 97] + 1) % MODO;
  }

  for (let i = 0; i < t; i++) {
    let charsFreqTemp = new Array(26).fill(0);

    for (let i = 0; i < 26; i++) {
      if (i != 25 && charsFreq[i] !== 0) {
        charsFreqTemp[i + 1] = charsFreqTemp[i + 1] + charsFreq[i] % MODO;
      } else if (i == 25) {
        charsFreqTemp[0] = charsFreqTemp[0] + charsFreq[i] % MODO;
        charsFreqTemp[1] = charsFreqTemp[1] + charsFreq[i] % MODO;
      }
    }

    charsFreq = charsFreqTemp;
  }

  return charsFreq.reduce((acc, e) => (((acc % MODO) + (e % MODO)) % MODO), 0);

  // Complexity analysis 
  // Time : O(N) + O(T * 25) 
  // Space : O(2 * 26) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3335. Total Characters in String After Transformations I - https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description/?envType=daily-question&envId=2025-05-13 

  console.log(lengthAfterTransformations("abcyy", 2));
  console.log(lengthAfterTransformations("azbk", 1));
  console.log(lengthAfterTransformations("jqktcurgdvlibczdsvnsg", 7517));
};

// User function Template for javascript

/**
 * @param {number} n
 * @param {number} r
 * @returns {number}
 */

class Problem2 {
  // Method to calculate nCr (Binomial Coefficient)
  nCr(n, r) {
    // code here
    if (r > n) return 0;

    let ncr = 1;

    for (let i = 0; i < r; i++) {
      ncr *= (n - i);
      ncr /= (i + 1);
    }

    return parseInt(ncr);

    // Complexity analysis 
    // Time : O(r) 
    // Space : O(1) 
  }
};

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks nCr - https://www.geeksforgeeks.org/problems/ncr1019/1 

  console.log(new Problem2().nCr(100, 100));
  console.log(new Problem2().nCr(100, 1));
  console.log(new Problem2().nCr(100, 10));
  console.log(new Problem2().nCr(100, 7));
};

(() => {
  // Day 13 of May 2025

  p1();

  p2();
})();
