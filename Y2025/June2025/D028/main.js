/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSubsequence = function (nums, k) {
  // const copy = nums.map((e, i) => [e, i])
  // copy.sort((a, b) => b[0] - a[0])

  // const knums = copy.slice(0, k)
  // knums.sort((a, b) => a[1] - b[1])

  // const output = knums.map((ei) => ei[0]);

  // return output;

  return nums.map((e, i) => [e, i]).sort((a, b) => b[0] - a[0]).slice(0, k).sort((a, b) => a[1] - b[1]).map((ei) => ei[0]);

  // Complexity analysis 
  // Time : O(N) + O(N * Log(N)) + O(K) + O(K * Log(K)) + O(K) 
  // Space : O(N) + O(K) + O(K) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2099. Find Subsequence of Length K With the Largest Sum - https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/?envType=daily-question&envId=2025-06-28 

  console.log(maxSubsequence([2, 1, 3, 3], 2));
  console.log(maxSubsequence([-1, -2, 3, 4], 3));
  console.log(maxSubsequence([3, 4, 3, 3], 2));
};

/**
 * @param {Number[]} a
 * @param {Number[]} b
 * @returns {number[]}
 */
class Problem2 {
  countLessEq(a, b) {
    // code here

    // return this.brute(a, b);

    // return this.better(a, b);

    return this.optimal(a, b);
  }

  brute(a, b) {
    const alen = a.length;
    const blen = b.length;

    const output = new Array(alen).fill(0);

    for (let i = 0; i < alen; i++) {
      for (let j = 0; j < blen; j++) {
        if (b[j] <= a[i]) output[i]++;
      }
    }

    return output;

    // Complexity analysis 
    // Time : O(N * M) 
    // Space : O(1) 
  }

  better(a, b) {
    const alen = a.length;
    const blen = b.length;

    const copyB = [...b].sort((x, y) => x - y);

    const output = new Array(alen).fill(0);

    for (let i = 0; i < alen; i++) {
      output[i] = this.upperBound(copyB, a[i]);
    }

    return output;

    // Complexity analysis 
    // Time : O(M * Log(M)) + O(N * Log(M)) 
    // Space : O(M) 
  }

  upperBound(arr, key) {
    let low = 0;
    let high = arr.length - 1;
    let ans = arr.length;

    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      if (arr[mid] > key) {
        ans = mid;
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    return ans;
  }

  optimal(a, b) {
    const alen = a.length;
    const blen = b.length;

    const copyA = a.map((e, i) => [e, i]).sort((x, y) => x[0] - y[0]);
    const copyB = [...b].sort((x, y) => x - y);

    const output = new Array(alen).fill(0);

    for (let i = 0, j = 0; i < alen; i++) {
      while (j < blen && copyB[j] <= copyA[i][0]) j++;
      output[copyA[i][1]] = j;
    }

    return output;

    // Complexity analysis 
    // Time : O(N * Log(N)) + O(M * Log(M)) + O(N + M) 
    // Space : O(N + M) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Counting elements in two arrays - https://www.geeksforgeeks.org/problems/counting-elements-in-two-arrays/1 

  const s = new Problem2();
  console.log(s.countLessEq([4, 8, 7, 5, 1], [4, 48, 3, 0, 1, 1, 5]));
  console.log(s.countLessEq([10, 20], [30, 40, 50]));
  console.log(s.countLessEq([4, 8, 7, 5, 1], [0, 0]));
};


(() => {
  // Day 28 of June 2025

  p1();

  p2();
})();
