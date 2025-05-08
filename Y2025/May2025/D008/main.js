/**
 * @param {number[][]} moveTime
 * @return {number}
 */
var minTimeToReach = function (moveTime) {
  const t = Number.MAX_SAFE_INTEGER;
  const _dirs = [[-1, 0], [0, +1], [+1, 0], [0, -1]];

  const n = moveTime.length;
  const m = moveTime[0].length;

  const validIndex = (i, j) => ((i >= 0 && i < n) && (j >= 0 && j < m));

  const minTime = Array.from({ length: n }, () => new Array(m).fill(t));

  const pq = new PriorityQueue((a, b) => a[0] - b[0]);

  // start [cost, ri, ci, ninc] 
  pq.enqueue([0, 0, 0, 1]);
  minTime[0][0] = 0;

  while (!pq.isEmpty()) {
    const [tcost, ti, tj, inc] = pq.dequeue();
    const ninc = inc === 1 ? 2 : 1;

    if ((ti == n - 1) && (tj == m - 1)) return tcost;

    for (let [pi, pj] of _dirs) {
      let ni = ti + pi;
      let nj = tj + pj;

      if (!validIndex(ni, nj)) continue;

      const ncost = Math.max(tcost, moveTime[ni][nj]) + inc;

      if (ncost < minTime[ni][nj]) {
        pq.enqueue([ncost, ni, nj, ninc]);
        minTime[ni][nj] = ncost;
      }
    }
  }

  return minTime[n - 1][m - 1];

  // Complexity analysis 
  // Time : O(N * M) 
  // Space : O(N * M) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3342. Find Minimum Time to Reach Last Room II - https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/description/?envType=daily-question&envId=2025-05-08 

  console.log(minTimeToReach([[0, 4], [4, 4]]));
  console.log(minTimeToReach([[0, 0, 0, 0], [0, 0, 0, 0]]));
  console.log(minTimeToReach([[0, 1], [1, 2]]));
  console.log(minTimeToReach([[15, 58], [67, 4]]));
  console.log(minTimeToReach([[17, 56], [97, 80]]));
  console.log(minTimeToReach([[56, 93], [3, 38]]));
};

// User function Template for javascript

/**
 * @param {number[]} arr
 * @return {number}
 */

class Problem2 {
  findMissing(arr) {
    // code here
    const N = arr.length;

    // another way to solve this is using sum of terms of ap 
    // find d, we have a0 as arr[0], 
    // calculate sum(arr) 
    // calculate ap sum Sn = (N/2) * (2*a + (N-1)D) 
    // just be careful at indices, and N 

    // missing will not follow ap rule 
    // find d 
    // then find ai

    // there is only one missing term 
    // all other terms are valid 

    // a0 will always be arr[0] 
    // if we use moores voting algo and find d 
    // we will be able to find d 

    // then we just have to varify earch arr[i] 

    // find d - common difference using moores voting algo 
    let d = 0;
    let f = 0;
    for (let i = 1; i < N; i++) {
      let td = arr[i] - arr[i - 1];
      if (d === td) {
        f++;
      } else {
        f--;
      }

      if (f <= 0) {
        d = td;
        f = 1;
      }
    }

    // a0 - 0th term 
    const a0 = arr[0];

    // verify - and return missing 
    for (let i = 0; i < N; i++) {
      const valid = (a0 + ((i) * d));
      if (valid !== arr[i]) return valid;
    }

    // return Nth term is no missing found 
    return (a0 + ((N) * d));

    // Complexity analysis 
    // Time : O(N) + O(N) 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Missing element of AP - https://www.geeksforgeeks.org/problems/missing-element-of-ap2228/1 

  console.log(new Problem2().findMissing([2, 4, 8, 10, 12, 14]));
  console.log(new Problem2().findMissing([1, 6, 11, 16, 21, 31]));
  console.log(new Problem2().findMissing([4, 7, 10, 13, 16]));
};

(() => {
  // Day 8 of May 2025

  p1();

  p2();
})();
