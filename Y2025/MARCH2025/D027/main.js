/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumIndex = function (nums) {
  // steps
  // 1. Find majority element using Moore's Voting algo
  // 2. Count freq of majority element in the entire array
  //    also take another variable leftCount = 0
  // 3. Iterate over the nums array
  //    if ith element is equal to majority element increase leftCount, and decrease rightCount
  //    at any index if count (right and left) satisfy the condition
  //     then return the index
  // at last return -1

  const N = nums.length;

  const moores = () => {
    let e = -1;
    let f = 0;

    for (let i = 0; i < N; i++) {
      if (f == 0) {
        e = nums[i];
        f = 1;
      } else if (nums[i] == e) {
        f++;
      } else {
        f--;
      }
    }

    return f != 0 ? e : -1;
  };

  let majorityElement = moores();

  // answer not possible if there is no majority element
  if (majorityElement == -1) return -1;

  // count frequency
  let rightCount = nums.reduce((acc, e) => acc + (e == majorityElement), 0);
  let leftCount = 0;

  // update freq and check for valid split index
  for (let i = 0; i < N; i++) {
    if (nums[i] == majorityElement) {
      leftCount++;
      rightCount--;

      let t1 = Math.floor((i + 1) / 2);
      let t2 = Math.floor((N - i - 1) / 2);

      // if its valid index
      if (leftCount > t1 && rightCount > t2) return i;
    }
  }

  return -1;

  // Complexity analysis
  // Time : O(N) + O(N) + O(N)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2780. Minimum Index of a Valid Split - https://leetcode.com/problems/minimum-index-of-a-valid-split/description/?envType=daily-question&envId=2025-03-27

  console.log(minimumIndex([1, 2, 2, 2]));
  console.log(minimumIndex([2, 1, 3, 1, 1, 1, 7, 1, 2, 1]));
  console.log(minimumIndex([3, 3, 3, 3, 7, 2, 2]));
};

// User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number[]} dep
 * @returns {number}
 */
class Problem2 {
  // Function to find the minimum number of platforms required at the
  // railway station such that no train waits.
  findPlatform(arr, dep) {
    // your code here
    const N = arr.length;
    let platforms = 0;

    const times = [];
    for (let i = 0; i < N; i++) times.push([arr[i], "A"]);
    for (let i = 0; i < N; i++) times.push([dep[i], "D"]);

    times.sort((a, b) => a[0] - b[0]);

    let temp = 0;

    for (let i = 0; i < 2 * N; i++) {
      if (times[i][1] == "A") {
        temp++;
      } else {
        temp--;
      }

      platforms = Math.max(platforms, temp);
    }

    return platforms;

    // Complexity analysis
    // Time : O(2N) + O(2N * LOG(2N)) + O(2N)
    // Space : O(2N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Minimum Platforms - https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

  console.log(new Problem2().findPlatform([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]));
};

(() => {
  // Day 27 of March 2025

  p1();

  p2();
})();
