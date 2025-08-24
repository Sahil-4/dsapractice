/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function (nums) {
  let N = nums.length;
  let lslen = 0;

  const solution1 = () => {
    let L = N - 1;

    const allOnes = nums.reduce((acc, e) => acc && e, true);
    if (allOnes) return L;

    for (let i = 0; i < N; i++) {
      // it should be a 0 with non zero neighbours on any size
      if (!(nums[i] === 0 && (i === 0 || nums[i - 1] !== 0 || i === L || nums[i + 1] !== 0)))
        continue;

      // move left and count continous 1s
      let l = i - 1;
      while (l >= 0 && nums[l] === 1) l--;

      // move right and count continous 1s
      let r = i + 1;
      while (r <= L && nums[r] === 1) r++;

      // update longest subarray length
      lslen = Math.max(lslen, r - l - 2);
    }

    // Complexity analysis
    // Time : O(N) + O(N*N)
    // Space : O(1)
  };

  const solution2 = () => {
    for (let l = 0, r = 0, zeroes = 0; r < N; r++) {
      zeroes += nums[r] === 0;

      while (zeroes > 1) {
        zeroes -= nums[l] === 0;
        l++;
      }

      lslen = Math.max(lslen, r - l);
    }

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  };

  // solution1();
  solution2();

  return lslen;
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1493. Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=daily-question&envId=2025-08-24

  console.log(longestSubarray([1, 1, 0, 1]));
  console.log(longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]));
  console.log(longestSubarray([1, 1, 1]));
  console.log(longestSubarray([0, 0, 0]));
  console.log(longestSubarray([0]));
  console.log(longestSubarray([1, 0]));
  console.log(longestSubarray([0, 1]));
  console.log(longestSubarray([1, 0, 0, 0, 0]));
};

class Solution2 {
  minDaysBloom(arr, k, m) {
    // code here
    // binary search problem

    // search space
    let low = Math.min(...arr); // min days
    let high = Math.max(...arr); // max days

    let ans = -1;

    // binary search
    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      // shrink search space
      if (this.isPossible(arr, k, m, mid)) {
        ans = mid;
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    return ans;

    // Complexity analysis
    // Time : O(Log(MAX(Arr) - MIN(Arr)) * N)
    // Space : O(1)
  }

  isPossible(arr, k, m, days) {
    let bouquet = 0;
    let flowers = 0;

    for (let i = 0; i < arr.length; i++) {
      if (arr[i] <= days) {
        if (++flowers === k) {
          bouquet++;
          flowers = 0;
        }
      } else {
        flowers = 0;
      }
    }

    return bouquet >= m;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Minimum days to make M bouquets - https://www.geeksforgeeks.org/problems/minimum-days-to-make-m-bouquets/1

  const s2 = new Solution2();
  console.log(s2.minDaysBloom([3, 4, 2, 7, 13, 8, 5], 2, 3));
  console.log(s2.minDaysBloom([5, 5, 5, 5, 10, 5, 5], 3, 2));
  console.log(s2.minDaysBloom([1, 10, 3, 10, 2], 2, 3));
};

(() => {
  // Day 24 of August 2025

  p1();

  p2();
})();
