/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[][]}
 */
var divideArray = function (nums, k) {
  // [1,3,4,8,7,9,3,5,1]
  // [1 1 3 3 4 5 7 8 9]
  // pick neighbours in threes (by checking difference between first and last)

  // [2,4,2,2,5,2]
  // [2 2 2 2 4 5]

  // [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11]
  // [2 2 2 4 5 5 5 5 7 7 8 8 9 9 10 11 12 12]
  // [[2 2 2], [4 5 5], [5 5 7], [7 8 8], [9 9 10], [11 12 12]]

  // Idea : 
  // We have to take elements in threes 
  // and these three elements should have difference less then or equal to k 
  // to make sure that two elements gets minimum difference we have to pick the closest element 
  // here we dont have to check for all three elements 
  // if first element (smallest) and third element (largest) in threes 
  // gives difference less then equal to k 
  // then we can say that all pairs will give difference <= k 
  // now to this (pick closest element) 
  // we have to first sort the array 
  // after sorting we can easily pick elements in threes 
  // we have to make trio for all elements, 
  // hence in case at any point if we are failing we can simply return empty array 

  const cnums = [...nums].sort((a, b) => a - b);
  const answer = [];

  for (let i = 0; i < cnums.length; i += 3) {
    let a = cnums[i];
    let b = cnums[i + 1];
    let c = cnums[i + 2];

    if (c - a > k) return [];

    answer.push([a, b, c]);
  }

  return answer;

  // Complexity analysis 
  // Time : O(N * Log(N)) + O(N) 
  // Space : O(N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2966. Divide Array Into Arrays With Max Difference - https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/?envType=daily-question&envId=2025-06-18 

  console.log(divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2));
  console.log(divideArray([2, 4, 2, 2, 5, 2], 2));
  console.log(divideArray([4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], 14));
};

/**
 * @param {string} S
 * @return {string[][]}
 */
class Problem2 {
  palinParts(s) {
    // code here

    // Approach 
    // we have to return all possible palindrome partitions of the string
    // for this, we use recursion + backtracking (to try out all possible ways to partition the string)
    // at every index i, we explore all substrings s[i..j]
    // and for each substring:
    // we check if it's a palindrome
    // if no, skip and move to next substring
    // if yes, we include it in the current partitions list/array (palinds) and recursively solve for the remaining part (j+1 to end)
    // after the recursive call, we backtrack (remove the last added substring) to try other combinations
    // once we reach the end of the string (i >= n), we add the current partition to the result (output)

    const output = [];
    const palinds = [];

    this.solve(output, palinds, s, 0, s.length);

    return output;

    // Complexity analysis 
    // Time : O(N ^ N) at each level we have (N - i - 1) substrings to check 
    // Space : O(N) stack + O(N) current partition palindromes 
  }

  solve(output, palinds, s, i, n) {
    if (i >= n) {
      output.push([...palinds]);
      return;
    }

    for (let j = i; j < n; j++) {
      const check = this.isPalindrome(s, i, j);

      if (check) {
        const sub = s.substring(i, j + 1);
        palinds.push(sub);
        this.solve(output, palinds, s, j + 1, n);
        palinds.pop();
      }
    }
  }

  isPalindrome(s, l, r) {
    while (l < r) {
      if (s[l] !== s[r]) return false;
      l++;
      r--;
    }

    return true;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Find all possible palindromic partitions of a String - https://www.geeksforgeeks.org/problems/find-all-possible-palindromic-partitions-of-a-string/1 

  const s = new Problem2();
  console.log(s.palinParts("abc"));
  console.log(s.palinParts("geeks"));
  console.log(s.palinParts("abcba"));
};


(() => {
  // Day 18 of June 2025

  p1();

  p2();
})();
