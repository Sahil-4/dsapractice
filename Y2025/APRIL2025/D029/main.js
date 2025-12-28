/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countSubarrays = function (nums, k) {
  const N = nums.length;

  // count of sub arrays 
  let count = 0;

  // find max element 
  let maxE = Math.max(...nums);

  // freq of maxE 
  let freq = 0;

  // sliding window 
  for (let l = 0, r = 0; r < N; r++) {
    // expand 
    if (nums[r] === maxE) freq++;

    // shrink 
    while (freq >= k) {
      count += (N - r);
      if (nums[l] === maxE) freq--;
      l++;
    }
  }

  return count;

  // Complexity analysis 
  // Time : O(2N) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2962. Count Subarrays Where Max Element Appears at Least K Times - https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=daily-question&envId=2025-04-29 

  console.log(countSubarrays([1, 3, 2, 3, 3], 2));
  console.log(countSubarrays([1, 4, 2, 1], 3));
  console.log(countSubarrays([28, 5, 58, 91, 24, 91, 53, 9, 48, 85, 16, 70, 91, 91, 47, 91, 61, 4, 54, 61, 49], 1));
  console.log(countSubarrays([1, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 2));
  console.log(countSubarrays([1, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 1));
  console.log(countSubarrays([3, 3, 3, 3, 3], 3));
  console.log(countSubarrays([1, 2, 3, 4, 5], 1));
  console.log(countSubarrays([5, 5, 1, 5, 2, 5, 5], 4));
};

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

/**
 * @param {Node} head
 * @returns {Node}
 */
class Problem2 {
  segregate(head) {
    // code here
    let zeroes = new Node(0);
    let zeroes_t = zeroes;

    let ones = new Node(1);
    let ones_t = ones;

    let twos = new Node(2);
    let twos_t = twos;

    while (head) {
      const next = head.next;
      head.next = null;

      switch (head.data) {
        case 0:
          zeroes_t.next = head;
          zeroes_t = zeroes_t.next;
          break;
        case 1:
          ones_t.next = head;
          ones_t = ones_t.next;
          break;
        case 2:
          twos_t.next = head;
          twos_t = twos_t.next;
          break;
        default:
          break;
      }

      head = next;
    }

    let temp = zeroes;
    while (temp) {
      if (!temp.next) {
        if (ones.next) {
          temp.next = ones.next;
          ones.next = null;
        } else if (twos.next) {
          temp.next = twos.next;
          twos.next = null;
        }
      }

      temp = temp.next;
    }

    return zeroes.next;

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(1) + 4 extra pointers 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Sort a linked list of 0s, 1s and 2s - https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1 

  const head = {
    data: 1,
    next: {
      data: 1,
      next: null,
    }
  };
  console.log(new Problem2().segregate(head));
};

(() => {
  // Day 29 of April 2025

  p1();

  p2();
})();
