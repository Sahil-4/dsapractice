import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class Pair {
    int current;
    int parent;

    Pair(int c, int p) {
        current = c;
        parent = p;
    }
}

class Index2D {
    int row;
    int col;

    Index2D(int r, int c) {
        row = r;
        col = c;
    }
}

class Pair2 {
    Index2D index;
    int steps;

    Pair2(Index2D i, int s) {
        index = i;
        steps = s;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 25 of September

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : GeeksForGeeks Undirected Graph Cycle -
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

    static boolean detectCycleBFS(int src, int[] visited, ArrayList<ArrayList<Integer>> adj) {
        visited[src] = 1;

        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(src, -1));

        while (!q.isEmpty()) {
            Pair top = q.remove();

            int current = top.current;
            int parent = top.parent;

            for (int n : adj.get(current)) {
                if (visited[n] != 1) {
                    q.add(new Pair(n, current));
                    visited[n] = 1;
                } else if (n != parent) {
                    return true;
                }
            }
        }

        return false;
    }

    // Function to detect cycle in an undirected graph.
    static boolean isCycle(int V, ArrayList<ArrayList<Integer>> adj) {
        // Code here
        int[] visited = new int[V];

        for (int i = 0; i < V; i++) {
            if (visited[i] != 1 && detectCycleBFS(i, visited, adj)) {
                return true;
            }
        }

        return false;

        // Complexity analysis
        // Time : O(components(V)) + O(V + 2E)
        // Space : O(V) + O(V)
    }

    static void p2() {
        // Problem 2 : Leetcode 542. 01 Matrix -
        // https://leetcode.com/problems/01-matrix/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/distance-of-nearest-cell-having-1-1587115620/1

        int[][] mat = { { 0, 0, 0 }, { 0, 1, 0 }, { 0, 0, 0 } };
        updateMatrix(mat);
    }

    static int NEAREST = 0;
    static int MARK = 100;

    static int[] nxtR = { -1, 0, +1, 0 };
    static int[] nxtC = { 0, +1, 0, -1 };

    static boolean isValidIndex(int r, int c, int rs, int cs) {
        return (r >= 0 && r < rs && c >= 0 && c < cs);
    }

    static int[][] updateMatrix(int[][] mat) {
        int rs = mat.length;
        int cs = mat[0].length;

        int[][] distance = new int[rs][cs];
        int[][] visited = new int[rs][cs];

        Queue<Pair2> q = new LinkedList<>();

        for (int i = 0; i < rs; i++) {
            for (int j = 0; j < cs; j++) {
                if (mat[i][j] == NEAREST) {
                    visited[i][j] = MARK;
                    q.add(new Pair2(new Index2D(i, j), 0));
                }
            }
        }

        while (!q.isEmpty()) {
            Pair2 top = q.remove();

            Index2D index = top.index;
            int steps = top.steps;

            distance[index.row][index.col] = steps;

            for (int i = 0; i < 4; i++) {
                int r = index.row + nxtR[i];
                int c = index.col + nxtC[i];

                if (isValidIndex(r, c, rs, cs) && visited[r][c] != MARK) {
                    visited[r][c] = MARK;
                    q.add(new Pair2(new Index2D(r, c), steps + 1));
                }
            }
        }

        return distance;

        // Complexity analysis
        // Time : O(n * m) + O(n * m)
        // Space : O(2 * |mat|)
    }
}
