
class Mat {
  constructor(copyFrom = null) {
    this.a = Array.from({ length: 26 }, () => new Array(26).fill(0n));
    if (copyFrom) {
      for (let i = 0; i < 26; i++) {
        for (let j = 0; j < 26; j++) {
          this.a[i][j] = copyFrom.a[i][j];
        }
      }
    }
  }

  mul(other) {
    const MOD = BigInt(1e9 + 7);
    const result = new Mat();
    for (let i = 0; i < 26; i++) {
      for (let j = 0; j < 26; j++) {
        for (let k = 0; k < 26; k++) {
          result.a[i][j] =
            (result.a[i][j] + this.a[i][k] * other.a[k][j]) % MOD;
        }
      }
    }
    return result;
  }
}

/* identity matrix */
function I() {
  const m = new Mat();
  for (let i = 0; i < 26; i++) {
    m.a[i][i] = 1n;
  }
  return m;
}

/* matrix exponentiation by squaring */
function quickmul(x, y) {
  let ans = I();
  let cur = new Mat(x);
  while (y > 0n) {
    if (y & (1n != 0n)) {
      ans = ans.mul(cur);
    }

    cur = cur.mul(cur);
    y >>= 1;
  }
  return ans;
}

/**
 * @param {string} s
 * @param {number} t
 * @param {number[]} nums
 * @return {number}
 */
var lengthAfterTransformations = function (s, t, nums) {
  const MOD = BigInt(1e9 + 7);

  const T = new Mat();
  for (let i = 0; i < 26; i++) {
    for (let j = 1; j <= nums[i]; j++) {
      T.a[(i + j) % 26][i] = 1n;
    }
  }

  const res = quickmul(T, t);
  const f = new Array(26).fill(0n);
  for (const ch of s) {
    f[ch.charCodeAt(0) - "a".charCodeAt(0)]++;
  }

  let ans = 0n;
  for (let i = 0; i < 26; i++) {
    for (let j = 0; j < 26; j++) {
      ans = (ans + res.a[i][j] * f[j]) % MOD;
    }
  }

  return Number(ans);

  // Complexity analysis 
  // Time : O(K^3 * Log(T)) 
  // Space : O(K^2) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3337. Total Characters in String After Transformations II - https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/description/?envType=daily-question&envId=2025-05-14 

  console.log(lengthAfterTransformations("abcyy", 2, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]));
  console.log(lengthAfterTransformations("azbk", 1, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]));
};

/**
 * @param {number} n
 * @returns {string}
 */
class Problem2 {
  countAndSay(n) {
    // return this.solve1(n);

    return this.solve2(n);
  }

  solve2(n) {
    // code here
    if (n === 1) return "1";

    let final = "1";

    for (let i = 2; i <= n; i++) {
      final = this.rle(final);
    }

    return final;

    // Complexity analysis 
    // Time : O(N * (2^N)) 
    // Space : O(2^N) 
  }

  solve1(n) {
    // code here
    if (n === 1) return "1";

    return this.rle(this.solve1(n - 1));

    // Complexity analysis 
    // Time : O(N * (2^N)) 
    // Space : O(2^N) + O(N) stack 
  }

  rle(str) {
    let d = str[0];
    let f = 1;
    let nstr = new Array();

    for (let i = 1; i <= str.length; i++) {
      if ((i == str.length) || (str[i] != d)) {
        nstr.push(f);
        nstr.push(d);

        if (i == str.length) break;

        d = str[i];
        f = 0;
      }

      f++;
    }

    return nstr.join("");
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Look and Say Pattern - https://www.geeksforgeeks.org/problems/decode-the-pattern1138/1 

  console.log(new Problem2().countAndSay(1));
  console.log(new Problem2().countAndSay(2));
  console.log(new Problem2().countAndSay(13));
  console.log(new Problem2().countAndSay(30));
};

(() => {
  // Day 14 of May 2025

  p1();

  p2();
})();
