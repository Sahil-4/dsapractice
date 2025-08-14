/**
 * @param {string} num
 * @return {string}
 */
var largestGoodInteger = function (num) {
  let str = "";

  for (let i = 0; i <= num.length - 3; i++) {
    if (!(num[i] === num[i + 1] && num[i + 1] === num[i + 2])) continue;
    let str2 = num[i] + num[i + 1] + num[i + 2];
    if (str < str2) str = str2;
  }

  return str;

  // Complexity analysis
  // Time : O(N)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2264. Largest 3-Same-Digit Number in String - https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/?envType=daily-question&envId=2025-08-14

  console.log(largestGoodInteger("6777133339"));
  console.log(largestGoodInteger("2300019"));
  console.log(largestGoodInteger("42352338"));
  console.log(largestGoodInteger("222"));
};

/**
 * @param {number[]} arr
 * @returns {number}
 */
class Solution2 {
  countRevPairs(arr) {
    // code here

    // return this.brute(arr);
    return this.optimal(arr);
  }

  merge(nums, l, m, h) {
    const temp = new Array();

    let l1 = l;
    let r1 = m + 1;

    while (l1 <= m && r1 <= h) {
      if (nums[l1] <= nums[r1]) temp.push(nums[l1++]);
      else temp.push(nums[r1++]);
    }

    while (l1 <= m) temp.push(nums[l1++]);
    while (r1 <= h) temp.push(nums[r1++]);

    let a = l;
    for (let b = 0; b < temp.length; b++) nums[a++] = temp[b];
  }

  countPairs(nums, l, m, h) {
    let count = 0;

    let r = m + 1;
    for (let i = l; i <= m; i++) {
      while (r <= h && nums[i] > 2 * nums[r]) r++;
      count += r - (m + 1);
    }

    return count;
  }

  mergeSort(nums, l, h) {
    let count = 0;

    if (l >= h) return count;

    let m = Math.floor((l + h) / 2);

    count += this.mergeSort(nums, l, m);
    count += this.mergeSort(nums, m + 1, h);
    count += this.countPairs(nums, l, m, h);
    this.merge(nums, l, m, h);

    return count;
  }

  optimal(arr) {
    const N = arr.length;
    let count = this.mergeSort(arr, 0, arr.length - 1);

    return count;

    // Complexity analysis
    // Time : O(N*Log(N))
    // Space : O(Log(N)) + O(N)
  }

  brute(arr) {
    const N = arr.length;
    let count = 0;

    for (let i = 0; i < N; i++) {
      for (let j = i + 1; j < N; j++) {
        if (arr[i] > 2 * arr[j]) count++;
      }
    }

    return count;

    // Complexity analysis
    // Time : O(N*N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Count Reverse Pairs - https://www.geeksforgeeks.org/problems/count-reverse-pairs/1

  const s2 = new Solution2();
  console.log(s2.countRevPairs([3, 2, 4, 5, 1, 20]));
  console.log(s2.countRevPairs([5, 4, 3, 2, 2]));
};

(() => {
  // Day 14 of August 2025

  p1();

  p2();
})();
