/**
 * @param {number[]} nums
 * @param {number} modulo
 * @param {number} k
 * @return {number}
 */
var countInterestingSubarrays = function (nums, modulo, k) {
  const N = nums.length;
  let interestingSubarraysCount = 0;

  let prefixSum = 0;
  const freq = new Map();

  freq.set(interestingSubarraysCount, 1);

  for (let num of nums) {
    const add = +((num % modulo) === k);

    prefixSum = ((prefixSum + add) % modulo);

    const need = ((prefixSum - k + modulo) % modulo);

    interestingSubarraysCount += freq.get(need) || 0;

    freq.set(prefixSum, (freq.get(prefixSum) || 0) + 1);
  }

  return interestingSubarraysCount;

  // Complexity analysis 
  // Time : O(N) 
  // Space : O(N) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2845. Count of Interesting Subarrays - https://leetcode.com/problems/count-of-interesting-subarrays/description/?envType=daily-question&envId=2025-04-25 

  console.log(countInterestingSubarrays([3, 2, 4], 2, 1));
  console.log(countInterestingSubarrays([3, 1, 9, 6], 3, 0));
};

// User function Template for javascript

/**
 * @param {number[]} arr
 * @returns {number}
 */

class Problem2 {
  majorityElement(arr) {
    // code here
    const N = arr.length;
    const _N = Math.floor(N / 2);

    // Approach : Moore's voting algorithm 
    // Divide the elements into two groups 
    // g1: element which appeared more then N/2 times and is just one 
    // g2: element(s) which appeared less then N/2 times and are more then one 
    // if cancel out frequency with each other 
    // we finally get the element which is majority element 

    let me = 0; // majority element 
    let fq = 0; // frequenct of majority element 

    for (let n of arr) {
      if (fq === 0) {
        me = n;
        fq = 1;
      } else if (me === n) {
        fq += 1;
      } else {
        fq -= 1;
      }
    }

    // we have majority element as me 
    // but we arent sure if there was a majority element 
    // and hence we will be verifying it for majority element 

    me = me;
    fq = 0;

    for (let n of arr) {
      if (me == n) {
        fq++;
      }
    }

    return (fq > _N) ? me : -1;

    // Complexity analysis 
    // Time : O(N) finding + O(N) verifying 
    // Space : O(1) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Majority Element - https://www.geeksforgeeks.org/problems/majority-element-1587115620/1 

  console.log(new Problem2().majorityElement([1, 1, 2, 1, 3, 5, 1]));
  console.log(new Problem2().majorityElement([5]));
  console.log(new Problem2().majorityElement([[2, 13]]));
};

(() => {
  // Day 25 of April 2025

  p1();

  p2();
})();
