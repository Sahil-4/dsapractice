
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        // Day 30 of September
        // Completed total 274 Days (CS + GfG + LC)

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 785. Is Graph Bipartite? -
        // https://leetcode.com/problems/is-graph-bipartite/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/bipartite-graph/1

        int[][] graph = {
                { 1, 2, 3 },
                { 0, 2 },
                { 0, 1, 3 },
                { 0, 2 },
        };

        boolean check = isBipartite(graph);
        System.out.println("isBipartite? ::" + check);
    }

    static boolean checkDFS(int curr, int color, int[] colored, int[][] graph) {
        colored[curr] = color;

        for (int n : graph[curr]) {
            if (colored[n] == -1) {
                if (!checkDFS(n, 1 - color, colored, graph)) {
                    return false;
                }
            } else if (colored[n] == color) {
                return false;
            }
        }

        return true;
    }

    static boolean isBipartiteDFS(int[][] graph) {
        int V = graph.length;

        int[] colored = new int[V];
        for (int i = 0; i < V; i++) {
            colored[i] = -1;
        }

        for (int i = 0; i < V; i++) {
            if (colored[i] == -1 && !checkDFS(i, 0, colored, graph)) {
                return false;
            }
        }

        return true;

        // Complexity analysis
        // Time : O(V) + O(2E)
        // Space : O(V) + O(E) Stack space
    }

    static boolean checkBFS(int start, int[] colored, int[][] graph) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        colored[start] = 0;

        while (!q.isEmpty()) {
            int top = q.remove();

            for (int n : graph[top]) {
                if (colored[n] == -1) {
                    colored[n] = 1 - colored[top];
                    q.add(n);
                } else if (colored[n] == colored[top]) {
                    return false;
                }
            }
        }

        return true;
    }

    static boolean isBipartiteBFS(int[][] graph) {
        int V = graph.length;

        int[] colored = new int[V];
        for (int i = 0; i < V; i++) {
            colored[i] = -1;
        }

        for (int i = 0; i < V; i++) {
            if (colored[i] == -1 && !checkBFS(i, colored, graph)) {
                return false;
            }
        }

        return true;

        // Complexity analysis
        // Time : O(V) + O(2E)
        // Space : O(V) + O(E)
    }

    static boolean isBipartite(int[][] graph) {
        // return isBipartiteBFS(graph);
        return isBipartiteDFS(graph);
    }
}