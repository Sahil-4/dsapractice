#include <iostream>
#include <string>

using namespace std;

string largestOddNumber(string num) {
    for (int i = num.length() - 1; i >= 0; i--) {
        int n = num[i] - '0';
        if (n & 1) return num.substr(0, i + 1);
    }

    return "";
}

void p1() {
    // Problem 1 : 1903. Largest Odd Number in String - https://leetcode.com/problems/largest-odd-number-in-string/ 

    // string num = "52";
    // string num = "42061";
    // string num = "4206102";
    // string num = "42061024";
    // string num = "35427";
    // string num = "";
    string num = "0";

    string out = largestOddNumber(num);
    cout << out << endl;
}

string reverseWords(string s) {
    string ans = "";

    for (int i = s.length() - 1; i >= 0; i--) {
        while (i >= 0 && s[i] == ' ') i--;
        int end = i;

        while (i >= 0 && s[i] != ' ') i--;
        int start = i + 1;

        if (start <= end) {
            if (ans != "") ans.append(" ");
            ans.append(s.substr(start, end - start + 1));
        }
    }

    return ans;
}

void p2() {
    // Problem 2 : 151. Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/ 

    string s = "  hello world  ";
    // string s = "a good   example";
    // string s = "the sky is blue";
    string out = reverseWords(s);
    cout << out << endl;
    cout << out.length() << endl;
}

int main() {
    // Day 30 

    p1();

    p2();


    return 0;
}