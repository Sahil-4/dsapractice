/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {boolean}
 */
var isZeroArray = function (nums, queries) {
  const N = nums.length;

  const differenceArray = new Array(N).fill(0);

  for (let [l, r] of queries) {
    differenceArray[l] -= 1;
    if (r + 1 < N) differenceArray[r + 1] += 1;
  }

  for (let i = 0, psum = 0; i < N; i++) {
    psum += differenceArray[i];
    if (nums[i] + psum > 0) return false;
  }

  return true;

  // Complexity analysis 
  // Time : O(Q) + O(N) 
  // Space : O(N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3355. Zero Array Transformation I - https://leetcode.com/problems/zero-array-transformation-i/description/?envType=daily-question&envId=2025-05-20 

  console.log(isZeroArray([1, 0, 1], [[0, 2]]));
  console.log(isZeroArray([4, 3, 2, 1], [[1, 3], [0, 2]]));
};

/**
 * @param {Node} root
 * @param {number} target
 * @return {number}
 */
/*
class Node {
    constructor(x){
        this.key=x;
        this.left=null;
        this.right=null;
    }
} */

class Problem {
  minTime(root, target) {
    // code here

    // adjacency map 
    const adjMap = new Map();

    const buildAdjacencyMap = (node, parent) => {
      if (!node) return;

      const neighbours = adjMap.get(node.key) || [];

      if (parent) neighbours.push(parent.key);
      if (node.left) neighbours.push(node.left.key);
      if (node.right) neighbours.push(node.right.key);

      adjMap.set(node.key, neighbours);

      buildAdjacencyMap(node.left, node);
      buildAdjacencyMap(node.right, node);
    };

    const calculateBurningTime = () => {
      let burning_time = 0;

      const visited = new Set();
      const queue = [];

      queue.push([target, burning_time]);
      visited.add(target);

      while (queue.length) {
        const [node, t] = queue.shift();

        burning_time = t;

        for (let n of adjMap.get(node)) {
          if (visited.has(n)) continue;
          queue.push([n, t + 1]);
          visited.add(n);
        }
      }

      return burning_time;
    };

    buildAdjacencyMap(root, null);

    return calculateBurningTime();

    // Complexity analysis 
    // Time : O(V) + O(V + E) 
    // Space : O(V + E) + O(V) + O(V) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Burning Tree - https://www.geeksforgeeks.org/problems/burning-tree/1 

  const root = {
    data: 2,
    left: {
      data: 1,
      left: null,
      right: null,
    },
    right: {
      data: 5,
      left: null,
      right: null,
    },
  };
  const target = 2;
  console.log(new Problem().minTime(root, target));
};


(() => {
  // Day 20 of May 2025

  p1();

  p2();
})();
