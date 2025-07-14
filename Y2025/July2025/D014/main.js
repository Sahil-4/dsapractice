/**
 * Definition for singly-linked list.
 */
class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }

  getLinkedList(arr) {
    const head = new ListNode(arr[0]);

    for (let i = 1, temp = head; i < arr.length; i++) {
      temp.next = new ListNode(arr[i]);
      temp = temp.next;
    }

    return head;
  }
}

/**
 * @param {ListNode} head
 * @return {number}
 */
var getDecimalValue = function (head) {
  // traverse linked list -
  // use a stack to store bits (from nodes)
  // process stack
  // and build integer

  const power2 = [
    1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072,
    262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728,
    268435456, 536870912,
  ];

  const stack = [];
  let temp = head;
  while (temp) {
    stack.push(temp.val);
    temp = temp.next;
  }

  let decimal = 0;
  let p = 0;
  while (stack.length) {
    let bit = stack.pop();
    decimal += power2[p] * bit;
    p++;
  }

  return decimal;

  // Complexity analysis
  // Time : O(2N)
  // Space : O(N)
  // can remove extra space by reversing the input linked list inplace
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1290. Convert Binary Number in a Linked List to Integer - https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/?envType=daily-question&envId=2025-07-14

  console.log(getDecimalValue(getLinkedList([1, 0, 1])));
  console.log(getDecimalValue(getLinkedList([0])));
  console.log(getDecimalValue(getLinkedList([1])));
  console.log(getDecimalValue(getLinkedList(new Array(30).fill(1))));
  console.log(getDecimalValue(getLinkedList(new Array(30).fill(0))));
};

/**
 * @param {string} s
 * @returns {number}
 */
class Solution2 {
  cuts(s) {
    // code here

    const N = s.length;
    // const memory = new Array(N).fill(-1);
    // const mcuts = this.memoization(s, N, 0, memory);
    const mcuts = this.tabulation(s, N);
    return mcuts > N ? -1 : mcuts;
  }

  isPower5(num) {
    const power5 = new Set([
      1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625,
      1220703125,
    ]);
    return power5.has(num);
  }

  memoization(s, n, i, memory) {
    if (i >= n) return 0;

    if (memory[i] !== -1) return memory[i];

    let mcuts = n + 1;
    let num = 0;

    for (let ci = i; ci < n; ci++) {
      num = num * 2 + (s[ci] == "1");

      if (s[i] !== "0" && this.isPower5(num)) {
        let next = this.memoization(s, n, ci + 1, memory);
        mcuts = Math.min(mcuts, 1 + next);
      }
    }

    return (memory[i] = mcuts);

    // Complexity analysis
    // Time : O(N * N) ~
    // Space : O(N) stack + O(N) memory
  }

  tabulation(s, n) {
    const memory = new Array(n + 1).fill(0);

    for (let i = n - 1; i >= 0; i--) {
      let mcuts = n + 1;
      let num = 0;

      for (let ci = i; ci < n; ci++) {
        num = num * 2 + (s[ci] == "1");

        if (s[i] !== "0" && this.isPower5(num)) {
          let next = memory[ci + 1];
          mcuts = Math.min(mcuts, 1 + next);
        }
      }

      memory[i] = mcuts;
    }

    return memory[0];

    // Complexity analysis
    // Time : O(N * N)
    // Space : O(N) memory
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Cutting Binary String - https://www.geeksforgeeks.org/problems/cutting-binary-string1342/1

  const s2 = new Solution2();
  console.log(s2.cuts("101101101"));
  console.log(s2.cuts("101001"));
  console.log(s2.cuts("111111111111111111111111111111"));
  console.log(s2.cuts("000000000000000000000000000000"));
  console.log(s2.cuts("101010101010101010101010101010101010101010101010101010101010"));
};

(() => {
  // Day 14 of July 2025

  p1();

  p2();
})();
