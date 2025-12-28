/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
function closestPrimes(left, right) {
  function solve1() {
    // for output
    let output = [-1, -1];
    let diff = right + left;

    // generate prime numbers in the range [left, right] inclusive
    let primes = [];

    for (let i = left; i <= right; i++) {
      if (i < 2) continue;
      let isPrime = true;
      for (let j = 2; j < i && isPrime; j++) {
        if (i % j == 0) isPrime = false;
      }

      if (isPrime) primes.push(i);
    }

    for (let i = 0; i < primes.length; i++) {
      for (let j = i + 1; j < primes.length; j++) {
        if (primes[j] - primes[i] < diff) {
          diff = primes[j] - primes[i];
          output = [primes[i], primes[j]];
        }
      }
    }

    return output;

    // Complexity analysis
    // Time : O(right * right) + O(N*N)
    // Space : O(N)
    // N = right - left;
  }

  function solve2() {
    // primes between 0 to N, inclusive - true is prime, else false
    const primes = new Array(right + 1).fill(true);
    primes[0] = primes[1] = false;

    // even numbers except 2
    for (let i = 4; i <= right; i += 2) {
      primes[i] = false;
    }

    // then rest odds
    for (let i = 3; i * i <= right; i += 2) {
      if (!primes[i]) continue;
      for (let j = i * i; j <= right; j += 2 * i) {
        primes[j] = false;
      }
    }

    // for output
    let output = [-1, -1];
    let diff = right;
    let prevPrime = 0; // last seen prime

    // index on primes bool array
    for (let currPrime = Math.max(2, left); currPrime < primes.length; currPrime++) {
      if (!primes[currPrime]) continue;

      if (prevPrime && currPrime - prevPrime < diff) {
        diff = currPrime - prevPrime;
        output = [prevPrime, currPrime];
      }

      prevPrime = currPrime;
    }

    return output;

    // Complexity analysis
    // Time : O(right * Log(right)) + O(N)
    // Space : O(right)
    // N = right - left
  }

  // return solve1();
  return solve2();
}

const p1 = () => {
  // Problem 1 : POTD Leetcode 2523. Closest Prime Numbers in Range - https://leetcode.com/problems/closest-prime-numbers-in-range/description/?envType=daily-question&envId=2025-03-07

  console.log(closestPrimes(1, 10));
  console.log(closestPrimes(1, 100));
  console.log(closestPrimes(1, 1000));
  console.log(closestPrimes(2, 700));
};

/**
 * @param {string} s
 * @return {number}
 */
class Solution {
  longestPalinSubseq(s) {
    // code here
    // return this.recursion(s, 0, s.length-1);

    const n = s.length;
    // const memo = Array.from({ length: n }, () => new Array(n).fill(-1));
    // return this.memoize(s, 0, s.length-1, memo);

    return this.tabulation(s, n);
  }

  recursion(str, i, j) {
    if (i > j) return 0;
    if (i == j) return 1;

    let op1 = this.recursion(str, i + 1, j);
    let op2 = this.recursion(str, i, j - 1);
    let op3 = 0;
    if (str[i] == str[j]) {
      op3 = 2 + this.recursion(str, i + 1, j - 1);
    }

    return Math.max(op1, op2, op3);

    // Complexity analysis
    // Time : O(3^N)
    // Space : O(N) stack
  }

  memoize(str, i, j, memo) {
    if (i > j) return 0;
    if (i == j) return 1;

    if (memo[i][j] != -1) return memo[i][j];

    let op1 = this.memoize(str, i + 1, j, memo);
    let op2 = this.memoize(str, i, j - 1, memo);
    let op3 = 0;
    if (str[i] == str[j]) {
      op3 = 2 + this.memoize(str, i + 1, j - 1, memo);
    }

    return (memo[i][j] = Math.max(op1, op2, op3));

    // Complexity analysis
    // Time : O(2*N*N)
    // Space : O(N) stack + O(N*N) memory
  }

  tabulation(str, n) {
    const memo = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));

    // edge cases
    for (let ij = 0; ij <= n; ij++) memo[ij][ij] = 1;

    for (let i = n - 1; i >= 0; i--) {
      for (let j = i + 1; j < n; j++) {
        let op1 = memo[i + 1][j];
        let op2 = memo[i][j - 1];
        let op3 = 0;
        if (str[i] == str[j]) {
          op3 = 2 + memo[i + 1][j - 1];
        }

        memo[i][j] = Math.max(op1, op2, op3);
      }
    }

    return memo[0][n - 1];

    // Complexity analysis
    // Time : O(N*N)
    // Space : O(N*N) memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Longest Palindromic Subsequence - https://www.geeksforgeeks.org/problems/longest-palindromic-subsequence-1612327878/1

  console.log(new Solution().longestPalinSubseq("babad"));
  console.log(new Solution().longestPalinSubseq("abcdabxab"));
};

(() => {
  // Day 7 of March 2025

  p1();

  p2();
})();
