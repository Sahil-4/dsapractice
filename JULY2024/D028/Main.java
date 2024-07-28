import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;

public class Main {
    static int referPage(ArrayList<Integer> lru, int C, int page) {
        int out = 0;

        for (int i = 0; i < lru.size(); i++) {
            if (lru.get(i) == page) {
                // remove page from lru
                lru.remove(i);
                out = 1;
            }
        }

        // check if size is equal to C, and remove starting page
        if (lru.size() == C) {
            lru.remove(0);
        }

        // add page back in lru array
        lru.add(page);

        return out;
    }

    static int pageFaults_Solution1(int N, int C, int pages[]) {
        // code here
        ArrayList<Integer> lru = new ArrayList<>();
        int faults = 0;

        for (int i = 0; i < N; i++) {
            if (referPage(lru, C, pages[i]) == 0) {
                // page not found
                faults++;
            }
        }

        return faults;
    }

    static int pageFaults(int N, int C, int pages[]) {
        // code here
        // number of page faults
        int faults = 0;

        // store the pages currently in lru
        HashSet<Integer> lru = new HashSet<>(C);

        // store the indexes of the pages in lru
        HashMap<Integer, Integer> index = new HashMap<>();

        for (int i = 0; i < N; i++) {
            int page = pages[i];

            if (lru.size() < C) {
                if (!lru.contains(page)) {
                    lru.add(page);
                    faults++;
                }
                index.put(page, i);
            } else {
                if (!lru.contains(page)) {
                    // page with lru index
                    int lruPage = Integer.MAX_VALUE, pg = Integer.MIN_VALUE;
                    Iterator<Integer> itr = lru.iterator();

                    while (itr.hasNext()) {
                        int temp = itr.next();

                        if (index.get(temp) < lruPage) {
                            lruPage = index.get(temp);
                            pg = temp;
                        }
                    }

                    // remove page with lru index
                    lru.remove(pg);
                    lru.add(page);
                    faults++;
                }
                index.put(page, i);
            }
        }

        return faults;
    }

    static void p1() {
        // Problem 1 : Geeksforgeeks Page Faults in LRU -
        // https://www.geeksforgeeks.org/problems/page-faults-in-lru5603/1

        int N = 9;
        int C = 4;
        int pages[] = { 5, 0, 1, 3, 2, 4, 1, 0, 5 };

        int f = pageFaults(N, C, pages);
        System.out.println(f);
    }

    public static int[][] insert(int[][] intervals, int[] newInterval) {
        int N = intervals.length;
        List<int[]> res = new ArrayList<>();
        int i = 0;

        // left non overlapping intervals
        while (i < N && intervals[i][1] < newInterval[0]) {
            res.add(intervals[i++]);
        }

        // middle overlapping intervals
        while (i < N && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        res.add(newInterval);

        // right non overlapping intervals
        while (i < N) {
            res.add(intervals[i++]);
        }

        return res.toArray(int[][]::new);
    }

    static void p2() {
        // Problem 2 : Leetcode 57. Insert Interval -
        // https://leetcode.com/problems/insert-interval/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/insert-interval-1666733333/0

        int[][] intervals = { { 1, 2 }, { 3, 5 }, { 6, 7 }, { 8, 10 }, { 12, 16 } };
        int[] newInterval = { 4, 8 };
        int[][] intervalsRe = insert(intervals, newInterval);
        for (int[] intv : intervalsRe) {
            System.out.println("start time ::" + intv[0] + ", end time ::" + intv[1]);
        }
    }

    public static void main(String[] args) {
        // Day 28

        p1();

        p2();
    }
}