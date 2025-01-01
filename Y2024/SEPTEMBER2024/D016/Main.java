import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

class Pair {
    int difference;
    int element;

    public Pair(int d, int e) {
        this.difference = d;
        this.element = e;
    }
}

class CustomComparator implements Comparator<Pair> {
    @Override
    public int compare(Pair a, Pair b) {
        if (a.difference != b.difference) return b.difference - a.difference;
        return b.element - a.element;
    }
}


public class Main {
    public static void main(String[] args) {
        // Day 8 of Heaps

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 658. Find K Closest Elements -
        // https://leetcode.com/problems/find-k-closest-elements/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/k-closest-elements3619/1

        int arr[] = { 1, 2, 3, 4, 5 };
        int k = 2;
        int x = 5;

        List<Integer> list = findClosestElements(arr, k, x);
        List<Integer> list2 = findClosestElements_Solution2(arr, k, x);
        System.out.println(list.toString());
        System.out.println(list2.toString());
    }

    static List<Integer> findClosestElements(int[] arr, int k, int x) {
        PriorityQueue<Pair> pq = new PriorityQueue<>(new CustomComparator());
        for (int i = 0; i < arr.length; i++) {
            pq.add(new Pair(Math.abs(arr[i] - x), arr[i]));
            if (pq.size() > k)
                pq.poll();
        }

        List<Integer> list = new ArrayList<>();
        while (!pq.isEmpty()) {
            list.add(pq.poll().element);
        }

        Collections.sort(list);

        return list;

        // Complexity analysis
        // Time : O(n * log(n)) + O(n * log(n)) + O(n * log(n))
        // Space : O(n)
    }

    static List<Integer> findClosestElements_Solution2(int[] arr, int k, int x) {
        int low = 0;
        int high = arr.length - 1;

        while (high - low >= k) {
            if (Math.abs(arr[low] - x) > Math.abs(arr[high] - x)) {
                low++;
            } else {
                high--;
            }
        }

        List<Integer> list = new ArrayList<>();
        for (; low <= high; low++) {
            list.add(arr[low]);
        }

        return list;
    }
}
