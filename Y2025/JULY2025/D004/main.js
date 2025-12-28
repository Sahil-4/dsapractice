const nextCharacter = (e, inc) => {
  if (e === "z") return inc === 0 ? "z" : "a";
  const ni = e.charCodeAt(0) + inc;
  return String.fromCharCode(ni);
};

/**
 * @param {number} k
 * @param {number[]} operations
 * @return {character}
 */
var kthCharacter = function (k, operations) {
  if (k === 1) return "a";

  const N = operations.length;

  let len = 1;
  let newK = 0;
  let inc = 0;

  for (let i = 0; i < N; i++) {
    len *= 2;

    if (len >= k) {
      newK = k - len / 2;
      inc = operations[i];
      break;
    }
  }

  const nextCh = kthCharacter(newK, operations);

  return nextCharacter(nextCh, inc);

  // Complexity analysis
  // Time : O(Log(K))
  // Space : O(Log(K))
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3307. Find the K-th Character in String Game II - https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/description/?envType=daily-question&envId=2025-07-04

  console.log(kthCharacter(5, [0, 0, 0]));
  console.log(kthCharacter(10, [0, 1, 0, 1]));
};

class Solution2 {
  countAtMostK(arr, k) {
    // code here
    // arr[] = [1, 2, 2, 3], k = 2
    // count = 1 + 2 + 3 + 3

    // arr[] = [1, 1, 1], k = 1
    // count = 1 + 2 + 3

    // arr[] = [1, 2, 1, 1, 3, 3, 4, 2, 1], k = 2
    // count = 1 + 2 + 3 + 4 + 3 + 4 + 3 + 2 + 2

    let count = 0;
    let distinct = 0;
    const frequency = new Map();

    for (let l = 0, r = 0, N = arr.length; r < N; r++) {
      // expand
      const e = arr[r];
      frequency.set(e, (frequency.get(e) || 0) + 1);
      if (frequency.get(e) === 1) distinct++;

      // shrink
      while (distinct > k) {
        const e = arr[l];
        frequency.set(e, (frequency.get(e) || 0) - 1);
        if (frequency.get(e) === 0) distinct--;
        l++;
      }

      // increment sub-array count
      count += r - l + 1;
    }

    return count;

    // Complexity analysis
    // Time : O(N)
    // Space : O(N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Subarrays With At Most K Distinct Integers - https://www.geeksforgeeks.org/problems/subarrays-with-at-most-k-distinct-integers/1

  const s = new Solution2();
  console.log(s.countAtMostK([1, 2, 2, 3], 2));
  console.log(s.countAtMostK([1, 1, 1], 1));
  console.log(s.countAtMostK([1, 2, 1, 1, 3, 3, 4, 2, 1], 2));
};

(() => {
  // Day 4 of July 2025

  p1();

  p2();
})();
