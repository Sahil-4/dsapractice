import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        // Day 17 of October - revisiting graph

        p1();

        p2();

        p3();
    }

    static void p1() {
        // Problem 1 : Geeksforgeeks DFS of Graph -
        // https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        adj.add(new ArrayList<>(Arrays.asList(2, 3, 1)));
        adj.add(new ArrayList<>(Arrays.asList(0)));
        adj.add(new ArrayList<>(Arrays.asList(0, 4)));
        adj.add(new ArrayList<>(Arrays.asList(0)));
        adj.add(new ArrayList<>(Arrays.asList(2)));

        ArrayList<Integer> t = dfsOfGraph(adj);
        System.out.println(t.toString());
    }

    static void dfs(ArrayList<Integer> out, int node, ArrayList<ArrayList<Integer>> adj, boolean[] visited) {
        visited[node] = true;

        out.add(node);

        for (int next : adj.get(node)) {
            if (!visited[next]) {
                dfs(out, next, adj, visited);
            }
        }
    }

    // Function to return a list containing the DFS traversal of the graph.
    static ArrayList<Integer> dfsOfGraph(ArrayList<ArrayList<Integer>> adj) {
        // Code here
        ArrayList<Integer> out = new ArrayList<>();

        int V = adj.size();
        boolean[] visited = new boolean[V];

        // if connected graph
        dfs(out, 0, adj, visited);

        // if not connexted graph
        // for (int node = 0; node < V; node++) {
        // if (!visited[node]) {
        // dfs(out, node, adj, visited);
        // }
        // }

        return out;

        // Complexity analysis
        // Time : O(V + 2E)
        // Space : O(V) + O(V) stack
    }

    static void p2() {
        // Problem 2 : Geeksforgeeks BFS of graph -
        // https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        adj.add(new ArrayList<>(Arrays.asList(2, 3, 1)));
        adj.add(new ArrayList<>(Arrays.asList(0)));
        adj.add(new ArrayList<>(Arrays.asList(0, 4)));
        adj.add(new ArrayList<>(Arrays.asList(0)));
        adj.add(new ArrayList<>(Arrays.asList(2)));

        ArrayList<Integer> t = bfsOfGraph(adj);
        System.out.println(t.toString());
    }

    // Function to return Breadth First Traversal of given graph.
    static ArrayList<Integer> bfsOfGraph(ArrayList<ArrayList<Integer>> adj) {
        // code here
        ArrayList<Integer> out = new ArrayList<>();

        int V = adj.size();

        boolean[] visited = new boolean[V];
        Queue<Integer> que = new LinkedList<>();

        que.offer(0); // starting point
        // mark it visited
        visited[0] = true;

        while (!que.isEmpty()) {
            // take out first node / element
            int top = que.poll();

            // add in output / traversal array
            out.add(top);

            // add adjacent nodes
            for (int next : adj.get(top)) {
                if (!visited[next]) {
                    // mark it visited
                    visited[next] = true;

                    // add in queue
                    que.offer(next);
                }
            }
        }

        return out;

        // Complexity analysis
        // Time : O(V + E)
        // Space : O(V) + O(V)
    }

    static void p3() {
        // Problem 3 : Leetcode 547. Number of Provinces -
        // https://leetcode.com/problems/number-of-provinces/

        int[][] isConnected = {
                { 1, 0, 0 },
                { 0, 1, 0 },
                { 0, 0, 1 },
        };

        int prs = findCircleNum(isConnected);
        System.out.println(prs);
    }

    static int findCircleNum(int[][] isConnected) {
        int provinces = 0;

        int V = isConnected.length;

        // create adjacency list
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (isConnected[i][j] == 1) {
                    adj.get(i).add(j);
                    adj.get(j).add(i);
                }
            }
        }

        boolean[] visited = new boolean[V];
        for (int node = 0; node < V; node++) {
            if (!visited[node]) {
                provinces++;
                dfs(new ArrayList<>(), node, adj, visited);
            }
        }

        return provinces;
    }
}
