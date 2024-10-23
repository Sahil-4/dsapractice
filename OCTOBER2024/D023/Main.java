import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

class NodeDistancePair {
    int node;
    int time;

    NodeDistancePair(int n, int d) {
        this.node = n;
        this.time = d;
    }
}

class NodeDistancePairComparator implements Comparator<NodeDistancePair> {
    @Override
    public int compare(NodeDistancePair p1, NodeDistancePair p2) {
        if (p1.time != p2.time) {
            return p1.time - p2.time;
        }
        return p1.node - p2.node;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 23 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 743. Network Delay Time -
        // https://leetcode.com/problems/network-delay-time/

        int source = 1;
        int V = 2;
        int[][] edges = { { 1, 2, 1 } };

        int t = networkDelayTime(edges, V, source);
        System.out.println(t);
    }

    static int TIME_BOUND = (int) 1e9;

    static int networkDelayTime(int[][] edges, int V, int source) {
        // create adjacency list
        List<List<NodeDistancePair>> adj = new ArrayList<>();
        for (int i = 0; i < V + 1; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adj.get(edge[0]).add(new NodeDistancePair(edge[1], edge[2]));
        }

        // store min time taken to send signal to each node
        int[] times = new int[V + 1];
        for (int i = 1; i < V + 1; i++) {
            times[i] = TIME_BOUND;
        }

        // perform dijkstra
        PriorityQueue<NodeDistancePair> pq = new PriorityQueue<>(new NodeDistancePairComparator());

        times[source] = 0;
        pq.add(new NodeDistancePair(source, 0));

        while (!pq.isEmpty()) {
            NodeDistancePair top = pq.remove();

            int node = top.node;
            int time = top.time;

            for (NodeDistancePair next : adj.get(node)) {
                int nnode = next.node;
                int ntime = next.time + time;

                if (times[nnode] > ntime) {
                    times[nnode] = ntime;
                    pq.add(new NodeDistancePair(nnode, ntime));
                }
            }
        }

        // find max time taken node
        int maxTime = -1;
        for (int i = 1; i < V + 1; i++) {
            maxTime = Math.max(maxTime, times[i]);
        }

        // return answer
        return maxTime == TIME_BOUND ? -1 : maxTime;

        // Complexity analysis
        // Time : O(V + E) + O(V) + O(pe * log(pe)) + O(V)
        // Space : O(2E) + O(V) + O(pe)
        // pe = number of elements in priority queue = MAX_BREADTH(graph)
    }

    static void p2() {
        // Problem 2 : Geeksforgeeks Distance from the Source (Bellman-Ford Algorithm) -
        // https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

        /**
         * Bellman form 
         * - find distance to all other vertices from a given source vertex 
         * -------------------------- algorithm -------------------------- 
         * - given edges of directed graph 
         * {u, v, w} - u = source node, v = destination node, w = cost to reach to v from u 
         * create a distance array of type int[] to store distance from source to all other vertices 
         * initially assign MAX_VALUE to all distance[i] 
         * update value of distance[source] = 0
         * relax all edges N - 1, N = number of nodes / vertices 
         * relaxation means update distance like this 
         * if (distance[u] + w < distance[v]) distance[v] = distance[u] + w
         * to detect negative cycle perform relaxation Nth time 
         * if we are able to do relaxation Nth time then there is a negative cycle in the graph 
         */

         int source = 0;
        int V = 2;
        ArrayList<ArrayList<Integer>> edges = new ArrayList<>();
        edges.add(new ArrayList<>(Arrays.asList(0, 1, 9)));

        int[] distance = bellmanFord(V, edges, source);
        System.out.println(Arrays.toString(distance));
    }

    static int MAXD = (int) 1e8;

    static int[] bellmanFord(int V, ArrayList<ArrayList<Integer>> edges, int source) {
        // Write your code here
        int[] dist = new int[V];
        for (int i = 0; i < V; i++) {
            dist[i] = MAXD;
        }

        dist[source] = 0;

        for (int i = 1; i < V; i++) {
            for (ArrayList<Integer> edge : edges) {
                int u = edge.get(0);
                int v = edge.get(1);
                int w = edge.get(2);

                // relaxation
                if (dist[u] != MAXD && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                }
            }
        }

        // nth iteration - to check negative cycle
        for (ArrayList<Integer> edge : edges) {
            int u = edge.get(0);
            int v = edge.get(1);
            int w = edge.get(2);

            // relaxation
            if (dist[u] != MAXD && dist[u] + w < dist[v]) {
                // negative cycle
                int[] tempo = { -1 };
                return tempo;
            }
        }

        return dist;

        // Complexity analysis
        // Time : O(V) + O(V * E) + O(E)
        // Space : O(1)
    }
}
