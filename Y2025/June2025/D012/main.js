/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAdjacentDistance = function (nums) {
  // Approach : 
  // simply traverse the array from left to right 
  // for each element a = nums[i], take another element b = nums[i+1], 
  // to make sure i+1 does not goes out of bound mod it with N 
  // a = nums[i], b = nums[((i + 1) % N)] 
  // calculate absolute difference 
  // update max absolute difference 

  const N = nums.length;

  let mad = 0;

  for (let i = 0; i < N; i++) {
    let a = nums[i];
    let b = nums[(i + 1) % N];

    let ad = Math.abs(a - b);

    mad = Math.max(mad, ad);
  }

  return mad;

  // Complexity analysis 
  // Time : O(N) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3423. Maximum Difference Between Adjacent Elements in a Circular Array  - https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description/?envType=daily-question&envId=2025-06-12 

  console.log(maxAdjacentDistance([1, 2, 4]));
  console.log(maxAdjacentDistance([-5, -10, -5]));
  console.log(maxAdjacentDistance([1, 2]));
};

/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */

class Problem2 {
  printKClosest(arr, k, x) {
    // code here

    // Intuition & Approach : 
    // visualise the array as a mountain 
    // its peak is either x, or first element greater then x 
    // now we can set two pointers around x, 
    // or on last element smaller then x, and first element greater then x 
    // then we can compare which pointer element is closest to x 
    // then we take that element and update pointer 
    // edge cases : 
    // any pointer goes out of bound 
    // x is not in arr also there is no element greater then x 

    const N = arr.length;

    // find index of x, or first element greater then x 
    let idx = this.binary_search_mod(arr, x);

    let left = idx - 1;
    let right = (idx < N && arr[idx] === x) ? idx + 1 : idx;

    const kclosest = new Array();

    while (k > 0 && left >= 0 && right < N) {
      const l = arr[left];
      const r = arr[right];
      const ldiff = Math.abs(l - x);
      const rdiff = Math.abs(r - x);

      if ((ldiff < rdiff) || (ldiff === rdiff && l > r)) {
        kclosest.push(l);
        left--;
      } else {
        kclosest.push(r);
        right++;
      }

      k--;
    }

    while (k > 0 && left >= 0) {
      const l = arr[left];
      kclosest.push(l);
      left--;
      k--;
    }

    while (k > 0 && right < N) {
      const r = arr[right];
      kclosest.push(r);
      right++;
      k--;
    }

    return kclosest;

    // Complexity analysis 
    // Time : O(Log(N)) + O(K) 
    // Space : O(1) 
  }

  binary_search_mod(arr, key) {
    let low = 0;
    let high = arr.length - 1;

    let ans = arr.length;

    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      if (arr[mid] >= key) {
        ans = mid;
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    return ans;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks K closest elements - https://www.geeksforgeeks.org/problems/k-closest-elements3619/1 

  const solve = new Problem2();
  console.log(solve.printKClosest([1, 3, 4, 10, 12], 2, 4));
  console.log(solve.printKClosest([1, 3, 4, 10, 12], 5, 5));
  console.log(solve.printKClosest([1, 3, 4, 10, 12], 5, 22));
  console.log(solve.printKClosest([12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56], 4, 35));
  console.log(solve.printKClosest([12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56], 12, 36));
};


(() => {
  // Day 12 of June 2025

  p1();

  p2();
})();
