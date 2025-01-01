import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

class CustomComparator implements Comparator<int[]> {
    @Override
    public int compare(int[] a, int[] b) {
        for (int i = 0; i < 3; i++) {
            if (a[i] != b[i]) {
                return a[i] - b[i];
            }
        }
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 25 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance -
        // https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

        int V = 4;
        int[][] edges = { { 0, 1, 3 }, { 1, 2, 1 }, { 1, 3, 4 }, { 2, 3, 1 } };
        int distanceThreshold = 4;

        int city = findTheCity(V, edges, distanceThreshold);
        System.out.println(city);
    }

    static int MAXD = (int) 1e9;

    static int findTheCity(int V, int[][] edges, int distanceThreshold) {
        // ---- trying floyd warshall ----

        // adjacency matrix - graph
        int[][] graph = new int[V][V];
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                graph[i][j] = MAXD;
                if (i == j) {
                    graph[i][j] = 0;
                }
            }
        }

        for (int[] edge : edges) {
            graph[edge[0]][edge[1]] = edge[2];
            graph[edge[1]][edge[0]] = edge[2];
        }

        // floyd
        for (int mid = 0; mid < V; mid++) {
            for (int src = 0; src < V; src++) {
                for (int end = 0; end < V; end++) {
                    graph[src][end] = Math.min(graph[src][end], graph[src][mid] + graph[mid][end]);
                }
            }
        }

        // find city with minimum neighbours at the distanceThreshold
        int city = 0;
        int neig = V;
        for (int src = 0; src < V; src++) {
            int tneig = 0;
            for (int dest = 0; dest < V; dest++) {
                if (graph[src][dest] <= distanceThreshold) {
                    tneig++;
                }
            }
            if (tneig <= neig) {
                city = src;
                neig = tneig;
            }
        }

        return city;

        // Complexity analysis
        // Time : O(V^2) + O(E) + (V^3) + (V^2)
        // Space : O(V^2)
    }

    static void p2() {
        // Problem 2 : Geeksforgeeks Minimum Spanning Tree -
        // https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1

        int V = 0;
        int E = 0;
        List<List<int[]>> adj = new ArrayList<>();

        int mstSum = spanningTree(V, E, adj);
        System.out.println(mstSum);
    }

    static int MARK = 100;

    static int spanningTree(int V, int E, List<List<int[]>> adj) {
        // Code Here.
        int mstSum = 0;

        int[] visited = new int[V];
        List<int[]> mstEdges = new ArrayList<>();
        // {weight, node, parent}
        PriorityQueue<int[]> pq = new PriorityQueue<>(new CustomComparator());

        pq.add(new int[] { 0, 0, -1 });

        while (!pq.isEmpty()) {
            int[] top = pq.remove();

            int weight = top[0];
            int node = top[1];
            int parent = top[2];

            if (visited[node] == MARK) {
                continue;
            }

            visited[node] = MARK;

            if (parent != -1) {
                mstEdges.add(new int[] { node, parent });
                mstSum += weight;
            }

            for (int[] next : adj.get(node)) {
                int nnode = next[0];
                int nweight = next[1];

                if (visited[nnode] == MARK) {
                    continue;
                }

                pq.add(new int[] { nweight, nnode, node });
            }
        }

        return mstSum;

        // Complexity analysis
        // Time : O(V * log(V))
        // Space : O(V) + O(V) + O(E)
    }
}
