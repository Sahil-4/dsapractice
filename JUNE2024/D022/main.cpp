#include <iostream>
#include <map>
#include <limits.h>

using namespace std;

int getIntegerForRoman(char ch) {
    map<char, int> table = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000},
    };

    return table[ch];
}

int romanToInt(string s) {
    int strLen = s.length();
    int ans = 0;

    for (int i = 0; i < strLen; i++) {
        int n1 = getIntegerForRoman(s[i]);
        int n2 = (i + 1 < strLen) ? getIntegerForRoman(s[i + 1]) : INT_MIN; 

        if (n1 < n2) ans -= n1;
        else ans += n1;
    }

    return ans;
}

void p1() {
    // Problem 1 : Leetcode 13. Roman to Integer - https://leetcode.com/problems/roman-to-integer 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/roman-number-to-integer3201/1 

    string s = "IV";
    int num = romanToInt(s);
    cout << num << endl;
}

int myAtoi(string s) {
    // steps 
    // 1. ignore only leading whitespaces 
    // 2. check result signedness - sign must be in beginning before any digit 
    // 3. convert digits and stop if encounter any non digit char 
    // 4. Rounding : keep the number / result within [-231, 231 - 1]

    int result = 0;
    int sign = 1;

    int start = 0;

    // skip leading whitespaces 
    for (start = 0; start < s.length(); start++) {
        if (s[start] != ' ') break;
    }

    // update sign 
    if (s[start] == '-') sign = -1, start++;
    else if (s[start] == '+') sign = 1, start++;

    // convert char digits to integers 
    for (start; start < s.length(); start++) {
        // stop if non digit char found 
        if (s[start] < '0' || s[start] > '9') break;

        // get int digit from char digit 
        int d = s[start] - '0';

        // round off 
        if (result > ((INT_MAX - d) / 10)) {
            cout << "abt to ret :: " << result << " d ::" << d << endl;
            if (sign == 1) return INT_MAX;
            else return INT_MIN;
        }

        // atoi
        result = (result * 10) + d;
    }

    return result * sign;
}

int atoi(string s) {
    //Your code here - gfg 
    int result = 0;
    int sign = 1;

    int start = 0;
    if (s[start] == '-') sign = -1, start++;

    for (start; start < s.length(); start++) {
        if (s[start] < '0' || s[start] > '9') return -1;

        result *= 10;
        result += s[start] - '0';
    }

    return result * sign;
}

void p2() {
    // Problem 2 : Leetcode 8. String to Integer (atoi) - https://leetcode.com/problems/string-to-integer-atoi/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/implement-atoi/1 

    string s = "445464";
    int num = myAtoi(s);
    cout << num << endl;
}


int main() {
    // Day 22 

    p1();  

    p2();


    return 0;
}