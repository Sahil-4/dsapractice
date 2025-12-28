/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function (nums) {
  // Dutch National Flag Algo 

  const N = nums.length;

  const swap = (i, j) => {
    const t = nums[i];
    nums[i] = nums[j];
    nums[j] = t;
  };

  let pointer_0 = 0; // this will take zeroes, and give any other 
  let pointer_1 = 0; // this will take ones, and give ones and twos to others 
  let pointer_2 = N - 1; // this will take twoes, and give any other 

  while (pointer_1 <= pointer_2) {
    if (nums[pointer_1] === 0) {
      // swap pointer_1, with pointer_0 
      swap(pointer_1, pointer_0);
      // increment pointer_0 and pointer_1 
      pointer_0++;
      pointer_1++;
    } else if (nums[pointer_1] === 2) {
      // swap pointer_1, with pointer_2 
      swap(pointer_1, pointer_2);
      // decrement pointer_2 
      pointer_2--;
    } else {
      // increment pointer_1 
      pointer_1++;
    }
  }

  // Complexity analysis 
  // Time : O(N) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 75. Sort Colors - https://leetcode.com/problems/sort-colors/description/?envType=daily-question&envId=2025-05-17 

  console.log(sortColors([2, 0, 2, 1, 1, 0]));
  console.log(sortColors([2, 0, 1]));
};

class Problem2 {
  sortArray(arr, A, B, C) {
    // Code Here

    // return this.brute(arr, A, B, C);

    return this.optimal(arr, A, B, C);
  }

  optimal(arr, A, B, C) {
    const fn = (x) => (A * (x * x) + (B * x) + C);

    const tarr = arr.map(fn);

    const output = new Array(arr.length);
    let i = (A >= 0) ? arr.length - 1 : 0;

    let l = 0;
    let r = arr.length - 1;

    while (l <= r) {
      const left = tarr[l];
      const right = tarr[r];

      if (A >= 0) {
        // pick bigger one 
        if (left > right) {
          output[i] = left;
          l++;
          i--;
        } else {
          output[i] = right;
          r--;
          i--;
        }
      } else {
        // pick smaller one 
        if (left < right) {
          output[i] = left;
          l++;
          i++;
        } else {
          output[i] = right;
          r--;
          i++;
        }
      }
    }

    return output;
  }

  brute(arr, A, B, C) {
    const fn = (x) => (A * (x * x) + (B * x) + C);

    const output = arr.map(fn);

    output.sort((a, b) => a - b);

    return output;

    // Complexity analysis 
    // Time : O(N) + O(N * Log(N)) 
    // Space : O(N) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Sort the given array after applying the given equation - https://www.geeksforgeeks.org/problems/sort-the-given-array-after-applying-the-given-equation0304/1 

  console.log(new Problem2().sortArray([-3, -1, 2, 4], -1, 0, 0));
  console.log(new Problem2().sortArray([-4, -2, 0, 2, 4], 1, 3, 5));
};


(() => {
  // Day 17 of May 2025

  p1();

  p2();
})();
