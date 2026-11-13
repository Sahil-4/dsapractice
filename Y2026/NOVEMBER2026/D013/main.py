from collections import deque
from typing import Any, Optional


class Solution1:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        N = len(nums)

        # prefix sum array to instantly calculate the sum of any subarray nums[i...j]
        pref_nums = [0] * (N + 1)
        for i in range(N):
            pref_nums[i + 1] = pref_nums[i] + nums[i]

        stack = []  # tuple structure: (start_idx, value, cumulative_area_till_end)
        ans = 0

        j = N - 1  # right pointer

        # calculates total operations required to make nums[start_i...end_j] non decreasing
        def get_cost(start_i: int, end_j: int) -> int:

            # binary search to find which maximum block in the stack covers the index end_j

            left, right = 0, len(stack) - 1
            block_idx = -1

            while left <= right:
                mid = (left + right) // 2

                if stack[mid][0] <= end_j:
                    block_idx = mid
                    right = mid - 1  # Look for an even smaller index bound if possible

                else:
                    left = mid + 1

            start_idx, val, _ = stack[block_idx]
            next_idx = stack[block_idx - 1][0] if block_idx > 0 else N
            area_after = stack[block_idx - 1][2] if block_idx > 0 else 0

            # area of the prefix maxes from (end_j + 1) to the end of the array
            sum_max_after_j = val * (next_idx - (end_j + 1)) + area_after

            # total area of prefix maxes exactly from start_i to end_j
            sum_max_i_to_j = stack[-1][2] - sum_max_after_j

            # actual sum of elements from start_i to end_j
            sum_nums_i_to_j = pref_nums[end_j + 1] - pref_nums[start_i]

            # operations required = target maximums sum - existing sum
            return sum_max_i_to_j - sum_nums_i_to_j

        # traverse right to left
        for i in range(N - 1, -1, -1):
            val = nums[i]

            # remove blocks that get completely dominated by the current nums[i]
            while stack and stack[-1][1] <= val:
                stack.pop()

            next_idx = stack[-1][0] if stack else N
            area_after = stack[-1][2] if stack else 0

            # add the new block for current index i
            new_area = val * (next_idx - i) + area_after
            stack.append((i, val, new_area))

            # two-pointers: shrink window from the right if the current configuration exceeds k
            while j >= i and get_cost(i, j) > k:
                j -= 1

            # all subarrays starting at i and ending anywhere up to j are valid
            if j >= i:
                ans += j - i + 1

        return ans

        # Complexity analysis
        # Time : O(N * Log(N))
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3420. Count Non-Decreasing Subarrays After K Operations - https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/description/?envType=daily-question&envId=2026-11-13

    testcase = [
        [[6, 3, 1, 2, 4, 4], 7, 17],
        [[6, 3, 1, 3, 6], 4, 12],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.countNonDecreasingSubarrays(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


# Structure of a Binary Search Tree node
class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def from_list(arr: list[Optional[int]]) -> Optional["Node"]:
        if not arr or arr[0] is None:
            return None

        root = Node(arr[0])
        q: deque[Node] = deque([root])

        i = 1
        while q and i < len(arr):
            node = q.popleft()

            if i < len(arr):
                data = arr[i]
                if data is not None:
                    node.left = Node(data)
                    q.append(node.left)
                i += 1

            if i < len(arr):
                data = arr[i]
                if data is not None:
                    node.right = Node(data)
                    q.append(node.right)
                i += 1

        return root

    def to_list(self) -> list[Any]:
        result = []
        q: deque[Optional[Node]] = deque([self])

        while q:
            node = q.popleft()

            if node:
                result.append(node.data)
                q.append(node.left)
                q.append(node.right)
            else:
                result.append(None)

        # remove trailing None values
        while result and result[-1] is None:
            result.pop()

        return result


class Solution2:
    def findCommon(self, r1: "Node", r2: "Node") -> list[int]:
        # code here
        intersection = []
        stack1, stack2 = [], []

        root1 = r1
        root2 = r2

        while True:
            # Traverse to the leftmost node for both trees
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left

            # If either stack is empty, we are done
            if not stack1 or not stack2:
                break

            node1 = stack1[-1]
            node2 = stack2[-1]

            # Compare the top elements
            if node1.data == node2.data:
                intersection.append(node1.data)
                stack1.pop()
                stack2.pop()
                # Move to the right subtrees
                root1 = node1.right
                root2 = node2.right

            elif node1.data < node2.data:
                stack1.pop()
                root1 = node1.right

            else:
                stack2.pop()
                root2 = node2.right

        return intersection

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(H1 + H2)


def p2():
    # Problem 2 : POTD Geeksforgeeks Common Nodes in Two BSTs - https://www.geeksforgeeks.org/problems/print-common-nodes-in-bst/1

    testcase = [
        [
            Node.from_list([5, 1, 10, 0, 4, 7, None, None, None, None, None, None, 9]),
            Node.from_list([10, 7, 20, 4, 9, None, None]),
            [4, 7, 9, 10],
        ],
        [
            Node.from_list([10, 2, 11, 1, 3, None, None]),
            Node.from_list([2, 1, 3]),
            [1, 2, 3],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.findCommon(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def _rob(self, nums: list[int]) -> int:
        N = len(nums)

        dp = [0] * (N + 1)
        dp[N], dp[N - 1] = 0, nums[N - 1]

        for i in range(N - 2, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        return max(dp)

    def rob(self, nums: list[int]) -> int:
        c1 = self._rob(nums[1:])
        c2 = self._rob(nums[:-1])

        return max(c1, c2)

        # Complexity analysis
        # Time : O(2N)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 213. House Robber II - https://leetcode.com/problems/house-robber-ii/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [[2, 3, 2], 3],
        [[1, 2, 3, 1], 4],
        [[1, 2, 3], 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.rob(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 13 of November 2026

    p1()

    p2()

    p3()
