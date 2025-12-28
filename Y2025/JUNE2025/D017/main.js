const R = 1000000007n;

const P = (x, n) => {
  if (n & 1) return P(x, n - 1) * x % R;
  return n ? P(x * x % R, n >> 1) : 1n;
};

const C = (n, m) => {
  if (m * m > m * n) return 0n;
  return F[n] * I[m] % R * I[n - m] % R;
};

let p = 1n;
const F = [...Array(1e5)].map((x, i) => i ? p = p * BigInt(i) % R : p);
p = Number(R) - 2;
const I = F.map(x => P(x, p));

/**
 * @param {number} n
 * @param {number} m
 * @param {number} k
 * @return {number}
 */
var countGoodArrays = function (n, m, k) {
  return Number(C(n - 1, k) * BigInt(m) % R * P(BigInt(m - 1), n - k - 1) % R);

  // Complexity analysis 
  // Time : O(log(n − k)) 
  // Space : O(2 * MX) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3405. Count the Number of Arrays with K Matching Adjacent Elements - https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/description/?envType=daily-question&envId=2025-06-17 

  console.log(countGoodArrays(3, 6, 0));
  console.log(countGoodArrays(4, 2, 2));
  console.log(countGoodArrays(5, 2, 0));
  console.log(countGoodArrays(6, 10, 0));
  console.log(countGoodArrays(6, 10, 4));
  console.log(countGoodArrays(100000, 100000, 10));
  console.log(countGoodArrays(100000, 100000, 1000));
  console.log(countGoodArrays(100000, 100000, 99999));
};

class Problem2 {
  minimumCoins(iarr, k) {
    // code here

    const N = iarr.length;

    let output = Number.MAX_SAFE_INTEGER;

    const arr = [...iarr].sort((a, b) => a - b);

    const psum = new Array(N + 1).fill(0);
    for (let i = 0; i < N; i++) {
      psum[i + 1] = psum[i] + arr[i];
    }

    for (let i = 0; i < N; i++) {
      const lrm = psum[i]; // coins to remove from left 
      const uindex = this.upperBound(arr, arr[i] + k);
      const rrm = psum[N] - psum[uindex] - (N - uindex) * (arr[i] + k); // coins to remove from right 

      const trm = lrm + rrm; // total coins to remove 
      output = Math.min(output, trm);
    }

    return output;

    // Complexity analysis 
    // Time : O(N * Log(N)) + O(N) + O(N * Log(N)) 
    // Space : O(N) copying dataset 
  }

  upperBound(arr, bound) {
    let low = 0;
    let high = arr.length - 1;
    let out = 0;

    while (low <= high) {
      const mid = Math.floor((low + high) / 2);

      if (arr[mid] <= bound) {
        out = mid + 1;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return out;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Coin Piles - https://www.geeksforgeeks.org/problems/coin-piles5152/1 

  const s = new Problem2();
  console.log(s.minimumCoins([2, 2, 2, 2], 0));
  console.log(s.minimumCoins([1, 5, 1, 2, 5, 1], 3));
  console.log(s.minimumCoins([1, 1, 2, 2, 5], 3));
  console.log(s.minimumCoins([1, 1, 1, 1, 1, 1, 2, 2, 5], 3));
};


(() => {
  // Day 17 of June 2025

  p1();

  p2();
})();
