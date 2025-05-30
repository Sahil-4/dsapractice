/**
 * @param {number[]} edges
 * @param {number} node1
 * @param {number} node2
 * @return {number}
 */
var closestMeetingNode = function (edges, node1, node2) {
  // Approach : 
  // build distance arrays with src = [node1, node2] - use edges only as there is at max one outgoing edge 
  // store distance in distance array d1[i] = di, to reach ith node from node 1 it takes di steps 
  // init answer with INT MAX 
  // go to every node check if its reachable by both node1 and node2 
  // if no then continue 
  // else take max out of d1[i], d2[i] 
  // and update answer accordingly 

  const t = Number.MAX_SAFE_INTEGER;
  const N = edges.length; // number of nodes 

  // get distance from u to all other nodes 
  const getDistance = (u) => {
    const d = new Array(N).fill(t);
    const visited = new Array(N).fill(false);

    d[u] = 0;
    visited[u] = true;

    let c = u;

    while (true) {
      let p = c;
      c = edges[c];

      if (c === -1 || visited[c]) break;

      visited[c] = true;
      d[c] = d[p] + 1;
    }

    return d;
  };

  const d1 = getDistance(node1); // distance from node1 to all 
  const d2 = getDistance(node2); // distance from node2 to all 

  let output = [-1, t]; // [node, dist] 

  // go to each node 
  for (let i = 0; i < N; i++) {
    // if node1 and node2 any one can not reach to this node
    if (d1[i] === t || d2[i] === t) continue;

    // get max difference from node1 path and node2 path 
    let md = Math.max(d1[i], d2[i]);

    // update answer 
    if ((output[1] > md) || (output[1] === md && output[0] > i)) {
      output = [i, md];
    }
  }

  return output[0];

  // Complexity analysis 
  // Time : O(3N) build distance arrays then build answer 
  // Space : O(3N) distance arrays + visited array 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2359. Find Closest Node to Given Two Nodes  - https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/?envType=daily-question&envId=2025-05-30 

  console.log(closestMeetingNode([2, 2, 3, -1], 0, 1));
  console.log(closestMeetingNode([1, 2, -1], 0, 2));
};

/*
class Node{
    constructor(data){
        this.data = data;
        this.left = null;
        this.right = null;
    }
} */

/**
 * @param {Node} root
 * @param {number} k
 * @return {number}
 */

class Problem2 {
  findMaxFork(root, k) {
    // code here

    let out = -1;
    let temp = root;

    while (!!temp) {
      if (temp.data <= k) {
        out = Math.max(out, temp.data);
        temp = temp.right;
      } else {
        temp = temp.left;
      }
    }

    return out;

    // Complexity analysis 
    // Time : O(H) 
    // Space : O(1) + extra pointer 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Closest Neighbour in BST - https://www.geeksforgeeks.org/problems/closest-neighbor-in-bst/1 

  const root = {
    data: 10,
    left: {
      data: 7,
      left: {
        data: 2,
        left: null,
        right: null,
      },
      right: {
        data: 8,
        left: null,
        right: null,
      },
    },
    right: {
      data: 15,
      left: {
        data: 11,
        left: null,
        right: null,
      },
      right: {
        data: 16,
        left: null,
        right: null,
      },
    },
  };
  const k = 14;
  // const k = 4;
  // const k = 1;
  console.log(new Problem2().findMaxFork(root, k));
};

(() => {
  // Day 30 of May 2025

  p1();

  p2();
})();
