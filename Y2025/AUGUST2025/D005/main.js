/**
 * @param {number[]} fruits
 * @param {number[]} baskets
 * @return {number}
 */
var numOfUnplacedFruits = function (fruits, baskets) {
  const N = fruits.length;
  let placed = 0; // number of fruits placed

  // is basket available
  const basketStatus = new Array(N).fill(true);

  // try placing fruits into first available basket
  // with capacity more then or equal to fruit
  for (const fruit of fruits) {
    for (let bi = 0; bi < N; bi++) {
      if (basketStatus[bi] && baskets[bi] >= fruit) {
        basketStatus[bi] = false;
        placed++;
        break;
      }
    }
  }

  // total fruits - placed fruits
  return N - placed;

  // Complexity analysis
  // Time : O(N * N)
  // Space : O(N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3477. Fruits Into Baskets II - https://leetcode.com/problems/fruits-into-baskets-ii/description/?envType=daily-question&envId=2025-08-05

  console.log(numOfUnplacedFruits([4, 2, 5], [3, 5, 4]));
  console.log(numOfUnplacedFruits([3, 6, 1], [6, 4, 7]));
};

/**
 * @param {string} s
 * @returns {boolean}
 */
class Solution2 {
  isPalinSent(s) {
    // code here

    // return this.sol1(s);
    return this.sol2(s);
  }

  sol2(s) {
    const lcase = (c) => c.toLowerCase();
    const isAlphaNumeric = (e) => (lcase(e) >= "a" && lcase(e) <= "z") || (e >= "0" && e <= "9");
    const isSame = (c1, c2) => lcase(c1) === lcase(c2);

    let low = 0;
    let high = s.length - 1;

    while (low < high) {
      if (!isAlphaNumeric(s[low])) low++;
      else if (!isAlphaNumeric(s[high])) high--;
      else if (isSame(s[low], s[high])) low++, high--;
      else return false;
    }

    return true;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

  sol1(s) {
    const check = (e) => (e >= "a" && e <= "z") || (e >= "0" && e <= "9");
    const arr = s.toLowerCase().split("").filter(check);

    let low = 0;
    let high = arr.length - 1;

    while (low < high) {
      if (arr[low] !== arr[high]) return false;
      low++;
      high--;
    }

    return true;

    // Complexity analysis
    // Time : O(N)
    // Space : O(N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Palindrome Sentence - https://www.geeksforgeeks.org/problems/string-palindromic-ignoring-spaces4723/1

  const s2 = new Solution2();
  console.log(s2.isPalinSent("Too hot to hoot"));
  console.log(s2.isPalinSent("Abc 012..## 10cbA"));
  console.log(s2.isPalinSent("ABC $. def01ASDF"));
  console.log(s2.isPalinSent("Abc 012..##3 10cbA"));
};

(() => {
  // Day 5 of August 2025

  p1();

  p2();
})();
