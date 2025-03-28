/**
 * @param {number[][]} grid
 * @param {number[]} queries
 * @return {number[]}
 */
var maxPoints = function (grid, queries) {
  // possible movements
  const directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  const m = grid.length;
  const n = grid[0].length;
  const k = queries.length;

  // sorted queries
  const sortedQueries = [];
  for (let i = 0; i < k; i++) {
    sortedQueries.push([queries[i], i]);
  }
  sortedQueries.sort((a, b) => a[0] - b[0]);

  // visited array
  const visited = Array.from({ length: m }, () => new Array(n).fill(false));

  const queueComparator = (a, b) => {
    if (a[0] != b[0]) return a[0] - b[0]; // cell value
    else if (a[1] != b[1]) return a[1] - b[1]; // cell row
    return a[2] - b[2]; // cell col
  };
  // pq to help in bfs
  const pq = new PriorityQueue(queueComparator);

  // start bfs
  pq.enqueue([grid[0][0], 0, 0]);
  visited[0][0] = true;

  let points = 0; // points count
  const result = new Array(k).fill(0);

  for (let i = 0; i < k; i++) {
    const [qv, qi] = sortedQueries[i];

    while (!pq.isEmpty() && pq.front()[0] < qv) {
      const i = pq.front()[1];
      const j = pq.front()[2];

      pq.dequeue();

      points++;

      for (let nextDir of directions) {
        const ni = i + nextDir[0];
        const nj = j + nextDir[1];

        if (ni >= 0 && ni < m && nj >= 0 && nj < n && !visited[ni][nj]) {
          pq.enqueue([grid[ni][nj], ni, nj]);
          visited[ni][nj] = true;
        }
      }
    }

    result[qi] = points;
  }

  return result;

  // Complexity analysis
  // Time : O(MN * LOG(MN))
  // Space : O(N) + O(NM)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2503. Maximum Number of Points From Grid Queries - https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description/?envType=daily-question&envId=2025-03-28

  console.log(
    maxPoints(
      [
        [1, 2, 3],
        [2, 5, 7],
        [3, 5, 1],
      ],
      [5, 6, 2],
    ),
  );
  console.log(
    maxPoints(
      [
        [5, 2, 1],
        [1, 1, 2],
      ],
      [3],
    ),
  );
};

class Problem2 {
  activitySelection(start, finish) {
    // code here.
    const N = start.length;

    const times = [];

    for (let i = 0; i < N; i++) {
      times.push([start[i], finish[i]]);
    }

    times.sort((a, b) => {
      if (a[1] != b[1]) return a[1] - b[1];
      return a[0] - b[0];
    });

    let count = 1;
    let currFinish = times[0][1];

    for (let i = 1; i < N; i++) {
      if (times[i][0] > currFinish) {
        count++;
        currFinish = times[i][1];
      }
    }

    return count;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Activity Selection - https://www.geeksforgeeks.org/problems/activity-selection-1587115620/1

  console.log(new Problem2().activitySelection([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]));
  console.log(new Problem2().activitySelection([10, 12, 20], [20, 25, 30]));
};

(() => {
  // Day 28 of March 2025

  p1();

  p2();
})();
