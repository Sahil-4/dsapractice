/**
 * @param {string[]} words
 * @return {number}
 */
var longestPalindrome = function (words) {
  let palinLen = 0;
  let wordsMap = new Map();

  for (let word of words) {
    // look for pair of word 
    let pair = word[1] + word[0];

    if (wordsMap.get(pair) > 0) {
      palinLen += 4;
      wordsMap.set(pair, wordsMap.get(pair) - 1);
    } else {
      wordsMap.set(word, (wordsMap.get(word) || 0) + 1);
    }
  }

  // look for words with both same letters 
  for (let [word, freq] of wordsMap) {
    if (word[0] == word[1] && freq > 0) {
      palinLen += 2;
      break;
    }
  }

  return palinLen;

  // Complexity analysis 
  // Time : O(2N) 
  // Space : O(N) 
  // Expected map look up takes constant time 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2131. Longest Palindrome by Concatenating Two Letter Words - https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/?envType=daily-question&envId=2025-05-25 

  console.log(longestPalindrome(["lc", "cl", "gg"]));
  console.log(longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]));
  console.log(longestPalindrome(["cc", "ll", "xx"]));
  console.log(longestPalindrome(["ll", "lb", "bb", "bx", "xx", "lx", "xx", "lx", "ll", "xb", "bx", "lb", "bb", "lb", "bl", "bb", "bx", "xl", "lb", "xx"]));
  console.log(longestPalindrome(["mm", "mm", "yb", "by", "bb", "bm", "ym", "mb", "yb", "by", "mb", "mb", "bb", "yb", "by", "bb", "yb", "my", "mb", "ym"]));
};

/**
 * @param {number[]} arr
 * @return {boolean}
 */

class Problem2 {
  pythagoreanTriplet(arr) {
    // code here
    const N = arr.length;

    if (N < 3) return false;

    // elements frequency 
    let t = Math.max(...arr);
    let count = new Array(t + 1).fill(0);
    for (let i = 0; i < N; i++) {
      count[arr[i]]++;
    }

    for (let a = 1; a <= t; a++) {
      for (let b = a + 1; b <= t; b++) {
        if (count[a] > 0 && count[b] > 0) {
          let as = a * a; // a square 
          let bs = b * b; // b square 

          let cs = as + bs; // c square 
          let c = Math.sqrt(cs); // c 

          if (((c * c) === cs) && c <= t && count[c] > 0) {
            return true;
          }
        }
      }
    }

    return false;

    // Complexity analysis 
    // Time : O(N) + O(N) + O(t*t * sqrt(cs)) 
    // Space : O(t) 
    // t = Max(...arr) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Pythagorean Triplet - https://www.geeksforgeeks.org/problems/pythagorean-triplet3018/1 

  console.log(new Problem2().pythagoreanTriplet([3, 2, 4, 6, 5]));
  console.log(new Problem2().pythagoreanTriplet([3, 8, 5]));
  console.log(new Problem2().pythagoreanTriplet([1, 1, 1]));
};


(() => {
  // Day 25 of May 2025

  p1();

  p2();
})();
