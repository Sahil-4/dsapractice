/**
 * @param {string} word
 * @return {boolean}
 */
var isValid = function (word) {
  if (word.length < 3) return false;
  if (!/^[a-zA-Z0-9]+$/.test(word)) return false;
  if (!/[aeiouAEIOU]/.test(word)) return false;
  if (!/[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]/.test(word)) return false;
  return true;

  // Complexity analysis
  // Time : O(N)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3136. Valid Word - https://leetcode.com/problems/valid-word/description/?envType=daily-question&envId=2025-07-15

  console.log(isValid("b3"));
  console.log(isValid("123"));
  console.log(isValid("abc"));
  console.log(isValid("ABC"));
  console.log(isValid("123abAC"));
  console.log(isValid("123abc#ABC"));
  console.log(isValid("UuE6"));
};

class Solution2 {
  divby13(s) {
    // code here
    // table = [13, 26, 39, 52, 65, 78, 91, 104, 117]
    // 2911285 / 13
    // num = 0, while num < 13
    // num = num * 10 + s[i];
    // num = 29, find <= 29 in table
    // num -= find(29)
    // num = 3, while num < 13
    // num = num * 10 + s[i];
    // num = 31
    // after processing all indices num should become 0 (at the end)
    // divby13(s) is true if num === 0

    const N = s.length;

    const table = [13, 26, 39, 52, 65, 78, 91, 104, 117];
    const findLTE = (num) => {
      let low = 0,
        high = 8;
      let out = 0;

      while (low <= high) {
        let mid = Math.floor((low + high) / 2);

        if (table[mid] <= num) {
          out = mid;
          low = mid + 1;
        } else {
          high = mid - 1;
        }
      }

      return table[out];
    };

    let num = 0;
    let i = 0;

    while (i < N) {
      while (i < N && num < 13) {
        num = num * 10;
        num = num + +s[i];
        i++;
      }

      num = num - findLTE(num);
    }

    return num === 0;

    // Complexity analysis
    // Time : O(N * Log(9))
    // Space : O(9)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Divisible by 13 - https://www.geeksforgeeks.org/problems/divisible-by-13/1

  const s2 = new Solution2();
  console.log(s2.divby13("2911285"));
  console.log(s2.divby13("26"));
  console.log(s2.divby13("26262626262626262626262626262626262626262626262626"));
  console.log(s2.divby13("27272727272727272727272727272727272727272727272727"));
};

(() => {
  // Day 15 of July 2025

  p1();

  p2();
})();
