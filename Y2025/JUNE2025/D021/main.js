/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var minimumDeletions = function (word, k) {
  const upperBound = (arr, bound) => {
    let low = 0;
    let high = arr.length - 1;
    let out = 0;

    while (low <= high) {
      const mid = Math.floor((low + high) / 2);

      if (arr[mid] <= bound) {
        out = mid + 1;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return out;
  };

  const characterFrequency = new Array(26).fill(0);
  for (let i = 0; i < word.length; i++) {
    characterFrequency[word.charCodeAt(i) - 97]++;
  }

  let deletions = Number.MAX_SAFE_INTEGER;

  characterFrequency.sort((a, b) => a - b);

  const psum = new Array(27).fill(0);
  for (let i = 0; i < 26; i++) {
    psum[i + 1] = psum[i] + characterFrequency[i];
  }

  for (let i = 0; i < 26; i++) {
    const lrm = psum[i];
    const uindex = upperBound(characterFrequency, characterFrequency[i] + k);
    const rrm = psum[26] - psum[uindex] - (26 - uindex) * (characterFrequency[i] + k);

    const trm = lrm + rrm;
    deletions = Math.min(deletions, trm);
  }

  return deletions;

  // Complexity analysis 
  // Time : O(N) + O(26 * Log(26)) + O(26) + O(26 * Log(26)) 
  // Space : O(26 * 2) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3085. Minimum Deletions to Make String K-Special - https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/description/?envType=daily-question&envId=2025-06-21 

  console.log(minimumDeletions("aabcaba", 0));
  console.log(minimumDeletions("dabdcbdcdcd", 2));
  console.log(minimumDeletions("aaabaaa", 2));
};

class Problem2 {
  catchThieves(arr, k) {
    // code here
    // arr[] = ['T', 'T', 'T', 'P', 'P'], k = 2
    // p1 -> 0
    // p2 -> 3
    // at this point police cannot catch thief 
    // which pointer to move ? smaller one.
    // p1 -> 1
    // p2 -> 3
    // at this point one thief catches one police 
    // which pointer to move ? both 

    const N = arr.length;
    let p = 0, t = 0;
    let count = 0;

    while (p < N && t < N) {
      while (p < N && arr[p] !== 'P') p++;
      while (t < N && arr[t] !== 'T') t++;

      if (p < N && t < N && Math.abs(p - t) <= k) {
        p++;
        t++;
        count++;
      } else if (p < t) {
        p++;
      } else {
        t++;
      }
    }

    return count;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Police and Thieves - https://www.geeksforgeeks.org/problems/police-and-thieves--141631/1 

  const s = new Problem2();
  console.log(s.catchThieves(['P', 'T', 'T', 'P', 'T'], 1));
  console.log(s.catchThieves(['T', 'T', 'P', 'P', 'T', 'P'], 2));
  console.log(s.catchThieves(['T', 'T', 'T', 'P', 'P'], 2));
};


(() => {
  // Day 21 of June 2025

  p1();

  p2();
})();
