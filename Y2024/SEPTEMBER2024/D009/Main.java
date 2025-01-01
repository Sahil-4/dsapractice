
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

class GFG {
    public static int H[] = new int[10009];
    public static int s = -1;

    public int parent(int i) {
        return (i - 1) / 2;
    }

    public int leftChild(int i) {
        return ((2 * i) + 1);
    }

    public int rightChild(int i) {
        return ((2 * i) + 2);
    }

    public void shiftUp(int i) {
        while (i > 0 && H[parent(i)] < H[i]) {
            int temp = H[i];
            H[i] = H[parent(i)];
            H[parent(i)] = temp;
            i = parent(i);
        }
    }

    public void shiftDown(int i) {
        int maxIndex = i;
        int l = leftChild(i);
        if (l <= s && H[l] > H[maxIndex]) {
            maxIndex = l;
        }
        int r = rightChild(i);

        if (r <= s && H[r] > H[maxIndex]) {
            maxIndex = r;
        }
        if (i != maxIndex) {
            int temp = H[i];
            H[i] = H[maxIndex];
            H[maxIndex] = temp;
            shiftDown(maxIndex);
        }
    }

    public void insert(int p) {
        s = s + 1;
        H[s] = p;
        shiftUp(s);
    }

    public static void main(String args[]) throws IOException {
        try (Scanner sc = new Scanner(System.in)) {
            GFG ob = new GFG();

            int t = sc.nextInt();
            while (t-- > 0) {
                int N = sc.nextInt();
                for (int i = 0; i < N; i++) {
                    int k = sc.nextInt();
                    ob.insert(k);
                }
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 1 of Heaps

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : GeeksForGeeks Implementation of Priority Queue using Binary Heap
        // https://www.geeksforgeeks.org/problems/implementation-of-priority-queue-using-binary-heap/1

        int max = extractMax();
        System.out.println(max);
    }

    static int extractMax() {
        // your code here
        GFG obj = new GFG();

        // get max priority element value
        int max = obj.H[0];

        // swap & shift - basically remove the high priority task re-strucure the heap
        obj.H[0] = obj.H[obj.s--];
        obj.shiftDown(0);

        return max;
    }

    static void p2() {
        // Problem 2 : Leetcode 215. Kth Largest Element in an Array -
        // https://leetcode.com/problems/kth-largest-element-in-an-array
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/k-largest-elements4206/1

        int[] arr = { 3, 5, 4, 2, 7, 12 };
        int k = 2;

        int kthL = findKthLargest(arr, k);
        System.out.println(kthL);
        int[] kthLArr = kLargest(arr, arr.length, k);
        System.out.println(Arrays.toString(kthLArr));
    }

    static int findKthLargest(int[] nums, int k) {
        // -- using priority quque or heap
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int e : nums) {
            pq.add(e);
            if (pq.size() > k)
                pq.poll();
        }

        return pq.peek();

        // Complexity analysis
        // Time : O(n * log(k)) O(n) for array traversal * O(log(k)) for insertion in
        // priority queue
        // Space : O(k) for storing k elements in priority queue
    }

    static int[] kLargest(int[] nums, int n, int k) {
        // code here
        // -- using priority quque or heap
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int e : nums) {
            pq.add(e);
            if (pq.size() > k)
                pq.poll();
        }

        int[] arr = new int[k];
        for (int i = 0; i < k; i++) {
            arr[k - i - 1] = pq.poll();
        }

        return arr;

        // Complexity analysis
        // Time : O(n * log(k)) O(n) for array traversal * O(log(k)) for insertion in
        // priority queue
        // Space : O(k) for storing k elements in priority queue
    }
}
