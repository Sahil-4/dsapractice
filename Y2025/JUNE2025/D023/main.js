/**
 * @param {number} k
 * @param {number} n
 * @return {number}
 */
var kMirror = function (k, n) {
  const convertToBase = (number) => {
    // convert given base 10 number to base k 
    const baseK = new Array();

    while (number > 0) {
      const d = number % k;
      number = Math.floor(number / k);
      baseK.push(d);
    }

    return baseK.join("");
  };

  const isPalindrome = (numberStr) => {
    // check if a number (string) is palindrome 
    let l = 0;
    let h = numberStr.length - 1;

    while (l < h) {
      if (numberStr[l] !== numberStr[h]) return false;
      l++, h--;
    }

    return true;
  };

  let sum = 0;
  let L = 1;

  while (n > 0) {
    const hlen = Math.floor((L + 1) / 2);
    const low = Math.pow(10, hlen - 1);
    const high = Math.pow(10, hlen) - 1;

    for (let num = low; num <= high; num++) {
      const left = num.toString().split("");
      const right = num.toString().split("").reverse();

      if (L & 1) right.shift();

      const number10 = parseInt(left.join("") + right.join("")); // palindrome (base 10)
      const numberK = convertToBase(number10); // palindrome (base k)

      if (isPalindrome(numberK)) {
        n--;
        sum += number10;
      }
      if (n === 0) break;
    }

    L++;
  }

  return sum;

  // Complexity analysis 
  // Time : O((10^(D/2)) * D), D = number of digits Log(N) 
  // Space : O(D) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2081. Sum of k-Mirror Numbers - https://leetcode.com/problems/sum-of-k-mirror-numbers/description/?envType=daily-question&envId=2025-06-23 

  console.log(kMirror(2, 5));
  console.log(kMirror(3, 7));
  console.log(kMirror(7, 17));
  console.log(kMirror(9, 30));
};

/**
 * @param {number[]} arr
 * @returns {string}
 */
class Problem2 {
  minSum(arr) {
    // code here
    const N = arr.length;
    const carr = [...arr].sort((a, b) => a - b);

    const num1 = new Array();
    const num2 = new Array();

    for (let i = 0; i < N; i += 2) {
      num1.push(carr[i]);
      if (i + 1 < N) num2.push(carr[i + 1]);
    }

    num1.reverse();
    num2.reverse();

    const sum = new Array();
    let carry = 0;
    let i, j;
    i = j = 0;

    while (i < num1.length && j < num2.length) {
      const dsum = num1[i] + num2[j] + carry;
      const d = dsum % 10;
      carry = (dsum - d) / 10;

      sum.push(d);

      i++, j++;
    }

    while (i < num1.length) {
      const dsum = num1[i] + carry;
      const d = dsum % 10;
      carry = (dsum - d) / 10;

      sum.push(d);

      i++;
    }

    while (j < num2.length) {
      const dsum = num2[j] + carry;
      const d = dsum % 10;
      carry = (dsum - d) / 10;

      sum.push(d);

      j++;
    }

    while (carry > 0) {
      const dsum = carry;
      const d = dsum % 10;
      carry = (dsum - d) / 10;

      sum.push(d);
    }

    while (sum.at(-1) === 0) sum.pop();

    return sum.reverse().join("");

    // Complexity analysis 
    // Time : O(N) + O(N * Log(N)) + O(N) + O(N) + O(N) + O(N) + O(N) 
    // Space : O(3N) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Minimum sum - https://www.geeksforgeeks.org/problems/minimum-sum4058/1 

  const s = new Problem2();
  console.log(s.minSum([6, 8, 4, 5, 2, 3]));
  console.log(s.minSum([5, 3, 0, 7, 4]));
  console.log(s.minSum([9, 4]));
  console.log(s.minSum([9]));
};


(() => {
  // Day 23 of June 2025

  p1();

  p2();
})();
