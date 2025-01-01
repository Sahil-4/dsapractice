#include <iostream>
#include <vector>

using namespace std;


void p1() {
    // problem 1 : Leetcode 268. Missing Number - https://leetcode.com/problems/missing-number/description/

    // using basic maths and sum of n 
    // init ans = sum of n 
    // run a loop from i = 0 to size of array - 1 
    // subtract arr[i] from ans 
    // at the end return ans 

    vector<int> nums = {3,0,1};

    int ans = (nums.size() * (nums.size()+1))/2;

    for (int i = 0; i < nums.size(); i++) {
        ans -= nums[i];
    }

    cout << ans << endl;
}


int main() {
    // Day 004 

    p1();

    return 0;
}