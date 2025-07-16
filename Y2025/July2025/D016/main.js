/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumLength = function (nums) {
  const N = nums.length;

  const followPattern = (pattern) => {
    let count = 0;
    for (let i = 0, pi = 0; i < N; i++) {
      if ((nums[i] & 1) === pattern[+pi]) {
        count++;
        pi = !pi;
      }
    }

    return count;
  };

  const op1 = followPattern([0, 0]);
  const op2 = followPattern([1, 1]);
  const op3 = followPattern([0, 1]);
  const op4 = followPattern([1, 0]);

  return Math.max(op1, op2, op3, op4);

  // Complexity analysis
  // Time : O(4N)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3201. Find the Maximum Length of Valid Subsequence I - https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/?envType=daily-question&envId=2025-07-16

  console.log(maximumLength([1, 2, 3, 4]));
  console.log(maximumLength([1, 2, 1, 1, 2, 1, 2]));
  console.log(maximumLength([1, 3]));
};

/**
 * @param {number} n
 * @returns {number}
 */
class Solution2 {
  countNumbers(n) {
    // code here

    // return this.brute(n);
    return this.optimal(n);
  }

  optimal(n) {
    // calculate primes till root(n)
    // for every pair of prime,
    // check 1 : p1^8 <= n
    // check 2 : p1 * p2 <= root(n) or (p1 * p2) * (p1 * p2) <= n,
    // if true increment count
    // else break
    // at last return count
    // some more optimization
    // find index of pair p2, p2i for p1
    // increment count by p2i
    // also make sure p2i !== p1i

    const limit = Math.floor(Math.sqrt(n));
    const primes = this.getPrimes(limit);
    let count = 0;

    // type 1 - p^8
    for (let i = 0; i < primes.length; i++) {
      let pp8 = Math.pow(primes[i], 8);
      if (pp8 <= n) count++;
      else break;
    }

    // type 2 - p1 * p2
    for (let i = 0, plen = primes.length; i < plen; i++) {
      for (let j = i + 1; j < plen; j++) {
        let p1 = primes[i];
        let p2 = primes[j];
        let prod = p1 * p2;
        if (prod <= limit) count++;
        else break;
      }
    }

    return count;

    // Complexity analysis
    // Time : O(root(N)) + O(root(N)) + O(root(N) * root(N))
    // Space : O(root(N))
  }

  getPrimes(limit) {
    // Sieve of Eratosthenes
    const sieve = new Array(limit + 1).fill(true);
    sieve[0] = sieve[1] = false;

    for (let i = 2; i * i <= limit; i++) {
      if (!sieve[i]) continue;
      for (let j = i * i; j <= limit; j += i) {
        sieve[j] = false;
      }
    }

    const primes = [];
    for (let i = 2; i <= limit; i++) {
      if (sieve[i]) primes.push(i);
    }

    return primes;
  }

  brute(n) {
    // brute force -
    // count = 0
    // run a loop num = 1, to num <= n
    // for each num, countDivisors(num)
    // if num has exactly 9 divisors increment count
    // at last return count
    // 100 = 1, 100, 2, 50, 4, 25, 5, 20, 10

    let count = 0;

    for (let num = 1; num <= n; num++) {
      let divisors = 0;

      for (let i = 1; i * i <= num; i++) {
        if (num % i === 0) {
          let a = i;
          let b = num / i;
          divisors += 1;
          divisors += a !== b;
        }
      }

      if (divisors === 9) count++;
    }

    return count;

    // Complexity analysis
    // Time : O(N * root(N))
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Nine Divisors - https://www.geeksforgeeks.org/problems/nine-divisors3751/1

  const s2 = new Solution2();
  console.log(s2.countNumbers(100));
  console.log(s2.countNumbers(200));
  console.log(s2.countNumbers(10000));
  console.log(s2.countNumbers(1000000000));
};

(() => {
  // Day 16 of July 2025

  p1();

  p2();
})();
