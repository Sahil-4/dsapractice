/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
  //    1
  //   1 1
  //  1 2 1
  //  1 3 3 1
  // 1 4 6 4 1

  const output = new Array();
  output.push([1]);

  for (let r = 2; r <= numRows; r++) {
    const crow = new Array();
    crow.push(1);
    for (let c = 1; c < r - 1; c++) {
      const cval = output[r - 2][c];
      const pval = output[r - 2][c - 1];
      crow.push(cval + pval);
    }
    crow.push(1);
    output.push(crow);
  }

  return output;

  // Complexity analysis
  // Time : O(R * C)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 118. Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/?envType=daily-question&envId=2025-08-01

  console.log(generate(1));
  console.log(generate(3));
  console.log(generate(5));
  console.log(generate(7));
  console.log(generate(15));
  console.log(generate(30));
};

class Solution2 {
  countBalanced(arr) {
    // code here
    // arr[] = ["aeio", "aa", "bc", "ot", "cdbd"]
    // map = {'0.0': -1, '0.4': 0, '0.6': 1, '2.6': 2, '3.7': 3, '7.7': 4 };
    // pscv[] = [[0,0], [0,4], [0,6], [2,6], [3,7], [7,7]];
    // instead of two variables seperate for vowel and consonant we use single vowel

    const N = arr.length;

    let count = 0;

    const prefixSumMap = new Map();
    let prefixSum = 0;

    prefixSumMap.set(prefixSum, 1);

    for (let i = 0; i < N; i++) {
      for (const ch of arr[i]) {
        prefixSum += ["a", "e", "i", "o", "u"].includes(ch) ? 1 : -1;
      }

      if (prefixSumMap.has(prefixSum)) count += prefixSumMap.get(prefixSum);
      prefixSumMap.set(prefixSum, (prefixSumMap.get(prefixSum) || 0) + 1);
    }

    return count;

    // Complexity analysis
    // Time : O(N * N) ~ <=10^5
    // Space : O(N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Balancing Consonants and Vowels Ratio - https://www.geeksforgeeks.org/problems/balancing-consonants-and-vowels-ratio/1

  const s2 = new Solution2();
  console.log(s2.countBalanced(["aeio", "aa", "bc", "ot", "cdbd"]));
  console.log(s2.countBalanced(["ab", "be"]));
  console.log(s2.countBalanced(["tz", "gfg", "ae"]));
};

(() => {
  // Day 1 of August 2025

  p1();

  p2();
})();
