/**
 * @param {number[]} status
 * @param {number[]} candies
 * @param {number[][]} keys
 * @param {number[][]} containedBoxes
 * @param {number[]} initialBoxes
 * @return {number}
 */
var maxCandies = function (status, candies, keys, containedBoxes, initialBoxes) {
  const N = status.length;

  const visited = new Array(N).fill(false);
  const foundBoxes = new Set();

  const collectCandies = (u) => {
    if (visited[u]) {
      return 0;
    }
    if (!status[u]) {
      foundBoxes.add(u);
      return 0;
    }

    let candiesCount = 0;

    visited[u] = true;
    candiesCount += candies[u];

    for (const v of containedBoxes[u]) {
      candiesCount += collectCandies(v);
    }

    for (const keyBox of keys[u]) {
      status[keyBox] = 1;
      if (foundBoxes.has(keyBox)) {
        candiesCount += collectCandies(keyBox);
      }
    }

    return candiesCount;
  };

  let candiesCount = 0;

  for (let box of initialBoxes) {
    candiesCount += collectCandies(box);
  }

  return candiesCount;

  // Complexity analysis 
  // Time : O(2N) 
  // Space : O(2N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1298. Maximum Candies You Can Get from Boxes  - https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/description/?envType=daily-question&envId=2025-06-03 

  console.log(maxCandies([1, 0, 1, 0], [7, 5, 4, 100], [[], [], [1], []], [[1, 2], [3], [], []], [0]));
  console.log(maxCandies([1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [[1, 2, 3, 4, 5], [], [], [], [], []], [[1, 2, 3, 4, 5], [], [], [], [], []], [0]));
};

// User function Template for javascript

/**
 * @param {string} str
 * @param {number} k
 * @return {number}
 */

class Problem2 {
  countSubstr(s, K) {
    // code here
    const countSubstrDistinctLTEK = (k) => {
      const charCode = c => c.charCodeAt(0) - 'a'.charCodeAt(0);

      const frequency = new Array(26).fill(0);
      let distinctCount = 0;

      let subsc = 0;

      for (let l = 0, r = 0; r < s.length; r++) {
        frequency[charCode(s[r])]++;
        if (frequency[charCode(s[r])] === 1) distinctCount++;

        while (distinctCount > k) {
          frequency[charCode(s[l])]--;
          if (frequency[charCode(s[l])] === 0) distinctCount--;
          l++;
        }

        subsc += (r - l + 1);
      }

      return subsc;
    };

    let a = countSubstrDistinctLTEK(K);
    let b = countSubstrDistinctLTEK(K - 1);

    return a - b;

    // Complexity analysis 
    // Time : O(4N) 
    // Space : O(26) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Substrings with K Distinct  - https://www.geeksforgeeks.org/problems/count-number-of-substrings4528/1 

  console.log(new Problem2().countSubstr("abc", 2));
  console.log(new Problem2().countSubstr("aba", 2));
  console.log(new Problem2().countSubstr("aaa", 1));
};


(() => {
  // Day 3 of June 2025

  p1();

  p2();
})();
