/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findKthNumber = function (n, k) {
  const count = (curr, next) => {
    let c = 0;

    while (curr <= n) {
      c += (next - curr);

      curr *= 10;
      next *= 10;

      next = Math.min(next, n + 1);
    }

    return c;
  };

  const solve = () => {
    let curr = 1;
    k -= 1;

    while (k > 0) {
      let c = count(curr, curr + 1);

      if (c <= k) {
        // skip this branch 
        curr++;
        k -= c;
      } else {
        // answer is in this branch 
        k -= 1; // skip root 
        curr *= 10; // go in depth 
      }
    }

    return curr;
  };

  return solve();

  // Complexity analysis 
  // Time : O(Log^2(N)) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 440. K-th Smallest in Lexicographical Order - https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/?envType=daily-question&envId=2025-06-09 

  console.log(findKthNumber(13, 2));
  console.log(findKthNumber(1, 1));
  console.log(findKthNumber(1000, 1000));
  console.log(findKthNumber(100000, 100000));
  console.log(findKthNumber(100000000, 100000000));
  console.log(findKthNumber(1000000000, 1000000000));
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

/**
 * @param {Node} root
 * @return {boolean}
 */

class Problem2 {
  isDeadEnd(root, low = 1, high = 3000) {
    // Code here
    if (!root) return false;
    if (!root.left && !root.right) return (low === high);

    return this.isDeadEnd(root.left, low, root.data - 1) || this.isDeadEnd(root.right, root.data + 1, high);
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks BST with Dead End - https://www.geeksforgeeks.org/problems/check-whether-bst-contains-dead-end/1 

  const p = new Problem2();
  const root = {
    data: 5,
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
  };
  console.log(p.isDeadEnd(root));
};


(() => {
  // Day 9 of June 2025

  p1();

  p2();
})();
