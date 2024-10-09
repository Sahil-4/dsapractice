
import java.util.ArrayList;
import java.util.PriorityQueue;

class Pair {
    long node;
    long cost;

    Pair(long n, long c) {
        this.node = n;
        this.cost = c;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 9 of October

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 1976. Number of Ways to Arrive at Destination -
        // https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/number-of-ways-to-arrive-at-destination/1

        int n = 3;
        int[][] roads = { { 0, 6, 7 }, { 0, 1, 2 }, { 1, 2, 3 }, { 1, 3, 3 }, { 6, 3, 3 }, { 3, 5, 1 }, { 6, 5, 1 },
                { 2, 5, 1 }, { 0, 4, 5 }, { 4, 6, 2 } };

        int paths = countPaths(n, roads);
        System.out.println(paths);
    }

    static long MAXIMUM = Long.MAX_VALUE;
    static long MODO = (int) 1e9 + 7;

    static int countPaths(int n, int[][] roads) {
        // adjacency list
        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] road : roads) {
            adj.get(road[0]).add(new Pair(road[1], road[2]));
            adj.get(road[1]).add(new Pair(road[0], road[2]));
        }

        // ways to reach at any vertec/city
        long[] ways = new long[n];

        // distance from source to this city
        long[] distance = new long[n];
        for (int i = 0; i < n; i++) {
            distance[i] = MAXIMUM;
            ways[i] = 0;
        }

        PriorityQueue<Pair> pq = new PriorityQueue<>((Pair p1, Pair p2) -> Long.compare(p1.cost, p2.cost));

        // beginning

        int start = 0;
        int destination = n - 1;

        ways[start] = 1;
        distance[start] = 0;

        // add start { city, distance }
        pq.add(new Pair(start, 0));

        while (!pq.isEmpty()) {
            Pair top = pq.remove();

            long node = top.node;
            long cost = top.cost;

            for (Pair p : adj.get((int) node)) {
                long adjNode = p.node;
                long nCost = p.cost;

                if (cost + nCost < distance[(int) adjNode]) {
                    distance[(int) adjNode] = cost + nCost;
                    ways[(int) adjNode] = ways[(int) node] % MODO;
                    pq.add(new Pair(adjNode, cost + nCost));
                } else if (cost + nCost == distance[(int) adjNode]) {
                    ways[(int) adjNode] = (ways[(int) adjNode] + ways[(int) node]) % MODO;
                }
            }
        }

        return (int) (ways[(int) destination] % MODO);
    }
}