#include <iostream>
#include <vector>
#include <cmath>

using namespace std;


int findFirstOccurrence(vector<int> nums, int target) {
    int l = 0, h = nums.size()-1;
    int mid = l + (h - l)/2;
    int ans = -1;

    while (l <= h) {
        if (nums[mid] == target) {
            ans = mid;
            h = mid-1;
        } else if (nums[mid] < target) {
            l = mid+1;
        } else {
            h = mid-1;
        }

        mid = l + (h - l)/2;
    }

    return ans;
}

int findLastOccurrence(vector<int> nums, int target) {
    int l = 0, h = nums.size()-1;
    int mid = l + (h - l)/2;
    int ans = -1;

    while (l <= h) {
        if (nums[mid] == target) {
            ans = mid;
            l = mid+1;
        } else if (nums[mid] < target) {
            l = mid+1;
        } else {
            h = mid-1;
        }

        mid = l + (h - l)/2;
    }

    return ans;
}

void p1() {
    // Problem 1 : Leetcode 34 - Find First and Last Position of Element in Sorted Array

    // logic : 
    // our array is already sorted 
    // we can use binary search to find the element 
    // but the element we have got can be first occurrence, it can be last occurrence it can also be any other 
    // as the array is sorted we can find first occurrence at left side 
    // and last occurrence at right side 
    // to find first and last occurrence also we can use binary search 

    // vector<int> nums = {5,7,7,8,8,10};
    // vector<int> nums = {};
    vector<int> nums = {8};
    int  target = 8;

    int f = findFirstOccurrence(nums, target);
    int l = findLastOccurrence(nums, target);

    cout << "first : " << f << " last : " << l << endl;

    vector<int> ans; // index of first and last occurrence 
    ans.push_back(f);
    ans.push_back(l);

    // !GETTING TLE 
}

void p2() {
    // Problem 2 : Two Repeated Elements - https://www.geeksforgeeks.org/problems/two-repeated-elements-1587115621/1 

    // logic : using hashmap 
    // traverse array from i = 0 to i < N 
    // assume that arr[i] is index 
    // multiply element at arr[i] index by -1 
    // now next time if we will check arr[i] < 0 
    // and we got true 
    // then it means that i is the repeating element 
    // we mapped elements with index simple 

    // int arr[] = {1,2,1,3,4,3};
    // int N = 4;
    int arr[] = {1,2,2,1};
    int N = 2;
    int size = N+2;
    vector<int> ans;

    for (int i = 0; i < size; i++) {
        if (arr[abs(arr[i])] < 0) {
            ans.push_back(abs(arr[i]));
        } else {
            arr[abs(arr[i])] *= -1;
        }
    }

    cout << ans[0] << ", " << ans[1] << endl;
}


int main() {
    // Day 006 

    // p1();

    p2();


    return 0;
}
