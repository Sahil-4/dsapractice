import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

class Item {
    public int data;
    public int index;

    Item(int a, int b) {
        data = a;
        index = b;
    }
}

class CustomSort implements Comparator<Item> {
    @Override
    public int compare(Item a, Item b) {
        return a.data - b.data;
    }
}

public class Main {
    public static int maxMeetings(int start[], int end[], int n) {
        // add your code here
        Item arr[] = new Item[n];
        for (int i = 0; i < n; i++) {
            arr[i] = new Item(end[i], i);
        }

        Arrays.sort(arr, new CustomSort());

        int meetingsDone = 0;
        int endTime = -1;

        for (int i = 0; i < n; i++) {
            int _index = arr[i].index;
            if (endTime < start[_index]) {
                endTime = end[_index];
                meetingsDone++;
            }
        }

        return meetingsDone;
    }

    static void p1() {
        // Problem 1 : Geeksforgeeks N meetings in one room -
        // https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

        int n = 6;
        int start[] = { 1, 3, 8, 0, 5, 5 };
        int end[] = { 2, 4, 9, 6, 7, 9 };

        int meetingsDone = maxMeetings(start, end, n);
        System.out.println(meetingsDone);
    }

    public static int maxEvents(int[][] events) {
        Arrays.sort(events, (a, b) -> a[0] - b[0]);

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int currDay = 0, eventsDone = 0;
        int i = 0, n = events.length;

        while (!pq.isEmpty() || i < n) {
            if (pq.isEmpty()) {
                currDay = events[i][0];
            }

            while (i < n && events[i][0] <= currDay) {
                pq.offer(events[i][1]);
                i++;
            }

            pq.poll();
            currDay++;
            eventsDone++;

            while (!pq.isEmpty() && pq.peek() < currDay) {
                pq.poll();
            }
        }

        return eventsDone;
    }

    static void p2() {
        // Problem 2 : Leetcode 1353. Maximum Number of Events That Can Be Attended -
        // https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/

        int events[][] = {{1,2},{2,3},{3,4}};
        int es = maxEvents(events);
        System.out.println(es);
    }

    public static void main(String[] args) {
        // Day 26 - Day 6 of Greedy

        p1();

        p2();
    }
}