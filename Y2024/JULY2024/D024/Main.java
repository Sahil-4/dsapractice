import java.util.Arrays;
import java.util.Comparator;

class Item {
    int value, weight;

    Item(int x, int y) {
        this.value = x;
        this.weight = y;
    }
}

class CustomSort implements Comparator<Item> {
    @Override
    public int compare(Item a, Item b) {
        // DESCENDING ORDER

        double v1 = (double) a.value / a.weight;
        double v2 = (double) b.value / b.weight;

        if (v1 < v2)
            return 1;
        else if (v1 > v2)
            return -1;
        return 0;
    }
}

public class Main {
    // Function to get the maximum total value in the knapsack.
    static double fractionalKnapsack(int W, Item arr[], int N) {
        // Your code here
        Arrays.sort(arr, new CustomSort());

        double totalValue = 0.0;

        for (int i = 0; i < N; i++) {
            if (arr[i].weight <= W) {
                totalValue += arr[i].value;
                W -= arr[i].weight;
            } else {
                totalValue += ((double) arr[i].value / (double) arr[i].weight) * (double) W;
                break;
            }
        }

        return totalValue;
    }

    static void p1() {
        // Problem 1 : Geeksforgeeks Fractional Knapsack -
        // https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

        int W = 24, N = 6;
        Item arr[] = new Item[N];
        arr[0] = new Item(1, 4);
        arr[1] = new Item(5, 9);
        arr[2] = new Item(7, 6);
        arr[3] = new Item(2, 3);
        arr[4] = new Item(7, 7);
        arr[5] = new Item(10, 3);
        double fk = fractionalKnapsack(W, arr, N);
        System.out.println(fk);
    }

    public static boolean lemonadeChange(int[] bills) {
        int fives = 0, tens = 0;

        for (int i = 0; i < bills.length; i++) {
            switch (bills[i]) {
                case 5 -> fives++;
                case 10 -> {
                    if (fives < 1)
                        return false;
                    tens++;
                    fives--;
                }
                default -> {
                    if (tens >= 1 && fives >= 1) {
                        tens--;
                        fives--;
                    } else if (fives >= 3) {
                        fives--;
                        fives--;
                        fives--;
                    } else {
                        return false;
                    }
                }
            }
        }

        return true;
    }

    static void p2() {
        // Problem 2 : Leetcode 860. Lemonade Change -
        // https://leetcode.com/problems/lemonade-change/descripion/
        // Geeksforgeeks - https://www.geeksforgeeks.org/problems/lemonade-change/0

        int arr[] = { 5, 5, 5, 10, 20 };
        boolean b = lemonadeChange(arr);
        System.out.println(b);
    }

    public static void main(String args[]) {
        // Day 24 - Day 4 of greedy

        p1();

        p2();
    }
}
