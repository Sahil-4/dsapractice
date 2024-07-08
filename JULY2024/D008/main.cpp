#include <iostream>
#include <vector>

using namespace std;

vector<int> getMaximumLeft(vector<int> &arr, int n) {
    vector<int> maxes(n, 0);
    int maxi = 0;

    for (int i = 0; i < n; i++) {
        maxes[i] = maxi;
        if (maxi < arr[i]) maxes[i] = 0;
        maxi = max(maxi, arr[i]);
    }

    return maxes;
}

vector<int> getMaximumRight(vector<int> &arr, int n) {
    vector<int> maxes(n, 0);
    int maxi = 0;

    for (int i = n - 1; i >= 0; i--) {
        maxes[i] = maxi;
        if (maxi < arr[i]) maxes[i] = 0;
        maxi = max(maxi, arr[i]);
    }

    return maxes;
}

int trap(vector<int>& height) {
    int trappedWater = 0;
    int n = height.size();

    vector<int> left_max = getMaximumLeft(height, n);
    vector<int> right_max = getMaximumRight(height, n);

    for (int i = 0; i < n; i++) {
        if (left_max[i] == 0 || right_max[i] == 0) continue;

        trappedWater += min(left_max[i], right_max[i]) - height[i];
    }

    return trappedWater;
}

void p1() {
    // Problem 1 : Leetcode 42. Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1 

    vector<int> h = {2,1,5,15,4,6};
    int water = trap(h);
    cout << "trapped water ::" << water << endl;
}


int main() {
    // Day 8 of July - revisiting 

    p1();


    return 0;
}