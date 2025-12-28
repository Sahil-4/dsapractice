/**
 * @param {string} s
 * @param {number} k
 * @param {character} fill
 * @return {string[]}
 */
var divideString = function (s, k, fill) {
  const slen = s.length;
  const output = [];

  for (let i = 0; i < Math.ceil(slen / k); i++) {
    const start = i * k;
    const end = start + k;
    const substring = s.substring(start, end).split("");
    while (substring.length < k) substring.push(fill);
    output.push(substring.join(""));
  }

  return output;

  // Complexity analysis 
  // Time : O(N + k) + immutable strings 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2138. Divide a String Into Groups of Size k - https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/?envType=daily-question&envId=2025-06-22 

  console.log(divideString("abcdefghi", 3, "x"));
  console.log(divideString("abcdefghij", 3, "x"));
  console.log(divideString("ctoyjrwtngqwt", 8, "n"));
};

class Problem2 {
  largestSubset(arr) {
    // code here
    // sort the array in DESC order 
    // go from 0 to N 
    // if we pick any element at ith index and any other element at jth index 
    // and they satisfy the arr[i]/arr[j] 
    // then if we take any element at any index k > j that satisfy arr[j]/arr[k] 
    // then it will also satisfy arr[i]/arr[k] (mathematically) 
    // hence we wont have to check all elements for validation 
    // to return the largest subset we already have sorted the array 
    // we will use dp + greedy approach and track the maximum length subset 

    const N = arr.length;
    const carr = [...arr].sort((a, b) => b - a);
    const dp = new Array(N).fill(1); // we can at least make subset of 1 length 
    const path = new Array(N); // path to build largest subset 

    // compute length of longest subset - satisfy the given conditions 
    // and build path of longest length subset 
    for (let i = 0; i < N; i++) {
      path[i] = i;
      for (let p = 0; p < i; p++) {
        if ((carr[p] % carr[i] === 0) && dp[i] < dp[p] + 1) {
          dp[i] = dp[p] + 1;
          path[i] = p;
        }
      }
    }

    // find longest length starting point - to start building the answer 
    let si = 0; // subset start index 
    for (let i = 0; i < N; i++) {
      if (dp[si] < dp[i]) si = i;
    }

    // build subset - backtrack on path 
    const output = [carr[si]];
    while (path[si] != si) {
      si = path[si];
      output.push(carr[si]);
    }

    return output;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Largest Divisible Subset - https://www.geeksforgeeks.org/problems/largest-divisible-subset--170643/1 

  const p = new Problem2();
  console.log(p.largestSubset([1, 16, 7, 8, 4]));
  console.log(p.largestSubset([2, 4, 3, 8]));
  console.log(p.largestSubset([1, 2, 3, 4, 5, 9, 7, 12, 14, 8]));
};


(() => {
  // Day 22 of June 2025

  p1();

  p2();
})();
