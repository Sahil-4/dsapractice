
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.TreeMap;

class Card {
    public int value;
    public int freq;

    public Card(int v, int f) {
        this.value = v;
        this.freq = f;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 4 of Heaps

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : GeeksForGeeks Convert Min Heap to Max Heap -
        // https://www.geeksforgeeks.org/problems/convert-min-heap-to-max-heap-1666385109/1

        int arr[] = { 1, 2, 3, 4 };
        convertMinToMaxHeap(arr.length, arr);
        System.out.println(Arrays.toString(arr));
    }

    static void maxHeapify(int arr[], int i, int n) {
        // get left and right childs
        int l = (i * 2) + 1;
        int r = (i * 2) + 2;

        // find largest among both childs and parent
        int largest = i; // assume parent is largest

        // now update largest
        if (l < n && arr[l] > arr[largest])
            largest = l;
        if (r < n && arr[r] > arr[largest])
            largest = r;

        // finally swap the values of parent node and largest child node ()
        if (largest == i)
            return;

        // swap
        arr[i] = arr[largest] ^ arr[i];
        arr[largest] = arr[largest] ^ arr[i];
        arr[i] = arr[largest] ^ arr[i];

        // call max heapify on changed node
        maxHeapify(arr, largest, n);
    }

    static void convertMinToMaxHeap(int N, int arr[]) {
        // code here
        for (int i = (N - 1) / 2; i >= 0; i--) {
            maxHeapify(arr, i, N);
        }

        // Complexity analysis
        // Time : O(n) * O(log(n)), O(n * log(n)) :: n = N
        // Space : O(1)
    }

    static void p2() {
        // Problem 2 : Leetcode 846. Hand of Straights -
        // https://leetcode.com/problems/hand-of-straights/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/hands-of-straights/0

        int hands[] = { 1, 2, 3, 6, 2, 3, 4, 7, 8 };
        int groupSize = 3;

        boolean check = isNStraightHand(hands, groupSize);
        System.out.println(check);
    }

    static boolean isNStraightHand(int[] hands, int groupSize) {
        Map<Integer, Integer> map = new TreeMap<>();
        for (int i = 0; i < hands.length; i++) {
            if (map.containsKey(hands[i])) {
                map.put(hands[i], map.get(hands[i]) + 1);
            } else {
                map.put(hands[i], 1);
            }
        }

        PriorityQueue<Card> pq = new PriorityQueue<>((Card a, Card b) -> a.value - b.value);
        for (Map.Entry<Integer, Integer> e : map.entrySet()) {
            pq.add(new Card(e.getKey(), e.getValue())); // key = card value, value = cards frequency
        }

        while (pq.size() >= groupSize) {
            List<Card> list = new ArrayList<>();
            Card prev = null;

            for (int i = 0; i < groupSize; i++) {
                Card c = pq.poll();
                c.freq--;
                if (c.freq > 0)
                    list.add(c);

                if (prev == null || (c.value - prev.value == 1)) {
                    prev = c;
                } else {
                    return false;
                }
            }

            pq.addAll(list);
        }

        return pq.isEmpty();

        // Complexity analysis
        // Time : O(n) * O(log(n)) + O(n) * O(log(n)) + O(n) * O(log(n))
        // Space : O(n) + O(n) + O(groupSize) {O(groupSize) for list}
        // ~
        // Time : O(n * log(n))
        // Space : O(2n) + O(groupSize)
    }
}
