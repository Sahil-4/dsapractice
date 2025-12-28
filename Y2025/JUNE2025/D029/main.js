/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var numSubseq = function (nums, target) {
  const MODO = 1000000007;

  const N = nums.length;
  const cnums = [...nums]
  cnums.sort((a, b) => a - b);

  const pow2 = new Array(nums.length + 1).fill(1);
  for (let i = 1; i < pow2.length; i++) {
    pow2[i] = (pow2[i - 1] * 2) % MODO;
  }

  let count = 0;

  let l = 0;
  let r = N - 1;

  while (l <= r) {
    if (cnums[l] + cnums[r] <= target) {
      count = (count + pow2[r - l]) % MODO;
      l++;
    } else {
      r--;
    }
  }

  return count;

  // Complexity analysis 
  // Time : O(N) + O(N * Log(N)) + O(N) + O(N) 
  // Space : O(N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1498. Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/?envType=daily-question&envId=2025-06-29 

  console.log(numSubseq([3, 5, 6, 7], 9));
  console.log(numSubseq([3, 3, 6, 8], 10));
  console.log(numSubseq([2, 3, 3, 4, 6, 7], 12));
  console.log(numSubseq([14, 4, 6, 6, 20, 8, 5, 6, 8, 12, 6, 10, 14, 9, 17, 16, 9, 7, 14, 11, 14, 15, 13, 11, 10, 18, 13, 17, 17, 14, 17, 7, 9, 5, 10, 13, 8, 5, 18, 20, 7, 5, 5, 15, 19, 14], 22));
};

/**
 * @param {number[]} arr
 * @param {number} k
 * @returns {number}
 */
class Problem2 {
  splitArray(arr, k) {
    // code here
    // in case of k = 1, we will have output as sum(arr)
    // in case of k == N, we will have output as max(arr)
    // by this we have got our search space [max(arr), sum(arr)]
    // now we will apply binary search on answer
    // if we are able to make sets of elements with sum limit, and they are <= k
    // then we will try with something less then limit
    // else we will try something more then limit
    // or in simple terms we will update limit

    const N = arr.length;

    const isSplitPossible = (limit) => {
      let kk = 1;

      for (let i = 0, sum = 0; i < N; i++) {
        if (sum + arr[i] > limit) {
          sum = 0;
          kk++;
        }

        sum += arr[i];
      }

      return kk <= k;
    };

    let low = Math.max(...arr);
    let high = arr.reduce((acc, e) => (acc + e), 0);
    let output = high;

    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      if (isSplitPossible(mid)) {
        high = mid - 1;
        output = mid;
      } else {
        low = mid + 1;
      }
    }

    return output;

    // Complexity analysis 
    // Time : O(N * Log(sum(arr))) 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Split Array Largest Sum - https://www.geeksforgeeks.org/problems/split-array-largest-sum--141634/1 

  const s = new Problem2();
  console.log(s.splitArray([1, 2, 3, 4], 3));
  console.log(s.splitArray([1, 1, 2], 2));
};


(() => {
  // Day 29 of June 2025

  p1();

  p2();
})();
