/**
 * @param {number[]} digits
 * @return {number[]}
 */
var findEvenNumbers = function (digits) {
  const freq = new Array(10).fill(0);

  for (let digit of digits) freq[digit]++;

  const output = [];

  for (let h = 1; h <= 9; h++) {
    if (freq[h] === 0) continue;
    freq[h]--;
    for (let t = 0; t <= 9; t++) {
      if (freq[t] === 0) continue;
      freq[t]--;
      for (let o = 0; o <= 8; o += 2) {
        if (freq[o] === 0) continue;
        freq[o]--;

        let myint = (h * 100) + (t * 10) + (o * 1);
        output.push(myint);

        freq[o]++;
      }
      freq[t]++;
    }
    freq[h]++;
  }

  return output;

  // Complexity analysis 
  // Time : O(N) + O(9 * 10 * 8) 
  // Space : O(10) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2094. Finding 3-Digit Even Numbers - https://leetcode.com/problems/finding-3-digit-even-numbers/description/?envType=daily-question&envId=2025-05-12 

  console.log(findEvenNumbers([2, 1, 3, 0]));
  console.log(findEvenNumbers([2, 2, 8, 8, 2]));
  console.log(findEvenNumbers([3, 7, 5]));
};

class MinHeap {
  constructor() {
    this.heap = [];
  }

  getParentIndex(i) {
    return Math.floor((i - 1) / 2);
  }

  getLeftChildIndex(i) {
    return 2 * i + 1;
  }

  getRightChildIndex(i) {
    return 2 * i + 2;
  }

  hasParent(i) {
    return this.getParentIndex(i) >= 0;
  }

  hasLeftChild(i) {
    return this.getLeftChildIndex(i) < this.heap.length;
  }

  hasRightChild(i) {
    return this.getRightChildIndex(i) < this.heap.length;
  }

  getParent(i) {
    return this.heap[this.getParentIndex(i)];
  }

  getLeftChild(i) {
    return this.heap[this.getLeftChildIndex(i)];
  }

  getRightChild(i) {
    return this.heap[this.getRightChildIndex(i)];
  }

  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }

  peek() {
    if (this.heap.length === 0) return null;
    return this.heap[0];
  }

  insert(item) {
    this.heap.push(item);
    this.heapifyUp();
  }

  heapifyUp() {
    let index = this.heap.length - 1;
    while (this.hasParent(index)) {
      const parent = this.getParent(index);
      const current = this.heap[index];
      if (parent[0] > current[0] || (parent[0] === current[0] && parent[1] > current[1])) {
        this.swap(index, this.getParentIndex(index));
        index = this.getParentIndex(index);
      } else {
        break;
      }
    }
  }

  extractMin() {
    if (this.heap.length === 0) return null;
    if (this.heap.length === 1) return this.heap.pop();
    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.heapifyDown();
    return min;
  }

  heapifyDown() {
    let index = 0;
    while (this.hasLeftChild(index)) {
      let smallerChildIndex = this.getLeftChildIndex(index);
      if (this.hasRightChild(index)) {
        const leftChild = this.getLeftChild(index);
        const rightChild = this.getRightChild(index);
        if (rightChild[0] < leftChild[0] || (rightChild[0] === leftChild[0] && rightChild[1] < leftChild[1])) {
          smallerChildIndex = this.getRightChildIndex(index);
        }
      }

      const current = this.heap[index];
      const smallerChild = this.heap[smallerChildIndex];
      if (current[0] > smallerChild[0] || (current[0] === smallerChild[0] && current[1] > smallerChild[1])) {
        this.swap(index, smallerChildIndex);
        index = smallerChildIndex;
      } else {
        break;
      }
    }
  }

  size() {
    return this.heap.length;
  }

  isEmpty() {
    return this.heap.length === 0;
  }
}

// User function Template for javascript

class Problem2 {
  mostBooked(n, meetings) {
    // code here

    // return this.brute(n, meetings);

    return this.optimal(n, meetings);
  }

  optimal(n, meetings) {
    // sort based on start time 
    meetings.sort((a, b) => {
      return (a[0] != b[0]) ? a[0] - b[0] : a[1] - b[1];
    });

    // rooms, and meetings hosted in it (count) 
    const roomMeetingsCount = new Array(n).fill(0);

    // free rooms 
    const availableRooms = new MinHeap();

    // occupied rooms [endT, room]
    const usedRooms = new MinHeap();

    for (let r = 0; r < n; r++) availableRooms.insert([0, r]);

    for (let [startI, endI] of meetings) {
      // look for best room - free or will free till i start or least delay 

      // room which have been freed before this meeting 
      while (!usedRooms.isEmpty() && usedRooms.peek()[0] <= startI) {
        const [et, ri] = usedRooms.extractMin();
        availableRooms.insert([0, ri]);
      }

      if (!availableRooms.isEmpty()) {
        // available room with smallest number 
        const [_, ri] = availableRooms.extractMin();
        usedRooms.insert([endI, ri]);
        roomMeetingsCount[ri]++;
      } else {
        // (or end time if not available) 
        const [et, ri] = usedRooms.extractMin();
        usedRooms.insert([et + (endI - startI), ri]);
        roomMeetingsCount[ri]++;
      }
    }

    return roomMeetingsCount.reduce(([c, i], ee, ei) => {
      return (ee > c) ? [ee, ei] : [c, i];
    }, [0, 0])[1];
  }

  brute(n, meetings) {
    // sort based on start time 
    meetings.sort((a, b) => {
      if (a[0] != b[0]) return a[0] - b[0];
      return a[1] - b[1];
    });

    // rooms, and meetings hosted in it (count) 
    const roomMeetingsCount = new Array(n).fill(0);

    // time when room will free 
    const roomFreeTime = new Array(n).fill(0);

    for (let [startI, endI] of meetings) {
      // look for best room - free or will free till i start or least delay 
      let flag = false;
      let ri = 0;

      for (let r = 0; r < n; r++) {
        if (roomFreeTime[r] <= startI) {
          flag = true;
          roomFreeTime[r] = endI;
          roomMeetingsCount[r]++;
          break;
        }

        if (roomFreeTime[r] < roomFreeTime[ri]) {
          ri = r;
        }
      }

      if (!flag) {
        roomFreeTime[ri] += (endI - startI);
        roomMeetingsCount[ri]++;
      }
    }

    return roomMeetingsCount.reduce(([c, i], ee, ei) => {
      return (ee > c) ? [ee, ei] : [c, i];
    }, [0, 0])[1];
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Meeting Rooms III - https://www.geeksforgeeks.org/problems/meeting-rooms-iii/1 

  console.log(new Problem2().mostBooked(2, [[0, 6], [2, 3], [3, 7], [4, 8], [6, 8]]));
  console.log(new Problem2().mostBooked(4, [[0, 8], [1, 4], [3, 4], [2, 3]]));
};

(() => {
  // Day 12 of May 2025

  p1();

  p2();
})();
