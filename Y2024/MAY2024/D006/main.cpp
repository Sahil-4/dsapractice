#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int singleNumber(vector<int>& nums) {
    int el = nums[0];
    for (int i = 1; i < nums.size(); i++) el = el ^ nums[i];
    return el;
}

void p1() {
    // Problem 1 : Leetcode 136. Single Number - https://leetcode.com/problems/single-number/ 

    vector<int> nums = {1, 2, 3, 2, 1};

    int duplicate = singleNumber(nums);
    cout << duplicate << endl;
}

vector<int> subset(vector<int>& nums, int dec) {
    vector<int> sub;
    if (dec == 0) return sub;

    int i = 0;
    while ((dec >> i) != 0) {
        if ((dec >> i) & 1) sub.push_back(nums[i]);
        i++;
    }

    return sub;
}

vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> ans;
    int n = nums.size();

    for (int i = 0; i <= pow(2, n) - 1; i++) ans.push_back(subset(nums, i));

    return ans;
}

void p2() {
    // Problem 2 : Leetcode 78. Subsets - https://leetcode.com/problems/subsets/description/ 

    vector<int> nums = {};

    vector<vector<int>> ans = subsets(nums);
    for (int i = 0; i < ans.size(); i++) {
        for (int j = 0; j < ans[i].size(); j++) cout << ans[i][j] << " ";
        cout << endl;
    }
}

int main() {
    // Day 6 

    p1();

    p2();


    return 0;
}