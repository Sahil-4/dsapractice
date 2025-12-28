/**
 * @param {string} colors
 * @param {number[][]} edges
 * @return {number}
 */
var largestPathValue = function (colors, edges) {
  const getColorIndex = (c) => (c.charCodeAt(0) - 'a'.charCodeAt(0));

  const N = colors.length;
  const M = edges.length;

  const adj = new Map();
  const indegree = new Array(N).fill(0);

  for (let [u, v] of edges) {
    let neigh = adj.has(u) ? adj.get(u) : [];
    neigh.push(v);
    adj.set(u, neigh);
    indegree[v]++;
  }

  const queue = [];
  const t = Array.from({ length: N }, () => new Array(26).fill(0));

  for (let i = 0; i < N; i++) {
    if (indegree[i] === 0) {
      queue.push(i);
      t[i][getColorIndex(colors[i])] = 1;
    }
  }

  let answer = 0;
  let countNodes = 0;

  while (queue.length) {
    let u = queue.shift();
    let uci = getColorIndex(colors[u]);

    countNodes++;

    answer = Math.max(answer, t[u][uci]);

    for (let v of adj.get(u) || []) {
      for (let c = 0; c < 26; c++) {
        let vci = getColorIndex(colors[v]);
        t[v][c] = Math.max(t[v][c], t[u][c] + (vci == c));
      }

      if (--indegree[v] === 0) queue.push(v);
    }
  }

  return (countNodes < N) ? -1 : answer;

  // Complexity analysis 
  // Time : O(E) + O(N * 26) + O(N) + O(V + E) 
  // Space : O(N + M) + O(N) + O(E) + O(N * 26) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1857. Largest Color Value in a Directed Graph - https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/?envType=daily-question&envId=2025-05-26 

  console.log(largestPathValue("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]));
  console.log(largestPathValue("a", [[0, 0]]));
  console.log(largestPathValue("iivvvvv", [[0, 1], [1, 2], [1, 3], [2, 3], [3, 4], [2, 4], [3, 5], [1, 5], [4, 5], [5, 6]]));
};

/**
 * @param {Node} head
 * @param {number} data
 * @returns {Node}
 */

/*
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
} */

class Problem2 {
  sortedInsert(head, data) {
    // code here

    // find tail 
    let tail = head;
    while (tail.next != head) tail = tail.next;

    // create new node 
    let nnode = { data, next: null };

    // edge case 1 - insert at head 
    // if data is smaller then head.data 
    if (data < head.data) {
      nnode.next = head;
      tail.next = nnode;
      return nnode;
    }

    // edge case 2 - insert after tail 
    // if data is greater then or equal to tail.data 
    if (data >= tail.data) {
      tail.next = nnode;
      nnode.next = head;
      return head;
    }

    // insert somewhere between 
    // insert node after temp if temp.next.data is greater 
    let temp = head;
    while (temp.next.data <= data) temp = temp.next;

    nnode.next = temp.next;
    temp.next = nnode;

    return head;

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(1) + 1 Node pointer 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Insert in Sorted Circular Linked List - https://www.geeksforgeeks.org/problems/sorted-insert-for-circular-linked-list/1 

  let head = {
    data: 3,
    next: {
      data: 4,
      next: {
        data: 5,
        next: {
          data: 7,
          next: {
            data: 11,
            next: null,
          },
        },
      },
    },
  };

  head.next.next.next.next.next = head;

  const printList = (head) => {
    let out = [];
    let temp = head;
    while (temp.next !== head) {
      out.push(temp.data);
      temp = temp.next;
    }

    console.log(out.join(" "));
  };

  printList(head);
  head = new Problem2().sortedInsert(head, 0);
  printList(head);
  head = new Problem2().sortedInsert(head, 50);
  printList(head);
  head = new Problem2().sortedInsert(head, 12);
  printList(head);
  head = new Problem2().sortedInsert(head, 5);
  printList(head);
};


(() => {
  // Day 26 of May 2025

  p1();

  p2();
})();
