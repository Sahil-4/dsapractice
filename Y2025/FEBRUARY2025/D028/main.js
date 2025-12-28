class Allocator {
  /**
   * @param {number} n
   */
  constructor(n) {
    this.blocksLength = n;
    this.blocks = new Array(n).fill(null);
  }

  /**
   * @param {number} size
   * @param {number} mID
   * @return {number}
   */
  allocate(size, mID) {
    for (let i = 0; i <= this.blocksLength - size; i++) {
      let flag = true;

      for (let j = i; j < i + size && flag; j++) {
        flag = flag && this.blocks[j] === null;
      }

      for (let j = i; j < i + size && flag; j++) {
        this.blocks[j] = mID;
      }

      if (flag) return i;
    }

    return -1;
  }

  /**
   * @param {number} mID
   * @return {number}
   */
  freeMemory(mID) {
    let unitCount = 0;

    for (let i = 0; i <= this.blocksLength; i++) {
      if (this.blocks[i] === mID) {
        this.blocks[i] = null;
        unitCount++;
      }
    }

    return unitCount;
  }
}

const p1 = () => {
  // Problem 1 : Leetcode 2502. Design Memory Allocator - https://leetcode.com/problems/design-memory-allocator/description/?envType=problem-list-v2&envId=2vp6ojv1

  const allocator = new Allocator(10);
  console.log(allocator.allocate(5, 1));
  console.log(allocator.allocate(2, 2));
  console.log(allocator.allocate(2, 3));
  console.log(allocator.freeMemory(2));
  console.log(allocator.allocate(7, 7));
  console.log(allocator.freeMemory(1));
  console.log(allocator.allocate(7, 7));
};

class NeighborSum {
  /**
   * @param {number[][]} grid
   */
  constructor(grid) {
    this.n = grid.length;
    this.grid = grid;
    this.val2RC = {};

    for (let r = 0; r < this.n; r++) {
      for (let c = 0; c < this.n; c++) {
        const val = grid[r][c];
        this.val2RC[val] = [r, c];
      }
    }
  }

  isValidIndex(r, c) {
    if (r < 0 || r >= this.n) return false;
    if (c < 0 || c >= this.n) return false;
    return true;
  }

  /**
   * @param {number} value
   * @return {number}
   */
  adjacentSum(value) {
    const delta = [
      [0, -1],
      [-1, 0],
      [0, +1],
      [+1, 0],
    ];
    const [R, C] = this.val2RC[value];

    let sum = 0;

    for (let i = 0; i < 4; i++) {
      let r = R + delta[i][0];
      let c = C + delta[i][1];

      if (this.isValidIndex(r, c)) {
        sum += this.grid[r][c];
      }
    }

    return sum;
  }

  /**
   * @param {number} value
   * @return {number}
   */
  diagonalSum(value) {
    const delta = [
      [-1, -1],
      [-1, 1],
      [+1, +1],
      [1, -1],
    ];
    const [R, C] = this.val2RC[value];

    let sum = 0;

    for (let i = 0; i < 4; i++) {
      let r = R + delta[i][0];
      let c = C + delta[i][1];

      if (this.isValidIndex(r, c)) {
        sum += this.grid[r][c];
      }
    }

    return sum;
  }
}

const p2 = () => {
  // Problem 2 : Leetcode 3242. Design Neighbor Sum Service - https://leetcode.com/problems/design-neighbor-sum-service/description/?envType=problem-list-v2&envId=2vp6ojv1

  const grid = [
    [1, 2, 0, 3],
    [4, 7, 15, 6],
    [8, 9, 10, 11],
    [12, 13, 14, 5],
  ];
  const service = new NeighborSum(grid);
  console.log(service.adjacentSum(5));
  console.log(service.diagonalSum(5));
  console.log(service.adjacentSum(15));
  console.log(service.diagonalSum(15));
  console.log(service.adjacentSum(7));
  console.log(service.diagonalSum(7));
};

function comparator(item1, item2) {
  if (item1 < item2) return -1;
  if (item1 > item2) return 1;
  return 0;
}

class SkiplistNode {
  constructor(data, next = null, down = null) {
    this.data = data;
    this.next = next;
    this.down = down; // points to the node below
  }
}

class Skiplist {
  constructor() {
    this.head = new SkiplistNode(-1); // dummy head
  }

  /**
   * @param {number} target
   * @return {boolean}
   */
  search(target) {
    let head = this.head;
    while (head) {
      while (head.next && comparator(head.next.data, target) < 0) {
        head = head.next;
      }
      if (head.next && comparator(head.next.data, target) === 0) return true;
      head = head.down; // move to lower level
    }
    return false;
  }

  /**
   * @param {number} num
   * @return {void}
   */
  add(num) {
    let stack = [];
    let head = this.head;

    while (head) {
      while (head.next && comparator(head.next.data, num) < 0) {
        head = head.next;
      }
      stack.push(head); // remember path for potential node insertion
      head = head.down; // move down
    }

    let insert = true;
    let down = null;

    while (insert && stack.length) {
      let node = stack.pop();
      node.next = new SkiplistNode(num, node.next, down);
      down = node.next; // move down for next level
      insert = Math.random() < 0.5; // 50% chance to promote
    }

    if (insert) {
      this.head = new SkiplistNode(-1, new SkiplistNode(num, null, down), this.head);
    }
  }

  /**
   * @param {number} num
   * @return {boolean}
   */
  erase(num) {
    let head = this.head;
    let found = false;

    while (head) {
      while (head.next && comparator(head.next.data, num) < 0) {
        head = head.next;
      }
      if (head.next && comparator(head.next.data, num) === 0) {
        head.next = head.next.next; // remove node
        found = true;
      }
      head = head.down; // move down
    }

    return found;
  }
}

const p3 = () => {
  // Problem 3 : Leetcode 1206. Design Skiplist - https://leetcode.com/problems/design-skiplist/description/?envType=problem-list-v2&envId=2vp6ojv1

  const skiplist = new Skiplist();
  skiplist.add(1);
  skiplist.add(5);
  skiplist.add(7);
  skiplist.add(2);
  skiplist.add(3);
  console.log(skiplist.search(0));
  console.log(skiplist.search(5));
  console.log(skiplist.search(2));
  console.log(skiplist.search(3));
  console.log(skiplist.erase(1));
  console.log(skiplist.erase(0));
  console.log(skiplist.erase(3));
  console.log(skiplist.search(0));
  console.log(skiplist.search(5));
  console.log(skiplist.search(2));
  console.log(skiplist.search(3));
};

(() => {
  // Day 28 of February 2025

  p1();

  p2();

  p3();
})();
