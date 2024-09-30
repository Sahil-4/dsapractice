import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Elem {
    int freq;
    int value;

    public Elem(int f, int v) {
        this.freq = f;
        this.value = v;
    }
}

class CustomComparator implements Comparator<Elem> {
    @Override
    public int compare(Elem e1, Elem e2) {
        if (e1.freq != e2.freq)
            return e2.freq - e1.freq;
        return e2.value - e1.value;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 6 of Heaps

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 347. Top K Frequent Elements -
        // https://leetcode.com/problems/top-k-frequent-elements/description/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/top-k-frequent-elements-in-array/1

        int[] nums = { 1, 1, 1, 2, 2, 3 };
        int k = 2;

        int[] top = topKFrequent(nums, k);
        for (int e : top) {
            System.out.println(e);
        }
    }

    static int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int e : nums) {
            map.put(e, map.getOrDefault(e, 0) + 1);
        }

        ArrayList<Integer>[] listArr = new ArrayList[nums.length + 1];
        for (Map.Entry<Integer, Integer> e : map.entrySet()) {
            int freq = e.getValue();
            int key = e.getKey();

            if (listArr[freq] == null) {
                listArr[freq] = new ArrayList<>();
            }

            listArr[freq].add(key);
        }

        int arr[] = new int[k];
        int c = 0;
        for (int i = nums.length; i >= 0; i--) {
            if (listArr[i] == null)
                continue;
            for (int e : listArr[i]) {
                arr[c++] = e;
                if (c == k)
                    return arr;
            }
        }

        return arr;

        // Complexity analysis
        // Time : O(n) + O(n) + O(n) --> O(n)
        // Space : O(n) + O(n) --> O(2n)
    }

    static int[] topKFrequent_Solution1(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int e : nums) {
            if (map.containsKey(e)) {
                map.put(e, map.get(e) + 1);
            } else {
                map.put(e, 1);
            }
        }

        PriorityQueue<Elem> pq = new PriorityQueue<>((Elem e1, Elem e2) -> e2.freq - e1.freq);
        for (Map.Entry<Integer, Integer> e : map.entrySet()) {
            pq.add(new Elem(e.getValue(), e.getKey()));
        }

        int arr[] = new int[k];
        for (int i = 0; i < k; i++) {
            Elem e = pq.poll();
            arr[i] = e.value;
        }

        return arr;

        // Complexity analysis
        // Time : O(n) + O(n * log(n)) + O(k) --> O(n * log(n))
        // Space : O(n) + O(n) + O(k) --> O(2n) + O(k)
    }

    public int[] topK(int[] nums, int k) {
        // Code here
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int e : nums) {
            map.put(e, map.getOrDefault(e, 0) + 1);
        }

        PriorityQueue<Elem> pq = new PriorityQueue<>(new CustomComparator());
        for (Map.Entry<Integer, Integer> e : map.entrySet()) {
            pq.add(new Elem(e.getValue(), e.getKey()));
        }

        int arr[] = new int[k];
        for (int i = 0; i < k; i++) {
            Elem e = pq.poll();
            arr[i] = e.value;
        }

        return arr;

        // Complexity analysis
        // Time : O(n) + O(n * log(n)) + O(k) --> O(n * log(n))
        // Space : O(n) + O(n) --> O(2n)
    }
}
