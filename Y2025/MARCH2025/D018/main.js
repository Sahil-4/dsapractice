/**
 * @param {number[]} nums
 * @return {number}
 */
var longestNiceSubarray = function (nums) {
  const n = nums.length;
  let lnlen = 1;

  const checkNiceSubarray = (i, j) => {
    // now in this subarray [i, j] (inclusive)
    // check bitwise AND of pairs
    // bitwise AND should be zero of all pairs
    for (let e1i = i; e1i <= j; e1i++) {
      for (let e2i = e1i + 1; e2i <= j; e2i++) {
        // not a nice subarray - bitwise AND is not zero
        if ((nums[e1i] & nums[e2i]) != 0) return false;
      }
    }

    return true;
  };

  const solve1 = () => {
    // i = start of subarray, j = end of subarray
    for (let i = 0; i < n; i++) {
      for (let j = i; j < n; j++) {
        // subarray [i, j] is a nice subarray (1) or not (0)
        let flag = checkNiceSubarray(i, j);

        // update length of longest nice subarray
        if (flag) lnlen = Math.max(lnlen, j - i + 1);
      }
    }

    // Complexity analysis
    // Time : O(N*N*N*N) -> O(N^4)
    // Space : O(1)
  };

  const solve2 = () => {
    let i = 0;
    let j = 0;

    while (j < n) {
      if (checkNiceSubarray(i, j)) {
        // nice subarray
        // update length of longest nice subarray
        lnlen = Math.max(lnlen, j - i + 1);
        // extend window
        j++;
      } else {
        // not nice subarray
        // shrink the window
        i++;
      }
    }

    // Complexity analysis
    // Time : O(N*N*N) -> O(N^3) ~
    // Space : O(1)
  };

  const checkNiceSubarray_optimised = (i, j) => {
    // now in this subarray [i, j] (inclusive)
    // check bitwise AND of pairs
    // bitwise AND should be zero of all pairs

    // optimization :
    // instead of checking pairs
    // check elements AND with mask
    // mask will contains 1 at the places where we have encountered 1s in prev elements
    let mask = 0;

    for (let e1i = i; e1i <= j; e1i++) {
      // not a nice subarray
      if ((mask & nums[e1i]) != 0) return false;

      // update mask
      mask = mask | nums[e1i];
    }

    return true;
  };

  const solve3 = () => {
    let i = 0; // left pointer
    let j = 0; // right pointer

    while (j < n) {
      if (checkNiceSubarray_optimised(i, j)) {
        lnlen = Math.max(lnlen, j - i + 1);
        j++;
      } else {
        i++;
      }
    }

    // Complexity analysis
    // Time : O(N*N) -> O(N^2) ~
    // Space : O(1)
  };

  const solve4 = () => {
    let i = 0; // left pointer
    let j = 0; // right pointer

    let mask = 0; // mask - contain 1s

    while (j < n) {
      // shrink window if it cant be a nice subarray
      while ((mask & nums[j]) != 0) {
        mask = mask ^ nums[i]; // remove 1s of ith element
        i++; // shring window
      }

      // update length of longest nice subarray
      lnlen = Math.max(lnlen, j - i + 1);

      // update mask - add 1s of jth element
      mask = mask | nums[j];

      // extent window
      j++;
    }

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  };

  // solve1();
  // solve2();
  // solve3();
  solve4();

  return lnlen;
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2401. Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/description/?envType=daily-question&envId=2025-03-18

  console.log(longestNiceSubarray([1, 3, 8, 48, 10]));
  console.log(longestNiceSubarray([3, 1, 5, 11, 13]));
  console.log(longestNiceSubarray([338970160, 525086042, 19212931, 213753017, 321613307, 553272419, 190837185, 548628106, 793546945, 243936947]));
};

/**
 * @param {number[]} arr
 * @returns {boolean}
 */
class Problem2 {
  equalPartition(arr) {
    // your code here
    let tsum = arr.reduce((acc, e) => acc + e, 0);

    // cant divide odd sum into two equal parts
    if (tsum & 1) return false;

    tsum = tsum / 2; // target sum

    // return this.recursion(arr, tsum, 0);
    // const N = arr.length;
    // const memo = Array.from({ length: N }, () => new Array(tsum+1).fill(-1));
    // return this.memoize(arr, tsum, 0, memo);

    // return this.tabulation(arr, tsum);
    return this.optimised(arr, tsum);
  }

  recursion(arr, tsum, i = 0) {
    if (i >= arr.length) return tsum == 0;

    let not_pick = this.recursion(arr, tsum, i + 1);
    let pick = false;
    if (tsum >= arr[i]) pick = this.recursion(arr, tsum - arr[i], i + 1);

    return not_pick || pick;

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) stack
  }

  memoize(arr, tsum, i, memo) {
    if (i >= arr.length) return tsum == 0;

    if (memo[i][tsum] != -1) return memo[i][tsum];

    let not_pick = this.memoize(arr, tsum, i + 1, memo);
    let pick = false;
    if (tsum >= arr[i]) pick = this.memoize(arr, tsum - arr[i], i + 1, memo);

    return (memo[i][tsum] = not_pick || pick);

    // Complexity analysis
    // Time : O(2*N*TSUM)
    // Space : O(N) stack + O(N*TSUM)
  }

  tabulation(arr, _tsum) {
    const N = arr.length;
    const memo = Array.from({ length: N + 1 }, () => new Array(_tsum + 1).fill(false));

    // base
    memo[N][0] = true;

    // recurrence
    for (let i = N - 1; i >= 0; i--) {
      for (let tsum = 0; tsum <= _tsum; tsum++) {
        let not_pick = memo[i + 1][tsum];
        let pick = false;
        if (tsum >= arr[i]) pick = memo[i + 1][tsum - arr[i]];

        memo[i][tsum] = not_pick || pick;
      }
    }

    // return
    return memo[0][_tsum];

    // Complexity analysis
    // Time : O(N*TSUM)
    // Space : O(N*TSUM)
  }

  optimised(arr, _tsum) {
    const N = arr.length;
    let next = new Array(_tsum + 1).fill(false);

    // base
    next[0] = true;

    // recurrence
    for (let i = N - 1; i >= 0; i--) {
      let curr = new Array(_tsum + 1).fill(false);

      for (let tsum = 0; tsum <= _tsum; tsum++) {
        let not_pick = next[tsum];
        let pick = false;
        if (tsum >= arr[i]) pick = next[tsum - arr[i]];

        curr[tsum] = not_pick || pick;
      }

      next = curr;
    }

    // return
    return next[_tsum];

    // Complexity analysis
    // Time : O(N*TSUM)
    // Space : O(2*TSUM)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Partition Equal Subset Sum - https://www.geeksforgeeks.org/problems/subset-sum-problem2014/1

  console.log(new Problem2().equalPartition([1, 5, 11, 5]));
  console.log(new Problem2().equalPartition([1, 3, 5]));
};

(() => {
  // Day 18 of March 2025

  p1();

  p2();
})();
