#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


vector<vector<int>> combinationSum(vector<int>& candidates, int target, vector<int> &pickedUpCandidates, int sum, int index) {
    // base cases 
    if (sum == target) return { pickedUpCandidates };
    if (sum > target || index >= candidates.size()) return {};

    // case : pick 
    pickedUpCandidates.push_back(candidates[index]);
    vector<vector<int>> arr1 = combinationSum(candidates, target, pickedUpCandidates, sum + candidates[index], index + 1);

    // case : not pick 
    pickedUpCandidates.pop_back();
    while (index < candidates.size() - 1 && candidates[index] == candidates[index + 1]) index++;
    vector<vector<int>> arr2 = combinationSum(candidates, target, pickedUpCandidates, sum, index + 1);

    // merge arrays 
    vector<vector<int>> ans;
    for (int it = 0; it < arr1.size(); it++) ans.push_back(arr1[it]);
    for (int it = 0; it < arr2.size(); it++) ans.push_back(arr2[it]);

    // return answer 
    return ans;
}

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end());
    vector<int> v;
    return combinationSum(candidates, target, v, 0, 0);
}


void p1() {
    // Problem 1 : Leetcode 40. Combination Sum II - https://leetcode.com/problems/combination-sum-ii/ 

    vector<int> candidates = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, };
    int target = 30;

    vector<vector<int>> out = combinationSum2(candidates, target);
    for (int it1 = 0; it1 < out.size(); it1++) {
        for (int it2 = 0; it2 < out[it1].size(); it2++) cout << out[it1][it2] << " ";
        cout << endl;
    }
}


int main() {
    // Day 23 

    p1();


    return 0;
}
