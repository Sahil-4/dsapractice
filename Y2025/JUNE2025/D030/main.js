/**
 * @param {number[]} nums
 * @return {number}
 */
var findLHS = function (nums) {
  // [1,3,2,2,5,2,3,7]
  // [1,2,2,2,3,3,5,7]
  // two pointers 
  // a = 0, b = 0
  // if difference is less then one advance b 
  // if difference is greater then one advance a 
  // if difference is exactly one update output 
  // another easy solution is to use map, store all elements with frequency in map 
  // for each element find its pair (e - 1) or (e + 1) 
  // then simply take the maximum sum of [(freq(e) + freq(e - 1)), (freq(e) + freq(e + 1))] 
  // and update output if necessory 

  const N = nums.length;
  const cnums = [...nums];
  cnums.sort((a, b) => a - b);

  let output = 0;

  let a = 0, b = 0;
  while (a < N && b < N) {
    let diff = cnums[b] - cnums[a];

    if (diff === 1) {
      output = Math.max(output, b - a + 1);
      b++;
    } else if (diff < 1) {
      b++;
    } else {
      a++;
    }
  }

  return output;

  // Complexity analysis 
  // Time : O(N) + O(N * Log(N)) + O(N) 
  // Space : O(N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 594. Longest Harmonious Subsequence - https://leetcode.com/problems/longest-harmonious-subsequence/description/?envType=daily-question&envId=2025-06-30 

  console.log(findLHS([1, 2, 3, 4]));
  console.log(findLHS([1, 1, 1, 1]));
  console.log(findLHS([1, 3, 2, 2, 5, 2, 3, 7]));
};

/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} w
 * @returns {number}
 */
class Problem2 {
  maxMinHeight(arr, k, w) {
    // code here

    let low = Math.min(...arr);
    let high = low + k;

    let output = low;

    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      if (this.canMakeMin(arr, k, w, mid)) {
        output = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return output;

    // Complexity analysis 
    // Time : O(N * Log(min(arr) + k)) 
    // Space : O(N) 
  }

  canMakeMin(arr, k, w, limit) {
    const N = arr.length;
    const water = new Array(N).fill(0);

    for (let i = 0; i < N; i++) {
      // prev effect - difference array technique 
      if (i > 0) water[i] += water[i - 1];

      let cheight = arr[i] + water[i];

      // prev effect - out of window - removing 
      if (i >= w) cheight -= water[i - w];

      if (cheight < limit) {
        let need = limit - cheight;
        water[i] += need;
        k -= need;

        if (k < 0) return false;
      }
    }

    return true;
  }

  brute(arri, k, w) {
    // code here

    // arr[] = [2, 3, 1, 1, 3], k = 2, w = 2
    // [2, 3, 2, 2, 3], at k = 1
    // [3, 4, 2, 2, 3], at k = 2

    const arr = [...arri];
    const N = arr.length;

    while (k > 0) {
      let mi = this.getMin(arr);
      for (let i = mi; i < Math.min(N, mi + w); i++) {
        arr[i] += 1;
      }

      k--;
    }

    return arr[this.getMin(arr)];

    // Complexity analysis 
    // Time : O(K * (N + W)) 
    // Space : O(N) 
  }

  getMin(arr) {
    let mi = 0;

    for (let i = 0; i < arr.length; i++) {
      if (arr[i] < arr[mi]) mi = i;
    }

    return mi;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Max min Height - https://www.geeksforgeeks.org/problems/max-min-height--170647/1 

  const s = new Problem2();
  console.log(s.maxMinHeight([2, 3, 4, 5, 1], 2, 2));
  console.log(s.maxMinHeight([2, 3, 1, 1, 3], 2, 2));
  console.log(s.maxMinHeight([5, 8], 5, 1));
};


(() => {
  // Day 30 of June 2025

  p1();

  p2();
})();
