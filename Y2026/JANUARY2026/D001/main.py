from typing import List


class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        # reverse digits, now least significant number -> most significant number
        # create new array output = []
        # init carry = 1
        # start from i = 0 to i < len(digits)
        # sum = digits[i] + carry
        # output.append(sum % 10)
        # carry = sum // 10
        # return output

        digits.reverse()

        output = []
        carry = 1
        for digit in digits:
            sum = digit + carry
            carry = sum // 10
            output.append(sum % 10)

        while carry > 0:
            sum = carry
            carry = sum // 10
            output.append(sum % 10)

        output.reverse()
        digits.reverse()

        return output

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 66. Plus One - https://leetcode.com/problems/plus-one/description/?envType=daily-question&envId=2026-01-01

    testcase = [
        [[1, 2, 3], [1, 2, 4]],
        [[4, 3, 2, 1], [4, 3, 2, 2]],
        [[9], [1, 0]],
    ]

    for line in testcase:
        [digits, expected] = line
        s1 = Solution1()
        result = s1.plusOne(digits)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def attach_at_tail(self, list):
        ptr = self
        while ptr.next:
            ptr = ptr.next

        ptr.next = list

    @classmethod
    def build_ll(cls, arr):
        head = Node(arr[0])
        curr = head
        for x in arr[1:]:
            curr.next = Node(x)
            curr = curr.next
        return head

    @classmethod
    def ll_to_list(cls, head):
        res = []
        while head:
            res.append(head.data)
            head = head.next
        return res


class Solution2:
    def intersectPoint(self, head1: Node, head2: Node) -> Node:
        # code here
        # use two pointers p1 and p2
        # p1 starts from head1, p2 starts from head2
        # traverse both lists
        # when p1 reaches end, move it to head2
        # when p2 reaches end, move it to head1
        # this way both pointers cover equal distance
        # the point where p1 == p2 is the intersection node

        p1, p2 = head1, head2

        while p1 is not p2:
            p1 = p1.next if p1 else head2
            p2 = p2.next if p2 else head1

        return p1

        # Complexity analysis
        # Time : O(N + M)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Intersection in Y Shaped Lists - https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1

    testcase = [
        [[10], [3, 6, 9], [15, 30], 15],
        [[4], [5, 6], [1, 8, 5], 1],
    ]

    for line in testcase:
        [arr1, arr2, arr3, expected] = line
        s2 = Solution2()
        head1, head2, common = (
            Node.build_ll(arr1),
            Node.build_ll(arr2),
            Node.build_ll(arr3),
        )
        head1.attach_at_tail(common)
        head2.attach_at_tail(common)
        result = s2.intersectPoint(head1, head2)
        assert (
            result.data == expected
        ), f"Test failed: expected {expected}, got {result.data}"
        print(f"Testcase passed (P2): result={result.data}")


if __name__ == "__main__":
    # Day 1 of January 2026

    p1()

    p2()
