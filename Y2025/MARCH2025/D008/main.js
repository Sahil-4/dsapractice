/**
 * @param {string} blocks
 * @param {number} k
 * @return {number}
 */
var minimumRecolors = function (blocks, k) {
  var solve1 = function () {
    const n = blocks.length;
    let mopr = Infinity;

    for (let i = 0; i <= n - k; i++) {
      let opr = 0;
      for (let j = i; j < i + k; j++) {
        if (blocks[j] == "W") opr++;
      }
      mopr = Math.min(mopr, opr);
    }

    return mopr;

    // Complexity analysis
    // Time : O(N*K)
    // Space : O(1)
  };

  var solve2 = function () {
    const n = blocks.length;
    let mopr = Infinity;
    let topr = 0;

    // iterator
    let l = 0, r = 0;

    // first window
    for (; r < k; r++) {
      if (blocks[r] == "W") topr++;
    }

    // first window ke liye
    mopr = Math.min(mopr, topr);

    // rest windows
    for (; r < n; r++, l++) {
      if (blocks[l] == "W") topr--;
      if (blocks[r] == "W") topr++;

      // baaki ki window ke liye
      mopr = Math.min(mopr, topr);
    }

    return mopr;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  };

  // return solve1();
  return solve2();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2379. Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/?envType=daily-question&envId=2025-03-08

  console.log(minimumRecolors("BBBBB", 5));
  console.log(minimumRecolors("WWWWW", 5));
  console.log(minimumRecolors("WWBWW", 5));
  console.log(minimumRecolors("BBWBB", 5));
};

var longestPalindrome = function (s) {
  // code here
  let lstring = [0, 1];
  let llen = 1;

  for (let i = 0, n = s.length; i < n; i++) {
    // odd length palindrome
    let l1 = i, h1 = i;
    while (l1 >= 0 && h1 < n && s[l1] == s[h1]) {
      l1--, h1++;
    }
    if (h1 - l1 - 1 > llen) {
      llen = h1 - l1 - 1;
      lstring = [l1 + 1, h1];
    }

    // even length palindrome
    let l2 = i - 1, h2 = i;
    while (l2 >= 0 && h2 < n && s[l2] == s[h2]) {
      l2--, h2++;
    }
    if (h2 - l2 - 1 > llen) {
      llen = h2 - l2 - 1;
      lstring = [l2 + 1, h2];
    }
  }

  return s.substring(lstring[0], lstring[1]);

  // Complexity analysis
  // Time : O(N*N)
  // Space : O(1)
};

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Longest Palindrome in a String - https://www.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1

  console.log(longestPalindrome("dkabcdfl"));
  console.log(longestPalindrome("dkabcbadfl"));
  console.log(longestPalindrome("dkabccbadfl"));
};

(() => {
  // Day 8 of March 2025

  p1();

  p2();
})();
