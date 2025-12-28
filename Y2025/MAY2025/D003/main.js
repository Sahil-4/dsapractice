/**
 * @param {number[]} tops
 * @param {number[]} bottoms
 * @return {number}
 */
var minDominoRotations = function (tops, bottoms) {
  // just check if we can convert a row (top or bottom) 
  // to a specific (1 - 6)
  // try with 1, then 2, ..., then 6 
  // we just have to make any one (top or bottom) same 

  const N = tops.length;
  const BOUND = 1000000;

  const canMake = (v) => {
    let t_opr = 0; // operations req to convert tops[i] to v 
    let b_opr = 0; // operations req to convert tops[i] to v 

    for (let i = 0; i < N; i++) {
      // need at least one to be v 
      if (tops[i] != v && bottoms[i] != v) return BOUND;

      // already set to v 
      if (tops[i] == v && bottoms[i] == v) continue;

      // setting top to v 
      if (tops[i] != v) t_opr++;

      // setting bottom to v 
      if (bottoms[i] != v) b_opr++;
    }

    return Math.min(t_opr, b_opr);
  };

  let min_oprs = BOUND;

  for (let i = 1; i <= 6; i++) {
    min_oprs = Math.min(min_oprs, canMake(i));
  }

  return min_oprs === BOUND ? -1 : min_oprs;

  // Complexity analysis 
  // Time : O(6 * N) 
  // Space : O(1) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1007. Minimum Domino Rotations For Equal Row - https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description/?envType=daily-question&envId=2025-05-03 

  console.log(minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]));
  console.log(minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]));
};

// User function Template for javascript
/**
 * @param {Node} head
 * @returns {Node}
 */
/*
class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}
*/

class Problem2 {
  // Function to return all prime numbers in the given link list.
  primeList(head) {
    // code here
    const getMax = () => {
      let maxx = 0;
      let temp = head;
      while (temp) {
        maxx = Math.max(maxx, temp.val);
        temp = temp.next;
      }

      return maxx;
    };

    const MAXXT = 2 * getMax();

    const getPrime = () => {
      const primes = new Array(MAXXT).fill(true);
      for (let i = 2; i <= MAXXT; i++) {
        if (!primes[i]) continue;
        for (let j = i + i; j <= MAXXT; j += i) {
          primes[j] = false;
        }
      }

      primes[0] = primes[1] = false;

      return primes.reduce((acc, e, i) => {
        if (e) acc.push(i);
        return acc;
      }, []);
    };

    const primes = getPrime();

    // till now I have all primes from 1 to MAXX 
    // MAXX is the largest element or node value in linked list 

    let temp = head;

    while (temp) {
      const val = temp.val;

      const closestPrimeLeft = this.lte(primes, val); // less then or equal to val 
      const closestPrimeRight = this.gte(primes, val); // greater then or equal to val 

      const diff1 = val - closestPrimeLeft;
      const diff2 = closestPrimeRight - val;

      if (diff1 == diff2) {
        temp.val = Math.min(closestPrimeLeft, closestPrimeRight);
      } else if (diff1 < diff2) {
        temp.val = closestPrimeLeft;
      } else {
        temp.val = closestPrimeRight;
      }

      temp = temp.next;
    }

    return head;

    // Complexity analysis 
    // Time : O(N) + O(MAXXT * sqrt(MAXXT)) + O(N * Log(sqrt(MAXXT))) 
    // Space : O(sqrt(MAXXT)) 
  }

  lte(arr, key) {
    const N = arr.length;
    let ans = -1;
    let low = 0;
    let high = N - 1;

    while (low <= high) {
      let mid = low + Math.floor((high - low) / 2);

      if (arr[mid] <= key) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return arr[ans];
  }

  gte(arr, key) {
    const N = arr.length;
    let ans = -1;
    let low = 0;
    let high = N - 1;

    while (low <= high) {
      let mid = low + Math.floor((high - low) / 2);

      if (arr[mid] >= key) {
        ans = mid;
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    return arr[ans];
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Prime List - https://www.geeksforgeeks.org/problems/prime-list--170646/1 

  const printList = (head) => {
    let temp = head;
    while (temp) {
      console.log(temp.val);
      temp = temp.next;
    }
  };

  const head = {
    val: 1,
    next: {
      val: 2,
      next: {
        val: 1000,
        next: {
          val: 10000,
          next: null,
        },
      },
    },
  };
  printList(head);
  const nhead = new Problem2().primeList(head);
  printList(nhead);
};

(() => {
  // Day 3 of May 2025

  p1();

  p2();
})();
