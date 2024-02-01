#include <iostream>
#include <string>

using namespace std;

bool checkPalindrome(string str, int l, int h) {
    // Recursion 

    if (l >= h) return true;

    if (str[l] == str[h]) return checkPalindrome(str, ++l, --h);

    return false;
}

void p1() {
    // Problem 1 : Check Palindrome - https://www.codingninjas.com/studio/problems/check-palindrome_4219630 

    // string str = "level";
    // string str = "anananana";
    // string str = "racecar";
    string str = "snbvdsssjdwkkjumxxtnntxxmujkkwdjsssdvbns";

    // cout << checkPalindrome(str, 0, str.size()-1) << endl;

    int l = 0, h = str.size()-1;
    while (l <= h) {
        if (str[l] != str[h]) {
            cout << 0 << endl;
            return;
        }

        l++;
        h--;
    }

    cout << 1 << endl;
}


int main() {
    // Day 20 

    p1();


    return 0;
}