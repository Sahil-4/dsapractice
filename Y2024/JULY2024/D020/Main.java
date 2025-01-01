class Main {
    public static boolean hasAllChars(int arr[], int n) {
        for (int i = 0; i < n; i++) {
            if (arr[i] == 0)
                return false;
        }

        return true;
    }

    public static int numberOfSubstrings(String s) {
        int count = 0;
        int n = s.length();
        int freq[] = new int[3];

        for (int l = 0, r = 0; r < n; r++) {
            freq[s.charAt(r) - 'a']++;

            while (hasAllChars(freq, 3)) {
                count += n - r;
                freq[s.charAt(l++) - 'a']--;
            }
        }

        return count;
    }

    public static void p1() {
        // Problem 1 : Leetcode 1358. Number of Substrings Containing All Three Characters -
        // https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
        // Geeksforgeeks - https://www.geeksforgeeks.org/problems/count-substring/1

        String s = "aabcbca";
        int subsCount = numberOfSubstrings(s);
        System.out.println(subsCount);
    }

    public static void main(String[] args) {
        // Day 20

        p1();
    }
}