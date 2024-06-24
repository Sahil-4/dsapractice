#include <iostream>

using namespace std;

int countHomogenous(string s) {
    int mod = 1000000007;
    int n = s.length();
    int out = 0;

    char ch = s[0];
    int count = 1;

    for (int j = 1; j < n; j++) {
        if (s[j] != ch) {
            out = ((out % mod) + (count % mod) % mod);

            ch = s[j];
            count = 1;
        } else {
            out = ((out % mod) + (count % mod) % mod);
            count = ((count % mod) + (1 % mod) % mod);
        }
    }
    out = ((out % mod) + (count % mod) % mod);

    return out % mod;
}

void p1() {
    // Problem 1 : Leetcode 1759. Count Number of Homogenous Substrings - https://leetcode.com/problems/count-number-of-homogenous-substrings/ 

    string s = "aaaaaaaz";
    int homo = countHomogenous(s);
    cout << "homo :" << homo << endl;
}

int countSubstringWithEqualEnds(string s) {
    // Your code goes here
    int out = 0;
    int arr[26] = { 0 };

    for (int i = 0; i < s.length(); i++) arr[s[i] - 'a']++;

    for (int i = 0; i < 26; i++) {
        int n = arr[i];
        out += (n * (n + 1)) / 2;
    }

    return out;
}

void p2() {
    // Problem 2 : GeeksForGeeks Substrings with same first and last characters - https://www.geeksforgeeks.org/problems/substrings-with-similar-first-and-last-characters3644/1 

    string s = "aabcabacba";
    int sub = countSubstringWithEqualEnds(s);
    cout << "subs ::" << sub << endl;
}

bool checkPalindrome(string &s, int i, int e) {
    if (i >= e) return true;
    return s[i] == s[e] && checkPalindrome(s, i+1, e-1);
}

string longestPalindrome_Solution1(string s) {
    int n = s.length();
    int start_index = 0, len = 1;

    for (int start = 0; start < n; start++) {
        for (int end = n - 1; end >= 0; end--) {
            if (checkPalindrome(s, start, end)) {
                if (len < end - start + 1) {
                    len = end - start + 1;
                    start_index = start;
                }

                break;
            }
        }
    }

    return s.substr(start_index, len);

    // Complexity analysis 
    // Time : O(n ^ 3) 
    // Space : O(1) 
}

string longestPalindrome(string s) {
    int n = s.length();
    int start_index = 0, len = 1;

    for (int i = 0; i < n; i++) {
        // odd len string 
        int low = i, high = i;
        while (s[low] == s[high]) {
            low--, high++;
            if (low == -1 || high == n) break;
        }

        if (len < high - low - 1) {
            len = high - low - 1;
            start_index = low + 1;
        }

        if (i == s.length() - 1) break;

        // even len string 
        low = i, high = i + 1;
        while (s[low] == s[high]) {
            low--, high++;
            if (low == -1 || high == n) break;
        }

        if (len < high - low - 1) {
            len = high - low - 1;
            start_index = low + 1;
        }
    }

    return s.substr(start_index, len);

    // Complexity analysis 
    // Time : O(n ^ 2) 
    // Space : O(1) 
}

void p3() {
    // Problem 3 : Leetcode 5. Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/longest-palindrome-in-a-string1956/1 

    string s = "abada";
    string longestPal = longestPalindrome(s);
    cout << "longestPal ::" << longestPal << endl;
}

int main() {
    // Day 24 

    p1();

    p2();

    p3();


    return 0;
}