#include <iostream>

using namespace std;

int search(int *arr, int size, int key) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == key) return i;
    }

    return -1;
}

void p1() {
    // Problem 1 : Search an element in array - https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1 

    int arr[] = {2, 4, 6, 0, 3, 5, 7, 9, 12};
    int size = sizeof(arr) / sizeof(arr[0]);
    int key = 5;

    int index = search(arr, size, key);
    cout << "element found at " << index << endl;
}

pair<long long, long long> getMinMax(long long a[], int n) {
    pair<long long, long long> ans = {a[0], a[0]}; // min, max 

    for (int i = 0; i < n; i++) {
        if (a[i] < ans.first) ans.first = a[i];
        if (a[i] > ans.second) ans.second = a[i];
    }

    return ans;
}

void p2() {
    // Problem 2 : Find minimum and maximum element in an array - https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1 

    long long arr[] = {3, 2, 1, 56, 1000, 167};
    int size = sizeof(arr) / sizeof(arr[0]);
    pair<long long, long long> indexes = getMinMax(arr, size);

    cout << "Min element : " << indexes.first << " max element : " << indexes.second << endl;
}

int main() {
    // Day 02 

    // p1();

    p2();


    return 0;
}