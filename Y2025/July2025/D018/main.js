/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDifference = function (nums) {
  // TC 1
  // nums = [3,1,2]
  // minSum = [3,1,1]
  // maxSum = [3,2,2]
  // TC 2
  // nums = [7,9,5,8,1,3]
  // minSum = [7,16,12,12,6,4]
  // maxSum = [17,17,13,11,4,3]

  const n = nums.length / 3;

  // Compute prefix min sums using a max heap
  const minSums = new Array(nums.length).fill(0);
  const maxHeap = new PriorityQueue((a, b) => b - a);
  let minSum = 0;

  for (let i = 0; i < 2 * n; i++) {
    maxHeap.enqueue(nums[i]);
    minSum += nums[i];
    if (maxHeap.size() > n) {
      minSum -= maxHeap.dequeue();
    }
    if (i >= n - 1) {
      minSums[i] = minSum;
    }
  }

  // Compute suffix max sums using a min heap
  const maxSums = new Array(nums.length).fill(0);
  const minHeap = new PriorityQueue((a, b) => a - b);
  let maxSum = 0;

  for (let i = nums.length - 1; i >= n; i--) {
    minHeap.enqueue(nums[i]);
    maxSum += nums[i];
    if (minHeap.size() > n) {
      maxSum -= minHeap.dequeue();
    }
    if (i <= 2 * n) {
      maxSums[i] = maxSum;
    }
  }

  // Calculate the minimum difference
  let result = Infinity;
  for (let i = n - 1; i < 2 * n; i++) {
    result = Math.min(result, minSums[i] - maxSums[i + 1]);
  }

  return result;

  // Complexity analysis
  // Time : O(2 * (2N * Log(N))) + O(2N)
  // Space : O(2N) + O(N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2163. Minimum Difference in Sums After Removal of Elements - https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/description/?envType=daily-question&envId=2025-07-18

  console.log(minimumDifference([3, 1, 2]));
  console.log(minimumDifference([7, 9, 5, 8, 1, 3]));
  console.log(
    minimumDifference([
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
      27,
    ])
  );
  console.log(
    minimumDifference([
      27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3,
      2, 1,
    ])
  );
};

class Solution2 {
  lcmTriplets(n) {
    // code  here

    // return this.brute(n);

    return this.optimal(n);
  }

  most_optimal(n) {
    let ans;

    if (n < 3) {
      ans = n;
    }

    // If n is odd, the product of the top 3 numbers gives maximum LCM
    else if (n % 2 !== 0) {
      ans = n * (n - 1) * (n - 2);
    }

    // If n is even and not divisible by 3, use n, n-1, n-3
    else if (n % 3 !== 0) {
      ans = n * (n - 1) * (n - 3);
    }

    // If n is even and divisible by 3, use n-1, n-2, n-3
    else {
      ans = (n - 1) * (n - 2) * (n - 3);
    }

    return ans;

    // Complexity analysis
    // Time : O(1) + some multiplications
    // Space : O(1)
  }

  optimal(n) {
    if (n & 1) {
      return this.lcm(n, n - 1, n - 2);
    } else {
      return Math.max(this.lcm(n, n - 1, n - 3), this.lcm(n - 1, n - 2, n - 3));
    }

    // Complexity analysis
    // Time : O(2 * 2 * Log(N))
    // Space : O(1)
  }

  __gcd__(a, b) {
    if (b === 0) return a;
    return this.__gcd__(b, a % b);
  }

  __lcm__(a, b) {
    return (a * b) / this.__gcd__(a, b);
  }

  lcm(a, b, c) {
    return this.__lcm__(this.__lcm__(a, b), c);
  }

  brute(n) {
    // fallback
    if (n < 3) return n;

    let maxx = 0;

    for (let a = 1; a <= n; a++) {
      for (let b = a + 1; b <= n; b++) {
        for (let c = b + 1; c <= n; c++) {
          let lcm = this.lcm(a, b, c);
          maxx = Math.max(maxx, lcm);
        }
      }
    }

    return maxx;

    // Complexity analysis
    // Time : O(N * N * N * 2 * Log(N))
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks LCM Triplet - https://www.geeksforgeeks.org/problems/lcm-triplet1501/1

  const s2 = new Solution2();
  console.log(s2.lcmTriplets(1));
  console.log(s2.lcmTriplets(2));
  console.log(s2.lcmTriplets(3));
  console.log(s2.lcmTriplets(5));
  console.log(s2.lcmTriplets(12));
  console.log(s2.lcmTriplets(60));
  console.log(s2.lcmTriplets(100));
  console.log(s2.lcmTriplets(300));
  console.log(s2.lcmTriplets(1000));
};

(() => {
  // Day 18 of July 2025

  p1();

  p2();
})();
