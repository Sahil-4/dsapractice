/**
 * @param {number} n
 * @return {number}
 */
function coloredCells(n) {
  let output = 1;

  for (let i = 2, x = 4; i <= n; i++, x += 4) {
    output += x;
  }

  return output;

  // Complexity analysis
  // Time : O(N)
  // Space : O(1)
}

const p1 = () => {
  // Problem 1 : POTD Leetcode 2579. Count Total Number of Colored Cells - https://leetcode.com/problems/count-total-number-of-colored-cells/description/?envType=daily-question&envId=2025-03-05

  console.log(coloredCells(1));
  console.log(coloredCells(2));
  console.log(coloredCells(3));
  console.log(coloredCells(5));
  console.log(coloredCells(15));
  console.log(coloredCells(131));
  console.log(coloredCells(10000));
  console.log(coloredCells(100000));
};

function longestStringChain(wordsArr) {
  // !TLE
  // code here
  wordsArr.sort((w1, w2) => w1.length - w2.length);

  const map = {}; // string -> chainLength
  let lsc = 0;
  for (let word of wordsArr) {
    let mlen = 0;

    for (let j = 0; j < word.length; j++) {
      const pred = word.substring(0, j) + word.substr(j + 1);
      if (map[pred]) {
        mlen = Math.max(mlen, map[pred]);
      }
    }

    map[word] = mlen + 1;
    lsc = Math.max(lsc, mlen + 1);
  }

  return lsc;

  // Complexity analysis
  // Time : O(N*Log(N)) + O(N*M*M)
  // Space : O(N) copy dataset for sorting + O(N) map for storing string and chain length

  /**
   * Corresponding CPP Code 
    sort(wordsArr.begin(), wordsArr.end(), [](const string& word1, const string& word2) {
        return word1.length() < word2.length();
    });

    unordered_map<string, int> mp; // string -> chainLength 
    int lsc = 0;
    for (const string& word : wordsArr) {
        int mlen = 0;

        for (int j = 0; j < word.length(); j++) {
            string pred = word.substr(0, j) + word.substr(j+1);
            if (mp.find(pred) != mp.end()) {
                mlen = max(mlen, mp[pred]);
            }
        }

        mp[word] = mlen + 1;
        lsc = max(lsc, mlen + 1);
    }

    return lsc;

    // Complexity analysis 
    // Time : O(N*Log(N)) + O(N*M*M) 
    // Space : O(N) copy dataset for sorting + O(N) map for storing string and chain length 
   */
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Longest String Chain - https://www.geeksforgeeks.org/problems/longest-string-chain/1

  console.log(longestStringChain(["ba", "b", "a", "bca", "bda", "bdca"]));
};

(() => {
  // Day 5 of March 2025

  p1();

  p2();
})();
