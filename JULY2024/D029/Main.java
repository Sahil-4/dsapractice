class Main {
    public static int candy_Solution1(int[] ratings) {
        int N = ratings.length;
        int candiesCount = 0;
        int arr[] = new int[N];

        for (int i = 0; i < N; i++) {
            // left to right
            if (i != 0 && ratings[i] > ratings[i - 1]) {
                arr[i] = Math.max(arr[i], arr[i - 1] + 1);
            } else {
                arr[i] = Math.max(arr[i], 1);
            }

            // right to left
            if (i != 0 && ratings[N - 1 - i] > ratings[N - i]) {
                arr[N - 1 - i] = Math.max(arr[N - 1 - i], arr[N - i] + 1);
            } else {
                arr[N - 1 - i] = Math.max(arr[N - 1 - i], 1);
            }
        }

        for (int i = 0; i < N; i++) {
            candiesCount += arr[i];
        }

        return candiesCount;

        // Complexity analysis
        // Time : O(n * 2)
        // Space : O(n)
    }

    public static int candy(int[] ratings) {
        int N = ratings.length;

        int candiesCount = 1;
        int i = 1;

        while (i < N) {
            // flat
            if (ratings[i] == ratings[i - 1]) {
                candiesCount++;
                i++;
                continue;
            }

            // peak - going upwards
            int peak = 1;
            while (i < N && ratings[i] > ratings[i - 1]) {
                peak++;
                candiesCount += peak;
                i++;
            }

            // peak - going downwards
            int down = 1;
            while (i < N && ratings[i] < ratings[i - 1]) {
                candiesCount += down;
                down++;
                i++;
            }

            // MAX logic - prev peak had less val then down
            if (down > peak) {
                candiesCount += down - peak;
            }
        }

        return candiesCount;
        // Complexity analysis
        // Time : O(n)
        // Space : O(1)
    }

    static void p1() {
        // Problem 1 : Leetcode 135. Candy - https://leetcode.com/problems/candy
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/candy/1

        int[] ratings = { 1, 2, 2 };
        int candies = candy(ratings);
        System.out.println(candies);
    }

    public static void main(String[] args) {
        // Day 29

        p1();
    }
}