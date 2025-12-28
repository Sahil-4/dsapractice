/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function (nums) {
  const N = nums.length;

  for (let i = 0; i < N; i++) {
    let old_numsi = nums[nums[i]] % N;
    let new_numsi = nums[i] + N * old_numsi;
    nums[i] = new_numsi;
  }

  for (let i = 0; i < N; i++) {
    nums[i] = Math.floor(nums[i] / N);
  }

  return nums;

  // Complexity analysis 
  // Time : O(2N) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1920. Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/?envType=daily-question&envId=2025-05-06 

  console.log(buildArray([0, 2, 1, 5, 3, 4]));
  console.log(buildArray([5, 0, 1, 2, 3, 4]));
};

// User function Template for javascript

/**
 * @param {Node} root
 * @returns {number[]}
 */

/*
class Node{
    constructor(data){
        this.data = data;
        this.left = null;
        this.right = null;
    }
}
*/

class DequeNode {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class Deque {
  constructor() {
    this.head = null; // front
    this.tail = null; // back
  }

  isEmpty() {
    return this.head === null;
  }

  // Enqueue at the back
  enqueue(item) {
    const newNode = new DequeNode(item);
    if (this.isEmpty()) {
      this.head = this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
  }

  // Dequeue from the front
  dequeue() {
    if (this.isEmpty()) return null;
    const data = this.head.data;
    this.head = this.head.next;
    if (!this.head) this.tail = null; // queue became empty
    return data;
  }

  peek() {
    return this.head ? this.head.data : null;
  }
}

class Problem2 {
  leftView(root) {
    // your code here
    let output = [];

    let dq = new Deque();
    if (root) dq.enqueue(root);
    let L = 1;

    while (!dq.isEmpty()) {
      let _L = L;
      L = 0;

      output.push(dq.peek().data);

      for (let i = 0; i < _L; i++) {
        let node = dq.dequeue();

        if (node.left) {
          dq.enqueue(node.left);
          L++;
        }

        if (node.right) {
          dq.enqueue(node.right);
          L++;
        }
      }
    }

    return output;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(W) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Left View of Binary Tree - https://www.geeksforgeeks.org/problems/left-view-of-binary-tree/1 

  const root = null;
  console.log(new Problem2().leftView(root));
};

(() => {
  // Day 6 of May 2025

  p1();

  p2();
})();
