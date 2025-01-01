#include <iostream>

using namespace std;

int findMin(int arr[], int n) {
    //complete the function here

    // edge cases 
    if (arr[0] < arr[n - 1]) return arr[0];
    if (arr[0] > arr[n - 1] && arr[n - 2] > arr[n - 1]) return arr[n - 1];

    int l = 0;
    int h = n - 1;

    int mid = l + (h - l) / 2;

    while (l <= h) {
        if (arr[mid - 1] > arr[mid] && arr[mid] < arr[mid + 1]) {
            // arr[mid] is the minimum element 
            return arr[mid];
        } else if (arr[mid] > arr[l]) {
            l = mid;
        } else {
            h = mid;
        }

        mid = l + (h - l) / 2;
    }

    return -1;
}

void p1() {
    // Proble 1 : Minimum element in a sorted and rotated array - https://www.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array3611/1 

    // int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    // int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    // int arr[] = { 7, 8, 9, 10, 1, 2, 3, 4, 5, 6};
    // int arr[] = { 7, 8, 9, 10, 1, 2, 3, 4, 5};
    int arr[] = { 7, 8, 9, 10, 1};
    int size = sizeof(arr) / sizeof(arr[0]);

    int min = findMin(arr, size);
    cout << min << endl;
}


int main() {
    // Day 29 

    p1();


    return 0;
}