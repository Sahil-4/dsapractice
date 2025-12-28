/**
 * @param {number} n
 * @return {number[]}
 */
var lexicalOrder = function (n) {
  const numbers = [];

  const fn = (num) => {
    if (num > n) return;

    numbers.push(num);

    const tnum = (num * 10);
    for (let i = 0; i <= 9; i++) {
      fn(tnum + i);
    }
  };

  for (let i = 1; i <= 9; i++) fn(i);

  return numbers;

  // Complexity analysis 
  // Time : O(10 ^ Log(N)) which is O(N) 
  // Space : O(Log(N)) stack space 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 386. Lexicographical Numbers - https://leetcode.com/problems/lexicographical-numbers/?envType=daily-question&envId=2025-06-08 

  console.log(lexicalOrder(13));
  console.log(lexicalOrder(2));
  console.log(lexicalOrder(100));
  console.log(lexicalOrder(10000));
  console.log(lexicalOrder(50000));
};

class Problem2 {
  isSumString(s) {
    // Code here
    const N = s.length;
    for (let l1 = 1; l1 < N; l1++) {
      for (let l2 = 1; l1 + l2 < N; l2++) {
        if (this.check(s, 0, l1, l2)) return true;
      }
    }

    return false;

    // Complexity analysis (overall) 
    // Time : O(N * N * (N)) 
    // Space : O(N) stack + O(N) to build sum of a, b + sum strings 
  }

  check(s, i, l1, l2) {
    const s1 = s.substring(i, i + l1);
    const s2 = s.substring(i + l1, i + l1 + l2);

    const s3 = this.addString(s1, s2);
    const l3 = s3.length;

    if (i + l1 + l2 + l3 > s.length) return false;

    if (s3 !== s.substring(i + l1 + l2, i + l1 + l2 + l3)) return false;

    if (i + l1 + l2 + l3 === s.length) return true;

    return this.check(s, i + l1, l2, l3);
  }

  addString(a, b) {
    // return a + b = c 

    if (a.length < b.length) {
      [a, b] = [b, a];
    }

    const c = [];

    let ai = a.length - 1;
    let bi = b.length - 1;

    let carry = 0;

    while (ai >= 0 && bi >= 0) {
      let sum = +a[ai] + +b[bi] + carry;

      let digit = sum % 10;
      carry = Math.floor(sum / 10);

      c.push(digit);

      ai--;
      bi--;
    }

    while (ai >= 0) {
      let sum = +a[ai] + carry;

      let digit = sum % 10;
      carry = Math.floor(sum / 10);

      c.push(digit);

      ai--;
    }

    while (carry > 0) {
      let sum = carry;

      let digit = sum % 10;
      carry = Math.floor(sum / 10);

      c.push(digit);
    }

    return c.reverse().join("");
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Sum-string - https://www.geeksforgeeks.org/problems/sum-string3151/1 

  const sol = new Problem2();
  console.log(sol.isSumString("12243660"));
  console.log(sol.isSumString("1111112223"));
  console.log(sol.isSumString("123456"));
  console.log(sol.isSumString("32571219"));
};


(() => {
  // Day 8 of June 2025

  p1();

  p2();
})();
