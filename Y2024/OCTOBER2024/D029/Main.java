import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

class CustomComparator implements Comparator<int[]> {
    @Override
    public int compare(int[] a, int[] b) {
        for (int i = 0; i < 3; i++) {
            if (a[i] != b[i]) {
                return a[i] - b[i];
            }
        }
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 29 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 332. Reconstruct Itinerary -
        // https://leetcode.com/problems/reconstruct-itinerary/

        List<List<String>> tickets = new ArrayList<>();
        List<String> itinerary = findItinerary(tickets);
        System.out.println(itinerary);
    }

    static String START = "JFK";

    static void dfs(String current, Map<String, PriorityQueue<String>> route, List<String> itinerary) {
        PriorityQueue<String> arrivals = route.get(current);
        while (arrivals != null && !arrivals.isEmpty()) {
            dfs(arrivals.poll(), route, itinerary);
        }

        itinerary.add(0, current);
    }

    static List<String> findItinerary(List<List<String>> tickets) {
        // --- topo sort ---

        // for output
        List<String> itinerary = new ArrayList<>();

        // adjacency map {u -> {v1, v2, v3}}
        Map<String, PriorityQueue<String>> route = new HashMap<>();
        for (List<String> ticket : tickets) {
            String u = ticket.get(0);
            String v = ticket.get(1);
            route.putIfAbsent(u, new PriorityQueue<>());
            route.get(u).add(v);
        }

        // dfs - solve
        dfs(START, route, itinerary);

        return itinerary;

        // Complexity analysis
        // Time : O(E) + O(E * log(E))
        // Space : O(V + E) + O(E)
    }

    static void p2() {
        // Problem 2 : Geeksforgeeks Minimum Cost Path -
        // https://www.geeksforgeeks.org/problems/minimum-cost-path3833/1

        int[][] grid = { { 9, 4, 9, 9 }, { 6, 7, 6, 4 }, { 8, 3, 3, 7 }, { 7, 4, 9, 10 } };

        int cost = minimumCostPath(grid);
        System.out.println(cost);
    }

    static final int MAXD = (int) 1e9;

    static int[][] getNextCells(int i, int j) {
        return new int[][] { { i, j - 1 }, { i, j + 1 }, { i - 1, j }, { i + 1, j } };
    }

    static boolean isValidIndex(int r, int c, int N, int M) {
        return (r >= 0 && r < N) && (c >= 0 && c < M);
    }

    // Function to return the minimum cost to react at bottom
    // right cell from top left cell.
    static int minimumCostPath(int[][] grid) {
        // Code here

        int N = grid.length;

        if (N == 1) {
            return grid[0][0];
        }

        int src[] = { 0, 0 };
        int dest[] = { N - 1, N - 1 };

        int costs[][] = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                costs[i][j] = MAXD;
            }
        }

        // { cost, cell_row, cell_col }
        PriorityQueue<int[]> pq = new PriorityQueue<>(new CustomComparator());

        pq.add(new int[] { grid[0][0], 0, 0 });
        costs[0][0] = grid[0][0];

        while (!pq.isEmpty()) {
            int[] top = pq.remove();

            int c_cost = top[0];
            int c_row = top[1];
            int c_col = top[2];

            int[][] nextCells = getNextCells(c_row, c_col);

            for (int[] next : nextCells) {
                int n_row = next[0];
                int n_col = next[1];

                if (!isValidIndex(n_row, n_col, N, N)) {
                    continue;
                }

                int n_cost = c_cost + grid[n_row][n_col];

                if (n_cost < costs[n_row][n_col]) {
                    pq.add(new int[] { n_cost, n_row, n_col });
                    costs[n_row][n_col] = n_cost;
                }
            }
        }

        return costs[dest[0]][dest[1]];

        // Complexity analysis
        // Time : O(N * N) + O(2N * log(2N)
        // Space : O(N * N) + O(N + N)
    }
}
