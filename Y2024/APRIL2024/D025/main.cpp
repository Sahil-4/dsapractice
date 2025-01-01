#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> letterCombinations(string digits, vector<vector<string>> &mappings, string cStr, int i) {
    if (i == digits.length()) return { cStr };

    vector<string> out;

    for (int it2 = 0; it2 < mappings[digits[i] - '0'].size(); it2++) {
        cStr += mappings[digits[i] - '0'][it2];
        vector<string> temp = letterCombinations(digits, mappings, cStr, i + 1);
        cStr.pop_back();

        out.insert(out.end(), temp.begin(), temp.end());
    }

    return out;
}

vector<string> letterCombinations(string digits) {
    if (digits == "") return {};

    vector<vector<string>> mappings = {
        {}, // 0 
        {}, // 1 
        {"a", "b", "c"}, // 2 
        {"d", "e", "f"},
        {"g", "h", "i"}, // 4 
        {"j", "k", "l"},
        {"m", "n", "o"},
        {"p", "q", "r", "s"}, // 7 
        {"t", "u", "v"},
        {"w", "x", "y", "z"} // 9 
    };

    return letterCombinations(digits, mappings, "", 0);
}

void p1() {
    // Problem 1 : Leetcode 17. Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/ 

    // string digits = "9999";
    string digits = "6789";
    vector<string> ans = letterCombinations(digits);
    for (string str : ans) cout << str << " ";
    cout << endl;
}


int main() {
    // Day 25 

    p1();


    return 0;
}