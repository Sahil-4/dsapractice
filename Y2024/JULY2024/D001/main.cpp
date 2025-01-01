#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> getPowers(int n) {
    int modo = 1000000007;
    vector<int> powers;
    int l = 1;

    for (int i = 0; i < n; i++) {
        powers.push_back(l);
        l = (l % modo) * 2 % modo;
    }

    return powers;
}

int numSubseq(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end());
    int modo = 1000000007;
    int n = nums.size();
    int count = 0;
    vector<int> powers = getPowers(n);

    int l = 0, h = n - 1;

    while (l <= h) {
        int sum = nums[l] + nums[h];

        if (sum <= target) {
            int p = h - l;
            long long c = powers[p];
            count = (count % modo) + (c % modo);

            l++;
        } else h--;
    }

    return count;
}

void p1() {
    // Problem 1 : Leetcode 1498. Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/ 

    vector<int> arr = {2, 4, 1, 4};
    int target = 7;

    int subseqCount = numSubseq(arr, target);
    cout << "subseqCount ::" << subseqCount << endl;
}

void solve(vector<vector<int>> &out, vector<int> &arr, int curr_index, vector<int> &comb, int need_more) {
    if (need_more == 0) {
        out.push_back(comb);
        return;
    }

    for (int i = curr_index; i < arr.size(); i++) {
        if (i > curr_index && arr[i] == arr[i - 1]) continue;
        if (arr[i] > need_more) return;

        comb.push_back(arr[i]);
        solve(out, arr, i + 1, comb, need_more - arr[i]);
        comb.pop_back();
    }
}

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    int n = candidates.size();
    sort(candidates.begin(), candidates.end());
    vector<int> comb = {};
    vector<vector<int>> out;
    solve(out, candidates, 0, comb, target);

    return out;
}

void p2() {
    // Problem 2 : Leetcode 40. Combination Sum II - https://leetcode.com/problems/combination-sum-ii/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/combination-sum-ii/1 

    vector<int> arr = {1, 5, 2, 5, 7, 2};
    int target = 12;
    vector<vector<int>> out = combinationSum2(arr, target);
    for (int i = 0; i < out.size(); i++) {
        for (int j = 0; j < out[i].size(); j++) {
            cout << out[i][j] << " ";
        } cout << endl;
    }
}

int main() {
    // Day 1 of July 183rd day of 2024 

    p1();

    p2();


    return 0;
}