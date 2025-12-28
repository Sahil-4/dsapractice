/**
 * @param {string} s
 * @return {number}
 */
var maxDifference = function (s) {
  // char to index, [a -> 0, b -> 1, ..., z -> 25] 
  const char2Code = (char) => char.charCodeAt(0) - 'a'.charCodeAt(0);

  // character frequency 
  const freq = new Array(26).fill(0);
  for (let i = 0; i < s.length; i++) {
    freq[char2Code(s[i])]++;
  }

  let maxOddFreq = 0;
  let minEvenFreq = 1001;
  for (let i = 0; i < 26; i++) {
    if (freq[i] === 0) continue;

    if (freq[i] & 1) {
      maxOddFreq = Math.max(maxOddFreq, freq[i]);
    } else {
      minEvenFreq = Math.min(minEvenFreq, freq[i]);
    }
  }

  return (maxOddFreq - minEvenFreq);

  // Complexity analysis 
  // Time : O(N) + O(26) 
  // Space : O(26) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3442. Maximum Difference Between Even and Odd Frequency I - https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/?envType=daily-question&envId=2025-06-10 

  console.log(maxDifference("aaaaabbc"));
  console.log(maxDifference("abcabcab"));
};

/**
 * @param {string} S
 * @returns {number}
 */
class Problem2 {
  countStrings(s) {
    // code here

    // building intuition 

    // geek
    // egek
    // eegk
    // keeg
    // gkee
    // geke

    // abc
    // bac
    // cba

    // abbc
    // babc
    // bbac
    // cbba
    // acbb
    // abcb

    // with how many other indices we can swap ith index char 
    // this will be the number of new substrings 
    // that we can obtain by swapping ith char with other chars (jth, j > i) 

    // char to index, [a -> 0, b -> 1, ..., z -> 25] 
    const char2Code = (char) => char.charCodeAt(0) - 'a'.charCodeAt(0);

    // character frequency 
    const freq = new Array(26).fill(0);
    let tfreq = 0;
    let flag = true;

    let count = 0;

    for (let i = s.length - 1; i >= 0; i--) {
      tfreq++;
      freq[char2Code(s[i])]++;

      count += (tfreq - freq[char2Code(s[i])]);

      if (flag && freq[char2Code(s[i])] > 1) {
        count++;
        flag = false;
      }
    }

    return count;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(26) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Exactly one swap - https://www.geeksforgeeks.org/problems/exactly-one-swap--170637/1 

  const solve = new Problem2();

  console.log(solve.countStrings("geek"));
  console.log(solve.countStrings("aaaa"));
  console.log(solve.countStrings("abc"));
  console.log(solve.countStrings("abbc"));
  console.log(solve.countStrings("subclasssuperclasshigherorderfunctionclassobject"));
};


(() => {
  // Day 10 of June 2025

  p1();

  p2();
})();
