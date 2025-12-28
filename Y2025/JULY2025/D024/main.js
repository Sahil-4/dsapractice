/**
 * @param {number[]} nums
 * @param {number[][]} edges
 * @return {number}
 */
var minimumScore = function (nums, edges) {
  // total number of nodes
  const N = nums.length;

  // adjacency list
  const adjacency = Array.from({ length: N }, () => new Array());
  for (const [n1, n2] of edges) {
    adjacency[n1].push(n2);
    adjacency[n2].push(n1);
  }

  // xor of entire tree nodes value
  const txor = nums.reduce((acc, e) => acc ^ e, 0);

  // final output
  let result = Number.MAX_SAFE_INTEGER;

  // for xor2 - back to parent/top
  const dfs2 = (u, parentU, xor1, ancestor) => {
    let xor2 = nums[u];

    for (const v of adjacency[u]) {
      if (v !== parentU) xor2 ^= dfs2(v, u, xor1, ancestor);
    }

    if (parentU === ancestor) return xor2;

    let xor3 = txor ^ xor1 ^ xor2;
    result = Math.min(result, Math.max(xor1, xor2, xor3) - Math.min(xor1, xor2, xor3));

    return xor2;
  };

  // for xor1 - towards bottom
  const dfs = (u, parentU) => {
    let xor1 = nums[u];

    for (const v of adjacency[u]) {
      if (v !== parentU) xor1 ^= dfs(v, u);
    }

    for (const v of adjacency[u]) {
      if (v === parentU) dfs2(v, u, xor1, u);
    }

    return xor1;
  };

  dfs(0, -1);

  return result;

  // Complexity analysis
  // Time : O(E) + O(N) + O(N * N)
  // Space : O(N * N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2322. Minimum Score After Removals on a Tree - https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/description/?envType=daily-question&envId=2025-07-24

  console.log(
    minimumScore(
      [1, 5, 5, 4, 11],
      [
        [0, 1],
        [1, 2],
        [1, 3],
        [3, 4],
      ]
    )
  );
  console.log(
    minimumScore(
      [5, 5, 2, 4, 4, 2],
      [
        [0, 1],
        [1, 2],
        [5, 2],
        [4, 3],
        [1, 3],
      ]
    )
  );
};

class Solution2 {
  getLastMoment(n, left, right) {
    // code here
    // collision is not an issue
    // there will be no effect of collision
    // because when two ants collide, and swap their paths and distance
    // so we just have to return the maximum distance,
    // travelled by any ant,
    // to reach the end
    // n = 4, left = [3], right = [1]
    // 0 1 2 3 4 - plank
    // 0 > 2 < 4 - ants position and direction
    // . 3 . 3 . - time taken by ant to reach end
    // 3 - output

    return Math.max(...left, ...right.map((re) => n - re));

    // Complexity analysis
    // Time : O(N + M)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Last Moment Before All Ants Fall Out - https://www.geeksforgeeks.org/problems/last-moment-before-all-ants-fall-out-of-a-plank/1

  const s2 = new Solution2();
  console.log(s2.getLastMoment(4, [2], [0, 1, 3]));
  console.log(s2.getLastMoment(4, [], [0, 1, 2, 3, 4]));
  console.log(s2.getLastMoment(4, [0, 1, 2, 3, 4], []));
  console.log(s2.getLastMoment(3, [0], [3]));
  console.log(s2.getLastMoment(4, [3], [1]));
};

(() => {
  // Day 24 of July 2025

  p1();

  p2();
})();
