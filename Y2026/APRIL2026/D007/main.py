from typing import List


class Robot:

    def __init__(self, width: int, height: int):
        self.curr_index = 0
        self.has_moved = False
        self.path = []  # list of [x, y, direction]

        # bottom row: move right - # East
        for x in range(width):
            self.path.append([x, 0, 0])

        # right side: move up - # North
        for y in range(1, height):
            self.path.append([width - 1, y, 1])

        # top row: move left - # West
        for x in range(width - 2, -1, -1):
            self.path.append([x, height - 1, 2])

        # left side: move down - # South
        for y in range(height - 2, 0, -1):
            self.path.append([0, y, 3])

        # fix direction at (0,0) after a full loop
        self.path[0][2] = 3  # South

    def step(self, num: int) -> None:
        self.has_moved = True
        self.curr_index = (self.curr_index + num) % len(self.path)

    def getPos(self) -> List[int]:
        x, y, _ = self.path[self.curr_index]
        return [x, y]

    def getDir(self) -> str:
        if not self.has_moved:
            return "East"

        direction = self.path[self.curr_index][2]

        if direction == 0:
            return "East"
        elif direction == 1:
            return "North"
        elif direction == 2:
            return "West"
        else:
            return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()


def p1():
    # Problem 1 : POTD Leetcode 2069. Walking Robot Simulation II - https://leetcode.com/problems/walking-robot-simulation-ii/description/?envType=daily-question&envId=2026-04-07

    testcase = [
        [
            [
                "Robot",
                "step",
                "step",
                "getPos",
                "getDir",
                "step",
                "step",
                "step",
                "getPos",
                "getDir",
            ],
            [[6, 3], [2], [2], [], [], [2], [1], [4], [], []],
            [None, None, None, [4, 0], "East", None, None, None, [1, 2], "West"],
        ],
    ]

    for line in testcase:
        commands, args, expected = line

        obj: Robot | None = None
        result = []

        for cmd, arg in zip(commands, args):
            if cmd == "Robot":
                obj = Robot(*arg)
                result.append(None)
            elif cmd == "step":
                assert obj is not None
                obj.step(*arg)
                result.append(None)
            elif cmd == "getPos":
                assert obj is not None
                result.append(obj.getPos())
            elif cmd == "getDir":
                assert obj is not None
                result.append(obj.getDir())

        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def stableMarriage(self, men: List[List[int]], women: List[List[int]]):
        # code here

        n = len(men)

        rank = [[0] * n for _ in range(n)]

        for w in range(n):
            for i, m in enumerate(women[w]):
                rank[w][m] = i

        # woman prefers m2 over current partner m1
        def prefers(w: int, m2: int, m1: int) -> bool:
            return rank[w][m2] < rank[w][m1]

        # women current partner
        w_partner = [-1] * n

        # man current partner
        m_partner = [-1] * n

        # next proposal index
        next_proposal = [0] * n

        # free man
        free_man = [True] * n

        free_count = n

        while free_count > 0:
            m = next((m for m in range(n) if free_man[m]), None)

            if m is None:
                break

            w = men[m][next_proposal[m]]
            next_proposal[m] += 1

            # w is free
            if w_partner[w] == -1:
                w_partner[w] = m
                m_partner[m] = w
                free_man[m] = False
                free_count -= 1
            else:
                m1 = w_partner[w]

                # w prefers m over current partner
                if prefers(w, m, m1):
                    w_partner[w] = m
                    m_partner[m] = w

                    free_man[m] = False
                    free_man[m1] = True

        return m_partner

        # Complexity analysis
        # Time : O(N^2)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Stable Marriage Problem - https://www.geeksforgeeks.org/problems/stable-marriage-problem/1

    testcase = [
        [
            2,
            [[0, 1], [0, 1]],
            [[0, 1], [0, 1]],
            [0, 1],
        ],
        [
            3,
            [[0, 1, 2], [0, 1, 2], [0, 1, 2]],
            [[2, 1, 0], [2, 1, 0], [2, 1, 0]],
            [2, 1, 0],
        ],
    ]

    for line in testcase:
        [n, men, women, expected] = line
        s2 = Solution2()
        result = s2.stableMarriage(men, women)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 7 of April 2026

    p1()

    p2()
