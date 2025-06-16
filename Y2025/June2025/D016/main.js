/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumDifference = function (nums) {
  // idea behind the solution : 
  // Thought 1 : 
  // I just need two elements, nums[i] and nums[j] such that 
  // nums[i] < nums[j], and i < j 
  // Thought 2 : 
  // to maximize the difference between nums[i], and nums[j], 
  // I will have to take nums[i] as small as possible, 
  // and I will have to take nums[j] as large as possible 
  // Thought 3 : 
  // I will traverse the entire array 
  // for each num in nums 
  // if its less then nums[i] (which initially assumed to be nums[0]) 
  // we update nums[i] with num (or nums[j] as we have used nums[j] in loop) 
  // Thought 4 : 
  // now now here we have to be careful and update max diff only if i < j (basically i != j) 
  // Thought 5 : 
  // we are taking nums[i] as small as possible 
  // and nums[j] we are trying to take as large as possible 
  // and while taking nums[j] we are updating max diff also 
  // this is greedy approach 

  const N = nums.length;

  let mdiff = -1;
  let i = 0;

  for (let j = 1; j < N; j++) {
    if (nums[j] <= nums[i]) i = j;

    if (i < j) {
      let d = nums[j] - nums[i];
      mdiff = Math.max(mdiff, d);
    }
  }

  return mdiff;

  // Complexity analysis 
  // Time : O(N) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2016. Maximum Difference Between Increasing Elements - https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/?envType=daily-question&envId=2025-06-16 

  console.log(maximumDifference([7, 1, 5, 4]));
  console.log(maximumDifference([9, 4, 3, 2]));
  console.log(maximumDifference([1, 5, 2, 10]));
  console.log(maximumDifference([999, 997, 980, 976, 948, 940, 938, 928, 924, 917, 907, 907, 881, 878, 864, 862, 859, 857, 848, 840, 824, 824, 824, 805, 802, 798, 788, 777, 775, 766, 755, 748, 735, 732, 727, 705, 700, 697, 693, 679, 676, 644, 634, 624, 599, 596, 588, 583, 562, 558, 553, 539, 537, 536, 509, 491, 485, 483, 454, 449, 438, 425, 403, 368, 345, 327, 287, 285, 270, 263, 255, 248, 235, 234, 224, 221, 201, 189, 187, 183, 179, 168, 155, 153, 150, 144, 107, 102, 102, 87, 80, 57, 55, 49, 48, 45, 26, 26, 23, 15]));
};

/**
 * @param {number[]} heights
 * @param {number} costs
 * @returns {number}
 */
class Problem2 {
  minCost(heights, costs) {
    // code here

    const N = heights.length;

    const calculateCost = (th) => {
      let tcost = 0;

      for (let i = 0; i < N; i++) {
        let rm = Math.abs(heights[i] - th);
        let c = rm * costs[i];
        tcost += c;
      }

      return tcost;
    };

    let mcost = -1;

    let low = Math.min(...heights);
    let high = Math.max(...heights);

    while (low <= high) {
      let m0 = Math.floor((low + high) / 2);

      let c0 = calculateCost(m0 - 1);
      let c1 = calculateCost(m0);
      let c2 = calculateCost(m0 + 1);

      if (c1 <= c0 && c1 <= c2) {
        mcost = c1;
        break;
      } else if (c0 >= c1 && c1 >= c2) {
        low = m0 + 1;
      } else if (c1 >= c0 && c2 >= c1) {
        high = m0 - 1;
      }
    }

    return mcost;

    // Complexity analysis 
    // Time : O(Log(max(heights)) * N) 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Equalize the Towers - https://www.geeksforgeeks.org/problems/equalize-the-towers2804/1 

  const s = new Problem2();
  console.log(s.minCost([1, 2, 3], [10, 100, 1000]));
  console.log(s.minCost([7, 1, 5], [1, 1, 1]));
};


(() => {
  // Day 16 of June 2025

  p1();

  p2();
})();
