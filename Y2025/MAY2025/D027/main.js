/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var differenceOfSums = function (n, m) {
  // Example Test Case 
  // n = 10, m = 3 
  // 1 2 3 4 5 6 7 8 9 10 - total numbers 
  // 1 2 4 5 7 8 10 - not divisible by m 
  // 3 6 9 - divisible by m 
  // Observation 
  // its Arithmetic progression problem 
  // find tsum = sum(1, ..., n) 
  // num2 = sum(m, 2m, ..., xm) 
  // num1 = tsum - num2 
  // output = num1 - num2 
  // sum of n terms in AP sn = (N/2) * ((2*A) + ((N-1) * D)) 

  // sum of first n N 
  let tsum = ((n * (n + 1)) / 2);

  // sum of series m, 2m, ..., xm, xm <= n 
  let x = Math.floor(n / m); // we have x terms 
  let num2 = (x / 2) * ((2 * m) + ((x - 1) * m));

  let num1 = tsum - num2;

  return num1 - num2;

  // Complexity analysis 
  // Time : O(1) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2894. Divisible and Non-divisible Sums Difference - https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/?envType=daily-question&envId=2025-05-27 

  console.log(differenceOfSums(10, 3));
  console.log(differenceOfSums(5, 6));
  console.log(differenceOfSums(5, 1));
};

/**
 * @param {number[]} preorder
 * @returns {number[]}
 */

class Problem2 {
  leafNodes(preorder) {
    // code here
    this.leafs = [];
    this.index = 0;
    this.preorder = preorder;

    this.getLeafs(0, 1001);

    return this.leafs;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) + O(N) stack 
  }

  getLeafs(lowerBound, upperBound) {
    if (this.index >= this.preorder.length) return;

    let sroot = this.preorder[this.index];

    if (sroot <= lowerBound || sroot >= upperBound) return;

    this.index++; // move index 

    const savedIndex = this.index; // before left and right 

    this.getLeafs(lowerBound, sroot);
    const leftIndex = this.index;

    this.getLeafs(sroot, upperBound);
    const rightIndex = this.index;

    // if there was not child to process for left and right 
    if (leftIndex === savedIndex && rightIndex === savedIndex) {
      this.leafs.push(sroot);
    }
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Print leaf nodes from preorder traversal of BST - https://www.geeksforgeeks.org/problems/print-leaf-nodes-from-preorder-traversal-of-bst2657/1 

  console.log(new Problem2().leafNodes([5, 2, 10]));
  console.log(new Problem2().leafNodes([4, 2, 1, 3, 6, 5]));
  console.log(new Problem2().leafNodes([8, 2, 5, 10, 12]));
};


(() => {
  // Day 27 of May 2025

  p1();

  p2();
})();
