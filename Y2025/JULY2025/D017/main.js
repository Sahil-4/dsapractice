const max = Math.max;

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumLength = function (nums, k) {
  const N = nums.length;

  const memoize = (cindex, pindex, val, memo) => {
    if (cindex >= N) return 0;

    if (memo[cindex][pindex] !== -1) {
      return memo[cindex][pindex];
    }

    // skip
    let op1 = memoize(cindex + 1, pindex, val, memo);

    // take
    let op2 = 0;
    if (pindex === 0 || (nums[pindex - 1] + nums[cindex]) % k === val) {
      op2 = 1 + memoize(cindex + 1, cindex + 1, val, memo);
    }

    return (memo[cindex][pindex] = max(op1, op2));

    // Complexity analysis
    // Time : O(2 * N * N)
    // Space : O(N) + O(N*N)
  };

  const tabulation_optimised = (val) => {
    let next = new Array(N + 1).fill(0);

    for (let cindex = N - 1; cindex >= 0; cindex--) {
      let curr = new Array(N + 1).fill(0);

      for (let pindex = cindex; pindex >= 0; pindex--) {
        // skip
        let op1 = next[pindex];

        // take
        let op2 = 0;
        if (pindex === 0 || (nums[pindex - 1] + nums[cindex]) % k === val) {
          op2 = 1 + next[cindex + 1];
        }

        curr[pindex] = max(op1, op2);
      }

      next = curr;
    }

    return next[0];

    // Complexity analysis
    // Time : O(N * N)
    // Space : O(2N)
  };

  const optimised = () => {
    let dp = Array.from({ length: k }, () => new Array(N).fill(1));
    let llen = 0;

    for (let cindex = 1; cindex < N; cindex++) {
      for (let pindex = 0; pindex < cindex; pindex++) {
        let mod = (nums[pindex] + nums[cindex]) % k;
        dp[mod][cindex] = max(dp[mod][cindex], 1 + dp[mod][pindex]);
        llen = max(llen, dp[mod][cindex]);
      }
    }

    return llen;

    // Complexity analysis
    // Time : O(N * N)
    // Space : O(K * N)
  };

  let output = 0;
  // for (let val = 0; val < k; val++) {
  //     let len = memoize(0, 0, val, Array.from({ length : N }, () => new Array(N).fill(-1)););
  //     let len = tabulation_optimised(val);
  //     output = max(output, len);
  // }

  output = optimised();

  return output;
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3202. Find the Maximum Length of Valid Subsequence II - https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/?envType=daily-question&envId=2025-07-17

  console.log(maximumLength([1, 2, 3, 4, 5], 2));
  console.log(maximumLength([1, 4, 2, 3, 1, 4], 3));
};

class Solution2 {
  maxKPower(n, k) {
    // code here
    const factors = this.primeFactors(k);
    let result = Infinity;

    for (const [prime, expInK] of factors) {
      // Count total exponent of 'prime' in n!
      // using Legendre’s formula
      const countInFact = this.legendre(n, prime);

      // Divide by its exponent in k
      result = Math.min(result, Math.floor(countInFact / expInK));
    }

    return result;
  }

  // Function to compute the prime
  // factorization of a number 'num'
  primeFactors(num) {
    const factors = [];

    let count = 0;
    while (num % 2 === 0) {
      num = Math.floor(num / 2);
      count++;
    }
    if (count > 0) factors.push([2, count]);

    // Check for odd factors starting from 3
    for (let i = 3; i * i <= num; i += 2) {
      count = 0;
      while (num % i === 0) {
        num = Math.floor(num / i);
        count++;
      }
      if (count > 0) factors.push([i, count]);
    }

    // If 'num' is still greater than 1,
    // it's a prime number
    if (num > 1) factors.push([num, 1]);

    return factors;
  }

  // Function to compute how many times prime p
  // appears in n! using Legendre's formula
  legendre(n, p) {
    let count = 0;
    let power = p;
    while (power <= n) {
      count += Math.floor(n / power);
      power *= p;
    }
    return count;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Power of k in factorial of n - https://www.geeksforgeeks.org/problems/power-of-k-in-n-where-k-may-be-non-prime4206/1

  const s2 = new Solution2();
  console.log(s2.maxKPower(7, 2));
  console.log(s2.maxKPower(10, 9));
  console.log(s2.maxKPower(10, 10));
  console.log(s2.maxKPower(100, 100));
  console.log(s2.maxKPower(100000, 100000));
};

(() => {
  // Day 17 of July 2025

  p1();

  p2();
})();
