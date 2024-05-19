#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int largestRectangleArea_Solution1(vector<int>& heights) {
    int sum = 0;
    int n = heights.size();

    for (int i = 0; i < n; i++) {
        int tempSum = heights[i];
        int l = i - 1, r = i + 1;

        while (l >= 0 || r < n) {
            if (l >= 0 && heights[l] > heights[i]) {
                tempSum += heights[i];
                l--;
            }
            if (r < n && heights[r] > heights[i]) {
                tempSum += heights[i];
                r++;
            }

            if ((l < 0 || heights[l] < heights[i]) && (r >= n || heights[r] < heights[i])) break;
        }

        if (tempSum > sum) sum = tempSum;
    }

    return sum;

    // TLE 
}

vector<int> smallToLeft(vector<int>& heights, int n) {
    vector<int> left(n, 0);
    stack<int> stk;

    for (int i = 0; i < n; i++) {
        while (!stk.empty() && heights[stk.top()] >= heights[i]) stk.pop();

        if (stk.empty()) left[i] = 0;
        else left[i] = stk.top() + 1;

        stk.push(i);
    }

    return left;
}

vector<int> smallToRight(vector<int>& heights, int n) {
    vector<int> right(n, n - 1);
    stack<int> stk;

    for (int i = n - 1; i >= 0; i--) {
        while (!stk.empty() && heights[stk.top()] >= heights[i]) stk.pop();

        if (stk.empty()) right[i] = n - 1;
        else right[i] = stk.top() - 1;

        stk.push(i);
    }

    return right;
}

int largestRectangleArea(vector<int>& heights) {
    int n = heights.size();
    int sum = 0;

    vector<int> left = smallToLeft(heights, n); // O(n) 
    vector<int> right = smallToRight(heights, n); // O(n) 

    for (int i = 0; i < n; i++) { // O(n) 
        int temp = right[i] - left[i] + 1; // width 
        temp *= heights[i]; // multiply by height 
        if (temp > sum) sum = temp;
    }

    return sum;
}

void p1() {
    // Problem 1 : Leetcode 84. Largest Rectangle in Histogram - https://leetcode.com/problems/largest-rectangle-in-histogram/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1 

    vector<int> heights = {10000, 10000, 10000};
    int sum = largestRectangleArea(heights);
    cout << "SUM :: " << sum << endl;
}


int main() {
    // Day 19

    p1();


    return 0;
}