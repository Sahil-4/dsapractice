/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function (n) {
  const rle = (i) => {
    const digits = String(i).split("");
    const strChars = [];

    let digit = digits[0];
    let freq = 1;

    for (let index = 1; index <= digits.length; index++) {
      if (index == digits.length || digit != digits[index]) {
        strChars.push(String(freq));
        strChars.push(String(digit));

        if (index == digits.length) break;

        digit = digits[index];
        freq = 1;
      } else {
        freq++;
      }
    }

    return strChars.join("");
  };

  const recursive = (i) => {
    if (i == 1) return "1";

    const prev = recursive(i - 1);
    return rle(prev);

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) stack + O(2^N) space for strings
  };

  const iterative = () => {
    let output = "1";

    for (let i = 2; i <= n; i++) {
      output = rle(output);
    }

    return output;

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(2^N) space for strings
  };

  // return recursive(n);
  return iterative();
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 38. Count and Say - https://leetcode.com/problems/count-and-say/description/?envType=daily-question&envId=2025-04-18

  console.log(countAndSay(1));
  console.log(countAndSay(5));
  console.log(countAndSay(10));
  console.log(countAndSay(30));
};

class Node {
  constructor(prefixCount = 1, wordEndsFlag = false) {
    this.childs = new Array(64).fill(null);
    this.prefixCount = prefixCount;
    this.wordEnds = wordEndsFlag;
  }

  hashFunction(char) {
    if (char >= "a" && char <= "z") {
      return char.charCodeAt(0) - 97;
    }
    if (char >= "A" && char <= "Z") {
      return char.charCodeAt(0) - 65 + 26;
    }
    if (char >= "0" && char <= "9") {
      return char.charCodeAt(0) - 48 + 26 + 26;
    }

    return 63;
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

  insert(word) {
    // Insert word into Trie
    let pointer = this.head;

    for (let char of word) {
      pointer = pointer.insertChild(char);
    }

    pointer.wordEnds = true;
  }

  remove(word) {
    if (!this.search(word)) return false;

    // Remove word from Trie
    let pointer = this.head;

    for (let char of word) {
      pointer = pointer.getChild(char);
      pointer.prefixCount--;
    }

    pointer.wordEnds = false;

    return true;
  }

  search(word) {
    // Search word in the Trie
    let pointer = this.head;

    for (let char of word) {
      pointer = pointer.getChild(char);
      if (!pointer) return false;
    }

    return pointer.wordEnds;
  }

  isPrefix(word) {
    // Search prefix word in the Trie
    // Search word in the Trie
    let pointer = this.head;

    for (let char of word) {
      pointer = pointer.getChild(char);
      if (!pointer) return false;
    }

    return pointer.prefixCount > 0;
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Implement Trie - https://www.geeksforgeeks.org/problems/trie-insert-and-search0651/1

  const trie = new Trie();
  console.log(trie.search("hello"));
  console.log(trie.isPrefix("hello"));
  trie.insert("hello");
  console.log(trie.search("hello"));
  console.log(trie.isPrefix("hello"));
  console.log(trie.search("hell"));
  console.log(trie.isPrefix("hell"));
  console.log(trie.isPrefix("hel"));
  trie.insert("hell");
  console.log(trie.search("hello"));
  console.log(trie.isPrefix("hello"));
  console.log(trie.search("hell"));
  console.log(trie.isPrefix("hell"));
  console.log(trie.isPrefix("hel"));
};

(() => {
  // Day 18 of April 2025

  p1();

  p2();
})();
