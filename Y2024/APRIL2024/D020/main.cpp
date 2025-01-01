#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool validParentheses(string s) {
    int c = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '(') c++;
        else c--;

        if (c < 0) return false;
    }

    return c == 0 ? true : false;
}

vector<string> generateParenthesis(string prev, int n, int i) {
    if (i == n) {
        if (validParentheses(prev)) return { prev };
        else return { };
    };

    vector<string> arr1 = generateParenthesis(prev + "(", n, i + 1);
    vector<string> arr2 = generateParenthesis(prev + ")", n, i + 1);

    vector<string> ans;
    for (int it = 0; it < arr1.size(); it++) ans.push_back(arr1[it]);
    for (int it = 0; it < arr2.size(); it++) ans.push_back(arr2[it]);

    return ans;
}

vector<string> generateParenthesis(int n) {
    return generateParenthesis("(", 2 * n, 1);
    // Tn = O(2 ^ n) 
}

void p1() {
    // Problem 1 : Leetcode 22. Generate Parentheses - https://leetcode.com/problems/generate-parentheses/ 

    int n = 1;

    vector<string> arr = generateParenthesis(n);
    for (int it = 0; it < arr.size(); it++) cout << arr[it] << " ";
    cout << endl;
}

vector<vector<int>> subsets(vector<int>& nums, vector<int> num, int i) {
    if (i == nums.size()) return { num };

    vector<vector<int>> arr1 = subsets(nums, num, i+1);
    num.push_back(nums[i]);
    vector<vector<int>> arr2 = subsets(nums, num, i+1);

    vector<vector<int>> ans;
    for (int it = 0; it < arr1.size(); it++) ans.push_back(arr1[it]);
    for (int it = 0; it < arr2.size(); it++) ans.push_back(arr2[it]);

    return ans;
}

vector<vector<int>> subsets(vector<int>& nums) {
    return subsets(nums, {}, 0);
    // Tn = O(2 ^ n), n = nums.size() 
}

void p2() {
    // Problem 2 : Leetcode 78. Subsets - https://leetcode.com/problems/subsets/ 

    vector<int> nums = {1, 2, 3};
    vector<vector<int>> ans = subsets(nums);
    for (int it1 = 0; it1 < ans.size(); it1++) {
        for (int it2 = 0; it2 < ans[it1].size(); it2++) cout << ans[it1][it2] << " ";
        cout << endl;
    }
}


int main() {
    // Day 20 

    p1();

    p2();


    return 0;
}