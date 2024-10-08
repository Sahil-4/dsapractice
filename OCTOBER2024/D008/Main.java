
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

class Pair {
    int first;
    int second;

    Pair(int f, int s) {
        this.first = f;
        this.second = s;
    }
}

class PairComparator implements Comparator<Pair> {
    @Override
    public int compare(Pair p1, Pair p2) {
        if (p1.first != p2.first) {
            return p1.first - p2.first;
        }
        return p1.second - p2.second;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 8 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : GeeksForGeeks Dijkstra Algorithm -
        // https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

        int source = 2;
        int V = 3;
        ArrayList<ArrayList<ArrayList<Integer>>> adj = new ArrayList<>();

        int[] dist = dijkstra(V, adj, source);
        System.out.println(Arrays.toString(dist));
    }

    static int MAX = (int) 1e9;

    // Function to find the shortest distance of all the vertices
    // from the source vertex S.
    static int[] dijkstra(int V, ArrayList<ArrayList<ArrayList<Integer>>> adj, int source) {
        // Write your code here
        int[] result = new int[V];
        for (int i = 0; i < V; i++) {
            result[i] = MAX;
        }
        result[source] = 0;

        PriorityQueue<Pair> pq = new PriorityQueue<>(new PairComparator());
        pq.add(new Pair(0, source));

        while (!pq.isEmpty()) {
            Pair top = pq.remove();

            int cost = top.first;
            int node = top.second;

            for (ArrayList<Integer> nc : adj.get(node)) {
                int nnode = nc.get(0);
                int ncost = nc.get(1);

                if (result[nnode] > cost + ncost) {
                    result[nnode] = cost + ncost;
                    pq.add(new Pair(cost + ncost, nnode));
                }
            }
        }

        return result;
    }

    static void p2() {
        // Problem 2 : Leetcode 743. Network Delay Time -
        // https://leetcode.com/problems/network-delay-time/

        int source = 2;
        int V = 3;
        int[][] times = {
                { 2, 1, 1 }, { 2, 3, 1 }, { 3, 4, 1 }
        };

        int maxDelay = networkDelayTime(times, V, source);
        System.out.println(maxDelay);
    }

    static int networkDelayTime(int[][] times, int V, int source) {
        ArrayList<ArrayList<ArrayList<Integer>>> adj = new ArrayList<>();

        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] time : times) {
            // make nodes zero based
            int src = time[0] - 1;
            int dst = time[1] - 1;

            // delay or edge weight
            int del = time[2];

            ArrayList<Integer> conn = new ArrayList<>();
            conn.add(dst);
            conn.add(del);

            adj.get(src).add(conn);
        }

        int[] result = dijkstra(V, adj, source - 1);

        int ans = -1;
        for (int i = 0; i < V; i++) {
            ans = Math.max(ans, result[i]);
        }

        return ans == MAX ? -1 : ans;

        // Complexity analysis
        // Time : O(E) + O(V) + O(E * log(V)) + O(V)
        // Space : O(E) + O(V) + O(V)
    }
}