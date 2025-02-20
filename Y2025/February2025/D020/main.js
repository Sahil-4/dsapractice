class MyStack {
  q1 = [];
  tope = null;

  /**
   * @param {number} x
   * @return {void}
   */
  push(x) {
    // push into queue
    this.q1.push(x);

    // update top element
    this.tope = x;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @return {number}
   */
  pop() {
    const val = this.tope;
    const qLength = this.q1.length;

    for (let i = 1; i < qLength; i++) {
      let v = this.q1.shift();
      this.q1.push(v);
      this.tope = v;
    }

    this.q1.shift();

    return val;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

  /**
   * @return {number}
   */
  top() {
    return this.tope;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @return {boolean}
   */
  empty() {
    // just check is q1 is empty
    return !this.q1.length;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }
}

const p1 = () => {
  // Problem 1 : Leetcode 225. Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/description/?envType=problem-list-v2&envId=2vp6ojv1
  // Geeksforgeeks - https://www.geeksforgeeks.org/problems/stack-using-two-queues/1

  const stack = new MyStack();
  stack.push(1);
  console.log(stack.top());
  console.log(stack.pop());
  stack.push(2);
  stack.push(3);
  console.log(stack.top());
  stack.push(4);
  stack.push(5);
  console.log(stack.pop());
  console.log(stack.pop());
  console.log(stack.pop());
};

class MyQueue {
  constructor() {
    this.s1 = [];
    this.s2 = [];
    this.front = -1;
  }

  /**
   * @param {number} x
   * @return {void}
   */
  push(x) {
    this.s1.push(x);
    if (this.front === -1) this.front = x;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @return {number}
   */
  pop() {
    const ffront = this.front;

    while (this.s1.length) {
      let e = this.s1.pop();
      if (this.s1.length) {
        this.front = e;
        this.s2.push(e);
      }
    }

    while (this.s2.length) {
      this.s1.push(this.s2.pop());
    }

    if (!this.s1.length) {
      this.front = -1;
    }

    return ffront;

    // Complexity analysis
    // Time : O(2N)
    // Space : O(1)
  }

  /**
   * @return {number}
   */
  peek() {
    return this.front;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @return {boolean}
   */
  empty() {
    return !this.s1.length;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : Leetcode 232. Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/description/?envType=problem-list-v2&envId=2vp6ojv1
  // Geeksforgeeks - https://www.geeksforgeeks.org/problems/queue-using-stack/1

  const que = new MyQueue();
  console.log(que.empty());
  console.log(que.peek());
  console.log(que.pop());
  que.push(1);
  console.log(que.empty());
  console.log(que.peek());
  console.log(que.pop());
  console.log(que.empty());
  que.push(2);
  que.push(3);
  que.push(4);
  console.log(que.empty());
  console.log(que.peek());
  console.log(que.pop());
  console.log(que.pop());
  console.log(que.peek());
  console.log(que.pop());
};

class MyHashSet {
  LF = 1000;

  getHash(key) {
    return key % this.LF;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  init() {
    // initilise keyset
    for (let i = 0; i < this.LF; i++) this.keyset[i] = [];

    // Complexity analysis
    // Time : O(LF)
    // Space : O(1)
  }

  constructor() {
    this.keyset = new Array(this.LF);
    this.init();

    // Complexity analysis
    // Time : O(LF)
    // Space : O(1)
  }

  /**
   * @param {number} key
   * @return {void}
   */
  add(key) {
    const index = this.getHash(key);
    this.keyset[index].push(key);

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @param {number} key
   * @return {void}
   */
  remove(key) {
    const index = this.getHash(key);
    this.keyset[index] = this.keyset[index].filter((k) => k !== key);

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

  /**
   * @param {number} key
   * @return {boolean}
   */
  contains(key) {
    const index = this.getHash(key);
    return this.keyset[index].reduce((acc, k) => acc || k === key, false);

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
}

const p3 = () => {
  // Problem 3 : Leetcode 705. Design HashSet - https://leetcode.com/problems/design-hashset/?envType=problem-list-v2&envId=2vp6ojv1

  const hset = new MyHashSet();
  console.log(hset.contains(5));
  console.log(hset.contains(4));
  hset.add(4);
  console.log(hset.contains(4));
  hset.remove(4);
  console.log(hset.contains(4));
  console.log(hset.contains(5));
  hset.add(5);
  console.log(hset.contains(5));
};

(() => {
  /// Day 20 of February
  // Started with Design Problems - leetcode.com/problem-list/2vp6ojv1/

  p1();

  p2();

  p3();
})();
