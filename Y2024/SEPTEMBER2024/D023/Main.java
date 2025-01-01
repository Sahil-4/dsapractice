import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        // Day 23 of September
        // Started with Graphs

        p1();

        p2();

        p3();

        p4();
    }

    static void p1() {
        // Problem 1 : GeeksForGeeks Print adjacency list -
        // https://www.geeksforgeeks.org/problems/print-adjacency-list-1587115620/1

        int[][] edges = { { 0, 1 }, { 0, 4 }, { 4, 1 }, { 4, 3 }, { 1, 3 }, { 1, 2 }, { 3, 2 } };
        int V = 5;

        List<List<Integer>> ajc = printGraph(V, edges);
        for (List<Integer> list : ajc) {
            System.out.println(list.toString());
        }
    }

    static List<List<Integer>> printGraph(int V, int edges[][]) {
        List<List<Integer>> ajc = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            ajc.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            int node1 = edge[0];
            int node2 = edge[1];

            // A --> B
            ajc.get(node1).add(node2);
            // B --> A
            ajc.get(node2).add(node1);
        }

        return ajc;
    }

    static void p2() {
        // Problem 2 : GeeksForGeeks BFS of graph -
        // https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

        int V = 5;
        int[][] edges = { { 0, 1 }, { 0, 4 }, { 4, 1 }, { 4, 3 }, { 1, 3 }, { 1, 2 }, { 3, 2 } };
        List<List<Integer>> adj = printGraph(V, edges);
        ArrayList<Integer> bfs = bfsOfGraph(V, adj);
        System.out.println(bfs.toString());
    }

    static ArrayList<Integer> bfsOfGraph(int V, List<List<Integer>> adj) {
        // Code here
        ArrayList<Integer> bfs = new ArrayList<>();

        int[] visited = new int[adj.size()];
        Queue<Integer> q = new LinkedList<>();

        q.offer(0);
        visited[0] = 1;

        while (!q.isEmpty()) {
            int node = q.poll();
            bfs.add(node);

            for (int n : adj.get(node)) {
                if (visited[n] != 1) {
                    q.offer(n);
                    visited[n] = 1;
                }
            }
        }

        return bfs;

        // Complexity analysis
        // Time : O(n + 2E)
        // Space : O(2n)
    }

    static void p3() {
        // Problem 3 : GeeksForGeeks DFS of Graph -
        // https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

        int V = 5;
        int[][] edges = { { 0, 1 }, { 0, 4 }, { 4, 1 }, { 4, 3 }, { 1, 3 }, { 1, 2 }, { 3, 2 } };
        List<List<Integer>> adj = printGraph(V, edges);

        ArrayList<Integer> dfs = dfsOfGraph(V, adj);
        System.out.println(dfs.toString());
    }

    static void dfstraversal(ArrayList<Integer> dfs, int node, List<List<Integer>> adj, int[] visited) {
        visited[node] = 1;
        dfs.add(node);

        for (int n : adj.get(node)) {
            if (visited[n] != 1) {
                dfstraversal(dfs, n, adj, visited);
            }
        }
    }

    // Function to return a list containing the DFS traversal of the graph.
    static ArrayList<Integer> dfsOfGraph(int V, List<List<Integer>> adj) {
        // Code here
        ArrayList<Integer> dfs = new ArrayList<>();
        int[] visited = new int[adj.size()];

        int start = 0;

        dfstraversal(dfs, start, adj, visited);

        return dfs;

        // Complexity analysis (complete)
        // Time : O(n) + O(E)
        // Space : O(n) + stack space for recursion
    }

    static void p4() {
        // Problem 4 : Leetcode 547. Number of Provinces -
        // https://leetcode.com/problems/number-of-provinces/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/number-of-provinces/1

        int[][] connections = { { 1, 1, 0 }, { 1, 1, 0 }, { 0, 0, 1 } };

        int provinces = findCircleNum(connections);
        System.out.println(provinces);
    }

    static List<List<Integer>> getAdjacencyList(int V, int edges[][]) {
        List<List<Integer>> ajd = new ArrayList<>();

        for (int i = 0; i < V; i++) {
            ajd.add(new ArrayList<>());
        }

        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (i != j && edges[i][j] == 1) {
                    ajd.get(i).add(j);
                    ajd.get(j).add(i);
                }
            }
        }

        return ajd;
    }

    static void dfstraversal(int node, List<List<Integer>> adj, int[] visited) {
        visited[node] = 1;

        for (int n : adj.get(node)) {
            if (visited[n] != 1) {
                dfstraversal(n, adj, visited);
            }
        }
    }

    static int findCircleNum(int[][] isConnected) {
        // number of vertices
        int V = isConnected.length;

        // adjacency list
        List<List<Integer>> adjList = getAdjacencyList(V, isConnected);

        // visited nodes
        int[] visited = new int[V];

        // count provinces
        int provinces = 0;
        for (int i = 0; i < V; i++) {
            if (visited[i] != 1) {
                provinces++;
                dfstraversal(i, adjList, visited);
            }
        }

        return provinces;
    }
}