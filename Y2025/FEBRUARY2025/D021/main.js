class MyHashMap {
  // Node { key, value };
  // dataset [ { hashIndex: Node[] } ];

  LF = 1001;

  constructor() {
    this.dataset = new Array(this.LF);

    // Complexity analysis
    // Time : O(LF) LF = Load factor (1001)
    // Space : O(1)
  }

  getHash(key) {
    return key % this.LF;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @param {number} key
   * @param {number} value
   * @return {void}
   */
  put(key, value) {
    const index = this.getHash(key);

    this.__remove__(index, key);

    if (!this.dataset[index]) this.dataset[index] = [];

    this.dataset[index].push({ key, value });

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @param {number} key
   * @return {number}
   */
  get(key) {
    const index = this.getHash(key);

    if (!this.dataset[index]) return -1;

    return this.dataset[index].reduce((out, node) => {
      return node.key === key ? node.value : out;
    }, -1);

    // Complexity analysis
    // Time : O(K) K = total nodes in dataset[index]
    // Space : O(1)
  }

  /**
   * @param {number} key
   * @return {void}
   */
  remove(key) {
    const index = this.getHash(key);
    this.__remove__(index, key);

    // Complexity analysis
    // Time : O(K) K = total nodes in dataset[index]
    // Space : O(1)
  }

  /**
   * @param {number} index
   * @param {number} key
   * @return {void}
   */
  __remove__(index, key) {
    if (!this.dataset[index]) return;

    this.dataset[index] = this.dataset[index].filter((node) => {
      if (node.key !== key) return node;
    });

    // Complexity analysis
    // Time : O(K) K = total nodes in dataset[index]
    // Space : O(1)
  }
}

const p1 = () => {
  // Problem 1 : Leetcode 706. Design HashMap - https://leetcode.com/problems/design-hashmap/description/?envType=problem-list-v2&envId=2vp6ojv1
  // Geeksforgeeks - https://www.geeksforgeeks.org/problems/design-hashmap/1

  const hmap = new MyHashMap();
  console.log(hmap.get(1));
  hmap.put(1, 1);
  console.log(hmap.get(1));
  hmap.put(1, 100);
  console.log(hmap.get(1));
  hmap.remove(1);
  console.log(hmap.get(1));
};

class Bitset {
  /**
   * @param {number} size
   */
  constructor(size) {
    this.bitsArray = new Array(size).fill(0);
    this.flipped = false;
    this.onesCount = 0;
    this.tsize = size;

    // Complexity analysis
    // Time : O(N) N = size
    // Space : O(1)
  }

  /**
   * @param {number} index
   * @return {void}
   */
  fix(index) {
    if (!!this.flipped === !!this.bitsArray[index]) {
      this.onesCount++;
    }
    this.bitsArray[index] = this.flipped ? 0 : 1;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @param {number} index
   * @return {void}
   */
  unfix(index) {
    if (!!this.bitsArray[index] !== !!this.flipped) {
      this.onesCount--;
    }
    this.bitsArray[index] = this.flipped ? 1 : 0;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @return {void}
   */
  flip() {
    this.onesCount = this.tsize - this.onesCount;
    this.flipped = !this.flipped;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @return {boolean}
   */
  all() {
    return this.onesCount === this.tsize;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @return {boolean}
   */
  one() {
    return this.onesCount >= 1;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @return {number}
   */
  count() {
    return this.onesCount;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @return {string}
   */
  toString() {
    return this.bitsArray.reduce((str, bit) => {
      return str + Number(this.flipped ? !bit : bit);
    }, "");

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : Leetcode 2166. Design Bitset - https://leetcode.com/problems/design-bitset/description/?envType=problem-list-v2&envId=2vp6ojv1

  const bitset = new Bitset(5);
  console.log(bitset.toString());
  bitset.fix(3);
  console.log(bitset.toString());
  bitset.flip();
  console.log(bitset.toString());
  bitset.fix(3);
  console.log(bitset.toString());
  bitset.count();
  console.log(bitset.toString());
};

class Node {
  constructor(val, next) {
    this.val = val;
    this.next = next;
  }
}

class OrderedStream {
  /**
   * @param {number} n
   */
  constructor(t) {
    this.head = new Node(-1);
    this.t = t;
    this.done = 0;

    let temp = this.head;
    while (t--) {
      temp.next = new Node(-1);
      temp = temp.next;
    }

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

  insertAt(value, index) {
    let temp = this.head;
    index = index - this.done;

    for (let i = 1; i <= index; i++) temp = temp.next;
    temp.val = value;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

  getOutput() {
    let temp = this.head;
    let output = [];

    while (temp.next && temp.next.val != -1) {
      temp = temp.next;
      output.push(temp.val);
    }

    this.head = temp;
    this.done += output.length;

    return output;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

  /**
   * @param {number} idKey
   * @param {string} value
   * @return {string[]}
   */
  insert(idKey, value) {
    this.insertAt(value, idKey);
    return this.getOutput();

    // Complexity analysis
    // Time : O(2N)
    // Space : O(1)
  }

  // All keys which are returned will be removed for saving memory
  // and also look up time
}

const p3 = () => {
  // Problem 3 : Leetcode 1656. Design an Ordered Stream - https://leetcode.com/problems/design-an-ordered-stream/description/?envType=problem-list-v2&envId=2vp6ojv1

  const stream = OrderedStream(5);
  console.log(stream.insert(3, "ccccc"));
  console.log(stream.insert(5, "eeeee"));
  console.log(stream.insert(2, "bbbbb"));
  console.log(stream.insert(1, "aaaaa"));
  console.log(stream.insert(7, "ggggg"));
  console.log(stream.insert(4, "ddddd"));
  console.log(stream.insert(6, "fffff"));
};

(() => {
  // Day 21 of February 2025

  p1();

  p2();

  p3();
})();
