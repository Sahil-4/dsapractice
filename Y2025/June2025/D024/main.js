/**
 * @param {number[]} nums
 * @param {number} key
 * @param {number} k
 * @return {number[]}
 */
var findKDistantIndices = function (nums, key, k) {
  // find occurrences of key in nums, store all indices 
  // from each index in occurrences 
  // we will have to take indices from i = (index - k) to i < index, 
  // and i = index to i <= (index + k) 
  // while doing same for next index of key 
  // just make sure to start the i from max((index - k), last_index + 1) to avoid taking duplicates 
  // last_index = -1, initially 
  // also to avoid goind out of bound take i <= min((index + k), N - 1) 

  const N = nums.length;
  const output = [];

  const occurrences = [];
  for (let i = 0; i < N; i++) {
    if (nums[i] === key) occurrences.push(i);
  }

  let li = -1;
  for (let index of occurrences) {
    // left 
    for (let i = Math.max(index - k, li + 1); i < index; i++) {
      output.push(i);
      li = i;
    }
    // right side 
    for (let i = li + 1; i <= Math.min((index + k), (N - 1)); i++) {
      output.push(i);
      li = i;
    }
  }

  return output;

  // Complexity analysis 
  // Time : O(2N) 
  // Space : O(N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2200. Find All K-Distant Indices in an Array - https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/description/?envType=daily-question&envId=2025-06-24 

  console.log(findKDistantIndices([3, 4, 9, 1, 3, 9, 5], 9, 1));
  console.log(findKDistantIndices([2, 2, 2, 2, 2], 2, 2));
};

class Problem2 {
  maxSubseq(s, k) {
    // code here

    // return this.brute(s, k);

    return this.better(s, k);
  }

  better(s, k) {
    const N = s.length;
    const stack = [];

    for (let i = 0; i < N; i++) {
      if (k === 0) {
        stack.push(s[i]);
      } else {
        while (k > 0 && stack.length !== 0 && s[i] > stack.at(-1)) {
          stack.pop();
          k--;
        }
        stack.push(s[i]);
      }
    }

    while (k > 0 && stack.length) {
      k--;
      stack.pop();
    }

    return stack.join("");

    // Complexity analysis 
    // Time : O(N + K) 
    // Space : O(N) 
  }

  brute(s, k) {
    const word = s.split("");

    while (k > 0) {
      for (let i = 0; i < word.length; i++) {
        if (i === word.length - 1 || word[i] < word[i + 1]) {
          word.splice(i, 1);
          break;
        }
      }

      k--;
    }

    return word.join("");

    // Complexity analysis 
    // Time : O(N * K) 
    // Space : O(N) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Lexicographically Largest String After K Deletions - https://www.geeksforgeeks.org/problems/lexicographically-largest-string-after-deleting-k-characters/1 

  const p = new Problem2();
  console.log(p.maxSubseq("ritz", 2));
  console.log(p.maxSubseq("zebra", 3));
  console.log(p.maxSubseq("xaaa", 2));
  console.log(p.maxSubseq("aaax", 2));
};


(() => {
  // Day 24 of June 2025

  p1();

  p2();
})();
