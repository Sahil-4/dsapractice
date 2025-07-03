/**
 * @param {number} k
 * @return {character}
 */
var kthCharacter = function (k) {
  // dry run for k = 5
  // word = ['a'], next = ['b']
  // word = ['a', 'b'], next = ['b', 'c']
  // word = ['a', 'b', 'b', 'c'], next = ['b', 'c', 'c', 'd']
  // word = ['a', 'b', 'b', 'c', 'b', 'c', 'c', 'd']
  // output = "b" 

  const nextCharacter = (e) => {
    if (e === "z") return "a";
    const ni = e.charCodeAt(0) + 1;
    return String.fromCharCode(ni);
  };

  const word = ["a"];

  while (word.length < k) {
    const next = word.map(nextCharacter);
    word.push(...next);
  }

  return word[k - 1];

  // Complexity analysis
  // Time : O(2^(k - 1))
  // Space : O(2^(k - 1))
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3304. Find the K-th Character in String Game I - https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/?envType=daily-question&envId=2025-07-03

  console.log(kthCharacter(1));
  console.log(kthCharacter(10));
  console.log(kthCharacter(100));
  console.log(kthCharacter(500));
};

/**
 * @param {string} s
 * @param {number} k
 * @returns {number}
 */
class Solution2 {
  longestKSubstr(s, k) {
    // code here
    const c2i = (c) => c.charCodeAt(0) - "a".charCodeAt(0);

    const frequency = new Array(26).fill(0);
    let distinct = 0;
    let llen = 0;

    for (let l = 0, r = 0; r < s.length; r++) {
      const index = c2i(s[r]);
      frequency[index]++;
      if (frequency[index] === 1) distinct++;

      while (distinct > k) {
        const index = c2i(s[l]);
        frequency[index]--;
        if (frequency[index] === 0) distinct--;
        l++;
      }

      if (distinct === k) {
        llen = Math.max(llen, r - l + 1);
      }
    }

    return llen === 0 ? -1 : llen;

    // Complexity analysis
    // Time : O(26) + O(2N)
    // Space : O(26)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Longest Substring with K Uniques - https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

  const s = new Solution2();
  console.log(s.longestKSubstr("aabacbebebe", 3));
  console.log(s.longestKSubstr("aaaa", 2));
  console.log(s.longestKSubstr("aabaaab", 2));
};

(() => {
  // Day 3 of July 2025

  p1();

  p2();
})();
