/**
 * @param {number[]} answers
 * @return {number}
 */
var numRabbits = function (answers) {
  const N = answers.length;

  // stores different answers, and how many rabbits answered same
  const map = new Map();

  for (let i = 0; i < N; i++) {
    const x = answers[i];
    map.set(x, (map.get(x) || 0) + 1);
  }

  let count = 0;

  // find group of rabbits and number of rabbits in one group who answered same
  for (let [key, value] of map) {
    let groups = Math.floor(value / (key + 1));
    if (value % (key + 1) > 0) groups += 1;

    let rabbits = groups * (key + 1);

    count += rabbits;
  }

  return count;

  // Complexity analysis
  // Time : O(N) + O(N) Assuming constant time in map look up
  // Space : O(N) map
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 781. Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/description/?envType=daily-question&envId=2025-04-20

  console.log(numRabbits([1, 1, 2]));
  console.log(numRabbits([10, 10, 10]));
  console.log(numRabbits([0, 0, 1, 1, 1]));
  console.log(numRabbits([2, 2, 1, 2, 8, 8, 2, 8, 8]));
  console.log(numRabbits([24, 24, 24, 24, 2, 2, 1, 2, 8, 8, 2, 8, 8]));
  console.log(numRabbits([2, 1, 0, 0, 0, 0, 0]));
  console.log(numRabbits([5, 1, 5, 3, 5, 2, 12, 4, 20, 20]));
  console.log(
    numRabbits([
      905, 401, 378, 983, 160, 183, 438, 585, 118, 90, 405, 120, 642, 812, 364, 903, 223, 350, 982, 752, 111, 996, 536, 701,
      791, 202, 341, 891, 335, 477,
    ]),
  );
};

// User function Template for JavaScript

/**
 * @param {number[]} arr
 * @returns {number}
 */
class Problem2 {
  findDuplicate(arr) {
    // code here

    return this.solve_1(arr);
    // return this.solve_2(arr);
  }

  solve_1(arr) {
    const N = arr.length - 1;
    const nNSum = Math.floor((N * (N + 1)) / 2);
    const arSum = arr.reduce((acc, e) => acc + e, 0);
    const duplicate = arSum - nNSum;

    return duplicate;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }

  solve_2(arr) {
    const N = arr.length;
    let xor = arr[0];

    for (let i = 1; i < N; i++) {
      xor = xor ^ arr[i] ^ i;
    }

    return xor;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Find Only Repetitive Element from 1 to n-1 - https://www.geeksforgeeks.org/problems/find-repetitive-element-from-1-to-n-1/1

  console.log(new Problem2().findDuplicate([1, 3, 2, 3, 4]));
  console.log(new Problem2().findDuplicate([1, 5, 1, 2, 3, 4]));
  console.log(new Problem2().findDuplicate([1, 1]));
};

(() => {
  // Day 20 of April 2025

  p1();

  p2();
})();
