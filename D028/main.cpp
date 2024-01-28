#include <iostream>
#include <vector>

using namespace std;

int search(vector<int>& arr, int target) {
    // ok lets use binary search with some modification 
    int l = 0, h = arr.size() - 1;
    int mid = l + (h - l) / 2;

    while (l <= h) {
        if (arr[mid] == target) return mid;

        if (arr[l] <= arr[mid]) {
            // left part is sorted 
            // use left part to find the next sub array to find the target 
            if (arr[l] <= target && target < arr[mid]) {
                h = mid - 1;
            } else {
                l = mid + 1;
            }
        } else {
            // right part is sorted 
            // use right part to find next sub array to find target 
            if (arr[mid] < target && target <= arr[h]) {
                l = mid + 1;
            } else {
                h = mid - 1;
            }
        }

        mid = l + (h - l) / 2;
    }

    return -1;
}


void p1() {
    // Problem 1 : Leetcode 33 Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/description/ 

    // vector<int> arr = {4,5,6,7,0,1,2};
    // vector<int> arr = {5};
    // vector<int> arr = {5, 3};
    // vector<int> arr = {5, 3, 4};
    vector<int> arr = {1, 3, 4};
    int target = 3;

    int ans = search(arr, target);

    cout << ans << endl;
}

int main() {
    // Day 028 

    // p1();


    return 0;
}