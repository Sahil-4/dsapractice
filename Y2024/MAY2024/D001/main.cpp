#include <iostream>
#include <vector>

using namespace std;


void solve(string &num, int &target, int idx, string exp, long long res, long long prev, vector<string> &ans) {
    if (idx == num.size()) {
        if (res == target) ans.push_back(exp);
        return;
    }

    for (int it = idx; it < num.size(); it++) {
        if (it > idx && num[idx] == '0') return;

        // creating current number to perform operations with 
        long long number = stoll(num.substr(idx, it - idx + 1));

        if (idx == 0) {
            // first time appeared 
            solve(num, target, it+1, exp + num.substr(idx, it - idx + 1), number, number, ans);
        } else {
            // add sign 
            solve(num, target, it+1, exp + "+" + num.substr(idx, it - idx + 1), res + number, number, ans);

            // subtract sign 
            solve(num, target, it+1, exp + "-" + num.substr(idx, it - idx + 1), res - number, -number, ans);

            // multiplication sign 
            solve(num, target, it+1, exp + "*" + num.substr(idx, it - idx + 1), res - prev + prev * number, prev * number, ans);
        }
    }
}

vector<string> addOperators(string num, int target) {
    vector<string> ans;
    solve(num, target, 0, "", 0, 0, ans);
    return ans;
}

void p1() {
    // Problem 1 : Leetcode 282. Expression Add Operators - https://leetcode.com/problems/expression-add-operators/ 

    string num = "254652";
    int target = 25;

    vector<string> ans = addOperators(num, target);
    for (int i = 0; i < ans.size(); i++) cout << ans[i] << " ";
}


int main() {
    // Day 1 of May Total 122nd Day 

    p1();


    return 0;
}