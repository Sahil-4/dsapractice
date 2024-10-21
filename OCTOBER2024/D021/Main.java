import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

class iPair {
    int first, second;

    iPair(int first, int second) {
        this.first = first; // node
        this.second = second; // distance
    }
}

class CustomSort implements Comparator<iPair> {
    @Override
    public int compare(iPair p1, iPair p2) {
        if (p1.second != p2.second) {
            return p1.second - p2.second;
        }
        return p1.first - p2.first;
    }
}

class Pair {
    int destination;
    int cost;

    Pair(int d, int c) {
        this.destination = d;
        this.cost = c;
    }
}

class Trio {
    int cost;
    int node;
    int stops;

    Trio(int c, int n, int s) {
        this.cost = c;
        this.node = n;
        this.stops = s;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 21 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Geeksforgeeks Dijkstra Algorithm -
        // https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

        ArrayList<ArrayList<iPair>> adj = new ArrayList<>();
        adj.add(new ArrayList<>(Arrays.asList(new iPair(1, 1), new iPair(2, 6))));
        adj.add(new ArrayList<>(Arrays.asList(new iPair(2, 3), new iPair(0, 1))));
        adj.add(new ArrayList<>(Arrays.asList(new iPair(1, 3), new iPair(0, 6))));
        int src = 2;

        ArrayList<Integer> out = dijkstra(adj, src);
        System.out.println(out.toString());
    }

    static int MAXD = (int) 1e9;

    // Function to find the shortest distance of all the vertices
    // from the source vertex src.
    static ArrayList<Integer> dijkstra(ArrayList<ArrayList<iPair>> adj, int src) {
        // Write your code here
        int V = adj.size();

        ArrayList<Integer> distances = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            distances.add(MAXD);
        }

        PriorityQueue<iPair> pq = new PriorityQueue<>(new CustomSort());
        pq.add(new iPair(src, 0));
        distances.set(src, 0);

        while (!pq.isEmpty()) {
            iPair top = pq.remove();

            int node = top.first;
            int distance = top.second;

            for (iPair next : adj.get(node)) {
                int nextNode = next.first;
                int nodeDist = next.second;

                if (distances.get(nextNode) > distance + nodeDist) {
                    distances.set(nextNode, distance + nodeDist);
                    pq.add(new iPair(nextNode, distance + nodeDist));
                }
            }
        }

        return distances;

        // Complexity analysis
        // Time : O(V) + O(V + E * Log(E))
        // Space : O(E)
    }

    static void p2() {
        // Problem 2 : Leetcode 787. Cheapest Flights Within K Stops -
        // https://leetcode.com/problems/cheapest-flights-within-k-stops/

        int V = 4;
        int[][] flights = { { 0, 1, 100 }, { 1, 2, 100 }, { 2, 0, 100 }, { 1, 3, 600 }, { 2, 3, 200 } };
        int src = 0;
        int dst = 3;
        int k = 2;

        int cost = findCheapestPrice(V, flights, src, dst, k);
        System.out.println(cost);
    }

    static int findCheapestPrice(int V, int[][] flights, int src, int dst, int k) {
        List<List<Pair>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }

        for (int flight[] : flights) {
            int from = flight[0];
            int to = flight[1];
            int cost = flight[2];

            adj.get(from).add(new Pair(to, cost));
        }

        int[] costs = new int[V];
        for (int i = 0; i < V; i++) {
            costs[i] = MAXD;
        }

        // PriorityQueue<Trio> que = new PriorityQueue<>(new CustomSort());
        Queue<Trio> que = new LinkedList<>();

        costs[src] = 0;
        que.add(new Trio(0, src, 0));

        while (!que.isEmpty()) {
            Trio top = que.remove();

            int node = top.node;
            int cost = top.cost;
            int stops = top.stops;

            if (stops > k) {
                continue;
            }

            for (Pair next : adj.get(node)) {
                int nnode = next.destination;
                int ncost = next.cost;

                if (costs[nnode] > cost + ncost && stops <= k) {
                    costs[nnode] = cost + ncost;
                    que.add(new Trio(cost + ncost, nnode, stops + 1));
                }
            }
        }

        return costs[dst] == MAXD ? -1 : costs[dst];

        // Complexity analysis
        // Time : O(V) + O(E) + O(V) + O(V + E)
        // Space : O(V + E) + O(V) + O(E)
    }
}
