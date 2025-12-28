/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number}
 */
var maxRemoval = function (nums, queries) {
  const NN = nums.length;
  const QN = queries.length;

  // sorted queries - based on start index 
  const squeries = [...queries].sort((a, b) => {
    if (a[0] === b[0]) return a[1] - b[1];
    return a[0] - b[0];
  });

  let sqi = 0;
  let usedQ = 0;

  // used queries - min heap 
  const usedQueries = new MinPriorityQueue();
  // available queries - max heap 
  const availableQueries = new MaxPriorityQueue();

  for (let i = 0; i < NN; i++) {
    // push queries (in squeries) (to availableQueries) starting at i 
    while (sqi < QN && squeries[sqi][0] == i) {
      availableQueries.enqueue(squeries[sqi][1]);
      sqi++;
    }

    // use previous queries to make ith element zero 
    nums[i] -= usedQueries.size();

    // use more queries if needed 
    while (nums[i] > 0 && !availableQueries.isEmpty() && availableQueries.front() >= i) {
      usedQueries.push(availableQueries.front());
      availableQueries.dequeue();
      nums[i] -= 1;
      usedQ++;
    }

    // unable to make ith element zero return -1 
    if (nums[i] > 0) return -1;

    // remove queries ending at i 
    while (!usedQueries.isEmpty() && usedQueries.front() === i) {
      usedQueries.dequeue();
    }
  }

  return QN - usedQ;

  // Complexity analysis 
  // Time : O(QN * Log(QN)) + O(NN * Log(QN)) 
  // Space : O(QN) + O(QN) + O(QN) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3362. Zero Array Transformation III - https://leetcode.com/problems/zero-array-transformation-iii/description/?envType=daily-question&envId=2025-05-22 

  console.log(maxRemoval([2, 0, 2], [[0, 2], [0, 2], [1, 1]]));
  console.log(maxRemoval([1, 1, 1, 1], [[1, 3], [0, 2], [1, 3], [1, 2]]));
  console.log(maxRemoval([1, 2, 3, 4], [[0, 3]]));
};

/**
 * @param {string} S
 * @returns {number}
 */

class Problem2 {
  minDeletions(s) {
    // code here
    const N = s.length;

    let prev = new Array(N).fill(0);

    for (let i = N - 1; i >= 0; i--) {
      let curr = new Array(N).fill(0);

      for (let j = i + 1; j < N; j++) {
        if (i >= j) continue;

        if (s[i] === s[j]) {
          curr[j] = prev[j - 1];
        } else {
          // delete ith char 
          let op1 = 1 + prev[j];

          // delete jth char 
          let op2 = 1 + curr[j - 1];

          // delete ith and jth char 
          let op3 = 2 + prev[j - 1];

          curr[j] = Math.min(op1, op2, op3);
        }
      }

      prev = curr;
    }

    return prev[N - 1];

    // Complexity analysis 
    // Time : O(N * N) 
    // Space : O(2 * N) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Minimum Deletions - https://www.geeksforgeeks.org/problems/minimum-deletitions1648/1 

  console.log(new Problem2().minDeletions("aebcbda"));
  console.log(new Problem2().minDeletions("geeksforgeeks"));
};


(() => {
  // Day 22 of May 2025

  p1();

  p2();
})();
