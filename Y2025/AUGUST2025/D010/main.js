/**
 * @param {number} n
 * @return {boolean}
 */
var reorderedPowerOf2 = function (n) {
  const str = String(n).split("").sort().join("");

  for (let i = 0; i < 32; i++) {
    let power = 1 << i;
    let str2 = String(power).split("").sort().join("");
    if (str == str2) return true;
  }

  return false;

  // Complexity analysis
  // Time : O(32 * 32)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 869. Reordered Power of 2 - https://leetcode.com/problems/reordered-power-of-2/description/?envType=daily-question&envId=2025-08-10

  console.log(reorderedPowerOf2(1));
  console.log(reorderedPowerOf2(2));
  console.log(reorderedPowerOf2(200));
  console.log(reorderedPowerOf2(2012));
  console.log(reorderedPowerOf2(625));
};

/**
 * @param {string} s
 * @returns {number}
 */
class Solution2 {
  countPS(s) {
    // code here
    const N = s.length;

    let count = 0;

    for (let i = 0; i < N - 1; i++) {
      count += this.checkPalindrom(s, i, i);
      count += this.checkPalindrom(s, i, i + 1);
    }

    return count;

    // Complexity analysis
    // Time : O(N * N)
    // Space : O(1)
  }

  checkPalindrom(s, l, r) {
    const N = s.length;
    let len = 0;

    while (l >= 0 && r < N) {
      if (s[l] != s[r]) break;

      len += 1;
      len += l != r ? 1 : 0;

      l--;
      r++;
    }

    return Math.floor(len / 2);
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Palindrome SubStrings - https://www.geeksforgeeks.org/problems/count-palindrome-sub-strings-of-a-string0652/1

  const s2 = new Solution2();
  console.log(s2.countPS("abaab"));
  console.log(s2.countPS("aaa"));
  console.log(s2.countPS("abbaeae"));
};

(() => {
  // Day 10 of August 2025

  p1();

  p2();
})();
