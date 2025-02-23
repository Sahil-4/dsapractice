class LRUCache {
  /**
   * @param {number} capacity
   */
  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
  }

  /**
   * @param {number} key
   * @return {number}
   */
  get(key) {
    if (!this.cache.has(key)) return -1;

    this.put(key, this.cache.get(key));

    return this.cache.get(key);
  }

  /**
   * @param {number} key
   * @param {number} value
   * @return {void}
   */
  put(key, value) {
    if (this.cache.has(key)) {
      this.cache.delete(key);
    }

    this.cache.set(key, value);

    if (this.cache.size > this.capacity) {
      this.cache.delete(this.cache.keys().next().value);
    }
  }
}

const p1 = () => {
  // Problem 1 : Leetcode 146. LRU Cache - https://leetcode.com/problems/lru-cache/description/?envType=problem-list-v2&envId=2vp6ojv1
  // Geeksforgeeks - https://www.geeksforgeeks.org/problems/lru-cache/1

  const cache = new LRUCache(2);
  console.log(cache.get(1));
  cache.set(1, 1);
  console.log(cache.get(1));
  cache.set(2, 2);
  console.log(cache.get(1));
  console.log(cache.get(2));
  cache.set(1, 100);
  console.log(cache.get(1));
  console.log(cache.get(2));
};

class ListNode {
  constructor(key, value) {
    this.key = key;
    this.val = value;
    this.next = this.prev = null;
    this.freq = 1;
  }
}

class LinkedList {
  constructor() {
    this.head = new ListNode(null, null);
    this.tail = new ListNode(null, null);
    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  insertHead(node) {
    node.prev = this.head;
    node.next = this.head.next;
    this.head.next.prev = node;
    this.head.next = node;
  }

  removeNode(node) {
    let prev = node.prev;
    let next = node.next;
    prev.next = next;
    next.prev = prev;
  }

  removeTail() {
    let node = this.tail.prev;
    this.removeNode(node);
    return node.key;
  }

  isEmpty() {
    return this.head.next.val === null;
  }
}

class LFUCache {
  /**
   * @param {number} capacity
   */
  constructor(capacity) {
    this.capacity = capacity; // max capacity of Cache
    this.currentSize = 0; // currently present keys
    this.leastFreq = 0; // freq of least used key
    this.nodeHash = new Map(); // store key -> value
    this.freqHash = new Map(); // store freq -> LinkedList
  }

  evict() {
    // evict least frequently used key
    let tailKey = this.freqHash.get(this.leastFreq).removeTail();
    this.nodeHash.delete(tailKey);
    this.currentSize--;
  }

  /**
   * @param {number} key
   * @return {number}
   */
  get(key) {
    let node = this.nodeHash.get(key);

    if (!node) return -1;

    this.freqHash.get(node.freq).removeNode(node);

    if (node.freq === this.leastFreq && this.freqHash.get(node.freq).isEmpty()) {
      this.leastFreq++;
    }

    node.freq++;

    if (!this.freqHash.get(node.freq)) {
      this.freqHash.set(node.freq, new LinkedList());
    }

    this.freqHash.get(node.freq).insertHead(node);

    return node.val;
  }

  /**
   * @param {number} key
   * @param {number} value
   * @return {void}
   */
  put(key, value) {
    let node = this.nodeHash.get(key);
    if (!node) {
      // new Node { key, value }

      this.currentSize++;

      if (this.currentSize > this.capacity) {
        this.evict();
      }

      if (!this.freqHash.get(1)) {
        this.freqHash.set(1, new LinkedList());
      }

      let nnode = new ListNode(key, value);
      this.freqHash.get(1).insertHead(nnode);
      this.nodeHash.set(key, nnode);

      this.leastFreq = 1;
    } else {
      // Node already exists

      this.freqHash.get(node.freq).removeNode(node);

      if (node.freq === this.leastFreq && this.freqHash.get(node.freq).isEmpty()) {
        this.leastFreq++;
      }

      node.val = value;
      node.freq++;

      if (!this.freqHash.get(node.freq)) {
        this.freqHash.set(node.freq, new LinkedList());
      }

      this.freqHash.get(node.freq).insertHead(node);
    }
  }
}

const p2 = () => {
  // Problem 2 : Leetcode 460. LFU Cache - https://leetcode.com/problems/lfu-cache/description/?envType=problem-list-v2&envId=2vp6ojv1
  // Geeksforgeeks - https://www.geeksforgeeks.org/problems/lfu-cache-1665050355/0

  const cache = new LFUCache(2);
  console.log(cache.get(5));
  cache.put(5, 4);
  cache.put(5, 5);
  cache.put(1, 1);
  cache.put(3, 3);
  console.log(cache.get(5));
  console.log(cache.get(1));
  console.log(cache.get(3));
};

/**
 * The rand7() API is already defined for you.
 * var rand7 = function() {}
 * @return {number} a random integer in the range 1 to 7
 */
const rand10 = () => {
  // Actual Problem : uniformly generate random number in range [1, 10]
  // using rand7() given uniformly random number in range [1, 7]

  let cell = 41;
  while (cell > 40) cell = (rand7() - 1) * 7 + rand7();

  return ((cell - 1) % 10) + 1;
};

const p3 = () => {
  // Problem 3 : Leetcode 470. Implement Rand10() Using Rand7() - https://leetcode.com/problems/implement-rand10-using-rand7/description/?envType=problem-list-v2&envId=2vp6ojv1

  for (let i = 0; i < 10; i++) {
    console.log(rand10());
  }
};

(() => {
  // Day 23 of February 2025

  p1();

  p2();

  p3();
})();
