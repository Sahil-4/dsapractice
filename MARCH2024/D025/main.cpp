#include <iostream>
#include <vector>

using namespace std;

int findKthPositive_solution1(vector<int>& arr, int k) {
    // kind of two pointer approach 

    int low = 1;
    int high = arr[arr.size() - 1] + k;

    int it = 0, mc = 0;

    for (low; low <= high; low++) {
        if (it < arr.size() && low == arr[it]) {
            it++;
        } else {
            mc++;
        }

        if (mc == k) return low;
    }

    return -1;
}

int findKthPositive(vector<int>& arr, int k) {
    // binary search - for direct solution 
    int l = 0, h = arr.size();
    int mid = l + (h - l) / 2;

    while (l < h) {
        int missings = arr[mid] - (mid + 1);

        if (missings < k) {
            l = mid + 1;
        } else {
            h = mid;
        }

        mid = l + (h - l) / 2;
    }

    return h + k;
}

void p1() {
    // Problem 1 : LC 1539. Kth Missing Positive Number - https://leetcode.com/problems/kth-missing-positive-number/  

    // vector<int> arr = {2,3,4,7,11};
    // int k = 5;
    vector<int> arr = {1,2,3,4};
    int k = 2;

    int missing = findKthPositive(arr, k);
    cout << missing << endl;
}

int main() {
    // Day 25 

    p1();


    return 0;
}