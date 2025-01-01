#include <iostream>

using namespace std;

void merge(int arr[], int l, int m, int r) {
    int temp[r - l] = { 0 };

    int left = l;
    int right = m + 1;
    int i = 0;

    // create a new sorted array from two sorted arrays left and right parts
    while (left <= m && right <= r) {
        if (arr[left] == arr[right]) {
            // taking benifits of duplicates elements 
            temp[i++] = arr[left++];
            temp[i++] = arr[right++];
        } else if (arr[left] < arr[right]) {
            temp[i++] = arr[left++];
        } else {
            temp[i++] = arr[right++];
        }
    }

    // left out elements 
    while (left <= m) {
        temp[i++] = arr[left++];
    }
    while (right <= r) {
        temp[i++] = arr[right++];
    }

    for (int i = l; i <= r; i++) {
        arr[i] = temp[i - l];
    }
}

void mergeSort(int arr[], int l, int r) {
    // base case 
    if (l >= r) return;

    // middle of the array 
    int m = l + (r - l) / 2;

    // sort left part 
    mergeSort(arr, l, m);

    // sort right part 
    mergeSort(arr, m + 1, r);

    // we have sorted two parts now lets merge then 
    merge(arr, l, m, r);
}

void p1() {
    // Problem 1 : Merge Sort - https://www.geeksforgeeks.org/problems/merge-sort/1 

    // int arr[] = {1, 2, 3, 4};
    // int arr[] = {5, 2, 3, 4};
    // int arr[] = {1, 2, 3, 4, 5, 1, 2, 3, 4};
    // int arr[] = { 5 };
    int arr[] = { 1726, 2371, 2732, 4849, 273, 
                        2135, 5133, 9800, 2737, 9310, 
                        5974, 7590, 9155, 1071, 9678, 
                        10935, 9743, 6081, 1825, 7517 };
    int size = sizeof(arr) / sizeof(arr[0]);

    mergeSort(arr, 0, size - 1);

    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}


int main() {
    // Day 022 

    p1();


    return 0;
}