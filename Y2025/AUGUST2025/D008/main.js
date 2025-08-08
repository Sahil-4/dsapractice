/**
 * @param {number} n
 * @return {number}
 */
var soupServings = function (n) {
  const P = 0.25; // probablity of one event to happen

  if (n > 5000) return 1;

  const calculate = (s1, s2, dp) => {
    // both emptied at same time
    if (s1 <= 0 && s2 <= 0) return 0.5;
    // soup 1 emptied first
    if (s1 <= 0) return 1.0;
    // soup 2 emptied first
    if (s2 <= 0) return 0.0;

    // memoized value
    if (dp[s1][s2] !== -1) return dp[s1][s2];

    dp[s1][s2] = 0.0;

    // we have total 4 events
    dp[s1][s2] += P * calculate(s1 - 4, s2 - 0, dp); // pour 100 mL from type A and 0 mL from type B
    dp[s1][s2] += P * calculate(s1 - 3, s2 - 1, dp); // pour 75 mL from type A and 25 mL from type B
    dp[s1][s2] += P * calculate(s1 - 2, s2 - 2, dp); // pour 50 mL from type A and 50 mL from type B
    dp[s1][s2] += P * calculate(s1 - 1, s2 - 3, dp); // pour 25 mL from type A and 75 mL from type B

    return dp[s1][s2];
  };

  const N = Math.ceil(n / 25.0);
  const dp = Array.from({ length: N + 1 }, () => new Array(N + 1).fill(-1));
  return calculate(N, N, dp);

  // Complexity analysis
  // Time : O(2*N*N)
  // Space : O(N*N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 808. Soup Servings - https://leetcode.com/problems/soup-servings/?envType=daily-question&envId=2025-08-08

  console.log(soupServings(50));
  console.log(soupServings(100));
  console.log(soupServings(10000));
  console.log(soupServings(50001));
  console.log(soupServings(500000));
};

/**
 * @param {string} s
 * @returns {number}
 */
class Solution2 {
  getLPSLength(s) {
    // code here

    const n = s.length;

    // longest common prefix suffix
    const lcps = new Array(n).fill(0);

    for (let i = 1, lpslen = 0; i < n; i++) {
      // lpslen = longest common prefix suffix length till ith index
      while (lpslen > 0 && s[i] != s[lpslen]) lpslen = lcps[lpslen - 1];
      if (s[i] == s[lpslen]) lcps[i] = ++lpslen;
    }

    return lcps[n - 1];

    // Complexity analysis
    // Time : O(2N)
    // Space : O(N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Longest Prefix Suffix - https://www.geeksforgeeks.org/problems/longest-prefix-suffix2527/1

  const s2 = Solution2();
  console.log(s2.getLPSLength("abab"));
  console.log(s2.getLPSLength("aabcdaabc"));
  console.log(s2.getLPSLength("aaaa"));
};

(() => {
  // Day 8 of August 2025

  p1();

  p2();
})();
