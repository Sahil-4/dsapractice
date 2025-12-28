/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function (nums) {
  const hasEvenDigits = (num) => {
    let digits = 0;
    while (num >= 1) {
      num = Math.floor(num / 10);
      digits++;
    }
    return !(digits & 1);
  };

  let count = nums.reduce((acc, e) => acc + hasEvenDigits(e), 0);
  return count;

  // Complexity analysis 
  // Time : O(N * Log(i)) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1295. Find Numbers with Even Number of Digits - https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/?envType=daily-question&envId=2025-04-30 

  console.log(findNumbers([12, 345, 2, 6, 7896]));
  console.log(findNumbers([555, 901, 482, 1771]));
};


// User function Template for javascript

/**
 * @param {Node} head
 * @returns {number}
 */

/*
class Node{
    constructor(data){
        this.data = data;
        this.next = null;
    }
}
*/

class Problem2 {
  // Function to find the length of a loop in the linked list.
  countNodesinLoop(head) {
    // code here

    let slow = head;
    let fast = head;

    while (fast && fast.next) {
      slow = slow.next;
      fast = fast.next.next;

      // loop 
      if (slow == fast) break;
    }

    if (!fast || !fast.next) return 0;

    fast = fast.next;
    let len = 1;

    while (fast != slow) {
      fast = fast.next;
      len++;
    }

    return len;

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(1) + some pointers 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Find length of Loop - https://www.geeksforgeeks.org/problems/find-length-of-loop/1 

  const head = {
    data: 0,
    next: null
  };
  console.log(new Problem2().countNodesinLoop(head));
};

(() => {
  // Day 30 of April 2025

  p1();

  p2();
})();
