
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        // Day 7 of Heaps

        p1();
    }

    static void p1() {
        // P1 Leetcode 451. Sort Characters By Frequency -
        // https://leetcode.com/problems/sort-characters-by-frequency/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/0

        String s = "abaabsc";
        String sorted = frequencySort(s);
        System.out.println(sorted);

        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(5);
        arr.add(5);
        arr.add(1);
        arr.add(2);
        arr.add(2);
        List<Integer> sortedList = frequencySort(arr);
        System.out.println(sortedList.toString());
    }

    static List<Integer> frequencySort(ArrayList<Integer> arr) {
        // Map<Character, Integer> freq = new TreeMap<>();
        Map<Integer, Integer> freq = new HashMap<>();
        for (int i = 0; i < arr.size(); i++) {
            freq.put(arr.get(i), freq.getOrDefault(arr.get(i), 0) + 1);
        }

        PriorityQueue<Integer>[] list = new PriorityQueue[arr.size() + 1];
        for (int key : freq.keySet()) {
            int f = freq.get(key);
            if (list[f] == null) {
                list[f] = new PriorityQueue<>();
            }

            list[f].add(key);
        }

        ArrayList<Integer> ans = new ArrayList<>();
        for (int i = list.length - 1; i >= 0; i--) {
            if (list[i] == null) continue;

            while (!list[i].isEmpty()) {
                int el = list[i].poll();

                for (int j = 0; j < i; j++) {
                    ans.add(el);
                }
            }
        }

        return ans;

        // Complexity analyssi
        // Time : O(n) + O(n * log(n)) + O(n)
        // Space : O(n) + O(n)
    }

    static String frequencySort(String s) {
        // Map<Character, Integer> freq = new TreeMap<>();
        Map<Character, Integer> freq = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            freq.put(s.charAt(i), freq.getOrDefault(s.charAt(i), 0) + 1);
        }

        ArrayList<Character>[] list = new ArrayList[s.length() + 1];
        for (char key : freq.keySet()) {
            int f = freq.get(key);
            if (list[f] == null) {
                list[f] = new ArrayList<>();
            }

            list[f].add(key);
        }

        StringBuilder ans = new StringBuilder();
        for (int i = list.length - 1; i >= 0; i--) {
            if (list[i] == null) continue;

            for (char c : list[i]) {
                for (int j = 0; j < i; j++) {
                    ans.append(c);
                }
            }
        }

        return ans.toString();

        // Complexity analyssi
        // Time : O(n) + O(n) + O(n)
        // Space : O(n) + O(n) + O(n)
    }
}
