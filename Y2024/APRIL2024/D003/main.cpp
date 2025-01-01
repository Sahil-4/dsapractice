#include <iostream>
#include <string>

using namespace std;

int countHomogenous(string s) {
    if (s.length() == 0 || s.length() == 1) return s.length();

    int modulo = 1000000007;

    string str = string("") + s[0];
    int count = 1;

    for (int i = 1; i < s.length(); i++) {
        if (str[0] == s[i]) {
            str.append(s[0] + string(""));
            count += str.length();
            count = count % modulo;
        } else {
            str = string("") + s[i];
            count++;
            count = count % modulo;
        }
    }

    return count;
}

void p1() {
    // P1 LC 1759. Count Number of Homogenous Substrings - https://leetcode.com/problems/count-number-of-homogenous-substrings/ 

    string s = "abbcccaa";

    int c = countHomogenous(s);

    cout << c << endl;
}

string longestPalindrome(string s) {
    if (s.length() <= 1) return s;

    string longest = "";

    for (int i = 0; i < s.length(); i++) {
        int l = i, h = i;
        while (s[l] == s[h]) {
            l--;
            h++;

            if (l == -1 || h == s.length()) break;
        }

        string palindrome = s.substr(l + 1, h - l - 1);
        if (palindrome.length() > longest.length()) longest = palindrome;

        if (i == s.length() - 1) continue;

        l = i, h = i + 1;
        while (s[l] == s[h]) {
            l--;
            h++;

            if (l == -1 || h == s.length()) break;
        }
        palindrome = s.substr(l + 1, h - l - 1);
        if (palindrome.length() > longest.length()) longest = palindrome;
    }

    return longest;
}

void p2() {
    // P2 LC 5. Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/ 

    string s = "abccbaa";
    string l = longestPalindrome(s);
    cout << l << endl;
}

int main() {
    // Day 3 

    p1();

    p2();


    return 0;
}