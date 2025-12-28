/**
 * @param {number} days
 * @param {number[][]} meetings
 * @return {number}
 */
var countDays = function (days, meetings) {
  // Approach :
  // perform merge intervals - sort schedules on day, merge overlapping schedules
  // then for every interval find the days and reduce it from total days
  // finally return the left days

  const intervals = [...meetings];

  // sorting fn
  const fn = (a, b) => {
    if (a[0] != b[0]) return a[0] < b[0] ? -1 : 1;
    if (a[1] != b[1]) return a[1] < b[1] ? -1 : 1;
    return 0;
  };
  intervals.sort(fn);

  // now merge intervals
  let daysLeft = days;
  let prev = intervals[0];

  for (let i = 0; i <= intervals.length; i++) {
    if (i == intervals.length || prev[1] < intervals[i][0]) {
      daysLeft -= prev[1] - prev[0] + 1;
      prev = intervals[i];
    } else {
      let curr = intervals[i];
      prev[0] = Math.min(prev[0], curr[0]);
      prev[1] = Math.max(prev[1], curr[1]);
    }
  }

  return daysLeft;

  // Complexity analysis
  // Time : O(N*LOG(N)) for sorting + O(N) for removing meeting days
  // Space : O(N) for copying given dataset
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3169. Count Days Without Meetings - https://leetcode.com/problems/count-days-without-meetings/description/?envType=daily-question&envId=2025-03-24

  console.log(countDays(10, [ [5, 7], [1, 3], [9, 10] ]));
  console.log(countDays(5, [ [2, 4], [1, 3] ]));
  console.log(countDays(6, [ [1, 6] ]));
};

class Problem2 {
  /**
   * @param {number[]} arr
   * @return {number}
   */
  matrixMultiplication(arr) {
    // code here

    // return this.recursion(arr, 1, arr.length-1);

    // const n = arr.length;
    // const memo = Array.from({ length: n }, () => new Array(n).fill(-1));
    // return this.memoize(arr, 1, n-1, memo);

    return this.tabulation(arr);
  }

  recursion(arr, i, j) {
    if (i == j) return 0;

    let minOperations = Infinity;

    for (let k = i; k < j; k++) {
      let leftPart = this.recursion(arr, i, k);
      let rightPart = this.recursion(arr, k + 1, j);

      let wholePart = arr[i - 1] * arr[k] * arr[j];

      let toperations = leftPart + wholePart + rightPart;

      minOperations = Math.min(minOperations, toperations);
    }

    return minOperations;

    // Complexity analysis
    // Time : O(2K^N)
    // Space : O(N)
  }

  memoize(arr, i, j, memo) {
    if (i == j) return 0;

    if (memo[i][j] != -1) return memo[i][j];

    let minOperations = Infinity;

    for (let k = i; k < j; k++) {
      let leftPart = this.memoize(arr, i, k, memo);
      let rightPart = this.memoize(arr, k + 1, j, memo);

      let wholePart = arr[i - 1] * arr[k] * arr[j];

      let toperations = leftPart + wholePart + rightPart;

      minOperations = Math.min(minOperations, toperations);
    }

    return (memo[i][j] = minOperations);

    // Complexity analysis
    // Time : O(2*K*N*N)
    // Space : O(N) stack + O(N*N) memory
  }

  tabulation(arr) {
    const n = arr.length;
    const memo = Array.from({ length: n }, () => new Array(n).fill(0));

    // base - handled

    // recurrence
    for (let i = n - 1; i >= 1; i--) {
      for (let j = i + 1; j <= n - 1; j++) {
        let minOperations = Infinity;

        for (let k = i; k < j; k++) {
          let leftPart = memo[i][k];
          let rightPart = memo[k + 1][j];

          let wholePart = arr[i - 1] * arr[k] * arr[j];

          let toperations = leftPart + wholePart + rightPart;

          minOperations = Math.min(minOperations, toperations);
        }

        memo[i][j] = minOperations;
      }
    }

    // return
    return memo[1][n - 1];

    // Complexity analysis
    // Time : O(N*N*N)
    // Space : O(N*N) memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Matrix Chain Multiplication - https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1

  console.log(new Problem2().matrixMultiplication([2, 1, 3, 4]));
  console.log(new Problem2().matrixMultiplication([1, 2, 3, 4, 3]));
  console.log(new Problem2().matrixMultiplication([3, 4]));
};

(() => {
  // Day 24 of March 2025

  p1();

  p2();
})();
