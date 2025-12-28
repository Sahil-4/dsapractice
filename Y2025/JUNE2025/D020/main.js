/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxDistance = function (s, k) {
  const abs = Math.abs;
  const min = Math.min;
  const max = Math.max;

  const slen = s.length;
  const k2 = k * 2;

  let mmhd = 0;
  let NCount, SCount, ECount, WCount;
  NCount = SCount = ECount = WCount = 0;

  for (let i = 0; i < slen; i++) {
    if (s[i] === 'N') NCount++;
    else if (s[i] === 'S') SCount++;
    else if (s[i] === 'E') ECount++;
    else if (s[i] === 'W') WCount++;

    const mhd = abs(NCount - SCount) + abs(ECount - WCount);
    mmhd = max(mmhd, min(mhd + k2, i + 1));
  }

  return mmhd;

  // Complexity analysis 
  // Time : O(N) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3443. Maximum Manhattan Distance After K Changes - https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/description/?envType=daily-question&envId=2025-06-20 

  console.log(maxDistance("NWSE", 1));
  console.log(maxDistance("NSWWEW", 3));
};

/**
 * @param {number[]} arr
 * @param {number} k
 * @returns {number}
 */
class Problem2 {
  validgroup(arr, k) {
    // code here
    const N = arr.length;
    const T = 100001;

    if (N % k != 0) return false;
    if (k == 1) return true;

    const carr = [...arr].sort((a, b) => a - b);
    const frequency = new Array(T).fill(0);

    for (let i = 0; i < N; i++) {
      frequency[carr[i]]++;
    }

    for (let i = 0; i < N; i++) {
      // already used 
      if (frequency[carr[i]] === 0) continue;

      for (let gi = carr[i]; gi < carr[i] + k; gi++) {
        if (frequency[gi] === 0) return false;
        frequency[gi]--;
      }
    }

    return true;

    // Complexity analysis 
    // Time : O(N * Log(N)) + O(N) + O(N * k) 
    // Space : O(N) + O(T) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Group Balls by Sequence - https://www.geeksforgeeks.org/problems/group-balls-by-sequence/1 

  const s = new Problem2();
  console.log(s.validgroup([10, 1, 2, 11], 2));
  console.log(s.validgroup([10, 1, 2, 11, 12], 2));
  console.log(s.validgroup([1, 1, 2, 2], 2));
  console.log(s.validgroup([1, 1, 2, 2, 3, 3], 2));
  console.log(s.validgroup([1, 1, 2, 2, 3, 3], 1));
};


(() => {
  // Day 20 of June 2025

  p1();

  p2();
})();
