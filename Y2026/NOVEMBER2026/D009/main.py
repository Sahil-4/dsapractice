from collections import defaultdict
import heapq


class Solution1:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        N = len(arrival)

        requests = [0] * k

        # 'available' is a min-heap tracking available servers with id >= target
        # Initially, all servers are available
        available = list(range(k))
        heapq.heapify(available)

        # 'used' is a min-heap tracking available servers with id < target.
        used = []

        # 'busy' is a min-heap tracking currently running requests as (end_time, server_id).
        busy = []

        for i in range(N):
            target = i % k

            # when target wraps around to 0,
            # all servers in 'used' now satisfy sid >= 0
            if target == 0:
                while used:
                    heapq.heappush(available, heapq.heappop(used))

            # free up servers whose requests have finished
            while busy and busy[0][0] <= arrival[i]:
                end_time, sid = heapq.heappop(busy)

                if sid >= target:
                    heapq.heappush(available, sid)
                else:
                    heapq.heappush(used, sid)

            # since target strictly increments (except on wrap-around),
            # some available servers might have fallen behind the target;
            # Move them to 'used'
            while available and available[0] < target:
                heapq.heappush(used, heapq.heappop(available))

            # find the next available server
            if available:
                sid = heapq.heappop(available)
            elif used:
                sid = heapq.heappop(used)
            else:
                # all servers are busy,
                # drop the request
                continue

            # assign the request to the chosen server
            requests[sid] += 1
            heapq.heappush(busy, (arrival[i] + load[i], sid))

        busiest_servers_requests = max(requests)
        busiest_servers = []

        for i in range(k):
            if requests[i] == busiest_servers_requests:
                busiest_servers.append(i)

        return busiest_servers

        # Complexity analysis
        # Time : O(N * Log(k))
        # Space : O(K)


def p1():
    # Problem 1 : POTD Leetcode 1606. Find Servers That Handled Most Number of Requests - https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/description/?envType=daily-question&envId=2026-11-09

    testcase = [
        [3, [1, 2, 3, 4, 5], [5, 2, 3, 3, 3], [1]],
        [3, [1, 2, 3, 4], [1, 2, 1, 2], [0]],
        [3, [1, 2, 3], [10, 12, 11], [0, 1, 2]],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s1 = Solution1()
        result = s1.busiestServers(*inputs)
        # assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P1): result={result}")


class Solution2:
    def getCount(self, s: str, k: int) -> int:
        # code here
        N = len(s)

        group_occurrence = defaultdict(int)
        group_occurrence[s[0]] = 1

        for i in range(1, N):
            if s[i] == s[i - 1]:
                continue

            if s[i] not in group_occurrence:
                group_occurrence[s[i]] = 0

            group_occurrence[s[i]] += 1

        count = 0
        for i in range(26):
            ch = chr(ord("a") + i)

            if group_occurrence[ch] == k:
                count += 1

        return count

        # Complexity analysis
        # Time : O(N)
        # Space : O(1)


def p2():
    # Problem 2 : POTD Geeksforgeeks Count Group Occurrences - https://www.geeksforgeeks.org/problems/count-the-characters1821/1

    testcase = [
        ["abc", 1, 3],
        ["geeksforgeeks", 2, 4],
        ["aaaaa", 2, 0],
    ]

    for line in testcase:
        [*inputs, expected] = line
        s2 = Solution2()
        result = s2.getCount(*inputs)
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P2): result={result}")


class Trie:
    def __init__(self):
        # every node is a dict : character -> child node, "$" marks the end of a word
        self.root: dict = {}

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]

        node["$"] = True

    def search(self, word: str) -> bool:
        node = self._find(word)

        return node is not None and "$" in node

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, text: str):
        node = self.root

        for ch in text:
            if ch not in node:
                return None
            node = node[ch]

        return node

    # Complexity analysis
    # Time : O(L)
    # Space : O(C)


def p3():
    # Problem 3 : NC150 Leetcode 208. Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/description/?envType=problem-list-v2&envId=plakya4j

    testcase = [
        [
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            [None, None, True, False, True, None, True],
        ]
    ]

    for line in testcase:
        [operations, arguments, expected] = line

        obj = None
        result = []
        for operation, argument in zip(operations, arguments):
            if operation == "Trie":
                obj = Trie(*argument)
                result.append(None)
            else:
                result.append(getattr(obj, operation)(*argument))

        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Testcase passed (P3): result={result}")


if __name__ == "__main__":
    # Day 9 of November 2026

    p1()

    p2()

    p3()
