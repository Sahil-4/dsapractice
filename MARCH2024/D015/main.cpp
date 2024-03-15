#include <iostream>
#include <vector>
#include <map>
#include <limits.h>

using namespace std;

vector<int> majorityElement_solution1(vector<int>& nums) {
    vector<int> ans;
    map<int, int> freq;
    int l_freq = (nums.size() / 3) + 1;

    for (int i = 0; i < nums.size(); i++) {
        freq[nums[i]] += 1;

        if (freq[nums[i]] == l_freq) ans.push_back(nums[i]);

        if (ans.size() == 2) break;
    }

    return ans;

    // T = O(n) 
    // S = O(n) 
}

vector<int> majorityElement(vector<int>& nums) {
    // Extended Moore's voting algo 

    int l_freq = (nums.size() / 3) + 1;

    int cnt1 = 0, cnt2 = 0;
    int e1 = INT_MIN, e2 = INT_MIN;

    for (int i = 0; i < nums.size(); i++) {
        if (cnt1 == 0 && e2 != nums[i]) cnt1 = 1, e1 = nums[i];
        else if (cnt2 == 0 && e1 != nums[i]) cnt2 = 1, e2 = nums[i];
        else if (e1 == nums[i]) cnt1++;
        else if (e2 == nums[i]) cnt2++;
        else cnt1--, cnt2--;
    }

    cnt1 = 0, cnt2 = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (e1 == nums[i]) cnt1++;
        if (e2 == nums[i]) cnt2++;
    }

    if (cnt1 >= l_freq && cnt2 >= l_freq) return {e1, e2};
    if (cnt1 >= l_freq) return {e1};
    if (cnt2 >= l_freq) return {e2};

    return {};
}

void p1() {
    // Problem 1 : Majority element - https://leetcode.com/problems/majority-element-ii/ 

    vector<int> arr = {3,2,3};
    vector<int> mje = majorityElement(arr);

    for (int i = 0; i < mje.size(); i++) cout << mje[i] << " ";
    cout << endl;
}


int main() {
    // Day 15 

    // p1();


    return 0;
}