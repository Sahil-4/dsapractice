#include <iostream>

using namespace std;

string removeKdigits(string num, int k) {
    string ans = "";

    for (int i = 0; i < num.length(); i++) {
        while (ans.length() > 0 && k > 0 && ans.back() > num[i]) {
            k--;
            ans.pop_back();
        }

        if (num[i] != '0' || ans.length() != 0) ans.push_back(num[i]);
    }

    while (!ans.empty() && k > 0) {
        k--;
        ans.pop_back();
    }

    if (ans == "") return "0";
    return ans;
}

void p1() {
    // Problem 1 : Leetcode 402. Remove K Digits - https://leetcode.com/problems/remove-k-digits/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/build-the-smallest2841/1 

    string num = "45556";
    int k = 5;

    string minNum = removeKdigits(num, k);
    cout << "num :: " << num << " k :: " << k << " minNum :: " << minNum << endl;
}

int main() {
    // Day 18 

    p1();


    return 0;
}
