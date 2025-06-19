/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var partitionArray = function (nums, k) {
  // nums = [3,6,1,2,5], k = 2
  // [3,6,1,2,5] -> [1,2,3,5,6] (sorting)
  // [1,2,3,5,6]
  // [[1,2,3], [5,6]]
  // output : 2

  // nums = [1,2,3], k = 1
  // [[1,2], [3]]
  // output : 2

  // nums = [2,2,4,5], k = 0
  // [[2,2], [4], [5]]
  // output : 3

  const N = nums.length;
  const cnums = [...nums].sort((a, b) => a - b);

  let subsequencesCount = 0;

  for (let i = 0; i < N;) {
    subsequencesCount++;
    let min = cnums[i];
    let max = cnums[i];

    while (i < N) {
      max = cnums[i];

      if ((max - min) <= k) i++;
      else break;
    }
  }

  return subsequencesCount;

  // Complexity analysis 
  // Time : O(N * Log(N)) for sorting + O(N) for counting subsequences 
  // Space : O(N) copying input 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2294. Partition Array Such That Maximum Difference Is K - https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/?envType=daily-question&envId=2025-06-19 

  console.log(partitionArray([3, 6, 1, 2, 5], 2));
  console.log(partitionArray([1, 2, 3], 1));
  console.log(partitionArray([2, 2, 4, 5], 0));
  console.log(partitionArray([2, 2, 2, 2], 0));
  console.log(partitionArray([2, 2, 2, 2], 1));
};

class Problem2 {
  caseSort(s) {
    // code here
    const N = s.length;
    const output = [];

    const [part1, part2] = [[], []];
    let [pointer_1, pointer_2] = [0, 0];

    for (let i = 0; i < N; i++) {
      if (s[i] >= 'A' && 'Z' >= s[i]) {
        part1.push(s[i]);
      } else {
        part2.push(s[i]);
      }
    }

    part1.sort();
    part2.sort();

    for (let i = 0; i < N; i++) {
      if (s[i] >= 'A' && 'Z' >= s[i]) {
        output.push(part1[pointer_1++]);
      } else {
        output.push(part2[pointer_2++]);
      }
    }

    return output.join("");

    // Complexity analysis 
    // Time : O(N) + O(N * Log(N)) + O(N) 
    // Space : O(2N) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Case-specific Sorting of Strings - https://www.geeksforgeeks.org/problems/case-specific-sorting-of-strings4845/1 

  const s = new Problem2();

  console.log(`defRTSersUXI -> ${s.caseSort("defRTSersUXI")}`);
  console.log(`HelLo -> ${s.caseSort("HelLo")}`);
  console.log(`hello -> ${s.caseSort("hello")}`);
  console.log(`XWMSPQ -> ${s.caseSort("XWMSPQ")}`);
  console.log(`GEekS -> ${s.caseSort("GEekS")}`);
};


(() => {
  // Day 19 of June 2025

  p1();

  p2();
})();
