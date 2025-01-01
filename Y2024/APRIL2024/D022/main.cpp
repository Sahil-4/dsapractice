#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int sum(vector<int> &pickedUpCandidates) {
    int s = 0;
    for (int it = 0; it < pickedUpCandidates.size(); it++) s += pickedUpCandidates[it];
    return s;
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target, vector<int> pickedUpCandidates, int index) {
    int candidateSum = sum(pickedUpCandidates);
    if (candidateSum == target) return { pickedUpCandidates };
    if (candidateSum > target || index >= candidates.size()) return {};

    vector<vector<int>> arr1 = combinationSum(candidates, target, pickedUpCandidates, index + 1);
    pickedUpCandidates.push_back(candidates[index]);
    vector<vector<int>> arr2 = combinationSum(candidates, target, pickedUpCandidates, index);

    vector<vector<int>> ans;
    for (int it = 0; it < arr1.size(); it++) ans.push_back(arr1[it]);
    for (int it = 0; it < arr2.size(); it++) ans.push_back(arr2[it]);

    return ans;
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end());
    return combinationSum(candidates, target, { }, 0);
}

void p1() {
    // Problem 1 : Leetcode 39. Combination Sum - https://leetcode.com/problems/combination-sum/ 

    vector<int> candidates = {2, 3, 5, 7, 9, 10};
    int target = 5;

    vector<vector<int>> cSum = combinationSum(candidates, target);
}

int main() {
    // Day 22 

    p1();


    return 0;
}