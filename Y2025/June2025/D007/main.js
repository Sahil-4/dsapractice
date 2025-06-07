/**
 * @param {string} s
 * @return {string}
 */
var clearStars = function (s) {
  const N = s.length;

  const comparator = (a, b) => (a[0] == b[0]) ? (b[1] - a[1]) : (a[0] < b[0]) ? -1 : 1;
  const mheap = new PriorityQueue(comparator);

  const output = s.split("");

  for (let i = 0; i < N; i++) {
    if (output[i] == '*') {
      // delete first smallest char on left 
      const [_, index] = mheap.dequeue();
      output[index] = '*';
    } else {
      mheap.enqueue([output[i], i]);
    }
  }

  return output.filter((e) => e != '*').join("");

  // Complexity analysis 
  // Time : O(N * Log(N)) 
  // Space : O(2N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3170. Lexicographically Minimum String After Removing Stars - https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/description/?envType=daily-question&envId=2025-06-07 

  console.log(clearStars("aaba*"));
  console.log(clearStars("abc"));
  console.log(clearStars("sy*stem*hang*homan*go"));
};

class Problem2 {
  longestCommonSum(a1, a2) {
    // Code here

    // return this.brute(a1, a2);

    return this.optimal(a1, a2);
  }

  optimal(a1, a2) {
    const N = a1.length;

    let len = 0;

    let s1 = 0;
    let s2 = 0;
    let dmap = new Map();
    dmap.set(0, -1);

    for (let i = 0; i < N; i++) {
      s1 += a1[i];
      s2 += a2[i];

      let d = s1 - s2;

      if (dmap.has(d)) {
        len = Math.max(len, i - dmap.get(d));
      } else {
        dmap.set(d, i);
      }
    }

    return len;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) 
  }

  brute(a1, a2) {
    const N = a1.length;

    let len = 0;

    for (let i = 0; i < N; i++) {
      let sum1 = 0;
      let sum2 = 0;
      for (let j = i; j < N; j++) {
        sum1 += a1[j];
        sum2 += a2[j];

        if (sum1 === sum2) {
          len = Math.max(len, j - i + 1);
        }
      }
    }

    return len;

    // Complexity analysis 
    // Time : O(N*N) 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Longest Span in two Binary Arrays - https://www.geeksforgeeks.org/problems/longest-span-with-same-sum-in-two-binary-arrays5142/1 

  const p = new Problem2();
  console.log(p.longestCommonSum([0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1]));
  console.log(p.longestCommonSum([0, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1]));
};


(() => {
  // Day 7 of June 2025

  p1();

  p2();
})();
