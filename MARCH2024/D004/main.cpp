#include <iostream>
#include <vector>

using namespace std;

int findMaxConsecutiveOnes(vector<int>& nums) {
    int count = 0;
    int temp_count = 0;

    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != 1) {
            count = (count > temp_count) ? count : temp_count;
            temp_count = 0;
        } else temp_count++;
    }

    count = (count > temp_count) ? count : temp_count;

    return count;
}

void p1() {
    // Problem 1 : LC 485. Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/description/ 

    vector<int> arr = {1, 1, 0, 1, 1, 1};
    int c = findMaxConsecutiveOnes(arr);
    cout << c << endl;
}

int placePivot(vector<int> &arr, int l, int h) {
    if (l >= h) return 0;

    int pivot_element = arr[l];

    int p1 = l;
    int p2 = h;

    while (p1 < p2) {
        while (arr[p1] <= pivot_element && p1 < h) p1++;
        while (arr[p2] > pivot_element && p2 > l) p2--;

        if (p1 < p2) swap(arr[p1], arr[p2]);
    }

    swap(arr[l], arr[p2]);

    return p2;
}

void quickSort(vector<int> &arr, int l, int h) {
    // take a pivot 
    // put it at its correct position 
    // devide the array into two parts from this position 
    // call quickSort recursively for both parts 
    // do this until we got one element in an array 
    if (l >= h) return;

    int pivot_index = placePivot(arr, l, h);
    quickSort(arr, l, pivot_index-1);
    quickSort(arr, pivot_index+1, h);
}

vector<int> sortArray(vector<int>& nums) {
    quickSort(nums, 0, nums.size() - 1);
    return nums;
}

void p2() {
    // Problem 2 Quick Sort - https://www.geeksforgeeks.org/problems/quick-sort/1 

    // vector<int> arr = {5, 7, 13, 1, 2, 5, 7, 12, 18};
    // vector<int> arr = {5, 7, 13};
    // vector<int> arr = {12, 5, 7, 13};
    vector<int> arr = {12, 5, 2, 7, 13};
    sortArray(arr);

    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    // Day 04 

    // p1();

    p2();


    return 0;
}