/**
 * @param {number[]} ranks
 * @param {number} cars
 * @return {number}
 */
var repairCars = function (ranks, cars) {
  const repairPossible = (t) => {
    let carsDone = 0;

    for (let rank of ranks) {
      let low_c = 0;
      let high_c = cars - carsDone;
      let done = 0;

      while (low_c <= high_c) {
        const mid_c = low_c + Math.floor((high_c - low_c) / 2);
        const mechanicRepairTime = rank * mid_c * mid_c;

        if (mechanicRepairTime <= t) {
          done = mid_c;
          low_c = mid_c + 1;
        } else {
          high_c = mid_c - 1;
        }
      }

      carsDone += done;
    }

    return carsDone >= cars;
  };

  let low_t = 1;
  let high_t = Math.min(...ranks) * cars * cars;
  let ans = high_t;

  while (low_t <= high_t) {
    const mid_t = low_t + Math.floor((high_t - low_t) / 2);

    if (repairPossible(mid_t)) {
      ans = mid_t;
      high_t = mid_t - 1;
    } else {
      low_t = mid_t + 1;
    }
  }

  return ans;

  // Complexity analysis
  // Time : O(Log(high_t) * (ranks * Log(cars)))
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2594. Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/?envType=daily-question&envId=2025-03-16

  console.log(repairCars([4, 2, 3, 1], 10));
  console.log(repairCars([5, 1, 8], 6));
};

/**
 * @param {number[]} arr
 * @return {number}
 */
class Problem2 {
  minJumps(arr) {
    // code here

    if (arr[0] == 0) return -1;
    if (arr.length == 1 && arr[0] != 0) return 1;

    let out = Infinity;

    // out = this.recursion(arr, 0);

    // const n = arr.length;
    // const memo = new Array(n).fill(-1);
    // out = this.memoize(arr, 0, memo);

    return this.tabulation(arr);
  }

  recursion(arr, i) {
    if (i >= arr.length - 1) return 0;

    let minSteps = Infinity;

    for (let n = 1; n <= arr[i]; n++) {
      minSteps = Math.min(minSteps, 1 + this.recursion(arr, i + n));
    }

    return minSteps;

    // Complexity analysis
    // Time : O(N^N) ~
    // Space : O(N) stack space
  }

  memoize(arr, i, memo) {
    if (i >= arr.length - 1) return 0;

    if (memo[i] != -1) return memo[i];

    let minSteps = Infinity;

    for (let n = 1; n <= arr[i]; n++) {
      minSteps = Math.min(minSteps, 1 + this.memoize(arr, i + n, memo));
    }

    return (memo[i] = minSteps);

    // Complexity analysis
    // Time : O(2*N*N) ~
    // Space : O(N) stack space + O(N) memory
  }

  tabulation(arr) {
    const N = arr.length;
    const memo = new Array(N + 1).fill(0);

    for (let i = N - 2; i >= 0; i--) {
      let minSteps = Infinity;

      for (let n = 1; n <= arr[i]; n++) {
        let steps = 1;
        if (i + n < N) steps += memo[i + n];
        minSteps = Math.min(minSteps, steps);
      }

      memo[i] = minSteps;
    }

    return memo[0] == Infinity ? -1 : memo[0];

    // Complexity analysis
    // Time : O(N*M)
    // Space : O(N) memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Minimum Jumps - https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1

  console.log(new Problem2().minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]));
  console.log(new Problem2().minJumps([1, 4, 3, 2, 6, 7]));
  console.log(new Problem2().minJumps([1]));
  console.log(new Problem2().minJumps([0]));
};

(() => {
  // Day 16 of March 2025

  p1();

  p2();
})();
