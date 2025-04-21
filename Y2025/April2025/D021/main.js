/**
 * @param {number[]} differences
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
var numberOfArrays = function (differences, lower, upper) {
  let hidden0 = 0;
  let minVal = 0;
  let maxVal = 0;

  for (let diff of differences) {
    hidden0 = hidden0 + diff;

    minVal = Math.min(minVal, hidden0);
    maxVal = Math.max(maxVal, hidden0);

    if (upper - maxVal - (lower - minVal) < 0) {
      return 0;
    }
  }

  return upper - maxVal - (lower - minVal) + 1;

  // Complexity analysis
  // Time : O(N)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2145. Count the Hidden Sequences - https://leetcode.com/problems/count-the-hidden-sequences/description/?envType=daily-question&envId=2025-04-21

  console.log(numberOfArrays([1, -3, 4], 1, 6));
  console.log(numberOfArrays([3, -4, 5, 1, -2], 4, 5));
  console.log(numberOfArrays([4, -7, 2], 3, 6));
};

/**
 * @param {number[]} arr
 * @returns {number}
 */
class Problem2 {
  missingNum(arr) {
    // code here

    // return this.solve1(arr);
    return this.solve2(arr);
  }

  solve1(arr) {
    // XOR will work

    const N = arr.length;
    let xorResult = 0;

    for (let i = 1; i <= N + 1; i++) {
      xorResult ^= i;
      if (i <= N) xorResult ^= arr[i - 1];
    }

    return xorResult;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

  solve2(arr) {
    // n sum

    const N = arr.length + 1;
    let arrSum = 0;
    let expSum = (N * (N + 1)) / 2;

    for (let i = 0; i < N - 1; i++) {
      arrSum += arr[i];
    }

    return expSum - arrSum;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Missing in Array - https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1

  console.log(new Problem2().missingNum([1, 2, 3, 5]));
  console.log(new Problem2().missingNum([8, 2, 4, 5, 3, 7, 1]));
  console.log(new Problem2().missingNum([1]));
};

(() => {
  // Day 21 of April 2025

  p1();

  p2();
})();
