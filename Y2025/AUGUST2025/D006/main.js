class SegmentTree {
  constructor(N) {
    this.tree = new Array(4 * N).fill(-1);
  }

  build(i, l, r, baskets) {
    if (l === r) {
      this.tree[i] = baskets[l];
      return;
    }

    const mid = Math.floor((l + r) / 2);

    this.build(2 * i + 1, l, mid, baskets);
    this.build(2 * i + 2, mid + 1, r, baskets);

    this.tree[i] = Math.max(this.tree[2 * i + 1], this.tree[2 * i + 2]);
  }

  query(i, l, r, fruit) {
    if (this.tree[i] < fruit) return false;
    if (l === r) {
      this.tree[i] = -1;
      return true;
    }

    const mid = Math.floor((l + r) / 2);
    let check = false;

    if (this.tree[2 * i + 1] >= fruit) {
      check = this.query(2 * i + 1, l, mid, fruit);
    } else {
      check = this.query(2 * i + 2, mid + 1, r, fruit);
    }

    this.tree[i] = Math.max(this.tree[2 * i + 1], this.tree[2 * i + 2]);

    return check;
  }
}

/**
 * @param {number[]} fruits
 * @param {number[]} baskets
 * @return {number}
 */
var numOfUnplacedFruits = function (fruits, baskets) {
  const N = fruits.length;

  // number of fruits placed
  let placed = 0;

  const segmentTree = new SegmentTree(N);
  segmentTree.build(0, 0, N - 1, baskets);

  for (let i = 0; i < N; i++) {
    if (segmentTree.query(0, 0, N - 1, fruits[i])) placed++;
  }

  // total fruits - placed fruits
  return N - placed;

  // Complexity analysis
  // Time : O(N * Log(N))
  // Space : O(4N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3479. Fruits Into Baskets III - https://leetcode.com/problems/fruits-into-baskets-iii/description/?envType=daily-question&envId=2025-08-06

  console.log(numOfUnplacedFruits([4, 2, 5], [3, 5, 4]));
  console.log(numOfUnplacedFruits([3, 6, 1], [6, 4, 7]));
  console.log(numOfUnplacedFruits([35, 61], [76, 56]));
};

/**
 * @param {string} s
 * @returns {number}
 */
class Solution2 {
  romanToDecimal(s) {
    // code here
    // I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
    // XI = 11
    // 0 + 1 + 10 = 11
    // IX = 9
    // 0 + 10 - 1 = 9
    // MCMIV = 1904
    // 0 + 5 - 1 + 1000 - 100 + 1000 = 1904
    // XCVII = 97
    // 0 + 1 + 1 + 5 + 100 - 10 = 97

    const resolver = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };

    let integerValue = 0;
    integerValue += resolver[s[s.length - 1]];

    for (let i = s.length - 2; i >= 0; i--) {
      let value_i1 = resolver[s[i + 1]];
      let value_i0 = resolver[s[i + 0]];
      if (value_i1 > value_i0) value_i0 *= -1;
      integerValue += value_i0;
    }

    return integerValue;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Roman Number to Integer - https://www.geeksforgeeks.org/problems/roman-number-to-integer3201/1

  const s2 = new Solution2();
  console.log(s2.romanToDecimal("XI"));
  console.log(s2.romanToDecimal("IX"));
  console.log(s2.romanToDecimal("MCMIV"));
  console.log(s2.romanToDecimal("XCVII"));
};

(() => {
  // Day 6 of August 2025

  p1();

  p2();
})();
