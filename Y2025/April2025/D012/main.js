/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var countGoodIntegers = function (n, k) {
  const factorial = new Array(11).fill(1);
  for (let i = 1; i <= 10; i++) {
    factorial[i] = factorial[i - 1] * i;
  }

  let counts = 0; // final result

  const kPalindromes = new Set();

  // digits in left half
  const d = Math.floor((n + 1) / 2);

  // range of d digit numbers
  const start = Math.pow(10, d - 1);
  const end = Math.pow(10, d) - 1;

  for (let num = start; num <= end; num++) {
    const leftHalf = String(num);
    let full = "";

    if (n & 1) {
      const rightHalf = leftHalf
        .substring(0, d - 1)
        .split("")
        .reverse()
        .join("");
      full = [...leftHalf.split(""), ...rightHalf.split("")].join("");
    } else {
      const rightHalf = leftHalf.split("").reverse().join("");
      full = [...leftHalf.split(""), ...rightHalf.split("")].join("");
    }

    const __num = Number(full);
    if (__num % k != 0) continue;

    const sortedFull = full.split("").sort().join("");

    kPalindromes.add(sortedFull);
  }

  kPalindromes.forEach((sortedFul) => {
    let freq = new Array(10).fill(0);
    for (let i = 0; i < sortedFul.length; i++) {
      freq[Number(sortedFul[i])]++;
    }

    let t_digits = sortedFul.length;
    let zeroes = freq[0];
    let nonZeroes = t_digits - zeroes;

    let perm = nonZeroes * factorial[t_digits - 1];

    for (let i = 0; i < 10; i++) {
      perm = Math.floor(perm / factorial[freq[i]]);
    }

    counts += perm;
  });

  return counts;

  // Complexity analysis
  // Time : O(10^d) + O((10^d) * N)
  // Space : O(10^d) string set
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 3272. Find the Count of Good Integers - https://leetcode.com/problems/find-the-count-of-good-integers/description/?envType=daily-question&envId=2025-04-12

  console.log(countGoodIntegers(3, 5));
  console.log(countGoodIntegers(1, 4));
  console.log(countGoodIntegers(5, 6));
};

// User function Template for javascript

/**
 * @param {number[][]} arr
 * @param {number} n
 * @param {number} m
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @returns {number[][]}
 */
class Problem2 {
  floodFill(image, sr, sc, newColor) {
    // code here

    // dimentions
    const N = image.length;
    const M = image[0].length;

    // copy given image
    const copyImage = [...image.map((row) => [...row])];
    // possible movements
    const _dirs = [
      [-1, 0],
      [0, +1],
      [+1, 0],
      [0, -1],
    ];
    // original color
    const og = image[sr][sc];

    // queue for bfs traversal
    const queue = [];

    // start of bfs - init with [sr, sc] point or cell
    if (og != newColor) {
      copyImage[sr][sc] = newColor;
      queue.push([sr, sc]);
    }

    // actual bfs
    while (queue.length) {
      const [ur, uc] = queue.shift();

      // explore adjacent cells
      for (let [_r, _c] of _dirs) {
        const [vr, vc] = [_r + ur, _c + uc];

        // invalid index
        if (vr < 0 || vr >= N) continue;
        if (vc < 0 || vc >= M) continue;

        // having same original color
        if (copyImage[vr][vc] != og) continue;

        // update color
        copyImage[vr][vc] = newColor;

        // add this cell into queue for further bfs traversal
        queue.push([vr, vc]);
      }
    }

    // return modified image
    return copyImage;

    // Complexity analysis
    // Time : O(N*M) copy + O(N*M) bfs
    // Space : O(N*M) copy image + O(N+M) queue at once
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Flood fill Algorithm - https://www.geeksforgeeks.org/problems/flood-fill-algorithm1856/1

  {
    const image = [
      [0, 1, 1, 1, 1, 0, 2, 0, 1, 0],
      [0, 1, 1, 0, 0, 0, 1, 1, 1, 2],
      [0, 2, 1, 2, 2, 1, 2, 1, 1, 2],
    ];
    const sr = 0;
    const sc = 0;
    const newColor = 5;
    console.log(image);
    console.table({ sr, sc, newColor });
    const args = [image, sr, sc, newColor];
    console.log(new Problem2().floodFill(...args));
  }
  {
    const image = [
      [0, 1, 1, 1, 1, 0, 2, 0, 1, 0],
      [0, 1, 1, 0, 0, 0, 1, 1, 1, 2],
      [0, 2, 1, 2, 2, 1, 2, 1, 1, 2],
    ];
    const sr = 0;
    const sc = 1;
    const newColor = 5;
    console.log(image);
    console.table({ sr, sc, newColor });
    const args = [image, sr, sc, newColor];
    console.log(new Problem2().floodFill(...args));
  }
};

(() => {
  // Day 12 of April 2025

  p1();

  p2();
})();
