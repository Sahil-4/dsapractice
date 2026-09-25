class Solution1:
    def braceExpansionII(self, expression: str) -> list[str]:
        N = len(expression)
        idx = 0

        def get_unit() -> set[str]:
            nonlocal idx

            if expression[idx] == "{":
                idx += 1  # Skip '{'
                result = perform_union()
                idx += 1  # Skip '}'
                return result

            ch = expression[idx]
            idx += 1  # Move past letter
            return {ch}

        def perform_concat() -> set[str]:
            nonlocal idx

            result = {""}

            while idx < N and (expression[idx] == "{" or expression[idx].isalpha()):
                temp = get_unit()
                result = {left + right for left in result for right in temp}

            return result

        def perform_union() -> set[str]:
            nonlocal idx

            result = set()

            while True:
                temp = perform_concat()
                result.update(temp)

                if idx < N and expression[idx] == ",":
                    idx += 1  # Skip ','
                else:
                    break

            return result

        final_set = perform_union()
        return sorted(list(final_set))

        # Complexity analysis
        # Time : O(W * L * log(W) + N)
        # Space : O(N + W * L)


def p1():
    # Problem 1 : POTD Leetcode 1096. Brace Expansion II - https://leetcode.com/problems/brace-expansion-ii/description/?envType=daily-question&envId=2026-09-25

    testcase = [
        [
            "{a,b}{c,{d,e}}",
            ["ac", "ad", "ae", "bc", "bd", "be"],
        ],
        [
            "{{a,z},a{b,c},{ab,z}}",
            ["a", "ab", "ac", "z"],
        ],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.braceExpansionII(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxHeight(self, da: list[int], db: list[int], dc: list[int]) -> int:
        # Code here

        N = len(da)
        boxes = []

        # generate all 3 valid base-height orientations for each box
        for i in range(N):
            d1, d2, d3 = da[i], db[i], dc[i]

            # orientation 1: height = d1, base = (max(d2, d3), min(d2, d3))
            boxes.append((d1, max(d2, d3), min(d2, d3)))

            # orientation 2: height = d2, base = (max(d1, d3), min(d1, d3))
            boxes.append((d2, max(d1, d3), min(d1, d3)))

            # orientation 3: height = d3, base = (max(d1, d2), min(d1, d2))
            boxes.append((d3, max(d1, d2), min(d1, d2)))

        # sort on width, length DESC
        # Format: (height, width, length)
        boxes.sort(key=lambda x: (x[1], x[2]), reverse=True)

        M = len(boxes)
        dp = [box[0] for box in boxes]
        # dp[i] represents the maximum stack height with boxes[i] at the top

        for i in range(M):
            h_i, w_i, l_i = boxes[i]

            for j in range(i):
                _, w_j, l_j = boxes[j]

                # Check strict base dimension constraint (box i placed on top of box j)
                if w_i < w_j and l_i < l_j:
                    dp[i] = max(dp[i], dp[j] + h_i)

        return max(dp) if dp else 0

        # Complexity analysis
        # Time : O(N^2)
        # Space : O(N)


def p2():
    # Problem 2 : POTD Geeksforgeeks Box Stacking - https://www.geeksforgeeks.org/problems/box-stacking/1

    testcase = [
        [[4, 1, 4, 10], [6, 2, 5, 12], [7, 3, 6, 32], 60],
        [[1, 4, 3], [2, 5, 4], [3, 6, 1], 15],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.maxHeight(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * (n + 1)

        for i in range(m - 2, -1, -1):
            dp_curr = [0] * (n + 1)

            for j in range(n - 1, -1, -1):
                dp_curr[j] = dp[j] + dp_curr[j + 1]

            dp = dp_curr

        return dp[0]

        # Complexity analysis
        # Time : O(N*M)
        # Space : O(N)


def p3():
    # Problem 3 : NC150 Leetcode 62. Unique Paths - https://leetcode.com/problems/unique-paths/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [3, 7, 28],
        [3, 2, 3],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s3 = Solution3()
        result = s3.uniquePaths(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 25 of September 2026

    p1()

    p2()

    p3()
