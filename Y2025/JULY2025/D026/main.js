/**
 * @param {number} n
 * @param {number[][]} conflictingPairs
 * @return {number}
 */
var maxSubarrays = function (n, conflictingPairs) {
  const conflictingPoints = Array.from({ length: n + 1 }, () => new Array());
  for (let pair of conflictingPairs) {
    const [a, b] = [Math.min(...pair), Math.max(...pair)];
    conflictingPoints[b].push(a);
  }

  let validSubarrays = 0;
  let fmaxConflictingPoint = 0;
  let smaxConflictingPoint = 0;
  const extraSubArrays = new Array(n + 1).fill(0);

  for (let end = 1; end <= n; end++) {
    for (const start of conflictingPoints[end]) {
      if (start >= fmaxConflictingPoint) {
        smaxConflictingPoint = fmaxConflictingPoint;
        fmaxConflictingPoint = start;
      } else if (start >= smaxConflictingPoint) {
        smaxConflictingPoint = start;
      }
    }

    validSubarrays += end - fmaxConflictingPoint;
    extraSubArrays[fmaxConflictingPoint] += fmaxConflictingPoint - smaxConflictingPoint;
  }

  return validSubarrays + Math.max(...extraSubArrays);

  // Complexity analysis
  // Time : O(PN) + O(N + PN)
  // Space : O(2N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3480. Maximize Subarrays After Removing One Conflicting Pair - https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/description/?envType=daily-question&envId=2025-07-26

  console.log(
    maxSubarrays(4, [
      [2, 3],
      [1, 4],
    ])
  );
  console.log(
    maxSubarrays(5, [
      [1, 2],
      [2, 5],
      [3, 5],
    ])
  );
};

class Solution2 {
  findMajority(arr) {
    // code here
    // Moores voting algo

    const N = arr.length;
    const n3 = Math.floor(N / 3);

    let candidate1 = null;
    let candidate1VoteCount = 0;
    let candidate2 = null;
    let candidate2VoteCount = 0;

    for (let i = 0; i < N; i++) {
      if (candidate1 === arr[i]) {
        candidate1VoteCount++;
      } else if (candidate2 === arr[i]) {
        candidate2VoteCount++;
      } else if (candidate1VoteCount === 0) {
        candidate1 = arr[i];
        candidate1VoteCount = 1;
      } else if (candidate2VoteCount === 0) {
        candidate2 = arr[i];
        candidate2VoteCount = 1;
      } else {
        candidate1VoteCount--;
        candidate2VoteCount--;
      }
    }

    candidate1VoteCount = 0;
    candidate2VoteCount = 0;
    for (let i = 0; i < N; i++) {
      candidate1VoteCount += arr[i] === candidate1;
      candidate2VoteCount += arr[i] === candidate2;
    }

    const maj = [];
    if (candidate1VoteCount > n3) maj.push(candidate1);
    if (candidate2VoteCount > n3) maj.push(candidate2);
    maj.sort((a, b) => a - b);

    return maj;

    // Complexity analysis
    // Time : O(N) + O(N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Majority Element II - https://www.geeksforgeeks.org/problems/majority-vote/1

  const s2 = new Solution2();
  console.log(s2.findMajority([2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]));
  console.log(s2.findMajority([1, 2, 3, 4, 5]));
  console.log(s2.findMajority([1, 1, 2, 3, 4, 5, 6, 1, 2, 1, 1]));
};

(() => {
  // Day 26 of July 2025

  p1();

  p2();
})();
