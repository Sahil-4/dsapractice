/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var longestSubsequenceRepeatedK = function (s, k) {
  const c2i = (c) => c.charCodeAt(0) - 'a'.charCodeAt(0);

  const i2c = (i) => String.fromCharCode('a'.charCodeAt(0) + i);

  const freq = new Array(26).fill(0);
  for (let c of s) freq[c2i(c)]++;

  const slen = s.length;
  const mlen = Math.floor(slen / k);

  const canUse = new Array(26).fill(false);
  const requiredFreq = new Array(26).fill(0);
  for (let i = 0; i < 26; ++i) {
    if (freq[i] >= k) {
      canUse[i] = true;
      requiredFreq[i] = Math.floor(freq[i] / k);
    }
  }

  const isSubsequence = (s, sub, k) => {
    let i = 0, j = 0;
    const L = sub.length;
    const n = s.length;

    while (i < n && j < k * L) {
      if (s[i] === sub[j % L]) j++;
      i++;
    }

    return j === k * L;
  };

  let result = "";

  const backtracking = (s, curr, canUse, requiredFreq, k, maxLen) => {
    if (curr.length === maxLen) {
      if (isSubsequence(s, curr, k)) {
        result = curr.join("");
        return true;
      }
      return false;
    }

    for (let i = 25; i >= 0; i--) {
      if (!canUse[i] || requiredFreq[i] === 0) continue;

      curr.push(i2c(i));
      requiredFreq[i]--;

      if (backtracking(s, curr, canUse, requiredFreq, k, maxLen)) return true;

      curr.pop();
      requiredFreq[i]++;
    }

    return false;
  };

  const n = s.length;
  const maxLen = Math.floor(n / k);
  for (let len = maxLen; len >= 1; len--) {
    const tempFreq = [...requiredFreq];
    if (backtracking(s, [], canUse, tempFreq, k, len)) return result;
  }

  return "";

  // Complexity analysis 
  // Time : O(N * ((N/K)!)) 
  // Space : O(N/K) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2014. Longest Subsequence Repeated k Times - https://leetcode.com/problems/longest-subsequence-repeated-k-times/description/?envType=daily-question&envId=2025-06-27 

  console.log(longestSubsequenceRepeatedK("letsleetcode", 2));
  console.log(longestSubsequenceRepeatedK("bb", 2));
  console.log(longestSubsequenceRepeatedK("ab", 2));
};

/**
 * @param {number} n
 * @returns {number}
 */
class Problem2 {
  getCount(n) {
    // code here
    const graph = [
      [0, 8],
      [1, 2, 4],
      [2, 1, 3, 5],
      [3, 2, 6],
      [4, 1, 5, 7],
      [5, 2, 4, 6, 8],
      [6, 3, 5, 9],
      [7, 4, 8],
      [8, 5, 7, 9, 0],
      [9, 6, 8],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    ];

    // const memo = Array.from({ length : n+1 }, () => new Array(11).fill(-1));
    // return this.memoize(graph, n, 10, memo);

    return this.tabulation(graph, n);
  }

  memoize(graph, n, ci, memo) {
    if (n <= 0) return 1;

    if (memo[n][ci] !== -1) return memo[n][ci];

    let count = 0;

    for (let ni of graph[ci]) {
      count += this.memoize(graph, n - 1, ni, memo);
    }

    return memo[n][ci] = count;

    // Complexity analysis 
    // Time : O(2 * N * 10) ~ 
    // Space : O(N) stack space + GRAPH + O(10 * N * 10) memory 
  }

  tabulation(graph, n) {
    const memo = Array.from({ length: n + 1 }, () => new Array(10).fill(0));

    for (let d = 0; d <= 9; d++) {
      memo[1][d] = 1;
    }

    for (let i = 2; i <= n; i++) {
      for (let ci = 0; ci <= 9; ci++) {
        for (let ni of graph[ci]) {
          memo[i][ci] += memo[i - 1][ni];
        }
      }
    }

    let count = 0;
    for (let d = 0; d <= 9; d++) {
      count += memo[n][d];
    }

    return count;

    // Complexity analysis 
    // Time : O(10) + O(N * 10 * 5) + O(10) 
    // Space : GRAPH + O(N * 10) memory 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Mobile numeric keypad - https://www.geeksforgeeks.org/problems/mobile-numeric-keypad5456/1 

  const s = new Problem2();
  console.log(s.getCount(1));
  console.log(s.getCount(2));
  console.log(s.getCount(3));
  console.log(s.getCount(5));
  console.log(s.getCount(7));
  console.log(s.getCount(10));
  console.log(s.getCount(12));
  console.log(s.getCount(15));
};


(() => {
  // Day 27 of June 2025

  p1();

  p2();
})();
