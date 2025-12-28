const solve1 = (words, groups) => {
  // DP 

  const N = words.length;

  const dp = new Array(N).fill(1);
  const prev = new Array(N).fill(-1);

  let maxLen = 1;
  let endIndex = 0;

  for (let i = 1; i < N; i++) {
    let bestLen = 1;
    let bestPrev = -1;

    for (let j = i - 1; j >= 0; j--) {
      if ((groups[i] !== groups[j]) && dp[j] + 1 > bestLen) {
        bestLen = dp[j] + 1;
        bestPrev = j;
      }
    }

    dp[i] = bestLen;
    prev[i] = bestPrev;
    if (dp[i] > maxLen) {
      maxLen = dp[i];
      endIndex = i;
    }
  }

  const res = [];
  for (let i = endIndex; i !== -1; i = prev[i]) {
    res.push(words[i]);
  }

  return res.reverse();

  // Complexity analysis 
  // Time : O(N^2) + O(N) 
  // Space : O(2N) dp 
};

const solve2 = (words, groups) => {
  // Greedy 
  // - concern on selecting any sequence based on just two bits 
  // 0, 1 - if we are able to get the unique alternating set we can use it to build answer 
  // since order also does not matter we can select any unique subseq 

  let ans = [];

  for (let i = 0; i < words.length; i++) {
    if (i === 0 || groups[i] !== groups[i - 1]) {
      ans.push(words[i]);
    }
  }

  return ans;

  // Complexity analysis 
  // Time : O(N) 
  // Space : O(1) 
};

/**
 * @param {string[]} words
 * @param {number[]} groups
 * @return {string[]}
 */
var getLongestSubsequence = function (words, groups) {
  // return solve1(words, groups);

  return solve2(words, groups);
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2900. Longest Unequal Adjacent Groups Subsequence I - https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description/?envType=daily-question&envId=2025-05-15 

  console.log(getLongestSubsequence(["e", "a", "b"], [0, 0, 1]));
  console.log(getLongestSubsequence(["a", "b", "c", "d"], [1, 0, 1, 1]));
};

/**
 * @param {string} s
 * @return {number}
 */
class Problem2 {
  countSubstring(s) {
    // code here
    let cnt = 0;

    // store freq 
    const farr = Array.from({ length: 26 }, () => 0);

    for (let i = 0; i < s.length; i++) {
      let ii = s.charCodeAt(i) - "a".charCodeAt(0);
      cnt += ++farr[ii];
    }

    return cnt;

    // Complexity analysis 
    // Time : O(26) + O(S_Length) 
    // Space : O(26) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Substrings with same first and last characters - https://www.geeksforgeeks.org/problems/substrings-with-similar-first-and-last-characters3644/1 

  console.log(new Problem2().countSubstring("abcab"));
  console.log(new Problem2().countSubstring("aba"));
};


(() => {
  // Day 15 of May 2025

  p1();

  p2();
})();
