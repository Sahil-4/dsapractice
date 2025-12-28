/**
 * @param {number[]} arr
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var countGoodTriplets = function (arr, a, b, c) {
  // check given condition
  const checkCondition = (e1, e2, l) => Math.abs(e1 - e2) <= l;

  const N = arr.length;
  let count = 0;

  for (let i = 0; i < N - 2; i++) {
    const ei = arr[i];
    for (let j = i + 1; j < N - 1; j++) {
      const ej = arr[j];
      if (!checkCondition(ei, ej, a)) continue;

      for (let k = j + 1; k < N; k++) {
        const ek = arr[k];
        if (!checkCondition(ej, ek, b)) continue;
        if (!checkCondition(ek, ei, c)) continue;

        count++;
      }
    }
  }

  return count;

  // Complexity analysis
  // Time : O(N^3)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1534. Count Good Triplets - https://leetcode.com/problems/count-good-triplets/description/?envType=daily-question&envId=2025-04-14

  console.log(countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3));
  console.log(countGoodTriplets([1, 1, 2, 2, 3], 0, 0, 1));
  console.log(countGoodTriplets([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000], 1000, 1000, 1000));
};

// User function Template for javascript
class Problem2 {
  dfs(u, graph, vis, rec, ans) {
    vis[u] = rec[u] = 1;

    for (let v = 0; v < 26; v++) {
      if (graph[u][v]) {
        if (!vis[v]) {
          if (!this.dfs(v, graph, vis, rec, ans)) {
            return false;
          }
        } else if (rec[v]) {
          return false;
        }
      }
    }

    ans.push(String.fromCharCode("a".charCodeAt(0) + u));
    rec[u] = 0;
    return true;
  }

  findOrder(words) {
    // code here

    const graph = Array.from({ length: 26 }, () => Array(26).fill(0));
    const exist = Array(26).fill(0);
    const vis = Array(26).fill(0);
    const rec = Array(26).fill(0);
    const ans = [];

    for (const word of words) {
      for (const ch of word) {
        exist[ch.charCodeAt(0) - "a".charCodeAt(0)] = 1;
      }
    }

    for (let i = 0; i + 1 < words.length; i++) {
      const a = words[i],
        b = words[i + 1];
      const n = a.length,
        m = b.length;
      let ind = 0;

      while (ind < n && ind < m && a[ind] === b[ind]) {
        ind++;
      }

      if (ind !== n && ind === m) {
        return "";
      }

      if (ind < n && ind < m) {
        const from = a.charCodeAt(ind) - "a".charCodeAt(0);
        const to = b.charCodeAt(ind) - "a".charCodeAt(0);
        graph[from][to] = 1;
      }
    }

    for (let i = 0; i < 26; i++) {
      if (exist[i] && !vis[i]) {
        if (!this.dfs(i, graph, vis, rec, ans)) {
          return "";
        }
      }
    }

    return ans.reverse().join("");
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Alien Dictionary - https://www.geeksforgeeks.org/problems/alien-dictionary/1

  console.log(new Problem2().findOrder(["baa", "abcd", "abca", "cab", "cad"]));
  console.log(new Problem2().findOrder(["caa", "aaa", "aab"]));
  console.log(new Problem2().findOrder(["ab", "cd", "ef", "ad"]));
};

(() => {
  // Day 14 of April 2025

  p1();

  p2();
})();
