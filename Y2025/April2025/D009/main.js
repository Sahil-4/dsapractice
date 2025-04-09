/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function (nums, k) {
  // Thought process -

  // Approach
  // now i just have to replace
  // all 1st largest e, with 2nd largest e
  // then all 2nd largest e, with 3rd largest e
  // this will go till we dont make all elements equal to k

  // Output
  // lets say we got X unique elements in nums
  // now applying above logic
  // if smallest element is equal to k then we dont have to temper it,
  // and here we will save one operation
  // in else case we will have to perform unique(nums).length operations

  // Edge case
  // suppose nums contains any element smaller then e,
  // now in this case we cant make it equal to k,
  // as we are reducing values from largest to smallest

  // smallest element in nums
  const smallest = nums.reduce((acc, e) => Math.min(acc, e), Infinity);

  // case - not possible case
  if (smallest < k) return -1;

  // count distinct elements in increasing order
  const set = new Set(nums);

  return smallest == k ? set.size - 1 : set.size;

  // Complexity analysis
  // Time : O(2N)
  // Space : O(N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3375. Minimum Operations to Make Array Values Equal to K - https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/?envType=daily-question&envId=2025-04-09

  console.log(minOperations([5, 2, 5, 4, 5]));
  console.log(minOperations([2, 1, 2]));
  console.log(minOperations([9, 7, 5, 3]));
};

class Problem2 {
  articulationPoints(V, edges) {
    // code here

    const adjacencyList = Array.from({ length: V }, () => new Array());

    for (let [u, v] of edges) {
      adjacencyList[u].push(v);
      adjacencyList[v].push(u);
    }

    const visited = new Array(V).fill(false);
    const insertionTime = new Array(V).fill(null);
    const lowestTime = new Array(V).fill(null);

    const artc = new Set();
    let timer = 0;

    const dfs = (u, parent) => {
      visited[u] = true;
      insertionTime[u] = lowestTime[u] = timer++;

      let childs = 0;

      for (let v of adjacencyList[u]) {
        if (v == parent) continue;
        if (visited[v]) {
          lowestTime[u] = Math.min(lowestTime[u], insertionTime[v]);
        } else {
          childs++;
          dfs(v, u);
          lowestTime[u] = Math.min(lowestTime[u], lowestTime[v]);
          if (lowestTime[v] >= insertionTime[u] && parent != -1) {
            artc.add(u); // !
          }
        }
      }

      if (childs > 1 && parent == -1) {
        artc.add(u);
      }
    };

    for (let i = 0; i < V; i++) {
      if (!visited[i]) dfs(i, -1);
    }

    return artc.size == 0 ? [-1] : Array.from(artc);

    // Complexity analysis
    // Time : O(E) + O(V + 2E)
    // Space : O(V + E) + O(3V)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Articulation Point - II - https://www.geeksforgeeks.org/problems/articulation-point2616/1

  {
    const args = [
      4,
      [
        [0, 1],
        [0, 2],
      ],
    ];
    console.log(new Problem2().articulationPoints(...args));
  }
  {
    const args = [
      5,
      [
        [0, 1],
        [1, 4],
        [4, 3],
        [4, 2],
        [2, 3],
      ],
    ];
    console.log(new Problem2().articulationPoints(...args));
  }
};

(() => {
  // Day 9 of April 2025

  p1();

  p2();
})();
