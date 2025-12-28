const lower_bound = (arr, key) => {
  let left = 0, right = arr.length;

  while (left < right) {
    let mid = Math.floor((left + right) / 2);
    if (arr[mid] < key) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  return left;
};

/**
* @param {number[]} tasks
* @param {number[]} workers
* @param {number} pills
* @param {number} strength
* @return {number}
*/
var maxTaskAssign = function (tasks, workers, pills, strength) {
  const N = tasks.length;
  const M = workers.length;

  tasks.sort((a, b) => a - b); // ASC 
  workers.sort((a, b) => b - a); // DESC 

  const isXTasksPossible = (X) => {
    let pillsUsed = 0;
    let bestMidWorkers = workers.slice(0, X + 1).sort((a, b) => a - b);

    for (let i = X - 1; i >= 0; i--) {
      let reqStrength = tasks[i];
      let workerStrength = bestMidWorkers[bestMidWorkers.length - 1];

      if (workerStrength >= reqStrength) {
        bestMidWorkers.pop();
      } else if (pillsUsed >= pills) {
        return false;
      } else {
        let weakWorker = lower_bound(bestMidWorkers, reqStrength - strength);
        if (weakWorker == bestMidWorkers.length) return false;

        bestMidWorkers.splice(weakWorker, 1);
        pillsUsed++;
      }
    }

    return true;
  };

  let maxTasks = 0;

  let low = 0;
  let high = Math.min(N, M);

  while (low <= high) {
    let X = low + Math.floor((high - low) / 2);

    if (isXTasksPossible(X)) {
      maxTasks = X;
      low = X + 1;
    } else {
      high = X - 1;
    }
  }

  return maxTasks;

  // Complexity analysis 
  // Time : O(N * Log(N)) + O(M * Log(M)) + O(Log(min(K)) * K * K) 
  // Space : O(N) + O(M) + O(K) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2071. Maximum Number of Tasks You Can Assign - https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/description/?envType=daily-question&envId=2025-05-01 

  {
    const args = [
      [3, 2, 1], [0, 3, 3], 1, 1
    ];
    console.log(maxTaskAssign(...args));
  }
  {
    const args = [
      [5, 4], [0, 0, 0], 1, 5
    ];
    console.log(maxTaskAssign(...args));
  }
  {
    const args = [
      [10, 15, 30], [0, 10, 10, 10, 10], 3, 10
    ];
    console.log(maxTaskAssign(...args));
  }
};

// User function Template for javascript

/**
 * @param {number} n
 * @return {number[]}
 */

class Problem2 {
  nthRowOfPascalTriangle(N) {
    // code here

    // return this.brute(N);
    return this.optimal(N);
  }

  optimal(N) {
    let out = new Array(N).fill(0);
    out[0] = 1;
    out[N - 1] = 1;

    for (let i = 1; i <= Math.floor(N / 2); i++) {
      out[i] = out[i - 1] * (N - i);
      out[i] = Math.floor(out[i] / i);
      out[N - i - 1] = out[i];
    }

    return out;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) 
  }

  brute(N) {
    let out = new Array(N + 1).fill(0);
    out[1] = 1;

    for (let i = 2; i <= N; i++) {
      let temp = new Array(N + 1).fill(0);
      for (let index = 1; index <= i; index++) {
        temp[index] = out[index] + out[index - 1];
      }

      out = temp;
    }

    out.shift();

    return out;

    // Complexity analysis 
    // Time : O(N*N) 
    // Space : O(2N) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Pascal Triangle - https://www.geeksforgeeks.org/problems/pascal-triangle0652/1 

  console.log(new Problem2().nthRowOfPascalTriangle(1));
  console.log(new Problem2().nthRowOfPascalTriangle(2));
  console.log(new Problem2().nthRowOfPascalTriangle(3));
  console.log(new Problem2().nthRowOfPascalTriangle(5));
  console.log(new Problem2().nthRowOfPascalTriangle(10));
  console.log(new Problem2().nthRowOfPascalTriangle(15));
  console.log(new Problem2().nthRowOfPascalTriangle(20));
};

(() => {
  // Day 1 of May 2025

  p1();

  p2();
})();
