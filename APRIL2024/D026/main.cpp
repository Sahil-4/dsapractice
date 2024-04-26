#include <iostream>
#include <string>
#include <vector>

using namespace std;


bool isPalindrome(string str, int left, int right) {
    if (left >= right) return true;
    return str[left] == str[right] && isPalindrome(str, left + 1, right - 1);
}

void solve(string s, int index, vector<string> &curr, vector<vector<string>> &answer) {
    if (index == s.length()) {
        answer.push_back(curr);
        return;
    }

    for (int it = index; it < s.length(); it++) {
        if (isPalindrome(s, index, it)) {
            curr.push_back(s.substr(index, it - index + 1));
            solve(s, it + 1, curr, answer);
            curr.pop_back();
        }
    }
}

vector<vector<string>> partition(string s) {
    vector<vector<string>> answer;
    vector<string> curr;
    solve(s, 0, curr, answer);

    return answer;
}

void p1() {
    // Problem 1 : Leetcode 131. Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/ 

    string s = "aab";
    vector<vector<string>> pals = partition(s);
    for (int it = 0; it < pals.size(); it++) {
        for (int j = 0; j < pals[it].size(); j++) cout << pals[it][j] << " ";
        cout << endl;
    }
}


int main() {
    // Day 26 

    p1();


    return 0;
}