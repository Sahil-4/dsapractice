/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function (n) {
  // pattern to obverse
  // [ 1 4 16 64 256 ]
  // 00000001
  // 00000100
  // 00010000
  // 01000000

  // Solution 1 :
  // this mask value will help us preserve only power of 4 (and avoid 2)
  // 1431655765 = 01010101010101010101010101010101
  const mask = 1431655765;
  return n > 0 && !(n & (n - 1)) && n & mask;

  // Complexity analysis
  // Time : O(1)
  // Space : O(1)

  // Solution 2 :
  // for (let i = 0; i < 32; i += 2) {
  //     let power = (1 << i);
  //     if (power === n) return true;
  // }
  // return false;

  // Complexity analysis
  // Time : O(32)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 342. Power of Four - https://leetcode.com/problems/power-of-four/description/?envType=daily-question&envId=2025-08-15

  console.log(isPowerOfFour(16));
  console.log(isPowerOfFour(5));
  console.log(isPowerOfFour(1));
  console.log(isPowerOfFour(4));
  console.log(isPowerOfFour(32));
  console.log(isPowerOfFour(1601645));
};

/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @returns {number[][]}
 */
class Solution2 {
  insertInterval(intervals, newInterval) {
    // code here
    // there can be three types of intervals in intervals[]
    // 1. ends before newInterval starts
    // 2. overlap with newInterval
    // 3. starts after newInterval ends

    const N = intervals.length;
    const updatedIntervals = new Array();

    let start = newInterval[0],
      end = newInterval[1];

    let i = 0;

    // case 1 : add all intervals - that are ending before new interval
    while (i < N) {
      if (intervals[i][1] >= start) break;
      updatedIntervals.push(intervals[i]);
      i++;
    }

    // case 2 : merge all intervals - that are overlapping with new interval
    while (i < N) {
      if (intervals[i][0] > end) break;
      start = Math.min(start, intervals[i][0]);
      end = Math.max(end, intervals[i][1]);
      i++;
    }
    // add merged interval
    updatedIntervals.push([start, end]);

    // case 3 : add rest intervals
    while (i < N) {
      updatedIntervals.push(intervals[i]);
      i++;
    }

    return updatedIntervals;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Insert Interval - https://www.geeksforgeeks.org/problems/insert-interval-1666733333/1

  const s2 = new Solution2();
  console.log(
    s2.insertInterval(
      [
        [1, 3],
        [4, 5],
        [6, 7],
        [8, 10],
      ],
      [5, 6]
    )
  );
  console.log(
    s2.insertInterval(
      [
        [1, 2],
        [3, 5],
        [6, 7],
        [8, 10],
        [12, 16],
      ],
      [4, 9]
    )
  );
};

(() => {
  // Day 15 of August 2025

  p1();

  p2();
})();
