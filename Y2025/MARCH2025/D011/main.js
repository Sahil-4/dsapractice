/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function (s) {
  const solve1 = () => {
    let count = 0;
    const n = s.length;

    for (let i = 0; i < n; i++) {
      const holder = new Set();
      for (let j = i; j < n; j++) {
        if (!holder.has(s[j])) {
          holder.add(s[j]);
        }

        if (holder.size == 3) {
          count += n - j;
          break;
        }
      }
    }

    return count;

    // Complexity analysis
    // Time : O(N*N)
    // Space : O(6)
  };

  const solve2 = () => {
    let count = 0;
    const n = s.length;
    const holder = { a: 0, b: 0, c: 0 };

    for (let l = 0, r = 0; r < n; r++) {
      holder[s[r]]++;

      while (holder.a > 0 && holder.b > 0 && holder.c > 0) {
        count += n - r;
        holder[s[l]]--;
        l++;
      }
    }

    return count;

    // Complexity analysis
    // Time : O(2N)
    // Space : O(6)
  };

  // return solve1();
  return solve2();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1358. Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/?envType=daily-question&envId=2025-03-11

  console.log(numberOfSubstrings("abababc"));
  console.log(numberOfSubstrings("abcabcabc"));
};

/**
 * @param {number} n
 * @returns {BigInt}
 */
class Solution {
  countWays(n) {
    // code here

    // return this.recursion(n);

    // const memo = new Array(n+1).fill(-1);
    // return this.memoization(n, memo);

    // return this.tabulation(n);

    return this.optimised(n);
  }

  recursion(n) {
    if (n == 0) return 1;
    if (n < 0) return 0;

    return this.countWays(n - 1) + this.countWays(n - 2);

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) stack
  }

  memoization(n, memo) {
    if (n == 0) return 1;
    if (n < 0) return 0;

    if (memo[n] != -1) return memo[n];

    return (memo[n] = this.memoization(n - 1, memo) + this.memoization(n - 2, memo));

    // Complexity analysis
    // Time : O(2*N)
    // Space : O(N) stack + O(N) memory
  }

  tabulation(n) {
    const memo = new Array(n + 1).fill(0);

    memo[0] = 1;
    memo[1] = 1;

    for (let i = 2; i <= n; i++) {
      memo[i] = memo[i - 1] + memo[i - 2];
    }

    return memo[n];

    // Complexity analysis
    // Time : O(N)
    // Space : O(N) memory
  }

  optimised(n) {
    let prev = 1;
    let next = 1;

    for (let i = 2; i <= n; i++) {
      let curr = prev + next;
      prev = next;
      next = curr;
    }

    return next;

    // Complexity analysis
    // Time : O(3)
    // Space : O(N) memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Ways to Reach the n'th Stair - https://www.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair-1587115620/1

  console.log(new Solution().countWays(1));
  console.log(new Solution().countWays(5));
  console.log(new Solution().countWays(7));
  console.log(new Solution().countWays(17));
  console.log(new Solution().countWays(44));
};

(() => {
  // Day 11 of March 2025

  p1();

  p2();
})();
