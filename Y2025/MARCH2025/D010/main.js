/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var countOfSubstrings = function (word, k) {
  var solve1 = function () {
    const n = word.length;
    let count = 0; // count of substrings

    for (let left = 0; left < n; left++) {
      // holds vowels and consonants
      let vowels = new Set();
      let consonants = new Array();

      // windows
      for (let right = left; right < n; right++) {
        if (["a", "e", "i", "o", "u"].includes(word[right])) {
          vowels.add(word[right]);
        } else {
          consonants.push(word[right]);
        }

        if (vowels.size == 5 && consonants.length == k) {
          count++;
        }
      }
    }

    return count;

    // Complexity analysis
    // Time : O(N*N)
    // Space : O(5) + O(K)
  };

  var solve2 = function () {
    const n = word.length;
    let count = 0;

    // find index of next consonant
    const nextConsonant = new Array(n).fill(n);
    for (let i = n - 1, nci = n; i >= 0; i--) {
      nextConsonant[i] = nci;
      if (!["a", "e", "i", "o", "u"].includes(word[i])) {
        nci = i;
      }
    }

    // holds count of vowel and consonant
    const holder = {
      a: 0,
      e: 0,
      i: 0,
      o: 0,
      u: 0,
      CO: 0,
    };

    for (let left = 0, right = 0; right < n; right++) {
      if (["a", "e", "i", "o", "u"].includes(word[right])) {
        holder[word[right]]++;
      } else {
        holder["CO"]++;
      }

      while (holder["CO"] > k) {
        if (["a", "e", "i", "o", "u"].includes(word[left])) {
          holder[word[left]]--;
        } else {
          holder["CO"]--;
        }
        left++;
      }

      while (
        left < n &&
        holder["a"] > 0 &&
        holder["e"] > 0 &&
        holder["i"] > 0 &&
        holder["o"] > 0 &&
        holder["u"] > 0 &&
        holder["CO"] == k
      ) {
        count += nextConsonant[right] - right;
        if (["a", "e", "i", "o", "u"].includes(word[left])) {
          holder[word[left]]--;
        } else {
          holder["CO"]--;
        }
        left++;
      }
    }

    return count;

    // Complexity analysis
    // Time : O(N) + O(2N)
    // Space : O(N) + O(6)
  };

  // return solve1();
  return solve2();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3306. Count of Substrings Containing Every Vowel and K Consonants II - https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/?envType=daily-question&envId=2025-03-10

  console.log(countOfSubstrings("ieaouqqieaouqq", 1));
  console.log(countOfSubstrings("aeiou", 0));
};

// User function Template for javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */
class Solution {
  editDistance(s1, s2) {
    // code here

    // return this.recursion(s1, 0, s2, 0);

    // const n = s1.length;
    // const m = s2.length;
    // const memo = Array.from({ length: n }, () => new Array(m).fill(-1));
    // return this.memoization(s1, 0, s2, 0, memo);

    return this.tabulation(s1, s2);
  }

  recursion(s1, i1, s2, i2) {
    if (i1 == s1.length) return s2.length - i2;
    if (i2 == s2.length) return s1.length - i1;

    if (s1[i1] == s2[i2]) {
      return this.recursion(s1, i1 + 1, s2, i2 + 1);
    }

    let op1 = this.recursion(s1, i1, s2, i2 + 1);
    let op2 = this.recursion(s1, i1 + 1, s2, i2);
    let op3 = this.recursion(s1, i1 + 1, s2, i2 + 1);

    return 1 + Math.min(op1, op2, op3);

    // Complexity analysis
    // Time : O(3^(N|M))
    // Space : O(N|M) stack
  }

  memoization(s1, i1, s2, i2, memo) {
    if (i1 == s1.length) return s2.length - i2;
    if (i2 == s2.length) return s1.length - i1;

    if (memo[i1][i2] != -1) return memo[i1][i2];

    let out = 0;

    if (s1[i1] == s2[i2]) {
      out = this.memoization(s1, i1 + 1, s2, i2 + 1, memo);
    } else {
      let op1 = this.memoization(s1, i1, s2, i2 + 1, memo);
      let op2 = this.memoization(s1, i1 + 1, s2, i2, memo);
      let op3 = this.memoization(s1, i1 + 1, s2, i2 + 1, memo);
      out = 1 + Math.min(op1, op2, op3);
    }

    return (memo[i1][i2] = out);

    // Complexity analysis
    // Time : O(2*3*(N*M))
    // Space : O(N|M) stack + O(N*M) memory
  }

  tabulation(s1, s2) {
    const n = s1.length;
    const m = s2.length;
    const memo = Array.from({ length: n + 1 }, () => new Array(m + 1).fill(0));

    // base case
    for (let i2 = 0; i2 <= m; i2++) memo[n][i2] = m - i2;
    for (let i1 = 0; i1 <= n; i1++) memo[i1][m] = n - i1;

    for (let i1 = n - 1; i1 >= 0; i1--) {
      for (let i2 = m - 1; i2 >= 0; i2--) {
        let out = 0;

        if (s1[i1] == s2[i2]) {
          out = memo[i1 + 1][i2 + 1];
        } else {
          let op1 = memo[i1][i2 + 1];
          let op2 = memo[i1 + 1][i2];
          let op3 = memo[i1 + 1][i2 + 1];
          out = 1 + Math.min(op1, op2, op3);
        }

        memo[i1][i2] = out;
      }
    }

    return memo[0][0];

    // Complexity analysis
    // Time : O(N*M)
    // Space : O(N*M) memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Edit Distance - https://www.geeksforgeeks.org/problems/edit-distance3702/1

  console.log(new Solution().editDistance("abd", "abd"));
  console.log(new Solution().editDistance("abd", "abdc"));
  console.log(new Solution().editDistance("abdc", "abd"));
};

(() => {
  // Day 10 of March 2025

  p1();

  p2();
})();
