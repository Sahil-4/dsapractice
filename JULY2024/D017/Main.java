import java.util.HashMap;

class Main {
    public static int totalFruit(int[] fruits) {
        int BASKETS = 2;
        int totalFruits = 0;
        HashMap<Integer, Integer> hMap = new HashMap<>();

        for (int l = 0, r = 0; r < fruits.length; r++) {
            if (hMap.containsKey(fruits[r])) {
                hMap.put(fruits[r], hMap.get(fruits[r]) + 1);
            } else {
                hMap.put(fruits[r], 1);
            }

            while (hMap.size() > BASKETS) {
                hMap.put(fruits[l], hMap.get(fruits[l]) - 1);
                if (hMap.get(fruits[l]) == 0)
                    hMap.remove(fruits[l]);
                l++;
            }

            int fruits_count = r - l + 1;
            totalFruits = Math.max(totalFruits, fruits_count);
        }

        return totalFruits;
    }

    public static void p1() {
        // Problem 1 : Leetcode 904. Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets/
        // Geeksforgeeks - https://www.geeksforgeeks.org/problems/fruit-into-baskets-1663137462/1

        int[] fruits = { 1, 2, 3, 2, 2 };
        int fruits_count = totalFruit(fruits);
        System.out.println(fruits_count);
    }

    public static void main(String[] args) {
        // Day 17

        p1();
    }
}