/**
 * @param {number[]} weights
 * @param {number} k
 * @return {number}
 */
var putMarbles = function (weights, k) {
  const N = weights.length;

  const pairSum = [];
  for (let i = 0; i < N - 1; i++) {
    pairSum.push(weights[i] + weights[i + 1]);
  }

  pairSum.sort((a, b) => a - b);

  let left = 0;
  let right = 0;

  for (let i = 0; i < k - 1; i++) {
    left += pairSum[i];
    right += pairSum[N - 1 - 1 - i];
  }

  return right - left;

  // Complexity analysis
  // Time : O(N) + O(N*LOG(N)) + O(K)
  // Space : O(N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2551. Put Marbles in Bags - https://leetcode.com/problems/put-marbles-in-bags/description/?envType=daily-question&envId=2025-03-31

  console.log(putMarbles([1, 3, 5, 1]));
  console.log(putMarbles([1, 3]));
};

// User function Template for javascript
/**
 * @param {string} s
 * @returns {number}
 */

class Problem2 {
  maxPartitions(s) {
    // code here
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

    return output.length;

    // Complexity analysis
    // Time : O(N) + O(N)
    // Space : O(N) memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Maximize partitions in a String - https://www.geeksforgeeks.org/problems/maximize-partitions-in-a-string/1

  console.log(new Problem2().maxPartitions("ababcbacadefegdehijhklij"));
  console.log(new Problem2().maxPartitions("eccbbbbdec"));
  console.log(new Problem2().maxPartitions("ababcbacadefegdehijhk"));
};

(() => {
  // Day 31 of March 2025

  p1();

  p2();
})();
