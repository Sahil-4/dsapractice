/**
 * @param {number} n
 * @param {number[][]} meetings
 * @return {number}
 */
var mostBooked = function (n, meetings) {
  const roomMeetingsCount = new Array(n).fill(0);

  const sortingComparator = (m1, m2) => {
    if (m1[0] !== m2[0]) return m1[0] - m2[0]; // meeting start time
    if (m1[1] !== m2[1]) return m1[1] - m2[1]; // meeting end time
    return 0;
  };
  const sortedMeetings = [...meetings];
  sortedMeetings.sort(sortingComparator);

  const occupiedRoomsComparator = (r1, r2) => {
    if (r1[0] !== r2[0]) return r1[0] - r2[0]; // meeting end time
    if (r1[1] !== r2[1]) return r1[1] - r2[1]; // room number
    return 0;
  };
  const occupiedRooms = new PriorityQueue(occupiedRoomsComparator);

  const availableRooms = new PriorityQueue((a, b) => a - b);
  for (let i = 0; i < n; i++) availableRooms.enqueue(i);

  for (const meeting of sortedMeetings) {
    const [start, end] = meeting;

    while (!occupiedRooms.isEmpty() && occupiedRooms.front()[0] <= start) {
      const [_, room] = occupiedRooms.dequeue();
      availableRooms.enqueue(room);
    }

    if (!availableRooms.isEmpty()) {
      const room = availableRooms.dequeue();
      occupiedRooms.enqueue([end, room]);
      roomMeetingsCount[room]++;
    } else {
      const [endj, room] = occupiedRooms.dequeue();
      const endi = endj + (end - start);
      occupiedRooms.enqueue([endi, room]);
      roomMeetingsCount[room]++;
    }
  }

  let minMeetRoom = 0;
  for (let i = 0; i < n; i++) {
    if (roomMeetingsCount[i] > roomMeetingsCount[minMeetRoom]) {
      minMeetRoom = i;
    }
  }

  return minMeetRoom;

  // Complexity analysis
  // Time : O(N) + O(N) + O(N * Log(N)) + O(N * Log(N)) + O(M * (N * Log(N) ~)) + O(N)
  // Space : O(N) + O(N) + O(N) + O(N)
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 2402. Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/description/?envType=daily-question&envId=2025-07-11

  console.log(
    mostBooked(2, [
      [0, 10],
      [1, 5],
      [2, 7],
      [3, 4],
    ])
  );
  console.log(
    mostBooked(3, [
      [1, 20],
      [2, 10],
      [3, 5],
      [4, 9],
      [6, 8],
    ])
  );
  console.log(
    mostBooked(3, [
      [1, 20],
      [2, 10],
      [3, 5],
      [4, 9],
      [6, 8],
      [8, 9],
      [9, 10],
    ])
  );
};

/**
 * @param number n
 * @returns number
 */
class Solution2 {
  countConsec(n) {
    // code here
    // IDEA : (using math)
    // find total number of binary string of length n, say "TN"
    // find the number of binary strings that do not contains consecutive ones
    // for a string to be like this it must have a 0 then any other bit,
    // or 1 then only 0 bit and goes till n (length)
    // this is similar to fibbonacci series fn(n) = fn(n-1) + fn(n-2)
    // fn(n-1), is the case we have fixed zero at current position
    // fn(n-2), is the case we have fixed one at current position, and want to have only zero bit next to this

    let TN = 1 << n; // total number of binary strings of length n

    // finding number of string without consecutive ones
    let prev = 1; // fn(0) - base
    let curr = 2; // fn(1) - base
    for (let i = 2; i <= n; i++) {
      let next = prev + curr;
      prev = curr;
      curr = next;
    }

    return TN - curr; // total string - strings with no consecutive ones

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Trail of ones - https://www.geeksforgeeks.org/problems/trail-of-ones3242/1

  const s2 = new Solution2();
  console.log(s2.countConsec(1));
  console.log(s2.countConsec(2));
  console.log(s2.countConsec(4));
  console.log(s2.countConsec(5));
  console.log(s2.countConsec(7));
  console.log(s2.countConsec(13));
  console.log(s2.countConsec(25));
  console.log(s2.countConsec(30));
};

(() => {
  // Day 11 of July 2025

  p1();

  p2();
})();
