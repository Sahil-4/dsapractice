from typing import Optional


class Solution1:
    def checkDivisibility(self, n: int) -> bool:
        digits_sum = 0
        digits_prod = 1

        for digit in str(n):
            digit_int = int(digit)
            digits_sum += digit_int
            digits_prod *= digit_int

        both_sum = digits_sum + digits_prod

        return n % both_sum == 0

        # Complexity analysis
        # Time : O(D)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 3622. Check Divisibility by Digit Sum and Product - https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/description/?envType=daily-question&envId=2026-08-22

    testcase = [
        [99, True],
        [23, False],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.checkDivisibility(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


# Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    @staticmethod
    def build(values: list) -> Optional["Node"]:
        """Level-order construction from a list (None = missing node)."""
        if not values:
            return None
        root = Node(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            if i < len(values) and values[i] is not None:
                node.left = Node(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = Node(values[i])
                queue.append(node.right)
            i += 1
        return root

    def to_list(self) -> list:
        """Level-order serialization for assertion comparison."""
        result, queue = [], [self]
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


class Solution2:
    def numberOfTurns(self, root: Optional[Node], p: int, q: int) -> int:
        # code here

        def find_lca(node, p, q):
            if not node:
                return None

            if node.data == p or node.data == q:
                return node

            left = find_lca(node.left, p, q)
            right = find_lca(node.right, p, q)

            if left and right:
                return node

            return left if left else right

        def find_path(node, target, path):
            if not node:
                return False

            if node.data == target:
                return True

            path.append("L")
            if find_path(node.left, target, path):
                return True
            path.pop()

            path.append("R")
            if find_path(node.right, target, path):
                return True
            path.pop()

            return False

        def count_turns(path):
            turns = 0

            for i in range(1, len(path)):
                if path[i] != path[i - 1]:
                    turns += 1

            return turns

        lca = find_lca(root, p, q)

        if not lca:
            return -1

        path_p = []
        path_q = []

        find_path(lca, p, path_p)
        find_path(lca, q, path_q)

        # If LCA is one of the nodes, there is no subtree change
        # at the LCA.
        if lca.data == p:
            turns = count_turns(path_q)
        elif lca.data == q:
            turns = count_turns(path_p)
        else:
            # Moving from p-side to q-side at LCA adds one turn.
            turns = count_turns(path_p) + count_turns(path_q) + 1

        return -1 if turns == 0 else turns

        # Complexity analysis
        # Time : O(N)
        # Space : O(H)


def p2():
    # Problem 2 : POTD Geeksforgeeks Number of Turns in Binary Tree - https://www.geeksforgeeks.org/problems/number-of-turns-in-binary-tree/1

    testcase = [
        [Node.build([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, 9, 10]), 5, 10, 4],
        [Node.build([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, 9, 10]), 1, 4, -1],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.numberOfTurns(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 22 of August 2026

    p1()

    p2()
