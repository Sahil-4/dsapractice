#include <iostream>
#include <string>
#include <map>
#include <limits.h>

using namespace std;

int beauty(string s) {
    if (s.length() == 1) return 0;
    map<char, int> mp;

    for (int i = 0; i < s.length(); i++) {
        if (mp.find(s[i]) == mp.end()) mp.insert({s[i], 1});
        else mp[s[i]]++;
    }

    int maxFreq = 0, minFreq = INT_MAX;
    for (auto it : mp) {
        maxFreq = max(it.second, maxFreq);
        minFreq = min(it.second, minFreq);
    }

    return maxFreq - minFreq;
}

int beautySum_solution1(string s) {
    int sum = 0;

    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j < s.length(); j++) {
            sum += beauty(s.substr(i, j - i + 1));
        }
    }

    return sum;
}

int beautySum(string s) {
    if (s.length() == 0 || s.length() == 1) return 0;

    int sum = 0;

    for (int i = 0; i < s.length(); i++) {
        map<char, int> mp;
        for (int j = i + 1; j < s.length(); j++) {
            mp[s[i]]++;

            int maxFreq = 0, minFreq = INT_MAX;

            for (auto it : mp) {
                maxFreq = max(it.second, maxFreq);
                minFreq = min(it.second, minFreq);
            }

            sum += maxFreq - minFreq;
        }
    }

    return sum;
}

void p1() {
    // Problem 1 : Leetcode 1781 Sum of Beauty of All Substrings - https://leetcode.com/problems/sum-of-beauty-of-all-substrings/ 

    string s = "aabcb";

    int sum = beautySum(s);
    cout << sum << endl;
}


int main() {
    // Day 4 

    p1();


    return 0;
}