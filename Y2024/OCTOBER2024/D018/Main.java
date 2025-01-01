import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

class Index2D {
    int row;
    int col;

    Index2D(int r, int c) {
        this.row = r;
        this.col = c;
    }
}

class Pair {
    Index2D index;
    int time;

    Pair(Index2D i, int t) {
        this.index = i;
        this.time = t;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 18 of October - revisiting graph

        p1();

        p2();

        p3();

        p4();
    }

    static void p1() {
        // Problem 1 : Leetcode 994. Rotting Oranges -
        // https://leetcode.com/problems/rotting-oranges/

        int[][] grid = { { 2, 1, 1 }, { 0, 1, 1 }, { 1, 0, 1 } };

        int t = orangesRotting(grid);
        System.out.println(t);
    }

    static int[] DROWS = { -1, 0, +1, 0 };
    static int[] DCOLS = { 0, -1, 0, +1 };

    static boolean isValidIndex(int r, int c, int rs, int cs) {
        return (r >= 0 && r < rs) && (c >= 0 && c < cs);
    }

    static int orangesRotting(int[][] grid) {
        int M = grid.length;
        int N = grid[0].length;

        int[][] copy = new int[M][N];
        for (int i = 0; i < M; i++) {
            System.arraycopy(grid[i], 0, copy[i], 0, N);
        }

        PriorityQueue<Pair> que = new PriorityQueue<>((Pair p1, Pair p2) -> p1.time - p2.time);

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (copy[i][j] == 2) {
                    // its a rotten orange and it will rot others also
                    que.add(new Pair(new Index2D(i, j), 0));
                }
            }
        }

        int maxTime = 0;

        // perform bfs and rot oranges
        while (!que.isEmpty()) {
            Pair top = que.remove();

            Index2D index = top.index;
            int time = top.time;

            maxTime = Math.max(maxTime, time);

            for (int i = 0; i < 4; i++) {
                // adjacent cell index
                int nrow = index.row + DROWS[i];
                int ncol = index.col + DCOLS[i];

                if (!isValidIndex(nrow, ncol, M, N)) {
                    // invalid index
                    continue;
                }

                if (copy[nrow][ncol] != 1) {
                    // adjacent cell does not have a fresh orange
                    continue;
                }

                // rotting it
                copy[nrow][ncol] = 2;
                que.add(new Pair(new Index2D(nrow, ncol), time + 1));
            }
        }

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (copy[i][j] == 1) {
                    return -1;
                }
            }
        }

        return maxTime;

        // Complexity analysis
        // Time : O(M * N) + O(M * N) + O(M * N * Log(M * N)) + O(M * N)
        // Space : O(M * N) + O(M * N)
    }

    static void p2() {
        // Problem 2 : Leetcode 733. Flood Fill -
        // https://leetcode.com/problems/flood-fill/

        int[][] image = { { 1, 1, 1 }, { 1, 1, 0 }, { 1, 0, 1 } };
        int sr = 1;
        int sc = 1;
        int color = 2;

        int[][] newimage = floodFill(image, sr, sc, color);
        for (int[] im : newimage) {
            System.out.println(Arrays.toString(im));
        }
    }

    static int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int M = image.length;
        int N = image[0].length;

        // starting pixel color
        int startColor = image[sr][sc];

        Queue<Index2D> que = new LinkedList<>();

        // color starting pixel
        image[sr][sc] = color;

        // add starting cell in que
        que.add(new Index2D(sr, sc));

        while (!que.isEmpty()) {
            Index2D index = que.remove();

            for (int i = 0; i < 4; i++) {
                int nrow = index.row + DROWS[i];
                int ncol = index.col + DCOLS[i];

                if (!isValidIndex(nrow, ncol, M, N)) {
                    continue;
                }

                if (image[nrow][ncol] != startColor || image[nrow][ncol] == color) {
                    continue;
                }

                image[nrow][ncol] = color;

                que.add(new Index2D(nrow, ncol));
            }
        }

        return image;

        // Complexity analysis
        // Time : O(M * N)
        // Space : O(M * N)
    }

    static void p3() {
        // Problem 3 : Geeksforgeeks Undirected Graph Cycle -
        // https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        adj.add(new ArrayList<>(Arrays.asList(1)));
        adj.add(new ArrayList<>(Arrays.asList(0, 2, 4)));
        adj.add(new ArrayList<>(Arrays.asList(1, 3)));
        adj.add(new ArrayList<>(Arrays.asList(2, 4)));
        adj.add(new ArrayList<>(Arrays.asList(1, 3)));

        System.out.println(isCycle(adj));
    }

    static int MARK = 100;

    static boolean detectCycle(int node, int parent, ArrayList<ArrayList<Integer>> adj, int[] visited) {
        visited[node] = MARK;

        for (int next : adj.get(node)) {
            if (next == parent) {
            } else if (visited[next] == MARK) {
                return true;
            } else {
                boolean check = detectCycle(next, node, adj, visited);
                if (check) {
                    return true;
                }
            }
        }

        return false;
    }

    // Function to detect cycle in an undirected graph.
    static boolean isCycle(ArrayList<ArrayList<Integer>> adj) {
        // Code here
        int V = adj.size();

        int[] visited = new int[V];

        for (int i = 0; i < V; i++) {
            if (visited[i] != MARK) {
                boolean check = detectCycle(i, -1, adj, visited);
                if (check) {
                    return true;
                }
            }
        }

        return false;

        // Complexity analysis
        // Time : O(V + 2E)
        // Space : O(V) + O(E) stack space for dfs
    }

    static void p4() {
        // Problem 4 : Geeksforgeeks Detect Cycle in a Directed Graph -
        // https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

        int V = 5;
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        adj.add(new ArrayList<>(Arrays.asList(1)));
        adj.add(new ArrayList<>(Arrays.asList(2, 4)));
        adj.add(new ArrayList<>(Arrays.asList(3)));
        adj.add(new ArrayList<>(Arrays.asList(2, 4)));
        adj.add(new ArrayList<>(Arrays.asList(1, 3)));

        System.out.println(isCyclic(V, adj));
    }

    static boolean detectCycle(int node, int parent, ArrayList<ArrayList<Integer>> adj, int[] visited,
            int[] pathVisited) {
        visited[node] = MARK;
        pathVisited[node] = MARK;

        for (int next : adj.get(node)) {
            if (visited[next] != MARK) {
                boolean check = detectCycle(next, node, adj, visited, pathVisited);
                if (check) {
                    return true;
                }
            } else if (pathVisited[next] == MARK) {
                return true;
            }
        }

        pathVisited[node] = 0;
        return false;
    }

    // Function to detect cycle in a directed graph.
    static boolean isCyclic(int V, ArrayList<ArrayList<Integer>> adj) {
        // code here

        int[] visited = new int[V];

        for (int i = 0; i < V; i++) {
            if (visited[i] != MARK) {
                int[] pathVisited = new int[V];
                boolean check = detectCycle(i, -1, adj, visited, pathVisited);
                if (check) {
                    return true;
                }
            }
        }

        return false;
    }
}
