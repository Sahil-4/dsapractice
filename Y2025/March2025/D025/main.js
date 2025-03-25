/**
 * @param {number} n
 * @param {number[][]} rectangles
 * @return {boolean}
 */
var checkValidCuts = function(n, rectangles) {
  // merge intervals (on x, y axis) 

  let output = false;

  const solve = (arr) => {
      arr.sort((a, b) => a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);

      const merged = [];

      for (let i = 0, prev = arr[0]; i <= arr.length; i++) {
          if (i == arr.length || prev[1] <= arr[i][0]) {
              merged.push(prev);
              prev = arr[i];
          } else {
              prev[0] = Math.min(prev[0], arr[i][0]);
              prev[1] = Math.max(prev[1], arr[i][1]);
          }
      }

      return merged.length >= 3;
  };

  output = output || solve(rectangles.map((co) => ([co[0], co[2]]))); // x axis 
  output = output || solve(rectangles.map((co) => ([co[1], co[3]]))); // y axis 

  return output;

  // Complexity analysis 
  // Time : O(N) + O(N*LOG(N)) + O(N) 
  // Space : O(2N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3394. Check if Grid can be Cut into Sections - https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/?envType=daily-question&envId=2025-03-25 

  console.log(checkValidCuts(5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]));
  console.log(checkValidCuts(3, [[0,0,1,3],[1,0,2,2],[2,0,3,2],[1,2,3,3]]));
  
};

// User function Template for javascript
/**
 * @param {string} s
 * @returns {number}
 */
class Problem2 {
  countWays(s) {
    // code here

    // return this.recursion(s, 0, s.length-1)[0];

    // const n = s.length;
    // const memo = Array.from({ length: n }, () => new Array(n).fill(null));
    // return this.memoize(s, 0, s.length-1, memo)[0];

    return this.tabulation(s)[0];
  }

  recursion(s, i, j, flag) {
    if (i > j) return [0, 0];
    if (i == j) return [s[i] == "T", s[i] == "F"];

    let ways_t = 0;
    let ways_f = 0;

    for (let k = i + 1; k < j; k += 2) {
      let right = this.recursion(s, k + 1, j);
      let left = this.recursion(s, i, k - 1);

      switch (s[k]) {
        case "&":
          ways_t += right[0] * left[0];
          ways_f += right[0] * left[1] + right[1] * left[0] + right[1] * left[1];
          break;
        case "|":
          ways_t += right[0] * left[1] + right[1] * left[0] + right[0] * left[0];
          ways_f += right[1] * left[1];
          break;
        case "^":
          ways_t += right[0] * left[1] + right[1] * left[0];
          ways_f += right[0] * left[0] + right[1] * left[1];
          break;
        default:
          break;
      }
    }

    return [ways_t, ways_f];
  }

  memoize(s, i, j, memo) {
    if (i > j) return [0, 0];
    if (i == j) return [Number(s[i] == "T"), Number(s[i] == "F")];

    if (memo[i][j] != null) return memo[i][j];

    let ways_t = 0;
    let ways_f = 0;

    for (let k = i + 1; k < j; k += 2) {
      let right = this.memoize(s, k + 1, j, memo);
      let left = this.memoize(s, i, k - 1, memo);

      switch (s[k]) {
        case "&":
          ways_t += right[0] * left[0];
          ways_f += right[0] * left[1] + right[1] * left[0] + right[1] * left[1];
          break;
        case "|":
          ways_t += right[0] * left[1] + right[1] * left[0] + right[0] * left[0];
          ways_f += right[1] * left[1];
          break;
        case "^":
          ways_t += right[0] * left[1] + right[1] * left[0];
          ways_f += right[0] * left[0] + right[1] * left[1];
          break;
        default:
          break;
      }
    }

    return (memo[i][j] = [ways_t, ways_f]);
  }

  tabulation(s) {
    const n = s.length;
    const memo = Array.from({ length: n }, () => new Array(n).fill(null));

    // recurrence
    for (let i = n - 1; i >= 0; i -= 2) {
      for (let j = 0; j <= n - 1; j += 2) {
        if (i > j) {
          memo[i][j] = [0, 0];
          continue;
        }
        if (i == j) {
          memo[i][j] = [Number(s[i] == "T"), Number(s[i] == "F")];
          continue;
        }

        let ways_t = 0;
        let ways_f = 0;

        for (let k = i + 1; k < j; k += 2) {
          let right = memo[k + 1][j];
          let left = memo[i][k - 1];

          switch (s[k]) {
            case "&":
              ways_t += right[0] * left[0];
              ways_f += right[0] * left[1] + right[1] * left[0] + right[1] * left[1];
              break;
            case "|":
              ways_t += right[0] * left[1] + right[1] * left[0] + right[0] * left[0];
              ways_f += right[1] * left[1];
              break;
            case "^":
              ways_t += right[0] * left[1] + right[1] * left[0];
              ways_f += right[0] * left[0] + right[1] * left[1];
              break;
            default:
              break;
          }
        }

        memo[i][j] = [ways_t, ways_f];
      }
    }

    return memo[0][n - 1];

    // Complexity analysis
    // Time : O(N*N*K)
    // Space : O(N*N*2)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Boolean Parenthesization - https://www.geeksforgeeks.org/problems/boolean-parenthesization5610/1

  console.log(new Problem2().countWays("T"));
  console.log(new Problem2().countWays("F"));
  console.log(new Problem2().countWays("F&F"));
  console.log(new Problem2().countWays("T&T"));
  console.log(new Problem2().countWays("T|F"));
  console.log(new Problem2().countWays("T|T&F^T"));
};

(() => {
  // Day 25 of March 2025

  p1();

  p2();
})();
