/**
 * @param {number} num
 * @return {number}
 */
var maxDiff = function (num) {
  const getMaxx = (darr) => {
    const N = darr.length;

    let digitToUpdate = null;
    for (let i = 0; i < N; i++) {
      if (digitToUpdate === null && darr[i] < 9) digitToUpdate = darr[i];
      if (digitToUpdate !== null && darr[i] === digitToUpdate) darr[i] = 9;
    }

    return parseInt(darr.join(""));
  };

  const getMinn = (darr) => {
    const N = darr.length;

    let digitToUpdate = darr[0] != 1 ? darr[0] : null;
    for (let i = 0; ((i < N) && digitToUpdate !== null); i++) {
      if (darr[i] === digitToUpdate) darr[i] = 1;
    }

    for (let i = 0; ((i < N) && (darr[0] == 1)); i++) {
      if (digitToUpdate === null && darr[i] > darr[0]) digitToUpdate = darr[i];
      if (darr[i] === digitToUpdate) darr[i] = 0;
    }

    return parseInt(darr.join(""));
  };

  let maxx = getMaxx(String(num).split(""));
  let minn = getMinn(String(num).split(""));

  return (maxx - minn);

  // Complexity analysis 
  // Time : O(2N) 
  // Space : O(2N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1432. Max Difference You Can Get From Changing an Integer - https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/description/?envType=daily-question&envId=2025-06-15 

  console.log(maxDiff(555));
  console.log(maxDiff(9));
  console.log(maxDiff(545454));
  console.log(maxDiff(1));
  console.log(maxDiff(100000000));
  console.log(maxDiff(99999999));
  console.log(maxDiff(1101057));
};

/**
 * @param {number[]} arr
 * @param {number} k
 * @returns {number}
 */

class Problem2 {
  smallestDivisor(arr, k) {
    // Code here

    const N = arr.length;

    const calculateCeilingSum = (divisor) => {
      let sum = 0;

      for (let i = 0; i < N; i++) {
        sum += Math.ceil(arr[i] / divisor);
      }

      return sum;
    };

    let low = 1;
    let high = Math.max(...arr);
    let ans = 0;

    while (low <= high) {
      let mid = Math.floor((low + high) / 2);

      let sum = calculateCeilingSum(mid);

      if (sum <= k) {
        ans = mid;
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    return ans;

    // Complexity analysis 
    // Time : O(Log(max(arr)) * N) 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Smallest Divisor - https://www.geeksforgeeks.org/problems/smallest-divisor/1 

  const p = new Problem2();
  console.log(p.smallestDivisor([1, 2, 5, 9], 6));
  console.log(p.smallestDivisor([1, 1, 1, 1], 4));
  console.log(p.smallestDivisor([1, 1, 1, 1], 6));
};


(() => {
  // Day 15 of June 2025

  p1();

  p2();
})();
