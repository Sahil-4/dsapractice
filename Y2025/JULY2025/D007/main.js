/**
 * @param {number[][]} events
 * @return {number}
 */
var maxEvents = function (events) {
  // IDEA :
  // we will have a min heap to store end day of events
  // if any event(s) starts from today we will put its end day in min heap
  // and attend event in order (they are ending)
  // if we cannot able to attend any event, we will remove it from min heap

  // sort events - [startDay, endDay]
  const comparator = (e1, e2) => (e1[0] !== e2[0] ? e1[0] - e2[0] : e1[1] - e2[1]);
  const events_sorted = [...events].sort(comparator);

  const N = events_sorted.length;

  let count = 0; // number of events attended
  let it = 0; // iterator to iterate over events array (sorted events)
  let currentDay = 0; // current day
  // in this priority queue we will store end day of event (which started on current day, when any events is already completed we will remove it this means we were not able to attend that event)
  const pendingEvents = new PriorityQueue((d1, d2) => d1 - d2);

  while (!pendingEvents.isEmpty() || it < N) {
    if (pendingEvents.isEmpty()) {
      // move day - there were no events in past, or they already got complted
      currentDay = events_sorted[it][0];
    }

    // add endDay of all events in queue that started today (current day)
    while (it < N && events_sorted[it][0] === currentDay) {
      pendingEvents.enqueue(events_sorted[it][1]);
      it++;
    }

    // attend one event today - that will end first
    pendingEvents.dequeue();
    currentDay++;
    count++;

    // remove all events which we cannot attend now - events that ended on past days
    while (!pendingEvents.isEmpty() && pendingEvents.front() < currentDay) {
      pendingEvents.dequeue();
    }
  }

  return count;

  // Complexity analysis
  // Time : O(N * Log(N)) + O(N)
  // Space : O(N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1353. Maximum Number of Events That Can Be Attended - https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/?envType=daily-question&envId=2025-07-07

  console.log(maxEvents([[1, 2], [2, 3],[3, 4]]));
  console.log(maxEvents([[1, 2], [2, 3],[3, 4], [1, 2]]));
  console.log(maxEvents([[1, 4], [2, 3],[3, 3], [1, 1]]));
  console.log(maxEvents([[1, 4], [2, 3],[4, 4], [1, 3]]));
  console.log(maxEvents([[1, 5], [1, 5],[1, 5], [2, 3], [2, 3]]));
};

class Solution2 {
  nextLargerElement(arr) {
    // code here
    const N = arr.length;

    const nge = new Array(N).fill(-1);

    const stack = [];

    for (let i = 2 * N - 1; i >= 0; i--) {
      const index = i % N;

      while (stack.length && stack.at(-1) <= arr[index]) stack.pop();

      nge[index] = !stack.length ? -1 : stack.at(-1);

      stack.push(arr[index]);
    }

    return nge;

    // Complexity analysis
    // Time : O(4N)
    // Space : O(2N)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Next Greater Element in Circular Array - https://www.geeksforgeeks.org/problems/next-greater-element/1

  const s2 = new Solution2();
  console.log(s2.nextLargerElement([1, 3, 2, 4])); // [3, 4, 4, -1]
  console.log(s2.nextLargerElement([1, 2, 1, 3, 4])); // [2, 3, 3, 4, -1]
  console.log(s2.nextLargerElement([5, 4, 3, 2, 1])); // [-1, 5, 5, 5, 5]
  console.log(s2.nextLargerElement([1, 2, 3, 4, 5])); // [2, 3, 4, 5, -1]
};

(() => {
  // Day 7 of July 2025

  p1();

  p2();
})();
