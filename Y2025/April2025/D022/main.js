/**
 * @param {number} n
 * @param {number} maxValue
 * @return {number}
 */
function idealArrays(n, maxValue) {

    const MOD = 1e9 + 7;
    const MAX_N = 10010;
    const MAX_P = 15; // There are up to 15 prime factors
    const c = Array.from({ length: MAX_N + MAX_P }, () => Array(MAX_P + 1).fill(0));
    const sieve = Array(MAX_N).fill(0); // Minimum prime factor
    const ps = Array.from({ length: MAX_N }, () => []); // List of prime factor counts

    (function init() {
        for (let i = 2; i < MAX_N; i++) {
            if (sieve[i] === 0) {
                for (let j = i; j < MAX_N; j += i) {
                    if (sieve[j] === 0) {
                        sieve[j] = i;
                    }
                }
            }
        }

        for (let i = 2; i < MAX_N; i++) {
            let x = i;
            while (x > 1) {
                const p = sieve[x];
                let cnt = 0;
                while (x % p === 0) {
                    x = Math.floor(x / p);
                    cnt++;
                }
                ps[i].push(cnt);
            }
        }

        c[0][0] = 1;
        for (let i = 1; i < MAX_N + MAX_P; i++) {
            c[i][0] = 1;
            for (let j = 1; j <= Math.min(i, MAX_P); j++) {
                c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD;
            }
        }
    })();

    let ans = 0n;
    for (let x = 1; x <= maxValue; x++) {
        let mul = 1n;
        for (const p of ps[x]) {
            mul = (mul * BigInt(c[n + p - 1][p])) % BigInt(MOD);
        }
        ans = (ans + mul) % BigInt(MOD);
    }

    return Number(ans);
}

const p1 = () => {
  // Problem 1 : POTD Leetcode 2338. Count the Number of Ideal Arrays - https://leetcode.com/problems/count-the-number-of-ideal-arrays/description/?envType=daily-question&envId=2025-04-22

  console.log(idealArrays(2, 5));
  console.log(idealArrays(5, 3));
  console.log(idealArrays(10000, 10000));
  console.log(idealArrays(10000, 1));
};

class Problem2 {
  findUnique(arr) {
    // code here
    return arr.reduce((acc, e) => acc ^ e, 0);

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Unique Number I - https://www.geeksforgeeks.org/problems/find-unique-number/1

  console.log(new Problem2().findUnique([1, 2, 1, 5, 5]));
  console.log(new Problem2().findUnique([2, 30, 2, 15, 20, 30, 15]));
};

(() => {
  // Day 22 of April 2025

  p1();

  p2();
})();
