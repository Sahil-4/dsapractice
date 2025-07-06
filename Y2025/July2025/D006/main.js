class FindSumPairs {
  /**
   * @param {number[]} nums1
   * @param {number[]} nums2
   */
  constructor(nums1, nums2) {
    this.nums1 = nums1;
    this.nums2 = nums2;
    this.nums2Map = new Map();
    for (let e of this.nums2) {
      const f = (this.nums2Map.get(e) || 0) + 1;
      this.nums2Map.set(e, f);
    }

    // Complexity analysis
    // Time : O(N + 2M)
    // Space : O(N + 2M)
  }

  /**
   * @param {number} index
   * @param {number} val
   * @return {void}
   */
  add(index, val) {
    const f1 = (this.nums2Map.get(this.nums2[index]) || 0) - 1;
    this.nums2Map.set(this.nums2[index], f1);

    this.nums2[index] += val;

    const f2 = (this.nums2Map.get(this.nums2[index]) || 0) + 1;
    this.nums2Map.set(this.nums2[index], f2);

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @param {number} tot
   * @return {number}
   */
  count(tot) {
    let count = 0;

    for (let i = 0; i < this.nums1.length; i++) {
      const need = tot - this.nums1[i];
      count += this.nums2Map.get(need) || 0;
    }

    return count;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * var obj = new FindSumPairs(nums1, nums2)
 * obj.add(index,val)
 * var param_2 = obj.count(tot)
 */

const p1 = () => {
  // Problem 1 : POTD Leetcode 1865. Finding Pairs With a Certain Sum - https://leetcode.com/problems/finding-pairs-with-a-certain-sum/description/?envType=daily-question&envId=2025-07-06

  const fsp = new FindSumPairs([1, 2, 3], [4, 5, 6]);
  console.log(fsp.count(7)); // 0
  console.log(fsp.count(8)); // 1
  console.log(fsp.count(9)); // 2
  console.log(fsp.count(10)); // 3
  fsp.add(0, 1); // nums2 becomes [5, 5, 6]
  console.log(fsp.count(7)); // 1
  console.log(fsp.count(8)); // 2
  console.log(fsp.count(9)); // 3
  console.log(fsp.count(10)); // 4
  fsp.add(1, 2); // nums2 becomes [5, 7, 6]
  console.log(fsp.count(7)); // 1
};

class Heap {
  constructor() {
    this.data = [];
  }

  push(val) {
    this.data.push(val);
    this.heapifyUp(this.data.length - 1);
  }

  pop() {
    if (this.data.length === 0) return null;

    const max = this.data[0];
    const last = this.data.pop();

    if (this.data.length > 0) {
      this.data[0] = last;
      this.heapifyDown(0);
    }

    return max;
  }

  top() {
    return this.data.length > 0 ? this.data[0] : null;
  }

  // For Max Heap - CUSTOM
  comparator(val1, val2) {
    if (val1[0] !== val2[0]) return val1[0] > val2[0];
    if (val1[1] !== val2[1]) return val1[1] < val2[1];
    if (val1[2] !== val2[2]) return val1[2] < val2[2];
    return false;
  }

  parent(i) {
    return Math.floor((i - 1) / 2);
  }

  left(i) {
    return 2 * i + 1;
  }

  right(i) {
    return 2 * i + 2;
  }

  heapifyUp(i) {
    while (i > 0) {
      const p = this.parent(i);

      if (this.comparator(this.data[i], this.data[p])) {
        [this.data[i], this.data[p]] = [this.data[p], this.data[i]];
        i = p;
      } else break;
    }
  }

  heapifyDown(i) {
    const n = this.data.length;

    while (true) {
      const l = this.left(i);
      const r = this.right(i);

      let largest = i;

      if (l < n && this.comparator(this.data[l], this.data[largest])) {
        largest = l;
      }

      if (r < n && this.comparator(this.data[r], this.data[largest])) {
        largest = r;
      }

      if (largest !== i) {
        [this.data[i], this.data[largest]] = [this.data[largest], this.data[i]];
        i = largest;
      } else break;
    }
  }

  size() {
    return this.data.length;
  }
}

class Solution2 {
  topKSumPairs(a, b, k) {
    // code here
    const N = a.length;

    const arr1 = [...a].sort((e1, e2) => e2 - e1);
    const arr2 = [...b].sort((e1, e2) => e2 - e1);

    const output = [];
    const heap = new Heap();
    const used = new Set();
    heap.push([arr1[0] + arr2[0], 0, 0]);
    used.add(`0.0`);

    while (output.length < k) {
      const [sum, i, j] = heap.pop();
      output.push(sum);

      if (i + 1 < N && !used.has(`${i + 1}.${j}`)) {
        heap.push([arr1[i + 1] + arr2[j], i + 1, j]);
        used.add(`${i + 1}.${j}`);
      }

      if (j + 1 < N && !used.has(`${i}.${j + 1}`)) {
        heap.push([arr1[i] + arr2[j + 1], i, j + 1]);
        used.add(`${i}.${j + 1}`);
      }
    }

    return output;

    // Complexity analysis
    // Time : O(2 * N) + O(2 * N * Log(N)) + O(K * Log(2K))
    // Space : O(2N) + O(2K) + O(2K)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Maximum Sum Combination - https://www.geeksforgeeks.org/problems/maximum-sum-combination/1

  const s2 = new Solution2();
  console.log(s2.topKSumPairs([1, 2, 3], [4, 5, 6], 3)); // [9, 8, 7]
  console.log(s2.topKSumPairs([10, 20, 30], [40, 50, 60], 3)); // [90, 80, 70]
  console.log(s2.topKSumPairs([1, 2, 3], [1, 2, 3], 3)); // [6, 5, 5]
};


(() => {
  // Day 6 of July 2025

  p1();

  p2();
})();
