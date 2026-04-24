class Solution1:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # "L" - go left
        # "R" - go right
        # "_" - free will for left and right

        point = 0  # where am I standing currently
        dashes = 0  # how many dashes I have, how further I can go in any direction - free will
        for move in moves:
            if move == "L":
                point -= 1
            elif move == "R":
                point += 1
            else:
                dashes += 1

        # go to right with free will
        x = point + dashes
        # go to left with free will
        y = point - dashes

        # return whichever is furthest
        return max(abs(x), abs(y))

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p1():
    # Problem 1 : POTD Leetcode 2833. Furthest Point From Origin - https://leetcode.com/problems/furthest-point-from-origin/description/?envType=daily-question&envId=2026-04-24

    testcase = [
        ["L_RL__R", 3],
        ["_R__LL_", 5],
        ["_______", 7],
    ]

    for line in testcase:
        [moves, expected] = line
        s1 = Solution1()
        result = s1.furthestDistanceFromOrigin(moves)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def visibleBuildings(self, arr):
        # code here
        N = len(arr)

        prev = arr[0]
        count = 1

        for i in range(1, N):
            if arr[i] >= prev:
                count += 1

            prev = max(prev, arr[i])

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Buildings with Sunlight - https://www.geeksforgeeks.org/problems/buildings-receiving-sunlight3032/1

    testcase = [
        [[6, 2, 8, 4, 11, 13], 4],
        [[2, 5, 1, 8, 3], 3],
        [[3, 3, 3, 1], 3],
    ]

    for line in testcase:
        [arr, expected] = line
        s2 = Solution2()
        result = s2.visibleBuildings(arr)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 24 of April 2026

    p1()

    p2()
