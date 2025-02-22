class Node {
  constructor(v) {
    this.val = v;
    this.next = null;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }
}

class MyLinkedList {
  constructor() {
    this.head = null;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @param {number} index
   * @return {number}
   */
  get(index) {
    let temp = this.head;

    while (temp && index--) {
      temp = temp.next;
    }

    return temp ? temp.val : -1;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

  /**
   * @param {number} val
   * @return {void}
   */
  addAtHead(val) {
    let next = null;

    if (this.head !== null) {
      next = this.head;
    }

    this.head = new Node(val);
    this.head.next = next;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @param {number} val
   * @return {void}
   */
  addAtTail(val) {
    if (this.head === null) {
      this.head = new Node(val);
      return;
    }

    let temp = this.head;

    while (temp.next != null) {
      temp = temp.next;
    }

    temp.next = new Node(val);

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

  /**
   * @param {number} index
   * @param {number} val
   * @return {void}
   */
  addAtIndex(index, val) {
    if (index === 0) {
      this.addAtHead(val);
      return;
    }

    let temp = this.head;
    while (temp && --index) {
      temp = temp.next;
    }

    if (temp) {
      const next = temp.next;
      temp.next = new Node(val);
      temp.next.next = next;
    }

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

  /**
   * @param {number} index
   * @return {void}
   */
  deleteAtIndex(index) {
    if (!this.head) return;

    if (index === 0) {
      this.head = this.head?.next;
      return;
    }

    let temp = this.head;
    while (temp && --index) {
      temp = temp.next;
    }

    if (temp && temp.next) {
      temp.next = temp.next.next;
    }

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

  print() {
    let temp = this.head;
    let out = [];

    while (temp) {
      out.push(temp.val);
      temp = temp.next;
    }

    console.log(out);
  }
}

const p1 = () => {
  // Problem 1 : Leetcode 707. Design Linked List - https://leetcode.com/problems/design-linked-list/description/?envType=problem-list-v2&envId=2vp6ojv1
  // Geeksforgeeks - https://www.geeksforgeeks.org/problems/introduction-to-linked-list/1

  const list = new MyLinkedList();
  list.print();
  list.addAtTail(0);
  list.print();
  list.addAtTail(1);
  list.print();
  list.deleteAtIndex(0);
  list.print();
};

class MyCircularDeque {
  /**
   * @param {number} k
   */
  constructor(k) {
    // init
    this.front = 0;
    this.rear = k - 1;
    this.capacity = k;
    this.count = 0;
    this.dataset = new Array(k).fill(0);
  }

  /**
   * @param {number} value
   * @return {boolean}
   */
  insertFront(value) {
    if (this.isFull()) return false;

    this.front = (this.front - 1 + this.capacity) % this.capacity;
    this.dataset[this.front] = value;
    this.count = this.count + 1;

    return true;
  }

  /**
   * @param {number} value
   * @return {boolean}
   */
  insertLast(value) {
    if (this.isFull()) return false;

    this.rear = (this.rear + 1) % this.capacity;
    this.dataset[this.rear] = value;
    this.count = this.count + 1;

    return true;
  }

  /**
   * @return {boolean}
   */
  deleteFront() {
    if (this.isEmpty()) return false;

    this.front = (this.front + 1) % this.capacity;
    this.count = this.count - 1;

    return true;
  }

  /**
   * @return {boolean}
   */
  deleteLast() {
    if (this.isEmpty()) return false;

    this.rear = (this.rear - 1 + this.capacity) % this.capacity;
    this.count = this.count - 1;

    return true;
  }

  /**
   * @return {number}
   */
  getFront() {
    return this.isEmpty() ? -1 : this.dataset[this.front];
  }

  /**
   * @return {number}
   */
  getRear() {
    return this.isEmpty() ? -1 : this.dataset[this.rear];
  }

  /**
   * @return {boolean}
   */
  isEmpty() {
    return this.count === 0;
  }

  /**
   * @return {boolean}
   */
  isFull() {
    return this.count === this.capacity;
  }

  // Complexity analysis
  // Time : O(1) except constructor
  // Space : O(1)
}

const p2 = () => {
  // Problem 2 : Leetcode 641. Design Circular Deque - https://leetcode.com/problems/design-circular-deque/description/?envType=problem-list-v2&envId=2vp6ojv1

  const obj = new MyCircularDeque(k);
  console.log(obj.insertFront(value));
  console.log(obj.insertLast(value));
  console.log(obj.deleteFront());
  console.log(obj.deleteLast());
  console.log(obj.getFront());
  console.log(obj.getRear());
  console.log(obj.isEmpty());
  console.log(obj.isFull());
};

class TrieNode {
  constructor() {
    this.list = {}; // map<char, TrieNode>
    this.ends = false; // it word ends here
    this.prefix = 0; // number of prefixes
  }
}

class Trie {
  constructor() {
    this.head = new TrieNode();
  }

  /**
   * @param {string} word
   * @return {void}
   */
  insert(word) {
    let temp = this.head;

    for (let i = 0; i < word.length; i++) {
      if (!temp.list[word[i]]) {
        temp.list[word[i]] = new TrieNode();
      }

      temp = temp.list[word[i]];
      temp.prefix += 1;
    }

    temp.ends = true;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

  /**
   * @param {string} word
   * @return {boolean}
   */
  search(word) {
    let temp = this.head;

    for (let i = 0; i < word.length; i++) {
      if (!temp.list[word[i]]) {
        return false;
      }

      temp = temp.list[word[i]];
    }

    return temp?.ends;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

  /**
   * @param {string} prefix
   * @return {boolean}
   */
  startsWith(prefix) {
    let temp = this.head;

    for (let i = 0; i < prefix.length; i++) {
      if (!temp.list[prefix[i]]) {
        return false;
      }

      temp = temp.list[prefix[i]];
    }

    return true;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
}

const p3 = () => {
  // Problem 3 : Leetcode 208. Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/description/?envType=problem-list-v2&envId=2vp6ojv1
  // Geeksforgeeks - https://www.geeksforgeeks.org/problems/trie-insert-and-search0651/1

  const trie = new Trie();
  console.log(trie.search("hello"));
  trie.insert("hello");
  console.log(trie.search("hello"));
  console.log(trie.search("hell"));
  console.log(trie.prefix("hell"));
  trie.insert("hell");
  console.log(trie.search("hell"));
  console.log(trie.prefix("hell"));
};

class MagicDictionary {
  constructor() {
    this.trie = new Trie();
  }

  /**
   * @param {string[]} dictionary
   * @return {void}
   */
  buildDict(dictionary) {
    dictionary.forEach((word) => {
      this.trie.insert(word);
    });

    // Complexity analysis
    // Time : O(N*M)
    // Space : O(1)
  }

  /**
   * @param {string} word
   * @param {Number} i
   * @param {TrieNode} node
   * @param {boolean} flag
   */
  __search__(word, i, node, flag) {
    if (i === word.length) return node.ends && flag;

    let res = false;

    for (let it = 0; it < 26 && !res; it++) {
      let ch = String.fromCharCode(97 + it);

      if (!node.list[ch]) continue;

      if (ch === word[i]) {
        res = this.__search__(word, i + 1, node.list[ch], flag);
      } else if (!flag) {
        res = this.__search__(word, i + 1, node.list[ch], true);
      }
    }

    return res;

    // Complexity analysis
    // Time : O(26 ^ len)
    // Space : O(1)
  }

  /**
   * @param {string} searchWord
   * @return {boolean}
   */
  search(searchWord) {
    return this.__search__(searchWord, 0, this.trie.head, false);

    // Complexity analysis
    // Time : O(26 ^ len)
    // Space : O(1)
  }
}

const p4 = () => {
  // Problem 4 : Leetcode 676. Implement Magic Dictionary - https://leetcode.com/problems/implement-magic-dictionary/description/?envType=problem-list-v2&envId=2vp6ojv1

  const dict = new MagicDictionary();
  dict.buildDict(["ab", "aaewfawi"]);
  console.log("ba");
};

(() => {
  // Day 22 of February 2025

  p1();

  p2();

  p3();

  p4();
})();
