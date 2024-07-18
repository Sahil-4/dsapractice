class Main {
    public static int characterReplacement(String s, int k) {
        int n = s.length();
        if (n == k) return n;

        int maxLen = 0;
        int maxFreq = 0;
        int charFreq[] = new int[26];

        for (int l = 0, r = 0; r < n; r++) {
            int idx = s.charAt(r) - 'A';
            charFreq[idx]++;

            maxFreq = Math.max(maxFreq, charFreq[idx]);

            if (((r - l + 1) - maxFreq) > k) charFreq[s.charAt(l++) - 'A']--;

            maxLen = Math.max(maxLen, r - l + 1);
        }

        return maxLen;
    }

    public static void p1() {
        // Problem 1 : Leetcode 424. Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/ 
        // Geeksforgeeks - https://www.geeksforgeeks.org/problems/longest-repeating-character-replacement/1 

        String s = "AABCAAA";
        int k = 2;
        int maxLen = characterReplacement(s, k);
        System.out.println(maxLen);
    }

    public static void main(String[] args) {
        // Day 18

        p1();
    }
}