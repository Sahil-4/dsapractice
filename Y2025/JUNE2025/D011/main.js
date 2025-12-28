/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxDifference = function (s, k) {
  const t = 100001;
  const N = s.length;

  const prefix = Array.from({ length: 5 }, () => new Array(N + 1).fill(0));

  for (let i = 0; i < N; i++) {
    for (let c = 0; c < 5; c++) {
      prefix[c][i + 1] = prefix[c][i];
    }
    prefix[+s[i]][i + 1]++;
  }

  const getMaxDifference = (a, b) => {
    const trackMin = [[t, t], [t, t]];

    const xpref = prefix[a];
    const ypref = prefix[b];

    let i = 0, j = k;
    let ans = -t;

    while (j <= N) {
      if (ypref[j] != ypref[i]) {
        while (j - i >= k) {
          let xp = xpref[i] % 2;
          let yp = ypref[i] % 2;

          trackMin[xp][yp] = Math.min(trackMin[xp][yp], xpref[i] - ypref[i]);

          i++;
        }
      }

      let max_at_j = xpref[j] - ypref[j] - trackMin[1 ^ (xpref[j] % 2)][ypref[j] % 2];
      ans = Math.max(ans, max_at_j);

      j++;
    }

    return ans;
  };

  let mdiff = -t;

  for (let a = 0; a < 5; a++) {
    if (prefix[a][N] === 0) continue;

    for (let b = 0; b < 5; b++) {
      if (prefix[b][N] === 0) continue;
      if (a === b) continue;

      mdiff = Math.max(mdiff, getMaxDifference(a, b));
    }
  }

  return mdiff;

  // Complexity analysis 
  // Time : O(5 * 5 ^ N) 
  // Space : O(5 * N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3445. Maximum Difference Between Even and Odd Frequency II - https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/description/?envType=daily-question&envId=2025-06-11 

  console.log(maxDifference("12233", 4));
  console.log(maxDifference("1122211", 3));
  console.log(maxDifference("110", 3));
  console.log(maxDifference("011234", 1));
};

class Problem2 {
  findLength(color, radius) {
    // code here
    const isSameBall = (b1, b2) => ((b1[0] === b2[0]) && (b1[1] === b2[1]));

    const stack = [];

    for (let i = 0; i < color.length; i++) {
      const ball = [color[i], radius[i]];

      if (stack.length && isSameBall(ball, stack.at(-1))) {
        stack.pop();
      } else {
        stack.push(ball);
      }
    }

    return stack.length;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Remove the balls - https://www.geeksforgeeks.org/problems/remove-the-balls--170647/1 

  const s = new Problem2();
  console.log(s.findLength([2, 3, 5], [3, 3, 5]));
  console.log(s.findLength([2, 2, 5], [3, 3, 5]));
};


(() => {
  // Day 11 of June 2025

  p1();

  p2();
})();
