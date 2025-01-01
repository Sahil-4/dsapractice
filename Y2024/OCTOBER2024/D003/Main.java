public class Main {
    public static void main(String[] args) {
        // Day 3 of October

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 947. Most Stones Removed with Same Row or Column -
        // https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/maximum-stone-removal-1662179442/1

        int[][] stones = { { 0, 0 }, { 0, 1 }, { 1, 0 }, { 1, 2 }, { 2, 1 }, { 2, 2 } };
        int n = removeStones(stones);
        System.out.println(n);
    }

    static void dfs(int[][] stones, int index, boolean[] visited) {
        visited[index] = true;

        for (int i = 0; i < stones.length; i++) {
            int r = stones[index][0];
            int c = stones[index][1];

            if (!visited[i] && (stones[i][0] == r || stones[i][1] == c)) {
                dfs(stones, i, visited);
            }
        }
    }

    static int removeStones(int[][] stones) {
        // using dfs
        int n = stones.length;

        boolean[] visited = new boolean[n];

        int g = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(stones, i, visited);
                g++;
            }
        }

        return n - g;
    }
}