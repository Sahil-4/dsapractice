#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    void makeCombinations(vector<vector<int>>& out, int i, int N, int K, vector<int>& cc) {
        if (i > N) {
            if (cc.size() == K) out.push_back(cc);
            return;
        }

        // take - but only if we can 
        if (cc.size() < K) {
            cc.push_back(i);
            makeCombinations(out, i + 1, N, K, cc);
            cc.pop_back();
        }

        // not take 
        makeCombinations(out, i + 1, N, K, cc);
    }

public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> out;
        vector<int> cc;
        makeCombinations(out, 1, n, k, cc);

        return out;

        // Complexity analysis 
        // Time : O(N^K) 
        // Space : O(K) for current combination + O(N) stack 
    }
};

void p1() {
    // Problem 1 : Leetcode 77. Combinations - https://leetcode.com/problems/combinations/?envType=study-plan-v2&envId=top-interview-150 

    vector<vector<int>> res = Problem1().combine(20, 2);
    for (vector<int> c : res) {
        for (int e : c) cout << e << " ";
        cout << endl;
    }
}

class Problem2 {
    vector<char> mappings[8] = {
        {'a', 'b', 'c'},
        {'d', 'e', 'f'},
        {'g', 'h', 'i'},
        {'j', 'k', 'l'},
        {'m', 'n', 'o'},
        {'p', 'q', 'r', 's'},
        {'t', 'u', 'v'},
        {'w', 'x', 'y', 'z'},
    };

    void makeCombinations(string& digits, int i, string& curr, vector<string>& out) {
        if (i == digits.length()) {
            if (curr != "") out.push_back(curr);
            return;
        }

        for (char c : mappings[digits[i] - '2']) {
            curr.push_back(c);
            makeCombinations(digits, i + 1, curr, out);
            curr.pop_back();
        }
    }

public:
    vector<string> letterCombinations(string digits) {
        vector<string> out;

        string curr = "";
        makeCombinations(digits, 0, curr, out);

        return out;

        // Complexity analysis
        // Time : O(4^digits_str_len)
        // Space : O(digits_str_len) stack space + vector for number to alphabets
    }
};

void p2() {
    // Problem 2 : Leetcode 17. Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/possible-words-from-phone-digits-1587115620/1 

    // vector<string> res = Problem2().letterCombinations("");
    // vector<string> res = Problem2().letterCombinations("23");
    vector<string> res = Problem2().letterCombinations("22");
    for (string &r: res) cout << r << endl;
}


int main() {
    // Day 1 of February 2025 

    p1();

    p2();


    return 0;
}