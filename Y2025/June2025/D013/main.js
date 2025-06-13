/**
 * @param {number[]} nums
 * @param {number} p
 * @return {number}
 */
var minimizeMax = function (nums, p) {
  // binary search on answer (d) 
  // search space [0, max(nums)] 
  // count pairs with difference mid 

  // sort nums - to find pairs efficiently 
  const N = nums.length;
  const sortedNums = [...nums];
  sortedNums.sort((a, b) => a - b);

  const countPairs = (diff) => {
    let pcount = 0;

    for (let i = 0; i < N - 1; i++) {
      let a = sortedNums[i];
      let b = sortedNums[i + 1];

      let d = Math.abs(a - b);

      if (d <= diff) {
        pcount++;
        i++;
      }
    }

    return pcount;
  };

  let low = 0;
  let high = sortedNums[N - 1];

  let ans = -1;

  while (low <= high) {
    let mid = Math.floor((low + high) / 2);

    if (countPairs(mid) >= p) {
      ans = mid;
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }

  return ans;

  // Complexity analysis 
  // Time : O(N * Log(N)) + O(LOG(max(nums)) * N) 
  // Space : O(N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2616. Minimize the Maximum Difference of Pairs - https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/?envType=daily-question&envId=2025-06-13 

  console.log(minimizeMax([10, 1, 2, 7, 1, 3], 2));
  console.log(minimizeMax([4, 2, 1, 2], 1));
};

class Problem2 {
  kokoEat(arr, k) {
    // code here
    // calculate time for s bananas per hour 
    // find optimal s 
    // use binary search for reducing search space [1, max(arr)] 

    const calculateHours = (s) => {
      // calculate hours to be taken to eat all bananas 
      // if speed is s bananas per hour 
      return arr.reduce((acc, e) => {
        acc += Math.ceil(e / s);
        return acc;
      }, 0);
    };

    let low = 1;
    let high = Math.max(...arr);

    let ans = -1;

    while (low <= high) {
      let s = Math.floor((low + high) / 2);

      if (calculateHours(s) <= k) {
        high = s - 1;
        ans = s;
      } else {
        low = s + 1;
      }
    }

    return ans;

    // Complexity analysis 
    // Time : O(N) + O(Log(Max(arr)) * N) 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Koko Eating Bananas - https://www.geeksforgeeks.org/problems/koko-eating-bananas/1 

  const p = new Problem2();

  console.log(p.kokoEat([3, 6, 7, 11], 8));
  console.log(p.kokoEat([30, 11, 23, 4, 20], 5));
  console.log(p.kokoEat([5, 10, 15, 20], 7));
};


(() => {
  // Day 13 of June 2025

  p1();

  p2();
})();
