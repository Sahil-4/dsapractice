/**
 * @param {string} word
 * @param {number} numFriends
 * @return {string}
 */
var answerString = function (word, numFriends) {
  // we just need one sub-string (lexicographically largest) 
  // longest length of this sub-string can be k = word.length - numFriends + 1 
  // now we just have to find the sub-string with length k 
  // and this sub-string should be lexicographically largest among all 
  // we still have a lot of sub-strings - to reduce this number 
  // lexicographically largest sub-string will start from the lexicographically largest character 
  // hence find the lexicographically largest char and start creating sub-string from that char 

  if (numFriends === 1) return word;

  const N = word.length;
  const K = N - numFriends + 1;

  let lc = 'a'; // lexicographically largest character in word 
  for (let c of word) {
    if (c > lc) lc = c;
  }

  let answer = "";

  for (let i = 0; i < N; i++) {
    if (word[i] !== lc) continue;
    let sub = word.substring(i, Math.min(i + K, N));
    if (answer < sub) answer = sub;
  }

  return answer;

  // Complexity analysis 
  // Time : O(N) + O(N * K) 
  // Space : O(K) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3403. Find the Lexicographically Largest String From the Box I - https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/description/?envType=daily-question&envId=2025-06-04 

  console.log(answerString("gh", 1));
  console.log(answerString("zzxyzdefcba", 1));
  console.log(answerString("zzxyzdefcba", 3));
  console.log(answerString("zzxyzdefcba", 6));
  console.log(answerString("zzxyzdefcba", 10));
  console.log(answerString("aann", 2));
  console.log(answerString("gggg", 4));
};

/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {number}
 */

class Problem2 {
  lcsOf3(s1, s2, s3) {
    // Code here

    // return this.recursion(s1, 0, s2, 0, s3, 0);

    // let iN = s1.length;
    // let jN = s2.length;
    // let kN = s3.length;

    // const memo = Array.from({ length: iN }, () => Array.from({ length: jN }, () => new Array(kN).fill(-1)));
    // return this.memoize(s1, 0, s2, 0, s3, 0, memo);

    // return this.tabulation(s1, s2, s3);
    return this.optimised(s1, s2, s3);
  }

  recursion(s1, p1, s2, p2, s3, p3) {
    // pointer goes out of bound 
    if (p1 >= s1.length) return 0;
    if (p2 >= s2.length) return 0;
    if (p3 >= s3.length) return 0;

    // case - char matches 
    if (s1[p1] == s2[p2] && s2[p2] == s3[p3]) {
      return 1 + this.recursion(s1, p1 + 1, s2, p2 + 1, s3, p3 + 1);
    }

    // case - char not match, advance pointers - all three 
    let c1 = this.recursion(s1, p1 + 1, s2, p2 + 1, s3, p3 + 1);

    // case - char not match, advance pointers - only two 
    let c2a = this.recursion(s1, p1 + 1, s2, p2 + 1, s3, p3);
    let c2b = this.recursion(s1, p1 + 1, s2, p2, s3, p3 + 1);
    let c2c = this.recursion(s1, p1, s2, p2 + 1, s3, p3 + 1);

    // case - char not match, advance pointers - only one 
    let c3a = this.recursion(s1, p1 + 1, s2, p2, s3, p3);
    let c3b = this.recursion(s1, p1, s2, p2 + 1, s3, p3);
    let c3c = this.recursion(s1, p1, s2, p2, s3, p3 + 1);

    // return the biggest path len 
    return Math.max(c1, c2a, c2b, c2c, c3a, c3b, c3c);

    // Complexity analysis 
    // Time : O(7 ^ (iN + jN + kN)) 
    // Space : O(iN + jN + kN) stack 
  }

