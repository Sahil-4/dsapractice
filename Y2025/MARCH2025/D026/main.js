/**
 * @param {number[][]} grid
 * @param {number} x
 * @return {number}
 */
var minOperations = function (grid, x) {
  // flatten given grid
  const values = grid.flat();

  // sort the values
  values.sort((a, b) => a - b);

  // check if all elements can meet at a same point or not
  const isUniValuePossible = () => {
    const MOD = values[0] % x;
    for (let i = 0; i < values.length; i++) {
      if (values[i] % x != MOD) return false;
    }
    return true;
  };

  if (!isUniValuePossible()) return -1;

  // get middle value - to make it meeting point
  const mpIndex = Math.floor(values.length / 2);
  const mp = values[mpIndex]; // all elements will meet here

  // number of operations to reach to meeting point
  return values.reduce((acc, e) => acc + Math.abs(e - mp) / x, 0);

  // Complexity analysis
  // Time : O(MN) + O((MN) * LOG(MN)) + O(MN) + O(MN)
  // Space : O(MN)
  // MN = M*N
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2033. Minimum Operations to Make a Uni-Value Grid - https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/?envType=daily-question&envId=2025-03-26

  console.log(minOperations([[2,4],[6,8]], 2));
  console.log(minOperations([[1,5],[2,3]], 1));
  console.log(minOperations([[1,2],[3,4]], 2));
  console.log(minOperations([[10,20,5],[70,30,40],[15,5,1030]], 5));
};

class Problem2 {
  wordBreak(s, dictionary) {
    // code here

    // return this.recursion(s, new Set(dictionary), 0);

    // const n = s.length;
    // const memo = new Array(n).fill(null);
    // return this.memoize(s, new Set(dictionary), 0, memo);

    return this.tabulation(s, dictionary);
  }

  recursion(s, dict, i) {
    if (i >= s.length) return true;

    let result = false;

    for (let ni = i; ni < s.length && !result; ni++) {
      // i->ni, in dict
      if (dict.has(s.substring(i, ni + 1))) {
        result = this.recursion(s, dict, ni + 1);
      }
    }

    return result;

    // Complexity analysis
    // Time : O(N^N * N) ~
    // Space : O(N) stack
  }

  memoize(s, dict, i, memo) {
    if (i >= s.length) return true;

    if (memo[i] != null) return memo[i];

    let result = false;

    for (let ni = i; ni < s.length && !result; ni++) {
      // i->ni, in dict
      if (dict.has(s.substring(i, ni + 1))) {
        result = this.memoize(s, dict, ni + 1, memo);
      }
    }

    return (memo[i] = result);

    // Complexity analysis
    // Time : O(N*N*N)
    // Space : O(N) stack + O(N) memory
  }

  tabulation(s, dictionary) {
    const n = s.length;
    const memo = new Array(n + 1).fill(false);

    // base
    memo[0] = true;

    for (let i = 1; i <= n; i++) {
      for (const w of dictionary) {
        const wlen = w.length;
        const start = i - wlen;
        if (start >= 0 && memo[start] && s.substring(start, start + w.length) == w) {
          memo[i] = true;
          break;
        }
      }
    }

    // return
    return memo[n];

    // Complexity analysis
    // Time : O(N*N*N)
    // Space : O(N) memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Word Break - https://www.geeksforgeeks.org/problems/word-break1352/1 

  console.log(new Problem2().wordBreak("ilikegfg", ["i", "like", "man", "india", "gfg",]));
  console.log(new Problem2().wordBreak("ilikemangoes", ["i", "like", "man", "india", "gfg",]));
};

(() => {
  // Day 26 of March 2025

  p1();

  p2();
})();
