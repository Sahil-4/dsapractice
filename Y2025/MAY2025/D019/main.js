/**
 * @param {number[]} nums
 * @return {string}
 */
var triangleType = function (nums) {
  // first check if sides can form a valid triangle 
  // if not return "none"
  // else based on three sides return type of triangle 
  // SOLUTION 2 : sort the sides, 
  // if nums[0] + nums[1] <= nums[2] it cannot be a valid triangle 
  // else check sides again 
  // (it will require less number of check as the sides are sorted now) 

  const validTriangle = () => {
    return ((nums[0] + nums[1] > nums[2]) && (nums[0] + nums[2] > nums[1]) && (nums[1] + nums[2] > nums[0]));
  };

  if (validTriangle()) {
    if (nums[0] === nums[1] && nums[1] === nums[2]) {
      return "equilateral";
    } else if (nums[0] === nums[1] || nums[0] === nums[2] || nums[1] === nums[2]) {
      return "isosceles";
    } else if (nums[0] !== nums[1] || nums[0] !== nums[2] || nums[1] !== nums[2]) {
      return "scalene";
    }
  }

  return "none";

  // Complexity analysis 
  // Time : O(1) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3024. Type of Triangle - https://leetcode.com/problems/type-of-triangle/?envType=daily-question&envId=2025-05-19 

  console.log(triangleType([3, 3, 3]));
  console.log(triangleType([3, 4, 5]));
  console.log(triangleType([8, 4, 2]));
};

/*BST Node
class Node {
    constructor(x) {
        this.data = x;
        this.left = null;
        this.right = null;
    }
} */

class Problem2 {
  findPreSuc(root, key) {
    // code here 
    let sc = this.successor(root, key);
    let pd = this.predecessor(root, key);

    return [pd, sc];

    // Complexity analysis 
    // Time : O(2H) 
    // Space : O(1) 
  }

  successor(root, key) {
    let sc = null;

    while (root) {
      if (root.data <= key) {
        root = root.right;
      } else {
        sc = root;
        root = root.left;
      }
    }

    return sc;
  }

  predecessor(root, key) {
    let pd = null;

    while (root) {
      if (root.data >= key) {
        root = root.left;
      } else {
        pd = root;
        root = root.right;
      }
    }

    return pd;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Predecessor and Successor - https://www.geeksforgeeks.org/problems/predecessor-and-successor/1 

  const root = {
    data: 8,
    left: {
      data: 1,
      left: null,
      right: null,
    },
    right: {
      data: 9,
      left: null,
      right: null,
    },
  };
  const key = 1;
  console.log(new Problem2().findPreSuc(root, key));
};


(() => {
  // Day 19 of May 2025

  p1();

  p2();
})();
