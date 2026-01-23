from typing import List
import heapq


class Solution1:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # intuition:
        # array becomes non-decreasing when there are no "bad pairs"
        # where nums[i] > nums[i+1]
        # operation rule is fixed:
        # we MUST always merge the adjacent pair with minimum sum
        # (if tie, leftmost one)
        # idea:
        # track how many bad pairs exist in the array
        # each merge may:
        # - remove an existing bad pair
        # - create a new bad pair with left neighbor
        # - create a new bad pair with right neighbor
        # approach:
        # treat array like a doubly linked list using prevIndex & nextIndex
        # so that removals and neighbor access are O(1)
        # maintain a min-heap of (pair_sum, left_index)
        # this allows us to always pick the valid adjacent pair
        # with the minimum sum as required by the problem
        # since heap may contain stale entries (due to previous merges),
        # we lazily discard invalid pairs until we find a valid one
        # for every merge:
        # - update badPairs count by checking affected neighbors only
        # - merge second element into first
        # - relink neighbors
        # - push newly formed adjacent pairs into heap
        # stop condition:
        # when badPairs == 0, array is non-decreasing
        # result:
        # total number of merges performed is the answer

        N = len(nums)

        temp = [int(x) for x in nums]

        nextIndex = [i + 1 for i in range(N)]
        prevIndex = [i - 1 for i in range(N)]

        # min-heap instead of set
        heap = []

        badPairs = 0
        for i in range(N - 1):
            if temp[i] > temp[i + 1]:
                badPairs += 1
            heapq.heappush(heap, (temp[i] + temp[i + 1], i))

        operations_count = 0

        while badPairs > 0:
            # get valid minimum pair
            while True:
                pair_sum, first = heapq.heappop(heap)
                second = nextIndex[first]

                if (
                    second < N
                    and temp[first] is not None
                    and temp[second] is not None
                    and prevIndex[second] == first
                    and temp[first] + temp[second] == pair_sum
                ):
                    break

            first_left = prevIndex[first]
            second_right = nextIndex[second]

            if temp[first] > temp[second]:
                badPairs -= 1

            # {d, (a,b)}
            if first_left >= 0:
                if (
                    temp[first_left] > temp[first]
                    and temp[first_left] <= temp[first] + temp[second]
                ):
                    badPairs -= 1
                elif (
                    temp[first_left] <= temp[first]
                    and temp[first_left] > temp[first] + temp[second]
                ):
                    badPairs += 1

            # {(a,b), d}
            if second_right < N:
                if (
                    temp[second_right] >= temp[second]
                    and temp[second_right] < temp[first] + temp[second]
                ):
                    badPairs += 1
                elif (
                    temp[second_right] < temp[second]
                    and temp[second_right] >= temp[first] + temp[second]
                ):
                    badPairs -= 1

            # update heap & links
            if first_left >= 0:
                heapq.heappush(
                    heap, (temp[first_left] + temp[first] + temp[second], first_left)
                )

            if second_right < N:
                heapq.heappush(
                    heap, (temp[first] + temp[second] + temp[second_right], first)
                )
                prevIndex[second_right] = first

            nextIndex[first] = second_right
            temp[first] += temp[second]

            operations_count += 1

        return operations_count

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3510. Minimum Pair Removal to Sort Array II - https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/?envType=daily-question&envId=2026-01-23

    testcase = [
        [[5, 2, 3, 1], 2],
        [[1, 2, 2], 0],
        [[2, 2, -1, 3, -2, 2, 1, 1, 1, 0, -1], 9],
    ]

    for line in testcase:
        [nums, expected] = line
        s1 = Solution1()
        result = s1.minimumPairRemoval(nums)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:

    def get_next_greater_left(self, arr, N):
        next_greater_left = [0] * N
        stack = []

        for i in range(N):
            # pop all smaller elements
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()

            if stack:
                next_greater_left[i] = i - stack[-1] - 1
            else:
                next_greater_left[i] = i

            stack.append(i)

        return next_greater_left

    def get_next_greater_right(self, arr, N):
        next_greater_right = [0] * N
        stack = []

        for i in range(N - 1, -1, -1):
            # pop all smaller elements
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()

            if stack:
                next_greater_right[i] = stack[-1] - i - 1
            else:
                next_greater_right[i] = N - i - 1

            stack.append(i)

        return next_greater_right

    def maxPeople(self, arr):
        # code here
        # number of people ith person can see will be
        # continuous smaller height people on left + continuous smaller height people on right + 1
        # arr[] = [6, 2, 5, 4, 5, 1, 6]
        # answer[2] = 1 + 1 + 1
        # answer[0] = 0 + 5 + 1 (maximum)
        # we need to know how many people are smaller then on left
        # and how many people are smaller then on right
        # ie. we need to know index of first element greater then or equal to
        # ith index element on left and right
        # for this we can use monotonic stack

        N = len(arr)

        next_greater_left = self.get_next_greater_left(arr, N)
        next_greater_right = self.get_next_greater_right(arr, N)

        result = 0

        for i in range(N):
            interm = next_greater_left[i] + next_greater_right[i] + 1
            result = max(result, interm)

        return result

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Maximum People Visible in a Line - https://www.geeksforgeeks.org/problems/maximum-people-visible-in-a-line/1

    testcase = [
        [[6, 2, 5, 4, 5, 1, 6], 6],
        [[1, 3, 6, 4], 4],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.maxPeople(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 23 of January 2026

    p1()

    p2()
