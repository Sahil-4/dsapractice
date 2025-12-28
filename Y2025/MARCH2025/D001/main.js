/**
 * @param {number[]} nums
 * @return {number[]}
 */
const applyOperations = (nums) => {
  let output = [...nums];

  // operation 1 : double if consecutive elements are equal
  for (let i = 1; i < output.length; i++) {
    if (output[i - 1] == output[i]) {
      output[i - 1] = output[i - 1] << 1;
      output[i] = 0;
    }
  }

  // operation 2 : move zeroes to back
  // move non zeroes to left
  let p = 0;
  for (let i = 0; i < output.length; i++) {
    if (output[i] != 0) {
      output[p++] = output[i];
    }
  }
  // move zeroes to right
  for (p; p < output.length; p++) {
    output[p] = 0;
  }

  return output;

  // Complexity analysis
  // Time : O(2N)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2460. Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/description/?envType=daily-question&envId=2025-03-01

  console.log(applyOperations([1, 2, 2, 1, 1, 0]));
  console.log(applyOperations([0, 1]));
};

const decodedString = (s) => {
  // code here
  let slen = s.length;

  let numberStack = [];
  let stringStack = [];

  let curStr = "";
  let curNum = 0;

  for (let char of s) {
    if (!isNaN(char)) {
      curNum = curNum * 10 + Number(char);
    } else if (char == "[") {
      numberStack.push(curNum);
      stringStack.push(curStr);
      curStr = "";
      curNum = 0;
    } else if (char == "]") {
      let n = numberStack.pop();
      let str = stringStack.pop();
      curStr = str + curStr.repeat(n);
    } else {
      curStr += char;
    }
  }

  return curStr;
};

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Decode the string - https://www.geeksforgeeks.org/problems/decode-the-string2444/1

  console.log(decodedString("3[b2[ca]]"));
  console.log(decodedString("5[12[AC]]"));
};

(() => {
  // Day 1 of March
  // Started with POTDs

  p1();

  p2();
})();
