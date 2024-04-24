#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> combinationSum3(int k, int n, vector<int> cArr, int sum, int i) {
    if (cArr.size() == k && sum == n) return { cArr };
    if (cArr.size() >= k || sum >= n || i > 9) return { };

    cArr.push_back(i);
    sum += i;
    vector<vector<int>> arr1 = combinationSum3(k, n, cArr, sum, i + 1);
    cArr.pop_back();
    sum -= i;
    vector<vector<int>> arr2 = combinationSum3(k, n, cArr, sum, i + 1);

    vector<vector<int>> out(arr1.begin(), arr1.end());
    out.insert(out.end(), arr2.begin(), arr2.end());

    return out;
}

vector<vector<int>> combinationSum3(int k, int n) {
    return combinationSum3(k, n, { }, 0, 1);

    // Tn = O(2^9) 
}

void p1() {
    // Problem 1 : Leetcode 216. Combination Sum III - https://leetcode.com/problems/combination-sum-iii/ 

    int k = 2, n = 60;

    vector<vector<int>> ans = combinationSum3(k, n);

    for (int i = 0; i < ans.size(); i++) {
        for (int j = 0; j < ans[i].size(); j++) cout << ans[i][j] << " ";
        cout << endl;
    }
}

vector<vector<int>> subsetsWithDup(vector<int>& nums, vector<int> subArr, int i) {
    if (i >= nums.size()) return { subArr };

    subArr.push_back(nums[i]);
    i++;
    vector<vector<int>> arr1 = subsetsWithDup(nums, subArr, i);

    subArr.pop_back();
    while (i < nums.size() && nums[i] == nums[i - 1]) i++;
    vector<vector<int>> arr2 = subsetsWithDup(nums, subArr, i);

    vector<vector<int>> out(arr1.begin(), arr1.end());
    out.insert(out.end(), arr2.begin(), arr2.end());

    return out;
}

vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    return subsetsWithDup(nums, {}, 0);
}

void p2() {
    // Problem 2 : Leetcode 90. Subsets II - https://leetcode.com/problems/subsets-ii/ 

    vector<int> nums = {2, 3, 5};

    vector<vector<int>> ans = subsetsWithDup(nums);

    for (int i = 0; i < ans.size(); i++) {
        for (int j = 0; j < ans[i].size(); j++) cout << ans[i][j] << " ";
        cout << endl;
    }
}


int main() {
    // Day 24 

    p1();

    p2();


    return 0;
}