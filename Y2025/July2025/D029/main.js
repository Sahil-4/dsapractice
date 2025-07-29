/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallestSubarrays = function (nums) {
  const N = nums.length;

  // output
  const output = new Array(N);

  // min index on right to set ith bit
  const setBitIndex = new Array(32).fill(-1);

  for (let i = N - 1; i >= 0; i--) {
    // find and update index of bits that can be set by nums[i]
    let num = nums[i];
    for (let j = 0; j < 32; j++) {
      if ((num >> j) & 1) setBitIndex[j] = i;
    }

    let endIndex = Math.max(...setBitIndex);
    output[i] = (endIndex === -1 ? i : endIndex) - i + 1;
  }

  return output;

  // Complexity analysis
  // Time : O(N * (32 + 32))
  // Space : O(32)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2411. Smallest Subarrays With Maximum Bitwise OR - https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/description/?envType=daily-question&envId=2025-07-29

  console.log(smallestSubarrays([1, 0, 2, 1, 3]));
  console.log(smallestSubarrays([1, 2]));
  console.log(smallestSubarrays([0]));
};

class Solution2 {
  asciirange(s) {
    // code here
    // [a,b,a,c,a,b]
    // [97,98,97,99,97,98]
    // [97,195,292,391,488,586]

    const N = s.length;

    // get ascii code of given char
    const ascii = (char) => char.charCodeAt(0);

    // find first & last index of every character
    const firstOccurrenceIndex = new Map();
    const lastOccurrenceIndex = new Map();
    for (let i = 0; i < N; i++) {
      if (!firstOccurrenceIndex.has(s[i])) firstOccurrenceIndex.set(s[i], i);
      lastOccurrenceIndex.set(s[i], i);
    }

    // find prefix sum
    const prefixSum = new Array(N).fill(0);
    prefixSum[0] = ascii(s[0]);
    for (let i = 1; i < N; i++) {
      prefixSum[i] = prefixSum[i - 1] + ascii(s[i]);
    }

    // build final output
    const output = new Array();
    for (const [char, sindex] of firstOccurrenceIndex) {
      const eindex = lastOccurrenceIndex.get(char);
      const sum = prefixSum[eindex - 1] - prefixSum[sindex];
      if (sum > 0) output.push(sum);
    }

    return output;

    // Complexity analysis
    // Time : O(3N)
    // Space : O(3N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks ASCII Range Sum - https://www.geeksforgeeks.org/problems/ascii-range-sum/1

  const s2 = new Solution2();
  console.log(s2.asciirange("abacab"));
  console.log(s2.asciirange("acdac"));
  console.log(s2.asciirange("a"));
  console.log(s2.asciirange("aa"));
  console.log(s2.asciirange("ab"));
  console.log(s2.asciirange("abc"));
};

(() => {
  // Day 29 of July 2025

  p1();

  p2();
})();
