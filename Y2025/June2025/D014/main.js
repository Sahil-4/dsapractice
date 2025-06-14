/**
 * @param {number} num
 * @return {number}
 */
var minMaxDifference = function (num) {
  // i need two numbers 
  // maxx, maximum number we can obtain by updating a digit in num to any other digit 
  // minn, minimum number we can obtain by updating a digit in num to any other digit 
  // finally return maxx - minn 
  // now find maxx, and minn 
  // maxx = to maximise the number num, we'll have to put 9 at most significant place 
  // minn = to minimize the number num, we'll have to put 0 at most significant place 
  // now whichever digit we update at these places we will store it and update all its occurrence in num for minn, and maxx 

  const getMaxx = (darr) => {
    const N = darr.length;

    let digitToUpdate = null;
    for (let i = 0; i < N; i++) {
      if (darr[i] < 9) {
        digitToUpdate = darr[i];
        break;
      }
    }

    for (let i = 0; i < N; i++) {
      if (darr[i] === digitToUpdate) {
        darr[i] = 9;
      }
    }

    return Number(darr.join(""));
  };

  const getMinn = (darr) => {
    const N = darr.length;

    let digitToUpdate = null;
    for (let i = 0; i < N; i++) {
      if (darr[i] > 0) {
        digitToUpdate = darr[i];
        break;
      }
    }

    for (let i = 0; i < N; i++) {
      if (darr[i] === digitToUpdate) {
        darr[i] = 0;
      }
    }

    return Number(darr.join(""));
  };

  const digits = String(num).split("");

  let maxx = getMaxx([...digits]);
  let minn = getMinn([...digits]);

  return (maxx - minn);

  // Complexity analysis 
  // Time : O(3N), N = length of number 
  // Space : O(2N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2566. Maximum Difference by Remapping a Digit  - https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description/?envType=daily-question&envId=2025-06-14 

  console.log(minMaxDifference(11891));
  console.log(minMaxDifference(90));
  console.log(minMaxDifference(1));
  console.log(minMaxDifference(5));
  console.log(minMaxDifference(10));
  console.log(minMaxDifference(1000));
  console.log(minMaxDifference(15545212));
  console.log(minMaxDifference(99999998));
};

/*
class Node {
    constructor(x){
        this.data=x;
        this.left=null;
        this.right=null;
    }
}
*/

/**
 * @param {Node} root
 * @return {boolean}
 */
class Problem2 {
  isSymmetric(root) {
    // Code here
    let queue = [];
    queue.push(root);

    while (queue.length) {
      let [isPalindrome, allNull] = this.checkPalindromeAndAllNull(queue);

      if (!isPalindrome) return false;
      if (allNull) break;

      let w = queue.length;
      for (let i = 0; i < w; i++) {
        let top = queue.shift();

        if (!top) {
          queue.push(null);
          queue.push(null);
        } else {
          queue.push(top.left);
          queue.push(top.right);
        }
      }
    }

    return true;

    // Complexity analysis 
    // Time : O(2^H) 
    // Space : O(W) queue space 
  }

  checkPalindromeAndAllNull(arr) {
    let flag = true;
    let i = 0;
    let j = arr.length - 1;

    while (i <= j) {
      if (arr[i]?.data !== arr[j]?.data) return [false, false];
      if (flag && (arr[i] !== null || arr[j] !== null)) flag = false;
      i++;
      j--;
    }

    return [true, flag];
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Symmetric Tree - https://www.geeksforgeeks.org/problems/symmetric-tree/1 

  const p = new Problem2();

  // const root = null;
  // const root = { data: 1, left: null, right: null };
  // const root = { data: 1, left: { data: 2, left: { data: 3, left: null, right: null }, right: null }, right: null };
  const root = { data: 1, left: { data: 2, left: null, right: null }, right: { data: 2, left: null, right: null } };

  console.log(p.isSymmetric(root));
};


(() => {
  // Day 14 of June 2025

  p1();

  p2();
})();
