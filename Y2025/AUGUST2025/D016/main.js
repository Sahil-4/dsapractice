/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number = function (num) {
  const str = String(num).split("");
  for (let i = 0; i < str.length; i++) {
    if (str[i] === "6") {
      str[i] = "9";
      break;
    }
  }

  return parseInt(str.join(""));

  // Complexity analysis
  // Time : O(2D)
  // Space : O(D)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1323. Maximum 69 Number - http://leetcode.com/problems/maximum-69-number/description/?envType=daily-question&envId=2025-08-16

  console.log(maximum69Number(9669));
  console.log(maximum69Number(9996));
  console.log(maximum69Number(9999));
};

/**
 * @param {number[]} arr
 * @returns {String}
 */
class Solution2 {
  findLargest(arr) {
    // code here

    // custom comparator
    const comparator = (a, b) => (a + b > b + a ? -1 : 1);

    // convert integer number to string
    const strs = arr.map(String);

    // sort string(numbers)
    strs.sort(comparator);

    // remove trailing zeroes
    while (strs.length > 1 && strs[0] == "0") strs.shift();

    // build output string
    return strs.join("");

    // Complexity analysis
    // Time : O(N) + O(N * Log(N)) + O(N)
    // Space : O(N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Form the Largest Number - https://www.geeksforgeeks.org/problems/largest-number-formed-from-an-array1117/1

  const s2 = new Solution2();
  console.log(s2.findLargest([4, 5, 7, 15, 20, 11]));
  console.log(s2.findLargest([3, 30, 34, 5, 9]));
  console.log(s2.findLargest([54, 546, 548, 60]));
  console.log(s2.findLargest([3, 4, 6, 5, 9]));
  console.log(s2.findLargest([0, 0, 0, 0, 0, 0, 0, 0]));
};

(() => {
  // Day 16 of August 2025

  p1();

  p2();
})();
