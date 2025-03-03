/**
 * @param {number[]} nums
 * @param {number} pivot
 * @return {number[]}
 */
var pivotArray = function (nums, pivot) {
  function solve1() {
    let output = [];

    nums.forEach((e) => {
      if (e < pivot) output.push(e);
    });
    nums.forEach((e) => {
      if (e == pivot) output.push(e);
    });
    nums.forEach((e) => {
      if (e > pivot) output.push(e);
    });

    return output;

    // Complexity analysis
    // Time : O(3N)
    // Space : O(1)
  }

  function solve2() {
    const n = nums.length;
    let output = new Array(n).fill(-1);
    let lt = 0,
      eq = 0,
      gt = 0;

    for (let i = 0; i < n; i++) {
      if (nums[i] < pivot) eq++;
      if (nums[i] <= pivot) gt++;
    }

    for (let i = 0; i < n; i++) {
      if (nums[i] < pivot) {
        output[lt++] = nums[i];
      } else if (nums[i] == pivot) {
        output[eq++] = nums[i];
      } else if (nums[i] > pivot) {
        output[gt++] = nums[i];
      }
    }

    return output;

    // Complexity analysis
    // Time : O(2N)
    // Space : O(1)
  }

  // return solve1();
  return solve2();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2161. Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/?envType=daily-question&envId=2025-03-03

  console.log(pivotArray([9, 12, 5, 10, 14, 3, 10], 10));
  console.log(pivotArray([9, 12, 5, 10, 14, 3, 10], 13));
};

var longestSubarray = function (arr, x) {
  // code here
  const n = arr.length;
  if (n < 2) return arr;

  function solve1() {
    let start = 0,
      end = 0;
    for (let i = 0; i < n; i++) {
      let tstart = i,
        tend = i;
      let minE = arr[i],
        maxE = arr[i];

      for (let j = i; j < n; j++) {
        minE = Math.min(minE, arr[j]);
        maxE = Math.max(maxE, arr[j]);
        if (maxE - minE > x) break;
        tend++;
      }

      if (tend - tstart > end - start) {
        start = tstart;
        end = tend;
      }
    }

    return arr.slice(start, end);

    // Complexity analysis
    // Time : O(N*N)
    // Space : O(1)
  }

  function solve2() {
    let maxDq = [];
    let minDq = [];

    let start = 0;
    let len = 0;
    let temp = 0;

    for (let end = 0; end < n; end++) {
      // remove smaller element indexes
      while (maxDq.length && arr[maxDq.at(-1)] < arr[end]) maxDq.pop();
      // remove larger element indexes
      while (minDq.length && arr[minDq.at(-1)] > arr[end]) minDq.pop();

      maxDq.push(end);
      minDq.push(end);

      while (minDq.length && maxDq.length && arr[maxDq.at(0)] - arr[minDq.at(0)] > x) {
        temp++;
        if (minDq[0] < temp) minDq.shift();
        if (maxDq[0] < temp) maxDq.shift();
      }

      if (end - temp + 1 > len) {
        len = end - temp + 1;
        start = temp;
      }
    }

    return arr.slice(start, start + len);

    // Complexity analysis
    // Time : O(2N)
    // Space : O(2N)
  }

  // return solve1();
  return solve2();
};

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Longest Bounded-Difference Subarray - https://www.geeksforgeeks.org/problems/longest-bounded-difference-subarray/1

  console.log(longestSubarray([9, 12, 5, 10, 14, 3, 10], 5));
  console.log(longestSubarray([9, 12, 5, 10, 14, 3, 10], 2));
  console.log(longestSubarray([9, 12, 5, 10, 14, 3, 10], 4));
};

(() => {
  // Day 3 of March 2025

  p1();

  p2();
})();
