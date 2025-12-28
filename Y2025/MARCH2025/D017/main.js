/**
 * @param {number[]} nums
 * @return {boolean}
 */
var divideArray = function (nums) {
  const solve1 = () => {
    // element frequency map
    const freq = new Map();

    // fill the map with element and frequency
    for (let i = 0; i < nums.length; i++) {
      freq.set(nums[i], (freq.get(nums[i]) || 0) + 1);
    }

    // false, if element has odd frequency
    let flag = true;

    // look up for odd frequency element
    for (const [e, f] of freq) {
      if (f & 1) {
        flag = false;
      }
    }

    return flag;

    // Complexity analysis
    // Time : O(2N)
    // Space : O(N)
  };

  const solve2 = () => {
    // element frequency object
    const freq = {};

    // fill the object with element and frequency
    // if contains even freq delete it from object
    for (let i = 0; i < nums.length; i++) {
      if (!freq[nums[i]]) freq[nums[i]] = 0;

      freq[nums[i]]++;

      if (!(freq[nums[i]] & 1)) delete freq[nums[i]];
    }

    // false, if element has odd frequency
    let flag = true;

    // check for odd frequency element
    // if freq object cotains any key it means that it has odd value
    // and hence output should be false
    flag = Object.keys(freq).length === 0;

    return flag;

    // Complexity analysis
    // Time : O(N)
    // Space : O(N)
  };

  // return solve1();
  return solve2();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2206. Divide Array Into Equal Pairs - https://leetcode.com/problems/divide-array-into-equal-pairs/description/?envType=daily-question&envId=2025-03-17

  console.log(divideArray(1, 2));
  console.log(divideArray(1, 1));
};

/**
 * @param {number[]} arr
 * @param {number} target
 * @return {boolean}
 */
class Problem2 {
  isSubsetSum(arr, sum) {
    // code here

    // return this.recursion(arr, sum, 0);

    // const n = arr.length;
    // const memo = Array.from({ length: n }, () => new Array(sum+1).fill(-1));
    // return this.memoize(arr, sum, 0, memo);

    // return this.tabulation(arr, sum);
    return this.optimised(arr, sum);
  }

  recursion(arr, sumLeft, i) {
    if (arr.length <= i) return sumLeft == 0;

    let not_pick = this.recursion(arr, sumLeft, i + 1);
    if (not_pick) return true;

    let pick = false;
    if (sumLeft >= arr[i]) pick = this.recursion(arr, sumLeft - arr[i], i + 1);

    return pick;

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) stack space
  }

  memoize(arr, sumLeft, i, memo) {
    if (arr.length <= i) return sumLeft == 0;

    if (memo[i][sumLeft] != -1) return memo[i][sumLeft];

    let not_pick = this.memoize(arr, sumLeft, i + 1, memo);
    if (not_pick) return true;

    let pick = false;
    if (sumLeft >= arr[i]) pick = this.memoize(arr, sumLeft - arr[i], i + 1, memo);

    return (memo[i][sumLeft] = pick);

    // Complexity analysis
    // Time : O(2*N*SUM)
    // Space : O(N) stack space + O(N*SUM) memory
  }

  tabulation(arr, sum) {
    // memory
    const n = arr.length;
    const memo = Array.from({ length: n + 1 }, () => new Array(sum + 1).fill(false));

    // base case
    for (let i = 0; i <= n; i++) memo[i][0] = true;

    // recurrence
    for (let i = n - 1; i >= 0; i--) {
      for (let sumLeft = 0; sumLeft <= sum; sumLeft++) {
        let not_pick = memo[i + 1][sumLeft];
        let pick = sumLeft >= arr[i] ? memo[i + 1][sumLeft - arr[i]] : false;

        memo[i][sumLeft] = not_pick || pick;
      }
    }

    // return
    return !!memo[0][sum];

    // Complexity analysis
    // Time : O(N*SUM)
    // Space : O(N*SUM) memory
  }

  optimised(arr, sum) {
    // memory
    const n = arr.length;
    let next = new Array(sum + 1).fill(false);

    // base case
    next[0] = true;

    // recurrence
    for (let i = n - 1; i >= 0; i--) {
      let curr = new Array(sum + 1).fill(false);
      curr[0] = true;

      for (let sumLeft = 0; sumLeft <= sum; sumLeft++) {
        let not_pick = next[sumLeft];
        let pick = sumLeft >= arr[i] ? next[sumLeft - arr[i]] : false;

        curr[sumLeft] = not_pick || pick;
      }

      next = curr;
    }

    // return
    return !!next[sum];

    // Complexity analysis
    // Time : O(N*SUM)
    // Space : O(2*SUM) memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Subset Sum Problem - https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

  console.log(new Problem2().isSubsetSum([3, 34, 4, 12, 5, 2], 9));
  console.log(new Problem2().isSubsetSum([3, 34, 4, 12, 5, 2], 30));
  console.log(new Problem2().isSubsetSum([1, 2, 3], 6));
};

(() => {
  // Day 17 of March 2025

  p1();

  p2();
})();
