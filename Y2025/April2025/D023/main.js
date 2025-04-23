/**
 * @param {number} n
 * @return {number}
 */
var countLargestGroup = function (n) {
  let count = 0;
  let maxFreq = 0;

  // digitSum(i) -> frequency
  const freqMap = new Map();

  const digitSum = (i) =>
    String(i)
      .split("")
      .reduce((acc, e) => acc + +e, 0);

  for (let i = 1; i <= n; i++) {
    let sum = digitSum(i);
    let freq = (freqMap.get(sum) || 0) + 1;

    freqMap.set(sum, freq);

    if (freq == maxFreq) {
      count += 1;
    } else if (freq > maxFreq) {
      count = 1;
      maxFreq = freq;
    }
  }

  return count;

  // Complexity analysis
  // Time : O(N * Log(N))
  // Space : O(N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1399. Count Largest Group - https://leetcode.com/problems/count-largest-group/description/?envType=daily-question&envId=2025-04-23

  console.log(countLargestGroup(1));
  console.log(countLargestGroup(3));
  console.log(countLargestGroup(5));
  console.log(countLargestGroup(13));
  console.log(countLargestGroup(10000));
};

// User function Template for javascript

/**
 * @param {number[]} arr
 * @return {number[]}
 */

class Problem2 {
  singleNum(arr) {
    // code here

    // different approaches to solve
    // 1. Brute force - O(N^2) using two nested loops
    // 2. Sorting - O(N*Log(N)) + O(N) and O(N) space for copying dataset
    // 3. Using Freq Map - O(N) + O(N) and O(N) space for map
    // 4. Bit magic - O(N) and O(1)

    // suppose unique numbes are x, y
    // we have to return [x, y]

    let _x_y_XOR = arr.reduce((acc, e) => acc ^ e, 0);

    // in _x_y_XOR, all elements having pair cancelled out each other
    // and we are left with XOR(x, y), where [x, y] is output

    // need rightmost set bit
    let rightestSet = _x_y_XOR & -_x_y_XOR;

    // rightestSet, whatever bit is this we can surely say
    // that is x and y this bit was different

    // now we have to find those numbers who have this bit set
    // and not set
    // hence we have to part the arr into two groups
    // and then individually perform xor of both groups
    // finally return [min(x, y), max(x, y)] as per problem requirement
    // here creating two groups is not required as we just have to perform XOR

    let x_y = 0;
    let y_x = 0;

    for (let e of arr) {
      if ((e & rightestSet) !== 0) {
        x_y = x_y ^ e;
      } else {
        y_x = y_x ^ e;
      }
    }

    return [Math.min(x_y, y_x), Math.max(x_y, y_x)];

    // Complexity analysis
    // Time : O(2N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Unique Number II - https://www.geeksforgeeks.org/problems/finding-the-numbers0215/1

  console.log(new Problem2().singleNum([1, 2, 3, 2, 1, 4]));
  console.log(new Problem2().singleNum([2, 1, 3, 2]));
  console.log(new Problem2().singleNum([2, 1, 3, 3]));
};

(() => {
  // Day 23 of April 2025

  p1();

  p2();
})();
