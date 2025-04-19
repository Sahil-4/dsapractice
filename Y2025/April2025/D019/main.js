/**
 * @param {number[]} nums
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
var countFairPairs = function (nums, lower, upper) {
  // sorting + two pointer

  const N = nums.length;
  let count = 0;

  // sort the input
  const sortedNums = [...nums].sort((a, b) => a - b);

  const lower_bound = (e, low, high) => {
    let ans = high + 1; // default to one past end

    while (low <= high) {
      let mid = low + Math.floor((high - low) / 2);

      if (sortedNums[mid] >= e) {
        ans = mid;
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    return ans; // first index where value >= e
  };

  const upper_bound = (e, low, high) => {
    let ans = high + 1;

    while (low <= high) {
      let mid = low + Math.floor((high - low) / 2);

      if (sortedNums[mid] > e) {
        ans = mid;
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    return ans; // first index where value > e
  };

  for (let i = 0; i < N; i++) {
    const numi = sortedNums[i];

    const _first_lt_numi = lower_bound(lower - numi, i + 1, N - 1) - 1;
    const _first_gt_numi = upper_bound(upper - numi, i + 1, N - 1) - 1;

    count += _first_gt_numi - _first_lt_numi;
  }

  return count;

  // Complexity analysis
  // Time : O(N * Log(N))
  // Space : O(N) copy dataset
};

const p1 = () => {
  // Problem 1 : OTD Leetcode 2563. Count the Number of Fair PairsP - https://leetcode.com/problems/count-the-number-of-fair-pairs/description/?envType=daily-question&envId=2025-04-19

  console.log(countFairPairs([0, 1, 7, 4, 4, 5], 3, 6));
  console.log(countFairPairs([1, 7, 9, 2, 5], 11, 11));
  console.log(countFairPairs([1, 7, 9, 2, 7, 9, 2, 5], 11, 11));
};

class Node {
  constructor(prefixCount = 1, endsFlag = false) {
    this.childs = new Array(2).fill(null);
    this.prefixCount = prefixCount;
    this.ends = endsFlag;
  }

  hashFunction(char) {
    return Number(char);
  }

  getChild(char) {
    return this.childs[this.hashFunction(char)];
  }

  insertChild(char) {
    if (!this.childs[this.hashFunction(char)]) {
      this.childs[this.hashFunction(char)] = new Node();
    } else {
      this.childs[this.hashFunction(char)].prefixCount++;
    }

    return this.childs[this.hashFunction(char)];
  }
}

// User function Template for javascript
class Trie {
  T = 64;

  constructor() {
    // Implement Trie
    this.head = new Node(false, false);
  }

  insert(number) {
    // Insert number into Trie
    let pointer = this.head;

    for (let i = 31; i >= 0; i--) {
      let bit = (number >> i) & 1;
      pointer = pointer.insertChild(bit);
    }

    pointer.wordEnds = true;
  }

  maxXor(number) {
    let pointer = this.head;
    let xor = 0;

    for (let i = 31; i >= 0; i--) {
      let bit = (number >> i) & 1;

      if (pointer.getChild(!bit)) {
        // preferred
        pointer = pointer.getChild(!bit);
        xor = xor | (1 << i);
      } else {
        // in case preferred one is not available
        pointer = pointer.getChild(bit);
      }
    }

    return xor;
  }
}

// User function Template for javascript

/**
 * @param {number[]} arr
 * @return {number}
 */

class Problem2 {
  maxXOR(arr) {
    // code here
    // return this.brute(arr);

    return this.optimal(arr);
  }

  optimal(arr) {
    // using trie to store the bits

    const trie = new Trie();

    // insert
    for (let num of arr) {
      trie.insert(num);
    }

    let mxor = 0;

    for (let num of arr) {
      let xor = trie.maxXor(num);
      mxor = Math.max(mxor, xor);
    }

    return mxor;

    // Complexity analysis
    // Time : O(N * 32) or O(N * Log(N))
    // Space : O(2^32)
  }

  brute(arr) {
    let mxor = 0;

    for (let i = 0; i < arr.length; i++) {
      for (let j = i; j < arr.length; j++) {
        const num1 = arr[i];
        const num2 = arr[j];

        const xor = num1 ^ num2;
        mxor = Math.max(mxor, xor);
      }
    }

    return mxor;

    // Complexity analysis
    // Time : O(N^2)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Maximum XOR of two numbers in an array - https://www.geeksforgeeks.org/problems/maximum-xor-of-two-numbers-in-an-array/1

  console.log(new Problem2().maxXOR([25, 10, 2, 8, 5, 3]));
  console.log(new Problem2().maxXOR([1, 2, 3, 4, 5, 6, 7]));
};

(() => {
  // Day 19 of April 2025

  p1();

  p2();
})();
