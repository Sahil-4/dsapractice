class Solution1:
    def generateString(self, str1: str, str2: str) -> str:

        n = len(str1)
        m = len(str2)

        N = n + m - 1
        word = [""] * N

        can_change = [False] * N

        # process "T"
        for i in range(n):
            if str1[i] == "T":
                for j in range(m):
                    if word[i + j] != "" and word[i + j] != str2[j]:
                        return ""
                    word[i + j] = str2[j]

        # remaining spaces with "a"
        for i in range(N):
            if word[i] == "":
                word[i] = "a"
                can_change[i] = True

        # process "F"
        for i in range(n):
            if str1[i] == "F":
                same = True
                for j in range(m):
                    if str2[j] != word[i + j]:
                        same = False
                if not same:
                    continue

                change = False
                for k in range(i + m - 1, i - 1, -1):
                    if can_change[k]:
                        word[k] = "b"
                        change = True
                        break

                if not change:
                    return ""

        return "".join(word)

        # Complexity analysis
        # Time : O(N)
        # Space : O(N)


def p1():
    # Problem 1 : POTD Leetcode 3474. Lexicographically Smallest Generated String - https://leetcode.com/problems/lexicographically-smallest-generated-string/description/?envType=daily-question&envId=2026-03-31

    testcase = [
        ["TFTF", "ab", "ababa"],
        ["TFTF", "abc", ""],
        ["F", "d", "a"],
    ]

    for line in testcase:
        [str1, str2, expected] = line
        s1 = Solution1()
        result = s1.generateString(str1, str2)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def maxProfit(self, arr, k):
        # Code here

        N = len(arr)

        prev = [0 for _ in range(2)]

        for i in range(N - 1, -1, -1):
            curr = [0 for _ in range(2)]

            buy = -arr[i] + prev[1]
            not_buy = prev[0]
            buy_profit = max(buy, not_buy)

            sell = -k + arr[i] + prev[0]
            not_sell = prev[1]
            sell_profit = max(sell, not_sell)

            curr[0] = buy_profit
            curr[1] = sell_profit

            prev = curr

        return prev[0]

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Buy Stock with Transaction Fee - https://www.geeksforgeeks.org/problems/buy-stock-with-transaction-fee/1

    testcase = [
        [[6, 1, 7, 2, 8, 4], 2, 8],
        [[7, 1, 5, 3, 6, 4], 1, 5],
    ]

    for line in testcase:
        [arr, k, expected] = line
        s2 = Solution2()
        result = s2.maxProfit(arr, k)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


if __name__ == "__main__":
    # Day 31 of March 2026

    p1()

    p2()
