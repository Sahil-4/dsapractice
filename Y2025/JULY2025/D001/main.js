/**
 * @param {string} word
 * @return {number}
 */
var possibleStringCount = function (word) {
  let count = 1; // for given

  for (let l = 0, r = 0, N = word.length; l < N; ) {
    while (r < N && word[l] === word[r + 1]) r++;

    count += r - l;

    l = r = r + 1;
  }

  return count;

  // Complexity analysis
  // Time : O(N)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3330. Find the Original Typed String I - https://leetcode.com/problems/find-the-original-typed-string-i/description/?envType=daily-question&envId=2025-07-01

  console.log(possibleStringCount("abbcccc"));
  console.log(possibleStringCount("abcd"));
  console.log(possibleStringCount("aaaa"));
  console.log(possibleStringCount("abbccccdeefffhhgighhiiijklmnoooopppop"));
};

class Problem2 {
  substrCount(s, k) {
    // code here

    const c2i = (c) => c.charCodeAt(0) - "a".charCodeAt(0);

    const frequency = new Array(26).fill(0);
    let distinctCount = 0;

    let count = 0;

    for (let l = 0, r = 0; r < s.length; r++) {
      const indexR = c2i(s[r]);
      frequency[indexR]++;
      if (frequency[indexR] === 1) distinctCount++;

      if (r - l + 1 === k) {
        if (distinctCount + 1 === k) count++;

        const indexL = c2i(s[l]);
        frequency[indexL]--;
        if (frequency[indexL] === 0) distinctCount--;

        l++;
      }
    }

    return count;

    // Complexity analysis
    // Time : O(N)
    // Space : O(26)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Substrings of length k with k-1 distinct elements - https://www.geeksforgeeks.org/problems/substrings-of-length-k-with-k-1-distinct-elements/1

  const s = new Problem2();
  console.log(s.substrCount("abcc", 2));
  console.log(s.substrCount("aabab", 3));
};

(() => {
  // Day 1 of July 2025

  p1();

  p2();
})();
