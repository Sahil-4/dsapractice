/**
 * @param {string} s
 * @return {string}
 */
var makeFancyString = function (s) {
  if (s.length < 3) return s;

  const fancyStringArr = new Array();

  fancyStringArr.push(s[0]);
  fancyStringArr.push(s[1]);

  for (let i = 2; i < s.length; i++) {
    const p0 = s[i];
    const p1 = fancyStringArr.at(-1);
    const p2 = fancyStringArr.at(-2);

    if (!(p0 === p1 && p1 === p2)) {
      fancyStringArr.push(s[i]);
    }
  }

  return fancyStringArr.join("");

  // Complexity analysis
  // Time : O(N)
  // Space : O(N) to store characters of fancy(s)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1957. Delete Characters to Make Fancy String - https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/?envType=daily-question&envId=2025-07-21

  console.log(makeFancyString("leeetcode"));
  console.log(makeFancyString("aaabaaaa"));
  console.log(makeFancyString("aab"));
  console.log(makeFancyString("aaaaaaaaaaaaaaa"));
  console.log(makeFancyString("aaa"));
  console.log(makeFancyString("aa"));
  console.log(makeFancyString("a"));
};

/**
 * @param {number[]} arr
 * @returns {number}
 */
class Solution2 {
  cntCoprime(arr) {
    // code here

    // return this.brute(arr);

    return this.optimal(arr);
  }

  optimal(arr) {
    const N = arr.length;
    const arrMax = Math.max(...arr);

    const frequency = new Array(arrMax + 1).fill(0);
    const divisibles = new Array(arrMax + 1).fill(0);
    const mobius = new Array(arrMax + 1).fill(1);

    // build frequency array
    for (let i = 0; i < N; i++) {
      frequency[arr[i]]++;
    }

    // build divisible count array
    for (let k = 1; k <= arrMax; k++) {
      for (let j = k; j <= arrMax; j += k) {
        divisibles[k] += frequency[j];
      }
    }

    // compute mobius value
    const isPrime = new Array(arrMax + 1).fill(1);
    mobius[0] = 0;

    for (let i = 2; i <= arrMax; i++) {
      if (!isPrime[i]) continue;

      for (let j = i; j <= arrMax; j += i) {
        mobius[j] *= -1;
        isPrime[j] = 0;
      }

      for (let j = i * i; j <= arrMax; j += i * i) {
        mobius[j] = 0;
      }
    }

    // build output
    let count = 0;
    for (let k = 1; k <= arrMax; k++) {
      if (mobius[k] === 0 || divisibles[k] < 2) continue;

      const pairs = (divisibles[k] * (divisibles[k] - 1)) / 2;
      count += mobius[k] * pairs;
    }

    return count;

    // Complexity analysis
    // Time : O(N) + O(max(arr) * Log(max(arr))) + O(max(arr) * Log(max(arr))) + O(max(arr))
    // Space : O(4 * max(arr))
  }

  brute(arr) {
    const N = arr.length;

    // form -> (a / b)
    const gcd = (a, b) => {
      if (b === 0) return a;
      return gcd(b, a % b);
    };

    let count = 0;

    for (let i = 0; i < N; i++) {
      for (let j = i + 1; j < N; j++) {
        if (gcd(arr[i], arr[j]) === 1) count++;
      }
    }

    return count;

    // Complexity analysis
    // Time : O(N * N * Log(arr[i]))
    // Space : O(Log(arr[i])) stack for gcd
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Count the Coprimes - https://www.geeksforgeeks.org/problems/count-the-coprimes/1

  const s2 = new Solution2();
  console.log(s2.cntCoprime([1, 2, 3]));
  console.log(s2.cntCoprime([4, 8, 3, 9]));
};

(() => {
  // Day 21 of July 2025

  p1();

  p2();
})();
