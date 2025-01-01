import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Index2D {
    int row;
    int col;

    Index2D(int r, int c) {
        row = r;
        col = c;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 5 of October 2024

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : GeeksForGeeks Shortest path in Undirected Graph -
        // https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1

        int n = 9;
        int m = 10;
        int src = 0;
        int[][] edges = {
                { 0, 1 }, { 0, 3 }, { 3, 4 }, { 4, 5 }, { 5, 6 },
                { 1, 2 }, { 2, 6 }, { 6, 7 }, { 7, 8 }, { 6, 8 }
        };

        int[] dist = shortestPath(edges, n, m, src);
        System.out.println(Arrays.toString(dist));
    }

    static int MAX = (int) 1e9;

    static int[] shortestPath(int[][] edges, int n, int m, int src) {
        // Code here
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            adj.get(edges[i][0]).add(edges[i][1]);
            adj.get(edges[i][1]).add(edges[i][0]);
        }

        int[] dist = new int[n];
        for (int i = 0; i < n; i++) {
            dist[i] = MAX;
        }
        dist[src] = 0;

        Queue<Integer> que = new LinkedList<>();
        que.add(src);

        while (!que.isEmpty()) {
            int top = que.remove();

            for (int e : adj.get(top)) {
                if (dist[top] + 1 < dist[e]) {
                    dist[e] = dist[top] + 1;
                    que.add(e);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (dist[i] == MAX) {
                dist[i] = -1;
            }
        }

        return dist;

        // Complexity analysis
        // Time : O(m) + O(N + 2E)
        // Space : O(n * n) + O(E)
    }

    static void p2() {
        // Problem 2 : Leetcode 1091. Shortest Path in Binary Matrix -
        // https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

        int[][] grid = { { 0, 0, 0 }, { 1, 1, 0 }, { 1, 1, 0 } };

        int p = shortestPathBinaryMatrix(grid);
        System.out.println(p);
    }

    static int[][] directions = {
            { 1, 1 }, { 0, 1 }, { 1, 0 }, { -1, 0 },
            { 0, -1 }, { -1, -1 }, { 1, -1 }, { -1, 1 }
    };

    static boolean canMove(int[][] graph, int row, int col) {
        return ((row >= 0 && row < graph.length) && (col >= 0 && col < graph.length) && (graph[row][col] == 0));
    }

    static int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;

        if (n == 0 || grid[0][0] != 0) {
            return -1;
        }

        int[][] graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            System.arraycopy(grid[i], 0, graph[i], 0, n);
        }
        Queue<Index2D> q = new LinkedList<>();
        q.add(new Index2D(0, 0));
        graph[0][0] = 1;

        int level = 0;

        while (!q.isEmpty()) {
            int N = q.size();

            while (N-- > 0) {
                Index2D index = q.remove();

                if (index.row == n - 1 && index.col == n - 1) {
                    return level + 1; // steps or stops
                }

                for (int[] dir : directions) {
                    int nrow = index.row + dir[0];
                    int ncol = index.col + dir[1];

                    if (!canMove(graph, nrow, ncol)) {
                        continue;
                    }

                    q.add(new Index2D(nrow, ncol));
                    graph[nrow][ncol] = 1;
                }
            }

            level++;
        }

        return -1;
    }
}
