/**
 * @param {number[][]} nums1
 * @param {number[][]} nums2
 * @return {number[][]}
 */
const mergeArrays = (nums1, nums2) => {
  let result = [];

  const n = nums1.length,
    m = nums2.length;
  let i = 0,
    j = 0;

  while (i < n || j < m) {
    if (i < n && j < m && nums1[i][0] === nums2[j][0]) {
      result.push([nums1[i][0], nums1[i][1] + nums2[j][1]]);
      i++, j++;
    } else if (j >= m || (i < n && nums1[i][0] < nums2[j][0])) {
      result.push([nums1[i][0], nums1[i][1] + 0]);
      i++;
    } else {
      result.push([nums2[j][0], 0 + nums2[j][1]]);
      j++;
    }
  }

  return result;

  // Complexity analysis
  // Time : O(N|M)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2570. Merge Two 2D Arrays by Summing Values - https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/?envType=daily-question&envId=2025-03-02

  console.log(mergeArrays([], []));
  console.log(mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]));
  console.log(mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]]));
  console.log(mergeArrays([[1,3],[4,3]], [[2,4],[3,6],[5,5]]));
};

const maxOfSubarrays = (arr, k) => {
  // code here
  let result = [];
  let monotonicStack = [];

  for (let i = 0; i < arr.length; i++) {
    // remove out of window indices
    while (monotonicStack.length && monotonicStack[0] <= i - k) monotonicStack.shift();

    // remove smaller value indices
    while (monotonicStack.length && arr[monotonicStack.at(-1)] < arr[i]) monotonicStack.pop();

    // add index i
    monotonicStack.push(i);

    // push output into result for this window
    if (i >= k - 1) result.push(arr[monotonicStack[0]]);
  }

  return result;

  // Complexity analysis
  // Time : O(N)
  // Space : O(K)
};

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks K Sized Subarray Maximum - https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1

  console.log(maxOfSubarrays([1, 2, 3, 1, 4, 5, 2, 3, 6], 3));
  console.log(maxOfSubarrays([1, 2, 3, 1, 1, 1, 2, 3, 1], 3));
};

(() => {
  // Day 2 of March 2025

  p1();

  p2();
})();
