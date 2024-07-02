#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

void solve(vector<vector<int>> &subsets, vector<int>& ds, int curr_index, vector<int> &curr_subset) {
    subsets.push_back(curr_subset);
    if (curr_index >= ds.size()) return;

    for (int i = curr_index; i < ds.size(); i++) {
        if (i != curr_index && ds[i] == ds[i - 1]) continue;

        curr_subset.push_back(ds[i]);
        solve(subsets, ds, i + 1, curr_subset);
        curr_subset.pop_back();
    }
}

vector<vector<int>> subsetsWithDup(vector<int> nums) {
    sort(nums.begin(), nums.end());

    vector<vector<int>> subsets = {};
    vector<int> curr_subset = {};
    solve(subsets, nums, 0, curr_subset);

    return subsets;

    // Complexity analysis 
    // Time : O(n ^ 2) 
    // Space : O(n), extra + call stack memory for recursion 
}

void p1() {
    // Problem 1 : Leetcode 90. Subsets II - https://leetcode.com/problems/subsets-ii/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/subsets-1587115621/1 

    vector<int> arr = {2,5,1,2,7,5};
    vector<vector<int>> subsets = subsetsWithDup(arr);
    for (int i = 0; i < subsets.size(); i++) {
       for (int j = 0; j < subsets.size(); j++) cout << subsets[i][j] << " ";
       cout << endl;
    }
}

// char to string mapping of phone dialer 
map<char, vector<string>> char_table = {
    {'2', {"a", "b", "c"}},
    {'3', {"d", "e", "f"}},
    {'4', {"g", "h", "i"}},
    {'5', {"j", "k", "l"}},
    {'6', {"m", "n", "o"}},
    {'7', {"p", "q", "r", "s"}},
    {'8', {"t", "u", "v"}},
    {'9', {"w", "x", "y", "z"}},
};

void solve(string &digits, int curr_index, vector<string> &combinations, string combination) {
    if (curr_index >= digits.length()) {
        combinations.push_back(combination);
        return;
    }

    for (int i = 0; i < char_table[digits[curr_index]].size(); i++) {
        solve(digits, curr_index + 1, combinations, combination + char_table[digits[curr_index]][i]);
    }
}

vector<string> letterCombinations(string digits) {
    if (digits.length() == 0) return {};

    vector<string> combinations;
    solve(digits, 0, combinations, "");

    return combinations;
}

void p2() {
    // Problem 2 : Leetcode 17. Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/possible-words-from-phone-digits-1587115620/1 

    string digits = "345";
    vector<string> combinations = letterCombinations(digits);
    for (int i = 0; i < combinations.size(); i++) cout << combinations[i] << endl;
}

int main() {
    // Day 2 of July 

    p1();

    p2();


    return 0;
}