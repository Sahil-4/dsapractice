#include <iostream>
#include <vector>
#include <string>

using namespace std;


int CountPS(char s[], int N) {
    // code here
    int count = 0;
    bool dp[N][N];

    for (int g = 0; g < N; g++) {
        int i = 0, j = g;

        while (j < N) {
            if (g == 0) {
                dp[i][j] = true;
            } else if (g == 1) {
                dp[i][j] = s[i] == s[j];
            } else {
                if (s[i] == s[j] && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                } else {
                    dp[i][j] = false;
                }
            }
            
            if (dp[i][j] && g >= 1) count++;

            i++;
            j++;
        }
    }

    return count;
}

void p1() {
    // Problem 1 : Count Palindrome Sub-Strings of a String - https://www.geeksforgeeks.org/problems/count-palindrome-sub-strings-of-a-string0652/1 

    // char str[] = "abcba";
    char str[] = "aaaaa";
    int n = sizeof(str)/sizeof(str[0]);

    int totalPalindromes = CountPS(str, n);
    cout << totalPalindromes << endl;
}

int main() {
    // Day 10 

    p1();


    return 0;
}