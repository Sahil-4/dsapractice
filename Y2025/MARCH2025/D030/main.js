/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function (s) {
  const N = s.length;

  const charLastOccurrence = new Map();
  for (let i = N - 1; i >= 0; i--) {
    if (!charLastOccurrence.has(s[i])) {
      charLastOccurrence.set(s[i], i);
    }
  }

  const output = [];
  let start = 0;
  let end = charLastOccurrence.get(s[0]);

  for (let i = 0; i <= N; i++) {
    if (i == N || i > end) {
      output.push(end - start + 1);
      start = i;
      end = charLastOccurrence.get(s[i]);
    } else {
      end = Math.max(end, charLastOccurrence.get(s[i]));
    }
  }

  return output;

  // Complexity analysis
  // Time : O(N) + O(N)
  // Space : O(N) memory
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 763. Partition Labels - https://leetcode.com/problems/partition-labels/description/?envType=daily-question&envId=2025-03-30

  console.log(partitionLabels("ababcbacadefegdehijhklij"));
  console.log(partitionLabels("eccbbbbdec"));
  console.log(partitionLabels("ababcbacadefegdehijhk"));
};

class Problem2 {
  startStation(gas, cost) {
    // Your code here
    const N = gas.length;

    const tgas = gas.reduce((acc, e) => acc + e, 0);
    const tcost = cost.reduce((acc, e) => acc + e, 0);

    if (tcost > tgas) return -1;

    let startPoint = 0;
    let _gas = 0;

    for (let i = 0; i < N; i++) {
      _gas += gas[i] - cost[i];

      if (_gas < 0) {
        _gas = 0;
        startPoint = i + 1;
      }
    }

    return startPoint;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Gas Station - https://www.geeksforgeeks.org/problems/circular-tour-1587115620/1

  console.log(new Problem2().startStation([4, 5, 7, 4], [6, 6, 3, 5]));
  console.log(new Problem2().startStation([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]));
};

(() => {
  // Day 30 of March 2025

  p1();

  p2();
})();
