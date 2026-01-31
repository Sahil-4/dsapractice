from typing import List


class Solution1:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # use binary search

        N = len(letters)

        low = 0
        high = N - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if letters[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return letters[ans if ans != -1 else 0]

        # Complexity analysis
        # Time : O(Log(N))
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 744. Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/?envType=daily-question&envId=2026-01-31

    testcase = [
        [["c", "f", "j"], "a", "c"],
        [["c", "f", "j"], "c", "f"],
        [["x", "x", "y", "y"], "z", "x"],
    ]

    for line in testcase:
        [letters, target, expected] = line
        s1 = Solution1()
        result = s1.nextGreatestLetter(letters, target)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class kQueues:
    def __init__(self, n, k):
        # Initialize your data members

        self.n = n  # size of array
        self.k = k  # number of queues

        self.arr = [0] * n  # array to store queue data
        self.next = list(range(1, n)) + [
            -1
        ]  # store next free slot or next item of current item queue
        self.front = [-1] * k  # stores front pointer of queues
        self.rear = [-1] * k  # stores rear pointer of queues

        self.freeSpot = 0  # first free slot index

    def isFull(self):
        # Check if array is full

        # there are no free slots
        return self.freeSpot == -1

    def isEmpty(self, i):
        # Check if queue i is empty

        # front pointer of ith queue is pointing to -1
        return self.front[i - 1] == -1

    def enqueue(self, x, i):
        # Enqueue element x into queue number i

        if self.isFull():
            # overflow
            return

        index = self.freeSpot
        self.freeSpot = self.next[
            index
        ]  # first free slot = next free slot of current free slow

        if self.front[i - 1] == -1:
            # first item in ith queue
            self.front[i - 1] = index
        else:
            self.next[self.rear[i - 1]] = index

        self.next[index] = -1  # update next item index of current item queue
        self.rear[i - 1] = index  # update rear pointer
        self.arr[index] = x  # update item value

    def dequeue(self, i):
        # Dequeue element from queue number i

        if self.isEmpty(i):
            # underflow
            return -1

        index = self.front[i - 1]
        self.front[i - 1] = self.next[index]

        self.next[index] = self.freeSpot
        self.freeSpot = index

        return self.arr[index]

    # Complexity analysis - of operations
    # Time : O(1)
    # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Implement k Queues in a Single Array - https://www.geeksforgeeks.org/problems/implement-k-queues-in-a-single-array/1

    # TC1
    n = 4
    k = 2
    queries = [
        [1, 5, 0],
        [1, 3, 0],
        [1, 1, 1],
        [2, 0],
        [1, 4, 1],
        [1, 1, 0],
        [3, 1],
        [4],
    ]
    expected = [5, False, True]

    q = kQueues(n, k)
    output = []

    for query in queries:
        if query[0] == 1:
            _, x, i = query
            q.enqueue(x, i + 1)
        elif query[0] == 2:
            _, i = query
            output.append(q.dequeue(i + 1))
        elif query[0] == 3:
            _, i = query
            output.append(q.isEmpty(i + 1))
        elif query[0] == 4:
            output.append(q.isFull())

    assert output == expected, f"Test 1 failed: expected {expected}, got {output}"
    print("Test 1 passed")

    # TC2
    n = 6
    k = 3
    queries = [
        [1, 3, 2],
        [2, 0],
        [1, 2, 1],
        [3, 2],
    ]
    expected = [-1, False]

    q = kQueues(n, k)
    output = []

    for query in queries:
        if query[0] == 1:
            _, x, i = query
            q.enqueue(x, i + 1)
        elif query[0] == 2:
            _, i = query
            output.append(q.dequeue(i + 1))
        elif query[0] == 3:
            _, i = query
            output.append(q.isEmpty(i + 1))

    assert output == expected, f"Test 2 failed: expected {expected}, got {output}"
    print("Test 2 passed")


if __name__ == "__main__":
    # Day 31 of January 2026

    p1()

    p2()
