import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        // Day 16 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Geeksforgeeks Strongly Connected Components (Kosaraju's Algo) -
        // https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1

        int V = 5;
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        adj.add(new ArrayList<>(Arrays.asList(2, 3)));
        adj.add(new ArrayList<>(Arrays.asList(0)));
        adj.add(new ArrayList<>(Arrays.asList(1)));
        adj.add(new ArrayList<>(Arrays.asList(4)));
        adj.add(new ArrayList<>(Arrays.asList()));

        int sccs = kosaraju(V, adj);
        System.out.println(sccs);
    }

    static int MARK_VISITED = 100;

    static void getNodesByFinishingTime(int node, ArrayList<ArrayList<Integer>> adj, int[] visited,
            Stack<Integer> nodes) {
        visited[node] = MARK_VISITED;

        for (int n : adj.get(node)) {
            if (visited[n] != MARK_VISITED) {
                getNodesByFinishingTime(n, adj, visited, nodes);
            }
        }

        nodes.push(node);
    }

    static ArrayList<ArrayList<Integer>> getReversedAdjacencyList(int V, ArrayList<ArrayList<Integer>> adj) {
        ArrayList<ArrayList<Integer>> adjT = new ArrayList<>();

        for (int i = 0; i < V; i++) {
            adjT.add(new ArrayList<>());
        }

        for (int u = 0; u < V; u++) {
            for (int v : adj.get(u)) {
                adjT.get(v).add(u);
            }
        }

        return adjT;
    }

    static void dfs(int node, ArrayList<ArrayList<Integer>> adjT, int[] visited) {
        visited[node] = MARK_VISITED;

        for (int n : adjT.get(node)) {
            if (visited[n] != MARK_VISITED) {
                dfs(n, adjT, visited);
            }
        }
    }

    // Function to find number of strongly connected components in the graph.
    static int kosaraju(int V, ArrayList<ArrayList<Integer>> adj) {
        // code here

        // get nodes sorted in finishing time
        Stack<Integer> nodes = new Stack<>();
        int[] visited = new int[V];
        for (int v = 0; v < V; v++) {
            if (visited[v] != MARK_VISITED) {
                getNodesByFinishingTime(v, adj, visited, nodes);
            }
        }

        // reverse edges
        ArrayList<ArrayList<Integer>> adjT = getReversedAdjacencyList(V, adj);

        // -- mark nodes unvisited for re-using visited array --
        for (int i = 0; i < V; i++) {
            visited[i] = 0;
        }

        // perfrom dfs in order of finishing time to get SCC
        int SCCs = 0;

        while (!nodes.isEmpty()) {
            int last = nodes.pop();
            if (visited[last] != MARK_VISITED) {
                SCCs++;
                dfs(last, adjT, visited);
            }
        }

        return SCCs;

        // Complexity analysis
        // Time : O(V + E) + O(E) + O(V) + O(V + E)
        // Space : O(V) + O(V) + O(E)
    }

    static void p2() {
        // Problem 2 : Leetcode 1192. Critical Connections in a Network -
        // https://leetcode.com/problems/critical-connections-in-a-network/
        // Geeksforgeeks -
        // https://www.geeksforgeeks.org/problems/critical-connections/1

        int V = 4;
        List<List<Integer>> connections = new ArrayList<>();
        connections.add(new ArrayList<>(Arrays.asList(0, 1)));
        connections.add(new ArrayList<>(Arrays.asList(1, 2)));
        connections.add(new ArrayList<>(Arrays.asList(2, 0)));
        connections.add(new ArrayList<>(Arrays.asList(1, 3)));

        List<List<Integer>> conn = criticalConnections(V, connections);
        for (List<Integer> c : conn) {
            System.out.println(c.toString());
        }
    }

    static int timer = 1;

    static void dfs(int node, int parent, List<List<Integer>> adj, int[] visited, int[] time, int[] low,
            List<List<Integer>> bridges) {
        // mark node visited
        visited[node] = MARK_VISITED;

        // update time and low time
        time[node] = low[node] = timer;

        // increament timer
        timer++;

        // visit adjacent nodes
        for (int v : adj.get(node)) {
            // skip parent node
            if (v == parent) {
                continue;
            }

            // if node is not already visited
            if (visited[v] != MARK_VISITED) {
                // move to adjacent node
                dfs(v, node, adj, visited, time, low, bridges);

                // update low with min of node and adjacent node
                low[node] = Math.min(low[node], low[v]);

                // if adjacent node cant reach to node - its a bridge
                if (low[v] > time[node]) {
                    bridges.add(Arrays.asList(v, node));
                }
            } else {
                low[node] = Math.min(low[node], low[v]);
            }
        }
    }

    static List<List<Integer>> criticalConnections(int V, List<List<Integer>> connections) {
        timer = 1;
        // -- tarjan's algorithm --

        // crete adjacency list
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }

        for (List<Integer> connection : connections) {
            int u = connection.get(0);
            int v = connection.get(1);

            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        // perform dfs - and update reach/insertiom time and low reach/insertiom time
        int[] visited = new int[V];
        int[] time = new int[V];
        int[] low = new int[V];

        List<List<Integer>> bridges = new ArrayList<>();

        dfs(0, -1, adj, visited, time, low, bridges);

        return bridges;

        // Complexity analysis
        // Time : O(V) + O(E) + O(V + 2E)
        // Space : O(2E) + O(3V)
    }
}
