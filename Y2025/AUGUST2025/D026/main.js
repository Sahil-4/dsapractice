/**
 * @param {number[][]} dimensions
 * @return {number}
 */
var areaOfMaxDiagonal = function (dimensions) {
  let [maxDiagonalArea, maxDiagonalLength] = [0, 0];

  for (const [length, width] of dimensions) {
    const area = length * width;
    const diagonalLength = Math.sqrt(length * length + width * width);

    if (
      diagonalLength > maxDiagonalLength ||
      (diagonalLength == maxDiagonalLength && area > maxDiagonalArea)
    ) {
      [maxDiagonalArea, maxDiagonalLength] = [area, diagonalLength];
    }
  }

  return maxDiagonalArea;

  // Complexity analysis
  // Time : O(N * sqrt(Arr[i]))
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3000. Maximum Area of Longest Diagonal Rectangle - https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/?envType=daily-question&envId=2025-08-26

  console.log(
    areaOfMaxDiagonal([
      [9, 3],
      [8, 6],
    ])
  );
  console.log(
    areaOfMaxDiagonal([
      [3, 4],
      [4, 3],
    ])
  );
};

/**
 * @param {string} s1
 * @param {string} s2
 * @returns {bool}
 */
class Solution2 {
  isSubSeq(s1, s2) {
    // code here
    const s1len = s1.length;
    const s2len = s2.length;

    if (s1len > s2len) return false;
    if (s1len == s2len && s1 != s2) return false;

    // using two pointers
    let p1 = 0;
    let p2 = 0;

    while (p1 < s1len && p2 < s2len) {
      if (s1[p1] == s2[p2]) p1++;
      p2++;
    }

    return p1 >= s1len;

    // Complexity analysis
    // Time : O(s2len)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Check if a String is Subsequence of Other - https://www.geeksforgeeks.org/problems/given-two-strings-find-if-first-string-is-a-subsequence-of-second/1

  const s2 = new Solution2();
  console.log(s2.isSubSeq("AXY", "YADXCP"));
  console.log(s2.isSubSeq("gksrek", "geeksforgeeks"));
  console.log(s2.isSubSeq("ABC", "AFBHC"));
};

(() => {
  // Day 26 of August 2025

  p1();

  p2();
})();
