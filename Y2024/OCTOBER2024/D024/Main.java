import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        // Day 24 of October

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 1976. Number of Ways to Arrive at Destination -
        // https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

        int V = 7;
        int[][] roads = {};

        int paths = countPaths(V, roads);
        System.out.println(paths);
    }

    static long MAXD = (long) 1e15;
    static long MODO = (long) 1e9 + 7;

    static int countPaths(int V, int[][] roads) {
        // adjacency list
        List<List<long[]>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] road : roads) {
            adj.get(road[0]).add(new long[] { road[1], road[2] });
            adj.get(road[1]).add(new long[] { road[0], road[2] });
        }

        long[] distance = new long[V];
        long[] paths = new long[V];

        for (int i = 0; i < V; i++) {
            distance[i] = MAXD;
        }

        long src = 0;
        long dest = V - 1;

        PriorityQueue<long[]> pq = new PriorityQueue<>((long[] arr1, long[] arr2) -> Long.compare(arr1[1], arr2[1]));

        distance[(int) src] = 0;
        paths[(int) src] = 1;
        pq.add(new long[] { src, 0 });

        while (!pq.isEmpty()) {
            long[] top = pq.remove();

            long node = top[0];
            long dist = top[1];

            if (distance[(int) node] < dist) {
                continue;
            }

            for (long[] next : adj.get((int) node)) {
                long nnode = next[0];
                long ndist = dist + next[1];

                if (distance[(int) nnode] == ndist) {
                    paths[(int) nnode] = (paths[(int) nnode] + paths[(int) node] % MODO);
                } else if (distance[(int) nnode] > ndist) {
                    paths[(int) nnode] = (paths[(int) node] % MODO);
                    distance[(int) nnode] = ndist;
                    pq.add(new long[] { nnode, ndist });
                }
            }
        }

        return (int) (paths[(int) dest] % MODO);

        // Complexity analysis
        // Time : O(V) + O(E) + O(V) + O(V + 2E)
        // Space : O(2E) + O(V) + O(V) + O(E)
    }

    static void p2() {
        // Problem 2 : Geeksforgeeks Floyd Warshall -
        // https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1

        int[][] matrix = {
                { 0, 4, 2, 1, 2, 9, 4, 8, -1, 4, -1, -1 },
                { 9, 0, 3, 6, 2, 6, 2, 3, 6, -1, -1, 3 },
                { 7, 1, 0, 10, 8, 9, 1, 3, -1, 7, -1, 10 },
                { 5, 1, 9, 0, 3, -1, 1, 10, 7, 1, -1, 7 },
                { -1, 5, 1, 4, 0, 2, 10, 4, 10, 6, 4, 5 },
                { 7, 8, 3, 7, 5, 0, 5, 1, 3, 5, 7, 2 },
                { 6, -1, 6, 1, 10, 7, 0, 10, -1, -1, 7, 7 },
                { -1, 3, 2, 7, 4, -1, 4, 0, 10, 5, 6, 10 },
                { 10, 6, 1, 10, 4, 4, 7, 10, 0, 4, 7, 4 },
                { 1, 1, 6, 8, 8, 9, 2, 10, 6, 0, -1, 3 },
                { 5, 9, 3, -1, 4, 3, -1, -1, -1, 3, 0, 1 },
                { 2, 2, 8, 6, 2, 4, 4, 3, -1, 3, 4, 0 }
        };

        shortestDistance(matrix);

        for (int mat[] : matrix) {
            System.out.println(Arrays.toString(mat));
        }
    }

    static void shortestDistance(int[][] mat) {
        // Code here
        /**
         * Floyd Warshall
         * Simple brute force algorithm to find distance from each node to all other nodes
         * 
         * to find distance from ui to vi we take an intermediatory ki
         * and go from ui to ki and then ki to vi
         * this will be the distance from ui to vi
         * 
         * we will have a adjacency matrix
         * where matrix[i][j] is weight of edge from i to j
         * 
         * to find shortest distance between each pair of node
         * we take a src, a destination and an intermediatory
         * for (interm) for (src) for (dest)
         * distance[src][dest] = MIN(distance[src][dest], distance[src][interm] +
         * distance[interm][dest])
         */

        int V = mat.length;
        int MAXD = (int) 1e9;

        // initial config
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (mat[i][j] == -1) {
                    mat[i][j] = MAXD;
                }
                if (i == j) {
                    mat[i][j] = 0;
                }
            }
        }

        for (int interm = 0; interm < V; interm++) {
            for (int src = 0; src < V; src++) {
                for (int dest = 0; dest < V; dest++) {
                    mat[src][dest] = Math.min(mat[src][dest], mat[src][interm] + mat[interm][dest]);
                }
            }
        }

        // un reachable nodes
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (mat[i][j] == MAXD) {
                    mat[i][j] = -1;
                }
            }
        }

        // Complexity analysis
        // Time : O(V ^ 3)
        // Space : O(1)
    }
}
