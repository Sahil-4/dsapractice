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

  // start 
  pq.enqueue([0, 0, 0]);
  minTime[0][0] = 0;

  while (!pq.isEmpty()) {
    const [tcost, ti, tj] = pq.dequeue();

    if ((ti == n - 1) && (tj == m - 1)) return tcost;

    for (let [pi, pj] of _dirs) {
      let ni = ti + pi;
      let nj = tj + pj;

      if (!validIndex(ni, nj)) continue;

      const ncost = Math.max(tcost, moveTime[ni][nj]) + 1;

      if (ncost < minTime[ni][nj]) {
        pq.enqueue([ncost, ni, nj]);
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
  // Problem 1 : POTD Leetcode 3341. Find Minimum Time to Reach Last Room I - https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description/?envType=daily-question&envId=2025-05-07 

  console.log(minTimeToReach([[0, 4], [4, 4]]));
  console.log(minTimeToReach([[0, 0, 0], [0, 0, 0]]));
  console.log(minTimeToReach([[0, 1], [1, 2]]));
  console.log(minTimeToReach([[94, 79, 62, 27, 69, 84], [6, 32, 11, 82, 42, 30]]));
  console.log(minTimeToReach([[15, 58], [67, 4]]));
  console.log(minTimeToReach([[17, 56], [97, 80]]));
};

/*

class Node{
    constructor(data){
        this.data = data;
        this.left = null;
        this.right = null;
    }
}
*/

class Problem2 {
  /**
  * @param Node root

  * @returns number[][]
  */
  Paths(root) {
    // code here
    const paths = new Array();

    this.traverseAndBuildPaths(root, [], paths);

    return paths;
  }

  traverseAndBuildPaths(root, currentPath, paths) {
    if (!root) return;
    if (!root.left && !root.right) {
      paths.push([...currentPath, root.data]);
      return;
    }

    currentPath.push(root.data);
    this.traverseAndBuildPaths(root.left, currentPath, paths);
    this.traverseAndBuildPaths(root.right, currentPath, paths);
    currentPath.pop();

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(H) + O(H) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Root to Leaf Paths - https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1 

  const root = {
    data: 0,
    left: {
      data: 1,
      left: {
        data: 3,
        left: null,
        right: null,
      },
      right: {
        data: 4,
        left: null,
        right: null,
      },
    },
    right: {
      data: 2,
      left: {
        data: 5,
        left: null,
        right: null,
      },
      right: null,
    },
  };
  console.log(new Problem2().Paths(root));
};

(() => {
  // Day 7 of May 2025

  p1();

  p2();
})();
