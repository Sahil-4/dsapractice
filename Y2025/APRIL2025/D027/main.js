/**
 * @param {number[]} nums
 * @return {number}
 */
var countSubarrays = function (nums) {
  const n = nums.length;
  let count = 0;

  for (let i = 1; i < n - 1; i++) {
    // const mid = nums[i] / 2;
    // const lr = nums[i-1] + nums[i+1];

    // divistion is expensive 

    const mid = nums[i];
    const lr = (nums[i - 1] + nums[i + 1]) * 2;

    count += (mid === lr);
  }

  return count;

  // Complexity analysis 
  // Time : O(N) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3392. Count Subarrays of Length Three With a Condition - https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description/?envType=daily-question&envId=2025-04-27 

  console.log(countSubarrays([1, 2, 1, 4, 1]));
  console.log(countSubarrays([1, 1, 1]));
  console.log(countSubarrays([2, -7, -6]));
};


// User function Template for javascript

/**
 * @param {string} s1
 * @param {string} s2
 * @returns {string}
 */

class Problem2 {
  multiplyStrings(s1, s2) {
    // code here
    const zero = "0".charCodeAt(0);

    let negativeCheck = false;

    if (s1[0] == '-') {
      s1 = s1.substring(1);
      negativeCheck = !negativeCheck;
    }
    if (s2[0] == '-') {
      s2 = s2.substring(1);
      negativeCheck = !negativeCheck;
    }

    s1 = s1.split("").reverse().join("");
    s2 = s2.split("").reverse().join("");

    const l1 = s1.length;
    const l2 = s2.length;

    const t = l1 + l2;

    const output = new Array(t).fill(0);

    for (let i = 0; i < l1; i++) {
      for (let j = 0; j < l2; j++) {
        output[i + j] += ((s1.charCodeAt(i) - zero) * (s2.charCodeAt(j) - zero));
        output[i + j + 1] += Math.floor(output[i + j] / 10);
        output[i + j] %= 10;
      }
    }

    while (output.at(-1) == 0) output.pop();

    if (negativeCheck && output.length) output.push('-');
    if (output.length === 0) output.push(0);

    output.reverse();

    return output.join("");

    // Complexity analysis 
    // Time : O(L1 * l2) 
    // Space : O(2t) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Multiply two strings - https://www.geeksforgeeks.org/problems/multiply-two-strings/1 

  console.log(new Problem2().multiplyStrings("2000", "12"));
  console.log(new Problem2().multiplyStrings("2000", "-12"));
  console.log(new Problem2().multiplyStrings("-2000", "-12"));
  console.log(new Problem2().multiplyStrings("-2000", "0000"));
};

(() => {
  // Day 27 of April 2025

  p1();

  p2();
})();
