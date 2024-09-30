import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

class Pair {
    int number;
    int frequency;

    Pair(int n, int f) {
        this.number = n;
        this.frequency = f;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 22 of September 2024 - Heap revisiting

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 846. Hand of Straights -
        // https://leetcode.com/problems/hand-of-straights/
        // GeeksForGeeks - 
        // https://www.geeksforgeeks.org/problems/hands-of-straights/0

        int[] hand = {};
        int groupSize = 4;

        boolean check = isNStraightHand(hand, groupSize);
        System.out.println(check);
    }

    static boolean isNStraightHand(int[] hand, int groupSize) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < hand.length; i++) {
            map.put(hand[i], map.getOrDefault(hand[i], 0) + 1);
        }

        PriorityQueue<Pair> pq = new PriorityQueue<>((Pair p1, Pair p2) -> p1.number - p2.number);
        for (Map.Entry<Integer, Integer> e: map.entrySet()) {
            pq.add(new Pair(e.getKey(), e.getValue()));
        }

        while (pq.size() >= groupSize) {
            List<Pair> list = new ArrayList<>();
            Pair prev = null;

            for (int i = 0; i < groupSize; i++) {
                if (prev == null || pq.peek().number - prev.number == 1) {
                    prev = pq.poll();
                    prev.frequency--;
                    if (prev.frequency > 0) list.add(prev);
                } else {
                    return false;
                }
            }

            pq.addAll(list);
        }

        return pq.isEmpty();
    }
}
