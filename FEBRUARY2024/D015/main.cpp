#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

void generateSubsets(vector<int> &arr, int i, vector<int> &subs, vector<vector<int>> &ans) {
    if (i == arr.size()) {
        ans.push_back(subs);
        return;
    }

    // dont take i 
    generateSubsets(arr, i+1, subs, ans);

    // take i 
    subs.push_back(arr[i]);
    generateSubsets(arr, i+1, subs, ans);
    subs.pop_back();
}

vector<vector<int>> subsets(vector<int>& arr) {
    //code here
    vector<vector<int>> ans;
    vector<int> subs;

    generateSubsets(arr, 0, subs, ans);
    sort(ans.begin(), ans.end());
    return ans;
}

void p1() {
    // Problem 1 : Subsets - https://www.geeksforgeeks.org/problems/subsets-1613027340/1 

    vector<int> arr = {1, 2, 3};

    vector<vector<int>> ans = subsets(arr);

    for (int i = 0; i < ans.size(); i++) {
        for (int j = 0; j < ans[i].size(); j++) {
            cout << ans[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    // Day 15 

    p1();


    return 0;
}