public class Main {
    public static int getSum(int[] arr, int n) {
        int sum = 0;
        for (int i = 0; i < n; i++)
            sum += arr[i];

        return sum;
    }

    public static int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length;
        int score = getSum(cardPoints, k);
        int temp_score = score;

        for (int l = k - 1, r = 0; r < k; r++) {
            temp_score -= cardPoints[l--];
            temp_score += cardPoints[n - 1 - r];

            score = Math.max(score, temp_score);
        }

        return score;
    }

    public static void p1() {
        // Problem 1 : Leetcode 1423. Maximum Points You Can Obtain from Cards -
        // https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
        // Geeksforgeeks -
        // https://www.geeksforgeeks.org/problems/maximum-point-you-can-obtain-from-cards/0

        int[] cardPoints = { 9, 7, 5, 6, 8, 10 };
        int k = 3;

        int maximumPoints = maxScore(cardPoints, k);
        System.out.println(maximumPoints);
    }

    public static void main(String[] args) {
        // Day 19

        p1();
    }
}