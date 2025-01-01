
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

class Task {
    public int freq;
    public char task;

    public Task(int f, char t) {
        this.freq = f;
        this.task = t;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 3 of Heaps

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : GeeksForGeeks Does array represent Heap-
        // https://www.geeksforgeeks.org/problems/does-array-represent-heap4345/1

        long arr[] = {};
        long n = 5;
        boolean check = countSub(arr, n);
        System.out.println(check);
    }

    static int childLeft(int i) {
        return (i * 2 + 1);
    }

    static int childRight(int i) {
        return (i * 2 + 2);
    }

    static boolean validateHeap(long arr[], long n, int idx) {
        // Your code goes here
        if (idx >= n) return true;
        if ((childLeft(idx) < n && arr[idx] < arr[childLeft(idx)]) || (childRight(idx) < n && arr[idx] < arr[childRight(idx)])) return false;

        boolean l = validateHeap(arr, n, childLeft(idx));
        if (!l) return false;
        return validateHeap(arr, n, childRight(idx));
    }

    static boolean countSub(long arr[], long n) {
        // Your code goes here
        return validateHeap(arr, n, 0);
    }

    static void p2() {
        // Problem 2 : Leetcode 621. Task Scheduler -
        // https://leetcode.com/problems/task-scheduler/
        // GeeksForGeeks - 
        // https://www.geeksforgeeks.org/problems/task-scheduler/1

        char tasks[] = { 'A', 'A', 'C', 'B', 'A', 'B' };
        int n = 2;

        int interval = leastInterval(tasks, n);
        System.out.println(interval);
    }

    static int leastInterval(char[] tasks, int n) {
        int freq[] = new int[26];
        for (int i = 0; i < tasks.length; i++) {
            freq[tasks[i] - 'A']++;
        }

        PriorityQueue<Task> pq = new PriorityQueue<>((Task t1, Task t2) -> t2.freq - t1.freq);
        for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) pq.add(new Task(freq[i], (char) ('A' + i)));
        }

        int interval = 0;

        while (!pq.isEmpty()) {
            List<Task> list = new ArrayList<>();

            for (int i = 0; i <= n; i++) {
                if (!pq.isEmpty()) {
                    Task t = pq.poll();
                    t.freq--;
                    list.add(t);
                }
            }

            for (Task t : list) {
                if (t.freq > 0) pq.add(t);
            }

            if (pq.isEmpty()) {
                interval += list.size();
            } else {
                interval += n + 1;
            }
        }

        return interval;

        // Complexity analysis
        // Time : O(arr_len) + O(26) + O(arr_len * log(26)), O(arr_len)
        // log(26) for heap operation
        // Space : O(26) + O(26) + O(n)
        // O(n) for holding n different tasks in list
    }
}
