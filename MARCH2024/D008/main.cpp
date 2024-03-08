#include <iostream>
#include <vector>

using namespace std;

vector<int> rearrangeArray(vector<int>& nums) {
    vector<int> ans(nums.size(), 0);
    int pos = 0, neg = 1;

    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] > 0) {
            // positive 
            ans[pos] = nums[i];
            pos += 2;
        } else {
            // negative 
            ans[neg] = nums[i];
            neg += 2;
        }
    }

    return ans;
}

void p1() {
    // Problem 1 : Rearrange elements by sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/ 

    vector<int> arr = {3,1,-2,-5,2,-4};

    vector<int> ans = rearrangeArray(arr);

    for (int i = 0; i < ans.size(); i++) cout << ans[i] << " ";
    cout << endl;

}


int main() {
    // Day 8

    p1();


    return 0;
}