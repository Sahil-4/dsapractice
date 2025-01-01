#include <iostream>
#include <vector>
#include <stack>

using namespace std;

vector<int> nextGreaterElements(vector<int>& nums) {
    int n = nums.size();
    vector<int> nge(n, -1);
    stack<int> stk;

    for (int i = 2*n - 1; i >= 0; i--) {
        int index = i % n;
        int el = nums[index];

        while (!stk.empty() && stk.top() <= el) stk.pop();

        if (stk.empty()) nge[index] = -1;
        else nge[index] = stk.top();

        stk.push(el);
    }

    return nge;
}

void p1() {
    // Problem 1 : Leetcode 503. Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/next-greater-element-2/1 

    vector<int> arr = {2, 4, 5, 7,3 ,5, 7, 1};
    vector<int> nges = nextGreaterElements(arr);
    for (int i = 0; i < arr.size(); i++) cout << "nge for ::" << arr[i] << " ->" << nges[i] << endl;
}

int main() {
    // Day 7 

    p1();


    return 0;
}