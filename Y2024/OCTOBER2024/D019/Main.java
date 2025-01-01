import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        // Day 19 of October

        p1();

        p2();

        p3();
    }

    static void p1() {
        // Problem 1 : Leetcode 1020. Number of Enclaves -
        // https://leetcode.com/problems/number-of-enclaves/

        int[][] grid = { { 0, 0, 0, 1, 1, 1, 0, 1, 0, 0 },
                { 1, 1, 0, 0, 0, 1, 0, 1, 1, 1 },
                { 0, 0, 0, 1, 1, 1, 0, 1, 0, 0 },
                { 0, 1, 1, 0, 0, 0, 1, 0, 1, 0 },
                { 0, 1, 1, 1, 1, 1, 0, 0, 1, 0 },
                { 0, 0, 1, 0, 1, 1, 1, 1, 0, 1 },
                { 0, 1, 1, 0, 0, 0, 1, 1, 1, 1 },
                { 0, 0, 1, 0, 0, 1, 0, 1, 0, 1 },
                { 1, 0, 1, 0, 1, 1, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 1, 1, 0, 0, 0, 1 } };

        int e = numEnclaves(grid);
        System.out.println(e);
    }

    static int[] DROWS = { -1, 0, +1, 0 };
    static int[] DCOLS = { 0, -1, 0, +1 };

    static boolean isValidIndex(int r, int c, int M, int N) {
        return ((r >= 0 && r < M) && (c >= 0 && c < N));
    }

    static void dfs(int[][] grid, int r, int c, int M, int N) {
        grid[r][c] = 0;

        for (int i = 0; i < 4; i++) {
            int nr = DROWS[i] + r;
            int nc = DCOLS[i] + c;

            if (isValidIndex(nr, nc, M, N) && grid[nr][nc] == 1) {
                dfs(grid, nr, nc, M, N);
            }
        }
    }

    static int numEnclaves(int[][] gridU) {
        int M = gridU.length;
        int N = gridU[0].length;

        int[][] grid = new int[M][N];
        for (int i = 0; i < M; i++) {
            System.arraycopy(gridU[i], 0, grid[i], 0, N);
        }

        // check boundary cells and call dfs if its 1
        for (int i = 0; i < N; i++) {
            // Left to Right on 1st and last row
            if (grid[0][i] == 1) {
                dfs(grid, 0, i, M, N);
            }

            if (grid[M - 1][i] == 1) {
                dfs(grid, M - 1, i, M, N);
            }
        }
        for (int i = 0; i < M; i++) {
            // Top to Bottom on 1st and last col
            if (grid[i][0] == 1) {
                dfs(grid, i, 0, M, N);
            }

            if (grid[i][N - 1] == 1) {
                dfs(grid, i, N - 1, M, N);
            }
        }

        int ones = 0;

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == 1) {
                    ones++;
                }
            }
        }

        return ones;

        // Complexity analysis
        // Time : O(M * N) + O(M * N) + O(M * N) + O(M * N)
        // Space : O(M * N) + O(M + N) stack space
    }

    static void p2() {
        // Problem 2 : Geeksforgeeks Number of Distinct Islands -
        // https://www.geeksforgeeks.org/problems/number-of-distinct-islands/0

        int[][] grid = { { 1, 1, 0, 0, 0 },
                { 1, 1, 0, 0, 0 },
                { 0, 0, 0, 1, 1 },
                { 0, 0, 0, 1, 1 } };

        int di = countDistinctIslands(grid);
        System.out.println(di);
    }

    static void dfs(int[][] grid, int r, int c, int sr, int sc, ArrayList<String> path, int M, int N) {
        grid[r][c] = 0;
        path.add(toString(r - sr, c - sc));

        for (int i = 0; i < 4; i++) {
            int nr = DROWS[i] + r;
            int nc = DCOLS[i] + c;

            if (isValidIndex(nr, nc, M, N) && grid[nr][nc] == 1) {
                dfs(grid, nr, nc, sr, sc, path, M, N);
            }
        }
    }

    static String toString(int r, int c) {
        return Integer.toString(r) + " " + Integer.toString(c);
    }

    static int countDistinctIslands(int[][] gridU) {
        // Your Code here
        int N = gridU.length;
        int M = gridU[0].length;

        int[][] grid = new int[N][M];
        for (int i = 0; i < N; i++) {
            System.arraycopy(gridU[i], 0, grid[i], 0, M);
        }

        HashSet<ArrayList<String>> st = new HashSet<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (grid[i][j] == 1) {
                    int sr = i;
                    int sc = j;
                    ArrayList<String> path = new ArrayList<>();
                    dfs(grid, i, j, sr, sc, path, N, M);
                    st.add(path);
                }
            }
        }

        return st.size();

        // Complexity analysis
        // Time : O(N * M) + O((N + M) * log(N * M) * (N * M))
        // Space : O(N * M) + O(N * M)
    }

    static void p3() {
        // Problem 3 : Geeksforgeeks Bipartite Graph -
        // https://www.geeksforgeeks.org/problems/bipartite-graph/1

        int V = 5;
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        adj.add(new ArrayList<>(Arrays.asList(1)));
        adj.add(new ArrayList<>(Arrays.asList(0)));
        adj.add(new ArrayList<>(Arrays.asList(3, 4)));
        adj.add(new ArrayList<>(Arrays.asList(2, 4)));
        adj.add(new ArrayList<>(Arrays.asList(2, 3)));

        boolean check = isBipartite(V, adj);
        System.out.println(check);
    }

    static boolean bfs(ArrayList<ArrayList<Integer>> adj, Queue<Integer> que, char[] color) {
        while (!que.isEmpty()) {
            int top = que.remove();
            char ncolor = color[top] == 'r' ? 'g' : 'r';

            for (int nnode : adj.get(top)) {
                if (nnode == top) {
                    continue;
                }
                if (color[nnode] != 'b') {
                    if (color[nnode] != ncolor) {
                        return false;
                    }
                } else {
                    que.add(nnode);
                    color[nnode] = ncolor;
                }
            }
        }

        return true;
    }

    static boolean isBipartite(int V, ArrayList<ArrayList<Integer>> adj) {
        // Code here
        Queue<Integer> que = new LinkedList<>();
        char[] color = new char[V]; // r or g
        for (int i = 0; i < V; i++) {
            color[i] = 'b';
        }

        for (int i = 0; i < V; i++) {
            if (color[i] == 'b') {
                que.add(i);
                color[i] = 'r';

                boolean check = bfs(adj, que, color);

                if (!check) {
                    return false;
                }
            }
        }

        return true;
    }
}
