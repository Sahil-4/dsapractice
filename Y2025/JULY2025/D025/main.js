/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSum = function (nums) {
  const set = new Set();

  let sum = 0;
  let count = 0;
  let maxx = -1000;

  for (let e of nums) {
    maxx = Math.max(maxx, e);
    if (e > 0 && !set.has(e)) {
      sum += e;
      set.add(e);
      count++;
    }
  }

  return count != 0 ? sum : maxx;

  // Complexity analysis
  // Time : O(N)
  // Space : O(N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3487. Maximum Unique Subarray Sum After Deletion - https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description/?envType=daily-question&envId=2025-07-25

  console.log(maxSum([1, 2, 3, 4, 5]));
  console.log(maxSum([1, 1, 0, 1, 1]));
  console.log(maxSum([1, 2, -1, -2, 1, 0, -1]));
  console.log(maxSum([-100]));
  console.log(maxSum([-100, -1]));
  console.log(maxSum([-100, 0]));
  console.log(maxSum([-100, 1]));
};

/*
 * @param {number[]} arr
 * @returns {number}
 */
class Solution2 {
  maxCircularSum(arr) {
    // code here

    // return this.brute(arr);

    return this.optimal(arr);
  }

  brute(arr) {
    const N = arr.length;

    let msum = -10001;

    for (let i = 0; i < N; i++) {
      let tsum = 0;
      for (let j = 0; j < N; j++) {
        const index = (i + j) % N;
        const element = arr[index];
        tsum += element;
        msum = Math.max(msum, tsum);
      }
    }

    return msum;

    // Complexity analysis
    // Time : O(N * N)
    // Space : O(1)
  }

  optimal(arr) {
    const N = arr.length;

    const totSum = arr.reduce((acc, e) => acc + e, 0);

    const minSum = this.kadane(arr, N, Math.min);
    const maxSum = this.kadane(arr, N, Math.max);

    const circularSum = totSum - minSum;

    return maxSum > 0 ? Math.max(maxSum, circularSum) : maxSum;

    // Complexity analysis
    // Time : O(3N)
    // Space : O(1)
  }

  kadane(arr, N, fn) {
    let sum = arr[0];
    let msum = arr[0];

    for (let i = 1; i < N; i++) {
      sum = fn(sum + arr[i], arr[i]);
      msum = fn(msum, sum);
    }

    return msum;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Max Circular Subarray Sum - https://www.geeksforgeeks.org/problems/max-circular-subarray-sum-1587115620/1

  const s2 = new Solution2();
  console.log(s2.maxCircularSum([8, -8, 9, -9, 10, -11, 12]));
  console.log(s2.maxCircularSum([1, -1, 5, -1, 2]));
  console.log(s2.maxCircularSum([-1, -2, -3]));
  console.log(s2.maxCircularSum([1, 2, 3]));
};

(() => {
  // Day 25 of July 2025

  p1();

  p2();
})();
