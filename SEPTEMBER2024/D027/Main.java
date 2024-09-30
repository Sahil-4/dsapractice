
public class Main {
    public static void main(String[] args) {
        // Day 27 of September

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 1020. Number of Enclaves -
        // https://leetcode.com/problems/number-of-enclaves/description/
        // GeeksForGeeks - 
        // https://www.geeksforgeeks.org/problems/number-of-enclaves/0

        int[][] grid = {};
        int enclaves = numEnclaves(grid);
        System.out.println(enclaves);
    }

    static char MARK = 'X';

    static boolean validIndex(int r, int c, int m, int n, int[][] copygrid, char[][] visited) {
        return ((r >= 0 && r < m && c >= 0 && c < n) && (copygrid[r][c] == 1) && (visited[r][c] != MARK));
    }

    static void dfs(int[][] copygrid, char[][] visited, int r, int c, int m, int n) {
        copygrid[r][c] = -1;
        visited[r][c] = MARK;

        int[] nxtr = { -1, 0, +1, 0 };
        int[] nxtc = { 0, +1, 0, -1 };

        for (int i = 0; i < 4; i++) {
            int nextrow = r + nxtr[i];
            int nextcol = c + nxtc[i];

            if (validIndex(nextrow, nextcol, m, n, copygrid, visited)) {
                dfs(copygrid, visited, nextrow, nextcol, m, n);
            }
        }
    }

    static void boundaryTraverse(char[][] visited, int[][] copygrid, int m, int n) {
        // first and last row
        for (int i = 0; i < n; i++) {
            if (copygrid[0][i] == 1 && visited[0][i] != MARK) {
                dfs(copygrid, visited, 0, i, m, n);
            }
            if (copygrid[m - 1][i] == 1 && visited[m - 1][i] != MARK) {
                dfs(copygrid, visited, m - 1, i, m, n);
            }
        }

        // first and last col
        for (int i = 0; i < m; i++) {
            if (copygrid[i][0] == 1 && visited[i][0] != MARK) {
                dfs(copygrid, visited, i, 0, m, n);
            }
            if (copygrid[i][n - 1] == 1 && visited[i][n - 1] != MARK) {
                dfs(copygrid, visited, i, n - 1, m, n);
            }
        }
    }

    static int numEnclaves(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        // make copy of given grid
        int[][] copygrid = new int[m][n];
        for (int i = 0; i < m; i++) {
            System.arraycopy(grid[i], 0, copygrid[i], 0, n);
        }

        // track visited cells using a matrix
        char[][] visited = new char[m][n];

        // traverse boundary, find 1s and make them -1 in copygrid using dfs
        boundaryTraverse(visited, copygrid, m, n);

        // now count 1s in copygrid
        int ones = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (copygrid[i][j] == 1) {
                    ones++;
                }
            }
        }

        // finally return ones
        return ones;

        // Complexity analysis
        // Time : O(m * n) + O(m * n) + O(m * n)
        // Space : O(m * n) + O(m * n) + recursion stack space for dfs
    }
}
