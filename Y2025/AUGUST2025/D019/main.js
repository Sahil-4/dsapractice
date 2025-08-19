/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function (nums) {
  const subArrayCount = (l) => (l * (l + 1)) / 2;

  let count = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) continue;
    let j = i;
    while (nums[j] === 0) j++;
    count += subArrayCount(j - i);
    i = j;
  }

  return count;

  // Complexity analysis
  // Time : O(N)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2348. Number of Zero-Filled Subarrays - https://leetcode.com/problems/number-of-zero-filled-subarrays/?envType=daily-question&envId=2025-08-19

  console.log(zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]));
  console.log(zeroFilledSubarray([0, 0, 0, 2, 0, 0]));
  console.log(zeroFilledSubarray([2, 10, 2019]));
  console.log(zeroFilledSubarray([0, 0, 0, 0, 0, 0]));
};

class Solution2 {
  /**
    @param {number[]}
    @returns {number[]}
  */
  farMin(arr) {
    // Code Here

    // return this.brute(arr);

    return this.optimal(arr);
  }

  binarySearch(arr, low, high, val) {
    // find farthest element smaller then val

    let ans = -1;

    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      if (arr[mid] < val) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return ans;
  }

  optimal(arr) {
    const N = arr.length;

    const suffixArray = new Array(N);
    for (let i = N - 1; i >= 0; i--) {
      if (i === N - 1) {
        suffixArray[i] = arr[i];
        continue;
      }
      suffixArray[i] = Math.min(arr[i], suffixArray[i + 1]);
    }

    const output = new Array(N).fill(-1);
    for (let i = 0; i < N; i++) {
      output[i] = this.binarySearch(suffixArray, i + 1, N - 1, arr[i]);
    }

    return output;

    // Complexity analysis
    // Time : O(N * Log(N))
    // Space : O(1)
  }

  brute(arr) {
    const N = arr.length;
    const output = new Array(N).fill(-1);

    for (let i = 0; i < N; i++) {
      for (let j = N - 1; j > i; j--) {
        if (arr[j] < arr[i]) {
          output[i] = j;
          break;
        }
      }
    }

    return output;

    // Complexity analysis
    // Time : O(N * N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Farthest Smaller Right - https://www.geeksforgeeks.org/problems/farthest-smaller-right/1

  const s2 = new Solution2();
  console.log(s2.farMin([2, 5, 1, 3, 2]));
  console.log(s2.farMin([2, 3, 5, 4, 1]));
  console.log(s2.farMin([5, 4, 6, 3, 1, 2, 5, 7, 8, 9, 5, 41, 1]));
};

(() => {
  // Day 19 of August 2025

  p1();

  p2();
})();
