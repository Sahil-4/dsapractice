/**
 * @param {string[]} words
 * @param {character} x
 * @return {number[]}
 */
var findWordsContaining = function (words, x) {
  return words.reduce((acc, word, i) => {
    if (word.includes(x)) acc.push(i);
    return acc;
  }, []);

  // Complexity analysis 
  // Time : O(W * Len(Wi)) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2942. Find Words Containing Character - https://leetcode.com/problems/find-words-containing-character/description/?envType=daily-question&envId=2025-05-24 

  console.log(findWordsContaining(["leet", "code"], "e"));
  console.log(findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a"));
  console.log(findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "z"));
};

/**
 * @param {string} s
 * @returns {number}
 */

class Problem2 {
  sumSubstrings(s) {
    // return this.bruteforce(s);

    return this.optimal(s);
  }

  optimal(s) {
    // 6759 
    // ends at i = 0 -> 6 -> 6*1 = 6 
    // ends at i = 1 -> 7 67 -> 7*2 + 10*6 = 74 
    // ends at i = 2 -> 5 75 675 -> 5*3 + 10*(7*2 + 10*(6)) = 755 
    // ends at i = 3 -> 9 59 759 6759 -> 9*4 + 10*(5*3 + 10*(7*2 + 10*(6)) = 7586 
    // t = 8421
    // f = 10(ends at i - 1) + ith * (i+1)

    const N = s.length;
    const dp = new Array(N);
    dp[0] = s[0];

    for (let i = 1; i < N; i++) {
      dp[i] = (10 * dp[i - 1]) + (+s[i] * (i + 1));
    }

    return dp.reduce((acc, e) => (acc + +e), 0);

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) 
  }

  bruteforce(s) {
    // code here
    // 6759
    // i = 0 -> 6 67 675 6759 = 7507
    // i = 1 -> 7 75 759 = 841
    // i = 2 -> 5 59 = 64
    // i = 3 -> 9 = 9
    // t = 8421

    // 421
    // i = 0 -> 4 42 421 = 467
    // i = 1 -> 2 21 = 23
    // i = 2 -> 1 = 1
    // t = 491

    let sum = 0;

    for (let i = 0; i < s.length; i++) {
      let num = 0;
      for (let j = i; j < s.length; j++) {
        num = (num * 10) + +s[j];
        sum = sum + num;
      }
    }

    return sum;

    // Complexity analysis 
    // Time : O(N*N) 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Sum of all substrings of a number - https://www.geeksforgeeks.org/problems/sum-of-all-substrings-of-a-number-1587115621/1 

  console.log(new Problem2().sumSubstrings("1234"));
  console.log(new Problem2().sumSubstrings("123456789"));
  console.log(new Problem2().sumSubstrings("999999999"));
};


(() => {
  // Day 24 of May 2025

  p1();

  p2();
})();
