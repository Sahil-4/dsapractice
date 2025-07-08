/**
 * @param {number[][]} events
 * @param {number} k
 * @return {number}
 */
var maxValue = function (events, k) {
  const sortedEvents = [...events].sort((e1, e2) => e1[0] - e2[0]);
  const N = sortedEvents.length;

  const memo = Array.from({ length: N + 1 }, () => new Array(k + 1).fill(0));

  for (let index = N - 1; index >= 0; index--) {
    for (let left = 1; left <= k; left++) {
      // skip & and call fpr next event
      let skip = 0 + memo[index + 1][left];

      // pick & and call fpr next event
      let nindex = index + 1;
      while (nindex < N && sortedEvents[nindex][0] <= sortedEvents[index][1]) nindex++;
      let pick = sortedEvents[index][2] + memo[nindex][left - 1];

      // updae maximum value
      memo[index][left] = Math.max(skip, pick);
    }
  }

  return memo[0][k];

  // Complexity analysis
  // Time : O(N) + O(N * Log(N)) + O(N * K)
  // Space : O(N) + O(N * K)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1751. Maximum Number of Events That Can Be Attended II - https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/?envType=daily-question&envId=2025-07-08

  console.log(maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2)); // 7
  console.log(maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 10]], 2)); // 10
  console.log(maxValue([[1, 1, 1], [2, 2, 2], [3, 3, 3],[4, 4, 4]], 3)); // 9 
};

class Solution2 {
  findGreater(arr) {
    // code here
    const N = arr.length;
    const ngfe = new Array(N).fill(-1);

    const frequency = new Map();
    for (let i = N - 1; i >= 0; i--) {
      const e = arr[i];
      const f = (frequency.get(e) || 0) + 1;
      frequency.set(e, f);
    }

    const stack = [];
    for (let i = N - 1; i >= 0; i--) {
      const e = arr[i];
      const f = frequency.get(e);

      while (stack.length && stack.at(-1)[0] <= f) stack.pop();

      if (stack.length) ngfe[i] = stack.at(-1)[1];

      stack.push([f, e]);
    }

    return ngfe;

    // Complexity analysis
    // Time : O(N) + O(N) + O(2N)
    // Space : O(N) + O(N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Next element with greater frequency - https://www.geeksforgeeks.org/problems/next-element-with-greater-frequency--170637/1

  const s2 = new Solution2();
  console.log(s2.findGreater([1, 1, 2, 3, 4, 2, 1, 3, 4, 5])); // [2, 3, -1, -1, -1, -1, -1, -1, -1, -1]
  console.log(s2.findGreater([1, 2, 3, 4, 5])); // [-1, -1, -1, -1, -1]
};

(() => {
  // Day 8 of July 2025

  p1();

  p2();
})();
