from typing import List


class Solution1:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()

        queue = [start]
        visited.add(start)

        while queue:
            current = queue.pop(0)

            if arr[current] == 0:
                return True

            left = current - arr[current]
            right = current + arr[current]

            if left >= 0 and left not in visited and left < len(arr):
                queue.append(left)
                visited.add(left)

            if right >= 0 and right not in visited and right < len(arr):
                queue.append(right)
                visited.add(right)

        return False

        # Complexity analysis:
        # Time : O(2N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 1306. Jump Game III - https://leetcode.com/problems/jump-game-iii/description/?envType=daily-question&envId=2026-05-17

    testcase = [
        [[4, 2, 3, 0, 3, 1, 2], 5, True],
        [[4, 2, 3, 0, 3, 1, 2], 0, True],
        [[3, 0, 2, 1, 2], 2, False],
    ]

    for line in testcase:
        [arr, start, expected] = line
        s1 = Solution1()
        result = s1.canReach(arr, start)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        # code here
        def is_beautiful_pair(e1: int, e2: int) -> bool:
            pos = e1 >= 0 and e2 >= 0
            neg = e1 < 0 and e2 < 0
            return pos or neg

        ans = []

        for item in arr:
            if not ans or is_beautiful_pair(ans[-1], item):
                ans.append(item)
            else:
                ans.pop()

        return ans

        # Complexity analysis:
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Make the array beautiful - https://www.geeksforgeeks.org/problems/make-the-array-beautiful--170647/1

    testcase = [
        [[4, 2, -2, 1], [4, 1]],
        [[2, -2, -1, 1], []],
        [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0]],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.makeBeautiful(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 17 of May 2026

    p1()

    p2()
