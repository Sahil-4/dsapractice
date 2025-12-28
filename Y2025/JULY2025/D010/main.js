/**
 * @param {number} eventTime
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @return {number}
 */
var maxFreeTime = function (eventTime, startTime, endTime) {
  const breaks = [];
  for (let i = 0, N = startTime.length; i <= N; i++) {
    if (i === 0 || i === startTime.length) {
      if (i === 0) breaks.push(startTime[0]);
      if (i === N) breaks.push(eventTime - endTime[N - 1]);
      continue;
    }
    breaks.push(startTime[i] - endTime[i - 1]);
  }

  const N = breaks.length;
  const maxFreeLeft = new Array(N).fill(0);
  const maxFreeRight = new Array(N).fill(0);

  for (let i = 1; i <= N - 1; i++) {
    maxFreeLeft[i] = Math.max(maxFreeLeft[i - 1], breaks[i - 1]);
  }

  for (let i = N - 2; i >= 0; i--) {
    maxFreeRight[i] = Math.max(maxFreeRight[i + 1], breaks[i + 1]);
  }

  let result = 0;
  for (let i = 1; i <= N - 1; i++) {
    const currEventDuration = endTime[i - 1] - startTime[i - 1];

    // case 1
    if (currEventDuration <= Math.max(maxFreeLeft[i - 1], maxFreeRight[i])) {
      result = Math.max(result, breaks[i - 1] + currEventDuration + breaks[i]);
    }

    // case 2
    result = Math.max(result, breaks[i - 1] + breaks[i]);
  }

  return result;

  // Complexity analysis
  // Time : O(4N)
  // Space : O(3N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3440. Reschedule Meetings for Maximum Free Time II - https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/description/?envType=daily-question&envId=2025-07-10

  console.log(maxFreeTime(5, [1, 3], [2, 5]));
  console.log(maxFreeTime(5, [0, 1, 2, 3, 4], [1, 2, 3, 4, 5]));
  console.log(maxFreeTime(34, [0, 17], [14, 19]));
  console.log(maxFreeTime(10, [0, 7, 9], [1, 8, 10]));
  console.log(maxFreeTime(10, [0, 3, 7, 9], [1, 4, 8, 10]));
};

class TrieNode {
  T = 27;

  constructor(prefixCount = 1, wordEndsFlag = false) {
    this.childs = new Array(this.T).fill(null);
    this.prefixCount = prefixCount;
    this.wordEnds = wordEndsFlag;
  }

  hashFunction(char) {
    if (char >= "a" && char <= "z") {
      return char.charCodeAt(0) - "a".charCodeAt(0);
    }

    return 26;
  }

  getChild(char) {
    return this.childs[this.hashFunction(char)];
  }

  insertChild(char) {
    if (!this.childs[this.hashFunction(char)]) {
      this.childs[this.hashFunction(char)] = new TrieNode();
    } else {
      this.childs[this.hashFunction(char)].prefixCount++;
    }

    return this.childs[this.hashFunction(char)];
  }
}

// User function Template for javascript
class Trie {
  T = 27;

  constructor() {
    // Implement Trie
    this.head = new TrieNode(0, false);
  }

  insert(word) {
    let ack = true;

    let pointer = this.head;

    const N = word.length;

    for (let i = 0; i < N - 1; i++) {
      if (!pointer.getChild(word[i])) ack = false;
      pointer = pointer.insertChild(word[i]);
    }

    pointer = pointer.insertChild(word[N - 1]);
    pointer.wordEnds = true;

    return ack;
  }
}

/**
 * @param {string[]} arr
 * @returns {string}
 */

class Solution2 {
  longestString(arr) {
    // code here
    // arr[] = ["ab", "a", "abc", "abd", "abda"]
    // arr[] = ["", "a", "ab", "abc", "abd", "abda"]

    const comparator = (w1, w2) => w1.length - w2.length;
    const words = [...arr].sort(comparator);

    const trie = new Trie();

    let output = "";

    for (const w of words) {
      if (trie.insert(w)) {
        if (w.length > output.length || (w.length === output.length && output.localeCompare(w) > 0))
          output = w;
      }
    }

    return output;

    // Complexity analysis
    // Time : O(N + (N * Log(N))) + O(N * WI)
    // Space : O(N) + TRIE
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Find the longest string - https://www.geeksforgeeks.org/problems/find-the-longest-string--170645/1

  const s2 = new Solution2();
  console.log(s2.longestString([["p", "pr", "pro", "probl", "pros", "process", "processor"]])); // pros
  console.log(s2.longestString(["ab", "a", "abc", "abd", "abda"])); // abda
  console.log(s2.longestString(["a", "ab", "abc", "abd", "abdaa"])); // abc
  console.log(s2.longestString(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])); // a
  console.log(s2.longestString(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "ab"])); // ab
};

(() => {
  // Day 10 of July 2025

  p1();

  p2();
})();
