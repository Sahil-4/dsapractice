/**
 * @param {string} dominoes
 * @return {string}
 */
var pushDominoes = function (dominoes) {
  const N = dominoes.length;

  // closest on left that pushes i, towards right 
  const leftClosestRight = new Array(N).fill(-1);
  // closest on right that pushes i, towards left 
  const rightClosestLeft = new Array(N).fill(-1);

  // computer leftClosestRight, and rightClosestLeft
  for (let i = 0; i < N; i++) {
    if (dominoes[i] == 'L') {
      leftClosestRight[i] = -1;
    } else if (dominoes[i] == 'R') {
      leftClosestRight[i] = i;
    } else {
      leftClosestRight[i] = i > 0 ? leftClosestRight[i - 1] : -1;
    }
  }

  for (let i = N - 1; i >= 0; i--) {
    if (dominoes[i] == 'L') {
      rightClosestLeft[i] = i;
    } else if (dominoes[i] == 'R') {
      rightClosestLeft[i] = -1;
    } else {
      rightClosestLeft[i] = (i < N - 1) ? rightClosestLeft[i + 1] : -1;
    }
  }

  const output = new Array(N).fill('.');

  // cancel out forces, and check where domino will fall 
  for (let i = 0; i < N; i++) {
    const distR2L = Math.abs(i - rightClosestLeft[i]);
    const distL2R = Math.abs(i - leftClosestRight[i]);

    if (rightClosestLeft[i] == leftClosestRight[i]) {
      output[i] = '.';
    } else if (rightClosestLeft[i] == -1) {
      output[i] = 'R';
    } else if (leftClosestRight[i] == -1) {
      output[i] = 'L';
    } else if (distR2L == distL2R) {
      output[i] = '.';
    } else {
      output[i] = distR2L < distL2R ? 'L' : 'R';
    }
  }

  return output.join("");

  // Complexity analysis 
  // Time : O(3N) 
  // Space : O(2N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 838. Push Dominoes - https://leetcode.com/problems/push-dominoes/description/?envType=daily-question&envId=2025-05-02 

  console.log(pushDominoes("RR.L"));
  console.log(pushDominoes(".L.R...LR..L.."));
};

// User function Template for javascript

/**
 * @param {number[]} arr
 * @returns {number}
 */

class Problem2 {
  findMaximum(arr) {
    // your code here
    const N = arr.length;

    let low = 0;
    let high = N - 1;

    while (low <= high) {
      const mid = low + Math.floor((high - low) / 2);

      if ((mid == 0 || arr[mid - 1] < arr[mid]) && (mid == N - 1 || arr[mid] > arr[mid + 1])) {
        return arr[mid];
      } else {
        if (arr[mid] < arr[mid + 1]) {
          low = mid + 1;
        } else {
          high = mid;
        }
      }
    }

    return -1;

    // Complexity analysis 
    // Time : O(Log(N)) 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Bitonic Point - https://www.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1 

  console.log(new Problem2().findMaximum([1, 2, 4, 5, 7, 8, 3]));
  console.log(new Problem2().findMaximum([10, 20, 30, 40, 50]));
  console.log(new Problem2().findMaximum([120, 100, 80, 20, 0]));
};

(() => {
  // Day 2 of May 2025

  p1();

  p2();
})();