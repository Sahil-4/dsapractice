class Solution1 {
  /**
   * @param {number} eventTime
   * @param {number} k
   * @param {number[]} startTime
   * @param {number[]} endTime
   * @return {number}
   */
  __maxFreeTime__(eventTime, k, startTime, endTime) {
    const N = startTime.length;

    const breaks = [];
    for (let i = 0, t = 0; i <= N; i++) {
      if (i === N) {
        breaks.push(eventTime - t);
        break;
      }

      breaks.push(startTime[i] - t);
      t = endTime[i];
    }

    let mwlen = 0;
    for (let i = 0, wlen = 0; i < breaks.length; i++) {
      wlen += breaks[i];
      mwlen = Math.max(mwlen, wlen);

      if (i >= k) wlen -= breaks[i - k];
    }

    return mwlen;

    // Complexity analysis
    // Time : O(2N)
    // Space : O(N)
  }

  /**
   * @param {number} eventTime
   * @param {number} k
   * @param {number[]} startTime
   * @param {number[]} endTime
   * @return {number}
   */
  maxFreeTime(eventTime, k, startTime, endTime) {
    const N = startTime.length;

    let mwlen = 0;

    for (let i = 0, wlen = 0; i <= N; i++) {
      // expand window
      const ti = i === 0 ? 0 : endTime[i - 1];
      const breaksi = i === N ? eventTime - ti : startTime[i] - ti;
      wlen += breaksi;

      mwlen = Math.max(mwlen, wlen);

      // shrink window
      if (i >= k) {
        const tik = i - k === 0 ? 0 : endTime[i - k - 1];
        const breaksik = startTime[i - k] - tik;
        wlen -= breaksik;
      }
    }

    return mwlen;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
}

const p1 = () => {
  // Problem 1 : POTD Leetcode 3439. Reschedule Meetings for Maximum Free Time I - https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/description/?envType=daily-question&envId=2025-07-09

  const s1 = new Solution1();
  console.log(s1.maxFreeTime(5, 1, [1, 3], [2, 5])); // Output: 2
  console.log(s1.maxFreeTime(10, 1, [0, 2, 9], [1, 4, 10])); // Output: 6
  console.log(s1.maxFreeTime(5, 2, [0, 1, 2, 3, 4], [1, 2, 3, 4, 5])); // Output: 0
  console.log(s1.maxFreeTime(10, 2, [1, 2, 4, 7, 9], [2, 4, 5, 8, 10])); // Output: 3
};

class Solution2 {
  sumSubMins(arr) {
    // code here
    // arr = [3, 1, 2, 4]
    // sml = [-1, -1, 1, 2]
    // smr = [1, N, N, N]
    // sum += (i - l) * (r - i)

    const N = arr.length;

    const nextSmall = (I, s, e, inc, fn) => {
      // const I = -1; // initial/default value
      // const s = 0; // start index
      // const e = N; // end or termination point
      // const inc = +1; // increment value
      // const fn = (a, b) => a >= b; // function to compare stack top with arr[i]

      const out = new Array(N);
      const stack = [];

      for (let i = s; i != e; i += inc) {
        while (stack.length && fn(stack.at(-1)[0], arr[i])) stack.pop();

        if (stack.length) out[i] = stack.at(-1)[1];
        else out[i] = I;

        stack.push([arr[i], i]);
      }

      return out;
    };

    const sml = nextSmall(-1, 0, N, +1, (a, b) => a >= b);
    const smr = nextSmall(N, N - 1, -1, -1, (a, b) => a > b);

    let sum = 0;

    for (let i = 0; i < N; i++) {
      const count = (i - sml[i]) * (smr[i] - i);
      const contri = count * arr[i];
      sum += contri;
    }

    return sum;

    // Complexity analysis
    // Time : O(2 * 2N) + O(N)
    // Space : O(2N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Sum of subarray minimum - https://www.geeksforgeeks.org/problems/sum-of-subarray-minimum/1

  const s2 = new Solution2();
  console.log(s2.sumSubMins([3, 1, 2, 4])); // Output: 17
  console.log(s2.sumSubMins([1, 2, 3, 4])); // Output: 20
  console.log(s2.sumSubMins([1, 1, 1])); // Output: 6
};

(() => {
  // Day 9 of July 2025

  p1();

  p2();
})();
