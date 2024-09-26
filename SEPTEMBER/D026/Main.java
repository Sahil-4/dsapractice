import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // Day 26 of September 2024

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : GeeksForGeeks Undirected Graph Cycle | DFS -
        // https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

        int V = 4;
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        // [[], [2], [1, 3], [2]]
        adj.add(new ArrayList<>());
        adj.add(new ArrayList<>());
        adj.add(new ArrayList<>());
        adj.add(new ArrayList<>());
        adj.get(1).add(2);
        adj.get(2).add(1);
        adj.get(2).add(3);
        adj.get(3).add(2);

        boolean check = isCycle(V, adj);
        System.out.println(check);
    }

    static int MARK2 = 100;

    static boolean detectCycleDFS(int current, int parent, int[] visited, ArrayList<ArrayList<Integer>> adj) {
        // mark visited
        visited[current] = MARK2;

        // call for adjacent
        for (int next : adj.get(current)) {
            if (visited[next] != MARK2) {
                if (detectCycleDFS(next, current, visited, adj)) {
                    return true;
                }
            } else if (next != parent) {
                return true;
            }
        }

        return false;
    }

    // Function to detect cycle in an undirected graph.
    static boolean isCycle(int V, ArrayList<ArrayList<Integer>> adj) {
        // Code here

        // --- using dfs ---

        // visited array
        int[] visited = new int[V];

        for (int i = 0; i < V; i++) {
            if (visited[i] == MARK2) continue;

            boolean check = detectCycleDFS(i, -1, visited, adj);
            if (check) return true;
        }

        return false;

        // Complexity analysis
        // Time : O()
        // Space : O(V)
    }

    static void p2() {
        // Problem 2 : Leetcode 130. Surrounded Regions -
        // https://leetcode.com/problems/surrounded-regions/description/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/replace-os-with-xs0052/1

        char[][] board = {
                { 'X', 'X', 'X', 'X' },
                { 'X', 'O', 'O', 'X' },
                { 'X', 'X', 'O', 'X' },
                { 'X', 'O', 'X', 'X' }
        };
        solve(board);

        for (char[] arr : board) {
            System.out.println(Arrays.toString(arr));
        }
    }

    static char MARK = 'V'; // visited mark

    static boolean validDirection(int nr, int nc, int m, int n, char[][] visited, char[][] board) {
        return (nr >= 0 && nr < m && nc >= 0 && nc < n) && (visited[nr][nc] != MARK) && (board[nr][nc] != 'X');
    }

    static void markVisitedDFS(int r, int c, char[][] visited, char[][] board, int m, int n) {
        visited[r][c] = MARK;

        int[] nxtRows = { -1, 0, +1, 0 };
        int[] nxtCols = { 0, +1, 0, -1 };

        for (int a = 0; a < 4; a++) {
            int nr = r + nxtRows[a];
            int nc = c + nxtCols[a];

            if (validDirection(nr, nc, m, n, visited, board)) {
                markVisitedDFS(nr, nc, visited, board, m, n);
            }
        }
    }

    static void markBoundaryOVisited(char[][] visited, char[][] board, int m, int n) {
        // first row and last row
        for (int c = 0; c < n; c++) {
            if (board[0][c] == 'O' && visited[0][c] != MARK) {
                markVisitedDFS(0, c, visited, board, m, n);
            }
            if (board[m - 1][c] == 'O' && visited[m - 1][c] != MARK) {
                markVisitedDFS(m - 1, c, visited, board, m, n);
            }
        }

        // first col and last col
        for (int r = 0; r < m; r++) {
            if (board[r][0] == 'O' && visited[r][0] != MARK) {
                markVisitedDFS(r, 0, visited, board, m, n);
            }
            if (board[r][n - 1] == 'O' && visited[r][n - 1] != MARK) {
                markVisitedDFS(r, n - 1, visited, board, m, n);
            }
        }
    }

    static void convertO2X(char[][] visited, char[][] board, int m, int n) {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] != MARK && board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
        }
    }

    static void solve(char[][] board) {
        int m = board.length;
        int n = board[0].length;

        char[][] visited = new char[m][n];

        markBoundaryOVisited(visited, board, m, n);

        convertO2X(visited, board, m, n);

        // Complexity analysis
        // Time : O(m * n) + O(m * n)
        // Space : O(n)
    }
}
