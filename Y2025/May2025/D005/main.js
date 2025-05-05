/**
 * @param {number} n
 * @return {number}
 */
var numTilings = function (N) {
  const MODO = 1000000007;
  const memo = new Array(N + 1).fill(-1);

  memo[1] = 1;
  memo[2] = 2;
  memo[3] = 5;

  const recursion = (n) => {
    if (memo[n] == -1) {
      memo[n] = ((2 * recursion(n - 1) % MODO) + recursion(n - 3) % MODO) % MODO;
    }
    return memo[n];

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) + O(N) 
  };

  const tabulation = () => {
    for (let n = 4; n <= N; n++) {
      memo[n] = ((2 * memo[n - 1] % MODO) + memo[n - 3] % MODO) % MODO;
    }

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) 
  };

  // recursion(N, memo);
  tabulation();

  return memo[N];
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 790. Domino and Tromino Tiling - https://leetcode.com/problems/domino-and-tromino-tiling/?envType=daily-question&envId=2025-05-05 

  console.log(numTilings(1));
  console.log(numTilings(3));
  console.log(numTilings(7));
  console.log(numTilings(100));
};

// User function Template for javascript
class Problem2 {
  findTarget(arr, target) {
    // code here
    const N = arr.length;

    let low = 0;
    let high = N - 1;

    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      if (arr[mid] == target) return mid;
      if (mid > 0 && arr[mid - 1] == target) return mid - 1;
      if (mid < N - 1 && arr[mid + 1] == target) return mid + 1;

      if (arr[mid] > target) {
        high = mid - 2;
      } else {
        low = mid + 2;
      }
    }

    return -1;

    // Complexity analysis 
    // Time : O(Log(n)) 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Search in an almost Sorted Array - https://www.geeksforgeeks.org/problems/search-in-an-almost-sorted-array/1 

  console.log(new Problem2().findTarget([10, 3, 40, 20, 50, 80, 70], 40));
  console.log(new Problem2().findTarget([10, 3, 40, 20, 50, 80, 70], 90));
  console.log(new Problem2().findTarget([-20], -20));
};

(() => {
  // Day 5 of May 2025

  p1();

  p2();
})();
