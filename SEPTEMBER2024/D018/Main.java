
import java.util.PriorityQueue;

class KthLargest {
    PriorityQueue<Integer> pq;
    int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.pq = new PriorityQueue<>();

        for (int e : nums) {
            pq.add(e);
            if (pq.size() > k) pq.poll();
        }

        // Complexity analysis
        // Time : O(n * log(k))
        // Space : O(1), O(k) for priority queue
    }

    public int add(int val) {
        pq.add(val);

        if (pq.size() < k) return -1;
        if (pq.size() > k) pq.poll();

        return pq.peek();

        // Complexity analysis
        // Time : O(log(k))
        // Space : O(1)
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 10 of Heaps

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 703. Kth Largest Element in a Stream -
        // https://leetcode.com/problems/kth-largest-element-in-a-stream/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/kth-largest-element-in-a-stream2220/1

        int k = 5;
        int arr[] = { 5, 4, 3, 1, 5, 8, 12 };
        int n = 7;

        int kths[] = kthLargest(k, arr, n);
        for (int e : kths) {
            System.out.println(e);
        }
    }

    static int[] kthLargest(int k, int[] arr, int n) {
        // code here
        int kths[] = new int[n];

        KthLargest obj = new KthLargest(k, new int[0]);

        for (int i = 0; i < n; i++) {
            kths[i] = obj.add(arr[i]);
        }

        return kths;

        // Complexity analysis
        // Time : O(n * log(k))
        // Space : O(k) Priority queue
    }
}
