/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
var kthSmallestProduct = function (nums1, nums2, k) {
  const N = nums1.length;
  const M = nums2.length;

  const countSmallest = (midProduct) => {
    let count = 0;

    for (let i = 0; i < N; i++) {
      if (nums1[i] >= 0) {
        let low = 0;
        let high = M - 1;
        let InValid = -1;

        while (low <= high) {
          let mid = low + Math.floor((high - low) / 2);
          let product = nums1[i] * nums2[mid];

          if (product <= midProduct) {
            InValid = mid;
            low = mid + 1;
          } else {
            high = mid - 1;
          }
        }

        count += (InValid + 1);
      } else {
        let low = 0;
        let high = M - 1;
        let InValid = M;

        while (low <= high) {
          let mid = low + Math.floor((high - low) / 2);
          let product = nums1[i] * nums2[mid];

          if (product <= midProduct) {
            InValid = mid;
            high = mid - 1;
          } else {
            low = mid + 1;
          }
        }

        count += (M - InValid);
      }
    }

    return count;
  };

  let output = 0;

  let low = -10000000000;
  let high = 10000000000;

  while (low <= high) {
    const mid = low + Math.floor((high - low) / 2);

    const smallestCount = countSmallest(mid);

    if (smallestCount >= k) {
      output = mid;
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }

  return output;

  // Complexity analysis 
  // Time : O(Log(2 * 1e10) * N * Log(M)) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2040. Kth Smallest Product of Two Sorted Arrays - https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/description/?envType=daily-question&envId=2025-06-25 

  console.log(kthSmallestProduct([2, 5], [3, 4], 2));
  console.log(kthSmallestProduct([-4, -2, 0, 3], [2, 4], 6));
  console.log(kthSmallestProduct([-2, -1, 0, 1, 2], [-3, -1, 2, 4, 5], 3));
};

/**
 * @param {string} s
 * @return {boolean}
 */
class Problem2 {
  sameFreq(s) {
    // code here
    const T = 26;
    const frequency = new Array(T).fill(0);

    for (let i = 0; i < s.length; i++) {
      frequency[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
    }

    const check = () => {
      let flag = true;
      for (let j = 0, check = null; j < 26; j++) {
        if (frequency[j] === 0) continue;
        if (check === null) check = frequency[j];

        flag = flag && (check === frequency[j]);
      }

      return flag;
    };

    for (let i = 0; i < 26; i++) {
      if (frequency[i] === 0) continue;

      if (check()) return true;
      frequency[i]--;
      if (check()) return true;
      frequency[i]++;
    }

    return false;

    // Complexity analysis 
    // Time : O(N) + O(T * (2T)) 
    // Space : O(T) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Check if frequencies can be equal - https://www.geeksforgeeks.org/problems/check-frequencies4211/1 

  const p = new Problem2();
  console.log(p.sameFreq("xyyz"));
  console.log(p.sameFreq("xyyzz"));
  console.log(p.sameFreq("xxxxyyzz"));
  console.log(p.sameFreq("aaaa"));
  console.log(p.sameFreq("aabb"));
};


(() => {
  // Day 25 of June 2025

  p1();

  p2();
})();