  memoize(s1, p1, s2, p2, s3, p3, memo) {
    // pointer goes out of bound 
    if (p1 >= s1.length) return 0;
    if (p2 >= s2.length) return 0;
    if (p3 >= s3.length) return 0;

    if (memo[p1][p2][p3] !== -1) return memo[p1][p2][p3];

    // case - char matches 
    if (s1[p1] == s2[p2] && s2[p2] == s3[p3]) {
      return memo[p1][p2][p3] = 1 + this.recursion(s1, p1 + 1, s2, p2 + 1, s3, p3 + 1);
    }

    // case - char not match, advance pointers - all three 
    let c1 = this.recursion(s1, p1 + 1, s2, p2 + 1, s3, p3 + 1);

    // case - char not match, advance pointers - only two 
    let c2a = this.recursion(s1, p1 + 1, s2, p2 + 1, s3, p3);
    let c2b = this.recursion(s1, p1 + 1, s2, p2, s3, p3 + 1);
    let c2c = this.recursion(s1, p1, s2, p2 + 1, s3, p3 + 1);

    // case - char not match, advance pointers - only one 
    let c3a = this.recursion(s1, p1 + 1, s2, p2, s3, p3);
    let c3b = this.recursion(s1, p1, s2, p2 + 1, s3, p3);
    let c3c = this.recursion(s1, p1, s2, p2, s3, p3 + 1);

    // return the biggest path len 
    return memo[p1][p2][p3] = Math.max(c1, c2a, c2b, c2c, c3a, c3b, c3c);

    // Complexity analysis 
    // Time : O(7 * (iN * jN * kN)) 
    // Space : O(iN * jN * kN) memory + O(iN + jN + kN) stack 
  }

  tabulation(s1, s2, s3) {
    let iN = s1.length;
    let jN = s2.length;
    let kN = s3.length;

    const memo = Array.from({ length: iN + 1 }, () => Array.from({ length: jN + 1 }, () => new Array(kN + 1).fill(0)));

    for (let p1 = iN - 1; p1 >= 0; p1--) {
      for (let p2 = jN - 1; p2 >= 0; p2--) {
        for (let p3 = kN - 1; p3 >= 0; p3--) {
          // case - char matches 
          if (s1[p1] == s2[p2] && s2[p2] == s3[p3]) {
            memo[p1][p2][p3] = 1 + memo[p1 + 1][p2 + 1][p3 + 1];
            continue;
          }

          // case - char not match, advance pointers - all three 
          let c1 = memo[p1 + 1][p2 + 1][p3 + 1];

          // case - char not match, advance pointers - only two 
          let c2a = memo[p1 + 1][p2 + 1][p3];
          let c2b = memo[p1 + 1][p2][p3 + 1];
          let c2c = memo[p1][p2 + 1][p3 + 1];

          // case - char not match, advance pointers - only one 
          let c3a = memo[p1 + 1][p2][p3];
          let c3b = memo[p1][p2 + 1][p3];
          let c3c = memo[p1][p2][p3 + 1];

          memo[p1][p2][p3] = Math.max(c1, c2a, c2b, c2c, c3a, c3b, c3c);
        }
      }
    }

    return memo[0][0][0];

    // Complexity analysis 
    // Time : O(iN * jN * kN) 
    // Space : O(iN * jN * kN) memory 
  }

  optimised(s1, s2, s3) {
    let iN = s1.length;
    let jN = s2.length;
    let kN = s3.length;

    let next = Array.from({ length: jN + 1 }, () => new Array(kN + 1).fill(0));

    for (let p1 = iN - 1; p1 >= 0; p1--) {
      let curr = Array.from({ length: jN + 1 }, () => new Array(kN + 1).fill(0));

      for (let p2 = jN - 1; p2 >= 0; p2--) {
        for (let p3 = kN - 1; p3 >= 0; p3--) {
          // case - char matches 
          if (s1[p1] == s2[p2] && s2[p2] == s3[p3]) {
            curr[p2][p3] = 1 + next[p2 + 1][p3 + 1];
            continue;
          }

          // case - char not match, advance pointers - all three 
          let c1 = next[p2 + 1][p3 + 1];

          // case - char not match, advance pointers - only two 
          let c2a = next[p2 + 1][p3];
          let c2b = next[p2][p3 + 1];
          let c2c = curr[p2 + 1][p3 + 1];

          // case - char not match, advance pointers - only one 
          let c3a = next[p2][p3];
          let c3b = curr[p2 + 1][p3];
          let c3c = curr[p2][p3 + 1];

          curr[p2][p3] = Math.max(c1, c2a, c2b, c2c, c3a, c3b, c3c);
        }
      }

      next = curr;
    }

    return next[0][0];

    // Complexity analysis 
    // Time : O(iN * jN * kN) 
    // Space : O(2 * jN * kN) memory 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks LCS of three strings - https://www.geeksforgeeks.org/problems/lcs-of-three-strings0028/1 

  console.log(new Problem2().lcsOf3("geeks", "geeksfor", "geeksforgeeks"));
  console.log(new Problem2().lcsOf3("abcd1e2", "bc12ea", "bd1ea",));
};


(() => {
  // Day 4 of June 2025

  p1();

  p2();
})();
