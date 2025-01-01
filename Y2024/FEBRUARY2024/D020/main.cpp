#include <iostream>
#include <limits.h>

using namespace std;

long long maxSubarraySum(int arr[], int n) {
    // Your code here 
    // simply traverse the array in one go 
    // and just discard the part of array that gives us negative sum 
    // if we get negative sum 
    // just make the sum = 0 
    // and keep iterating next elements 

    long long sum = 0;
    long long max_sum = LONG_MIN;

    for (int i = 0; i < n; i++) {
        sum += arr[i];

        if (max_sum < sum) max_sum = sum;

        if (sum < 0) sum = 0;
    }

    return max_sum;
}

void p1() {
    // Problem 1 : Kaden's Algorithm - https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1 
    // int arr[] = {1,2,3,-2,5};
    int arr[] = {1,2,3};
    int size = sizeof(arr) / sizeof(arr[0]);

    long long sum = maxSubarraySum(arr, size);
    cout << sum << endl;
}


int main() {
    // Day 020 

    p1();


    return 0;
}
