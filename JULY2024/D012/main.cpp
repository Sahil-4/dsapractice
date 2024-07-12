#include <iostream>
#include <vector>
#include <stack>
#include <deque>

using namespace std;

int largestRectangleArea_Solution1(vector<int>& heights) {
    int n = heights.size();
    int ar = 0;

    for (int i = 0; i < n; i++) {
        int ar_temp = 0;

        for (int j = i; j < n; j++) {
            if (heights[j] < heights[i]) break;
            ar_temp += heights[i];
        }
        for (int j = i - 1; j >= 0; j--) {
            if (heights[j] < heights[i]) break;
            ar_temp += heights[i];
        }

        ar = max(ar, ar_temp);
    }

    return ar;
}

vector<int> nextSmallRight(vector<int>& arr, int n) {
    vector<int> out(n, n - 1);
    stack<int> stk;

    for (int i = n - 1; i >= 0; i--) {
        while (!stk.empty() && arr[stk.top()] >= arr[i]) stk.pop();

        if (!stk.empty()) out[i] = stk.top() - 1;
        stk.push(i);
    }

    return out;
}

vector<int> nextSmallLeft(vector<int>& arr, int n) {
    vector<int> out(n, 0);
    stack<int> stk;

    for (int i = 0; i < n; i++) {
        while (!stk.empty() && arr[stk.top()] >= arr[i]) stk.pop();

        if (!stk.empty()) out[i] = stk.top() + 1;
        stk.push(i);
    }

    return out;
}

int largestRectangleArea(vector<int>& heights) {
    int n = heights.size();
    int ar = 0;
    vector<int> ns_l = nextSmallLeft(heights, n);
    vector<int> ns_r = nextSmallRight(heights, n);

    for (int i = 0; i < n; i++) {
        int e = heights[i], r = ns_r[i], l = ns_l[i];

        int ar_temp = (r - l + 1) * e;
        ar = max(ar, ar_temp);
    }

    return ar;
}

void p1() {
    // Problem 1 : Leetcode 84. Largest Rectangle in Histogram - https://leetcode.com/problems/largest-rectangle-in-histogram/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1 

    vector<int> h = {2,1,5,6,2,3};
    int area = largestRectangleArea(h);
    cout << "area ::" << area << "\n";
}

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    vector<int> maxes;
    deque<int> visible_window;

    for (int i = 0; i < nums.size(); i++) {
        while (!visible_window.empty() && visible_window.front() <= i - k) visible_window.pop_front();
        while (!visible_window.empty() && nums[visible_window.back()] < nums[i]) visible_window.pop_back();
        visible_window.push_back(i);

        if (i >= k - 1) maxes.push_back(nums[visible_window.front()]);
    }

    return maxes;
}

void p2() {
    // Problem 2 : Leetcode 239. Sliding Window Maximum - https://leetcode.com/problems/sliding-window-maximum/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1 

    vector<int> arr = {1,3,-1,-3,5,3,6,7};
    int k = 3;
    vector<int> maxes = maxSlidingWindow(arr, k);
    for (int i = 0; i < maxes.size(); i++) cout << maxes[i] << " ";
    cout << endl;
}

int main() {
    // Day 12 

    p1();

    p2();


    return 0;
}