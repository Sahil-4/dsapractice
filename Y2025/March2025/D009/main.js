/**
 * @param {number[]} colors
 * @param {number} k
 * @return {number}
 */
var numberOfAlternatingGroups = function (colors, k) {
  var solve1 = function () {
    const n = colors.length;
    let count = 0;

    for (let i = 0; i < n; i++) {
      let flag = true;
      let prev = -1;

      for (let j = i; j < i + k && flag; j++) {
        flag = prev != colors[j % n];
        prev = colors[j % n];
      }

      if (flag) count++;
    }

    return count;

    // Complexity analysis
    // Time : O(N*K)
    // Space : O(1)
  };

  var solve2 = function () {
    const n = colors.length;
    let count = 0;
    let prev = -1;

    for (let l = 0, r = 0; l < n; r++) {
      if (prev == colors[r % n]) l = r;

      prev = colors[r % n];

      if (r - l + 1 >= k) {
        count++;
        l++;
      }
    }

    return count;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  };

  // return solve1();
  return solve2();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3208. Alternating Groups II - https://leetcode.com/problems/alternating-groups-ii/description/?envType=daily-question&envId=2025-03-09

  console.log(numberOfAlternatingGroups([0, 1, 0, 1], 4));
  console.log(numberOfAlternatingGroups([0, 1, 0, 1], 3));
};

/**
 * @param string s
 * @returns number
 */
function countPS(s) {
  // code here
  const k = 2;
  const n = s.length;
  let count = 0;

  for (let i = 0; i < n; i++) {
    // odd length palindromic sub strings
    let l1 = i, h1 = i;
    while (l1 >= 0 && h1 < n && s[l1] == s[h1]) {
      if (h1 - l1 + 1 >= k) count++;
      l1--, h1++;
    }

    // even length palindromic sub strings
    let l2 = i - 1, h2 = i;
    while (l2 >= 0 && h2 < n && s[l2] == s[h2]) {
      if (h2 - l2 + 1 >= k) count++;
      l2--, h2++;
    }
  }

  return count;

  // Complexity analysis
  // Time : O(N*N) >
  // Space : O(1)
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Palindrome SubStrings - https://www.geeksforgeeks.org/problems/count-palindrome-sub-strings-of-a-string0652/1

  console.log(countPS("abaab"));
  console.log(countPS("abaabab"));
};

(() => {
  // Day 9 of March 2025

  p1();

  p2();
})();
