/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function (n) {
  return n <= 0 ? false : !(n & (n - 1));

  // Complexity analysis
  // Time : O(1)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 231. Power of Two - https://leetcode.com/problems/power-of-two/submissions/1728672097/?envType=daily-question&envId=2025-08-09

  console.log(isPowerOfTwo(0));
  console.log(isPowerOfTwo(2));
  console.log(isPowerOfTwo(1));
  console.log(isPowerOfTwo(16));
  console.log(isPowerOfTwo(3));
  console.log(isPowerOfTwo(-2147483648));
};

/**
 * @param {string} s
 * @returns {number}
 */

class Solution2 {
  // function to compute Z-array
  // z[i] = length of the longest substring starting at i
  // that matches the prefix of s
  zFunction(s) {
    let n = s.length;
    let z = new Array(n).fill(0);

    // [l, r] is the current segment that matches a prefix
    let l = 0,
      r = 0;
    for (let i = 1; i < n; ++i) {
      if (i <= r) {
        // inside the z-box: reuse previously computed values
        z[i] = Math.min(r - i + 1, z[i - l]);
      }
      // try to extend the match beyond the current z-box
      while (i + z[i] < n && s[z[i]] === s[i + z[i]]) {
        z[i]++;
      }
      // update the z-box if the match extended beyond
      // current right boundary
      if (i + z[i] - 1 > r) {
        l = i;
        r = i + z[i] - 1;
      }
    }

    return z;
  }

  getLongestPrefix(s) {
    let n = s.length;
    let z = this.zFunction(s);

    // traverse z-array to find position where
    // suffix equals prefix
    for (let i = n - 1; i > 0; i--) {
      if (z[i] === n - i) {
        // s[i:] is a suffix that is equal to
        // the prefix of length n - i
        return i;
      }
    }
    return -1;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Longest Periodic Proper Prefix - https://www.geeksforgeeks.org/problems/longest-periodic-proper-prefix/1

  const s2 = new Solution2();
  console.log(s2.getLongestPrefix("aaaaaa"));
  console.log(s2.getLongestPrefix("abcab"));
  console.log(s2.getLongestPrefix("ababd"));
};

(() => {
  // Day 9 of August 2025

  p1();

  p2();
})();
