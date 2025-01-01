import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Day 31 of October

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 1192. Critical Connections in a Network -
        // https://leetcode.com/problems/critical-connections-in-a-network/
        // Geeksforgeeks -
        // https://www.geeksforgeeks.org/problems/critical-connections/1

        int N = 4;
        List<List<Integer>> connections = new ArrayList<>();
        connections.add(new ArrayList<>(Arrays.asList(0, 1)));
        connections.add(new ArrayList<>(Arrays.asList(1, 2)));
        connections.add(new ArrayList<>(Arrays.asList(2, 0)));
        connections.add(new ArrayList<>(Arrays.asList(1, 3)));

        List<List<Integer>> bridges = criticalConnections(N, connections);

        for (List<Integer> bridge : bridges) {
            System.out.println(bridge);
        }
    }

    static int MARK = 100;
    static int counter = 1;

    static void dfs(int node, int parent, List<List<Integer>> adj, int[] visited, int[] insertion_time, int[] lowest_time, List<List<Integer>> bridges) {
        visited[node] = MARK;

        insertion_time[node] = lowest_time[node] = counter++;

        for (int next : adj.get(node)) {
            if (next != parent && visited[next] != MARK) {
                dfs(next, node, adj, visited, insertion_time, lowest_time, bridges);
                lowest_time[node] = Math.min(lowest_time[node], lowest_time[next]);

                if (lowest_time[next] > insertion_time[node]) {
                    bridges.add(new ArrayList<>(Arrays.asList(node, next)));
                }
            } else if (next != parent) {
                lowest_time[node] = Math.min(lowest_time[node], lowest_time[next]);
            }
        }
    }

    static List<List<Integer>> criticalConnections(int N, List<List<Integer>> connections) {
        // create adjacency list
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            adj.add(new ArrayList<>());
        }
        for (List<Integer> conn : connections) {
            int u = conn.get(0);
            int v = conn.get(1);
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        int[] visited = new int[N];

        int[] insertion_time = new int[N];
        int[] lowest_time = new int[N];

        List<List<Integer>> bridges = new ArrayList<>();

        dfs(0, -1, adj, visited, insertion_time, lowest_time, bridges);

        return bridges;

        // Complexity analysis
        // Time : O(N + E) + O(N + 2E)
        // Space : O(N + 2E) + O(N) + O(N) + O(N) + (O(E) stack)
    }
}
