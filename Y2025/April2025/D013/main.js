/**
 * @param {number} n
 * @return {number}
 */
var countGoodNumbers = function (n) {
  const MODO = BigInt(1000000007);

  const myPow = (base, exp) => {
    let result = BigInt(1);

    base = BigInt(base);
    exp = BigInt(exp);

    while (exp > 0) {
      if (exp % BigInt(2) === BigInt(1)) {
        result = (result * base) % MODO;
      }

      base = (base * base) % MODO;
      exp = exp / BigInt(2);
    }

    return result;
  };

  // even places
  const _pe = Math.floor((n + 1) / 2);
  // odd places
  const _po = Math.floor(n / 2);

  // even possibilities
  const _evpos = myPow(5, _pe);
  // odd possibilities
  const _odpos = myPow(4, _po);

  return Number((_evpos * _odpos) % MODO);

  // Complexity analysis
  // Time : O(Log(N))
  // Space : O(1) + using BigInts
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1922. Count Good Numbers - https://leetcode.com/problems/count-good-numbers/description/?envType=daily-question&envId=2025-04-13

  console.log(countGoodNumbers(1));
  console.log(countGoodNumbers(5));
  console.log(countGoodNumbers(10));
  console.log(countGoodNumbers(20));
  console.log(countGoodNumbers(100));
  console.log(countGoodNumbers(1000000000000000));
};

// User function Template for javascript

class Node {
  constructor(val, neighbors = []) {
    this.val = val;
    this.neighbors = neighbors;
  }
}

class Problem2 {
  cloneGraph(node) {
    // code here
    const nodeRefs = new Map();
    const cloneNode = new Node(node.val);
    nodeRefs.set(node.val, cloneNode);
    this.clone(node, cloneNode, nodeRefs);

    return cloneNode;

    // Complexity analysis
    // Time : O(V + 2E)
    // Space : O(V) stack
  }

  clone(node, cloneNode, nodeRefs) {
    for (let nnode of node.neighbors) {
      if (nodeRefs.get(nnode.val)) {
        const ncloneNode = nodeRefs.get(nnode.val);
        ncloneNode.neighbors.push(nodeRefs.get(nnode.val));
      } else {
        const ncloneNode = new Node(nnode.val, [cloneNode]);
        nodeRefs.set(nnode.val, ncloneNode);
        this.clone(nnode, ncloneNode, nodeRefs);
      }
    }
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Clone an Undirected Graph - https://www.geeksforgeeks.org/problems/clone-graph/1

  const node = new Node(0);
  console.log(new Problem2().cloneGraph(node));
};

(() => {
  // Day 13 of April 2025

  p1();

  p2();
})();
