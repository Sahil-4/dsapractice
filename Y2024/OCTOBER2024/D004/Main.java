import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class Pair {
    int destination;
    int cost;

    Pair(int d, int c) {
        destination = d;
        cost = c;
    }
}

class Trio {
    int stops;
    int src;
    int cost;

    Trio(int st, int sc, int c) {
        stops = st;
        src = sc;
        cost = c;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 4 of October

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 787. Cheapest Flights Within K Stops -
        // https://leetcode.com/problems/cheapest-flights-within-k-stops/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/cheapest-flights-within-k-stops/0

        int n = 0;
        int[][] flights = {};
        int source = 0;
        int destination = 3;
        int k = 2;
        int cost = findCheapestPrice(n, flights, source, destination, k);
        System.out.println(cost);
    }

    static int findCheapestPrice(int n, int[][] flights, int source, int destination, int k) {
        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] flight : flights) {
            int from = flight[0];
            int to = flight[1];
            int cost = flight[2];
            adj.get(from).add(new Pair(to, cost));
        }

        // stops, current node/city, cost
        Queue<Trio> q = new LinkedList<>();
        q.add(new Trio(0, source, 0));

        int dist[] = new int[n];
        for (int i = 0; i < n; i++) {
            dist[i] = (int) (1e9);
        }
        dist[source] = 0;

        while (!q.isEmpty()) {
            Trio top = q.remove();

            int stops = top.stops;
            int city = top.src;
            int cost = top.cost;

            if (stops > k) {
                continue;
            }

            for (Pair p : adj.get(city)) {
                int e = p.destination;
                int c = p.cost;

                if ((cost + c < dist[e]) && stops <= k) {
                    dist[e] = cost + c;
                    q.add(new Trio(stops + 1, e, cost + c));
                }
            }
        }

        return dist[destination] == (int) (1e9) ? -1 : dist[destination];

        // Complexity analysis
        // Time : O(s) s = flights.length
        // Space : O(n*n) + O(s) + O(n)
    }
}