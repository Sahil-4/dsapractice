/**
 * @param {number[]} players
 * @param {number[]} trainers
 * @return {number}
 */
var matchPlayersAndTrainers = function (players, trainers) {
  const PN = players.length;
  const TN = trainers.length;

  let matchings = 0;

  const comparator = (e1, e2) => e2 - e1;
  const sortedPlayers = [...players];
  const sortedTrainers = [...trainers];
  sortedPlayers.sort(comparator);
  sortedTrainers.sort(comparator);

  let p = 0;
  let t = 0;

  while (p < PN && t < TN) {
    if (sortedPlayers[p] <= sortedTrainers[t]) {
      matchings++;
      t++;
    }
    p++;
  }

  return matchings;

  // Complexity analysis
  // Time : O(N) + O(M) + O(N * Log(N)) + O(M * Log(M)) + O(N + M)
  // Space : O(N) + O(M)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2410. Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/?envType=daily-question&envId=2025-07-13

  console.log(matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8]));
  console.log(matchPlayersAndTrainers([1, 1, 1], [10]));
};

class Solution2 {
  nonLisMaxSum(arr) {
    // code here
    const N = arr.length;
    const tsum = arr.reduce((acc, e) => acc + e, 0);

    // [len, minsum] lis ending at index i
    const dp = arr.map((e) => [1, e]);

    for (let i = 1; i < N; i++) {
      for (let j = 0; j < i; j++) {
        if (arr[j] < arr[i]) {
          const nlen = dp[j][0] + 1;
          const nsum = dp[j][1] + arr[i];

          if (nlen > dp[i][0] || (nlen === dp[i][0] && nsum < dp[i][1])) {
            dp[i] = [nlen, nsum];
          }
        }
      }
    }

    const maxlen = Math.max(...dp.map((sub) => sub[0]));
    const minSum = Math.min(...dp.filter((sub) => sub[0] === maxlen).map((sub) => sub[1]));

    return tsum - minSum;

    // Complexity analysis
    // Time : O(N) + O(N) + O(N * N) + O(N) + O(2N)
    // Space : O(2N) memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Maximum sum of elements not part of LIS - https://www.geeksforgeeks.org/problems/maximum-sum-of-elements-not-part-of-lis/1

  const s2 = new Solution2();
  console.log(s2.nonLisMaxSum([4, 6, 1, 2, 3, 8]));
  console.log(s2.nonLisMaxSum([5, 4, 3, 2, 1]));
  console.log(s2.nonLisMaxSum([1, 2, 3, 4, 5]));
  console.log(s2.nonLisMaxSum([4, 6, 1, 2, 3, 8, 4, 6, 1, 2, 3, 8, 4, 6, 1, 2, 3, 8]));
};

(() => {
  // Day 13 of July 2025

  p1();

  p2();
})();
