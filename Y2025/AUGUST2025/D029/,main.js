/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var flowerGame = function (n, m) {
  // observation
  // (x = 1, y = 1) -> bob wins
  // (x = 1, y = 2) -> alice wins
  // (x = 1, y = 3) -> bob wins
  // (x = 1, y = 4) -> alice wins
  // (x = 2, y = 1) -> alice wins
  // (x = 2, y = 2) -> bob wins
  // (x = 2, y = 3) -> alice wins
  // (x = 3, y = 1) -> bob wins
  // (x = 3, y = 2) -> alice wins
  // key
  // (x = odd, y = odd) -> bob wins
  // (x = odd, y = even) -> alice wins
  // (x = even, y = even) -> bob wins
  // (x = even, y = odd) -> alice wins
  // total alice wins = (oddX * evenY) + (evenX * oddY)
  // simplified formula for output : floor((n*m) / 2)

  let total = 0;
  let l1, l2;

  // case 1 : odd in lane 1, even in lane 2
  l1 = Math.floor((n + 1) / 2);
  l2 = Math.floor((m + 0) / 2);
  total += l1 * l2;

  // case 2 : even in lane 1, odd in lane 2
  l1 = Math.floor((n + 0) / 2);
  l2 = Math.floor((m + 1) / 2);
  total += l1 * l2;

  return total;

  // Complexity analysis
  // Time : O(1)
  // Space : O(1)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3021. Alice and Bob Playing Flower Game - https://leetcode.com/problems/alice-and-bob-playing-flower-game/description/?envType=daily-question&envId=2025-08-29

  console.log(flowerGame(3, 2));
  console.log(flowerGame(1, 1));
  console.log(flowerGame(4, 5));
  console.log(flowerGame(5, 4));
  console.log(flowerGame(100000, 100000));
};

/**
 * @param {string} s
 * @param {string} p
 * @return {string}
 **/
class Solution2 {
  smallestWindow(s, p) {
    // code here
    // sliding window problem

    const char2index = (char) => char.charCodeAt(0) - "a".charCodeAt(0);

    const smap = new Array(26).fill(0);
    const pmap = new Array(26).fill(0);

    const validWindow = () => {
      for (let i = 0; i < 26; i++) {
        if (pmap[i] > smap[i]) return false;
      }
      return true;
    };

    let [start, end] = [0, s.length];

    for (let r = 0; r < p.length; r++) {
      pmap[char2index(p[r])]++;
    }

    for (let l = 0, r = 0; r < s.length; r++) {
      smap[char2index(s[r])]++;

      while (l <= r && validWindow()) {
        // update answer
        if (end - start > r - l) {
          start = l;
          end = r;
        }

        // shrink the window
        smap[char2index(s[l++])]--;
      }
    }

    if (end === s.length) return "";
    return s.substring(start, end + 1);

    // Complexity analysis
    // Time : O(Plem) + O(2 * SLen * 26)
    // Space : O(2 * 26)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Smallest window containing all characters - https://www.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1

  const s2 = new Solution2();
  console.log(s2.smallestWindow("timetopractice", "toc"));
  console.log(s2.smallestWindow("zoomlazapzo", "oza"));
  console.log(s2.smallestWindow("zoom", "zooe"));
};

(() => {
  // Day 29 of August 2025

  p1();

  p2();
})();
