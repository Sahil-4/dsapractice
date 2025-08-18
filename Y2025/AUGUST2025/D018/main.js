/**
 * @param {number[]} cards
 * @return {boolean}
 */
var judgePoint24 = function (cards) {
  const isValid4 = ([a, b, c, d]) => {
    if (
      isValid3([a + b, c, d]) ||
      isValid3([a - b, c, d]) ||
      isValid3([a * b, c, d]) ||
      isValid3([a / b, c, d])
    )
      return true;
    if (
      isValid3([a, b + c, d]) ||
      isValid3([a, b - c, d]) ||
      isValid3([a, b * c, d]) ||
      isValid3([a, b / c, d])
    )
      return true;
    if (
      isValid3([a, b, c + d]) ||
      isValid3([a, b, c - d]) ||
      isValid3([a, b, c * d]) ||
      isValid3([a, b, c / d])
    )
      return true;
    return false;
  };

  const isValid3 = ([a, b, c]) => {
    if (
      isValid2([a + b, c]) ||
      isValid2([a - b, c]) ||
      isValid2([a * b, c]) ||
      isValid2([a / b, c])
    )
      return true;
    if (
      isValid2([a, b + c]) ||
      isValid2([a, b - c]) ||
      isValid2([a, b * c]) ||
      isValid2([a, b / c])
    )
      return true;
    return false;
  };

  const isValid2 = ([a, b]) => {
    return isValid1([a + b]) || isValid1([a - b]) || isValid1([a * b]) || isValid1([a / b]);
  };

  const isValid1 = ([a]) => {
    return Math.abs(a - 24.0) < 1e-6;
  };

  for (let ai = 0; ai < 4; ai++) {
    for (let bi = 0; bi < 4; bi++) {
      if (ai == bi) continue;
      for (let ci = 0; ci < 4; ci++) {
        if (ai == ci || bi == ci) continue;
        for (let di = 0; di < 4; di++) {
          if (ai == di || bi == di || ci == di) continue;
          if (isValid4([cards[ai], cards[bi], cards[ci], cards[di]])) return true;
        }
      }
    }
  }

  return false;
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 679. 24 Game - https://leetcode.com/problems/24-game/?envType=daily-question&envId=2025-08-18

  console.log(judgePoint24([4, 1, 8, 7]));
  console.log(judgePoint24([1, 2, 1, 2]));
  console.log(judgePoint24([3, 3, 8, 8]));
};

/**
 * @param {number[]} citations
 * @returns {number}
 */
class Solution2 {
  brute(citations) {
    // there are h papers with h citations
    // if h is 1 then there is 1 paper with citations 1
    // if h is 2 then there are 2 papers with citations 2
    // if h is 3 then there are 3 papers with citations 3
    // we have to find the maximum h

    const N = citations.length; // total number of papers
    let h = 0;

    for (let ch = 1; ch <= N; ch++) {
      let pcount = 0;
      for (let i = 0; i < N; i++) {
        if (citations[i] >= ch) pcount++;
      }

      if (pcount >= ch) h = ch;
    }

    return h;

    // Complexity analysis
    // Time : O(N*N)
    // Space : O(1)
  }

  binary_search(citations) {
    const N = citations.length; // total number of papers

    let hIndex = 0;

    let l = 1;
    let h = N;
    while (l <= h) {
      let ci = Math.floor((l + h) / 2);

      let pcount = 0;
      for (let i = 0; i < N; i++) {
        if (citations[i] >= ci) pcount++;
      }

      if (pcount >= ci) {
        hIndex = ci;
        l = ci + 1;
      } else {
        h = ci - 1;
      }
    }

    return hIndex;

    // Complexity analysis
    // Time : O(Log(N) * N)
    // Space : O(1)
  }

  sort_count(citations) {
    let N = citations.length;

    citations.sort((a, b) => b - a);
    // sort(citations.begin(), citations.end(), greater<int>());

    let hi = 0;
    while (hi < N && citations[hi] > hi) hi++;

    return hi;

    // Complexity analysis
    // Time : O(N*Log(N) + N)
    // Space : O(1)
  }

  counting_sort(citations) {
    let N = citations.length;

    const citationsCount = new Array(N + 1).fill(0);

    // count citaions
    for (const c of citations) {
      if (c >= N) citationsCount[N]++;
      else citationsCount[c]++;
    }

    let count = 0;
    // return maximum possible h index
    for (let i = N; i >= 0; i--) {
      count += citationsCount[i];
      if (count >= i) return i;
    }

    return 0;

    // Complexity analysis
    // Time : O(N + N)
    // Space : O(N)
  }

  hIndex(citations) {
    // code here

    // return this.brute(citations);

    // return this.binary_search(citations);

    // return this.sort_count(citations);

    return this.counting_sort(citations);
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Find H-Index - https://www.geeksforgeeks.org/problems/find-h-index--165609/1

  const s2 = new Solution2();
  console.log(s2.hIndex([3, 0, 5, 3, 0]));
  console.log(s2.hIndex([5, 1, 2, 4, 1]));
  console.log(s2.hIndex([0, 0]));
};

(() => {
  // Day 18 of August 2025

  p1();

  p2();
})();
