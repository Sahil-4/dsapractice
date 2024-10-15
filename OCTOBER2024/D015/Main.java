import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // Day 15 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 778. Swim in Rising Water -
        // https://leetcode.com/problems/swim-in-rising-water/

        int[][] grid = {
                { 0, 1, 2, 3, 4 },
                { 24, 23, 22, 21, 5 },
                { 12, 13, 14, 15, 16 },
                { 11, 17, 18, 19, 20 },
                { 10, 9, 8, 7, 6 }
        };

        int t = swimInWater(grid);
        System.out.println(t);
    }

    static int[] DROWS = { -1, 0, +1, 0 };
    static int[] DCOLS = { 0, -1, 0, +1 };

    static boolean isValidIndex(int r, int c, int N) {
        return ((r >= 0 && r < N) && (c >= 0 && c < N));
    }

    static boolean dfs(int[][] grid, boolean[][] visited, int row, int col, int N, int time) {
        // cant move through this - required more time
        if (time < grid[row][col]) {
            return false;
        }

        // reached to destination - reached last cell
        if (row == N - 1 && col == N - 1) {
            return true;
        }

        // mark current cell visited
        visited[row][col] = true;

        // try moving in all 4 directions
        for (int i = 0; i < 4; i++) {
            int nrow = row + DROWS[i];
            int ncol = col + DCOLS[i];

            // invalid index - cant go to this cell
            if (!isValidIndex(nrow, ncol, N)) {
                continue;
            }

            // already visited cell - no need to go to this cell
            if (visited[nrow][ncol]) {
                continue;
            }

            // move to [nrow][ncol] cell
            boolean check = dfs(grid, visited, nrow, ncol, N, time);
            if (check) {
                // return true if we can reach to last cell
                return true;
            }
        }

        // unable to reach to last cell
        return false;
    }

    static int swimInWater(int[][] grid) {
        // --- binary search & DFS ---

        int N = grid.length;

        int low = 0;
        int high = N * N - 1;

        while (low < high) {
            int mid = low + ((high - low) / 2);

            boolean[][] visited = new boolean[N][N];

            boolean check = dfs(grid, visited, 0, 0, N, mid);

            if (check) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        return low;

        // Complexity analysis
        // Time : O(log(N*N)) * O(N*N)
        // Space : O(N*N) visited array + O(N + N) stack space
    }

    static void p2() {
        // Problem 2 : Geeksforgeeks Directed Graph Cycle -
        // https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

        int V = 6;
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        adj.add(new ArrayList<>(Arrays.asList(5, 3)));
        adj.add(new ArrayList<>(Arrays.asList(3, 1)));
        adj.add(new ArrayList<>(Arrays.asList(1, 2)));
        adj.add(new ArrayList<>(Arrays.asList(2, 4)));
        adj.add(new ArrayList<>(Arrays.asList(4, 0)));

        boolean cycle = isCyclic(V, adj);
        System.out.println(cycle);
    }

    static boolean isCycle(ArrayList<ArrayList<Integer>> adj, int current, boolean[] visited, boolean[] path) {
        visited[current] = true;
        path[current] = true;

        for (int next : adj.get(current)) {
            if (!visited[next]) {
                boolean check = isCycle(adj, next, visited, path);
                if (check) {
                    return true;
                }
            } else if (path[next]) {
                return true;
            }
        }

        path[current] = false;

        return false;
    }

    // Function to detect cycle in a directed graph.
    static boolean isCyclic(int V, ArrayList<ArrayList<Integer>> adj) {
        // code here
        boolean[] visited = new boolean[V];
        for (int i = 0; i < V; i++) {
            if (visited[i]) {
                continue;
            }

            boolean[] path = new boolean[V];

            boolean check = isCycle(adj, i, visited, path);
            if (check) {
                return true;
            }
        }

        return false;

        // Complexity analysis
        // Time : O(V) + O(E)
        // Space : O(V) + O(V) + stack O(V)
    }
}
