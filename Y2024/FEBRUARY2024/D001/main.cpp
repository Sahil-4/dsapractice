#include <iostream>

using namespace std;

void insert(int *arr, int i) {
    while (i > 0 && arr[i] < arr[i - 1]) {
        int temp = arr[i];
        arr[i] = arr[i - 1];
        arr[i - 1] = temp;

        i--;
    }
}

void insertSort(int *arr, int n) {
    // insertion sort 
    for (int i = 1; i < n; i++) {
        insert(arr, i);
    }
}

void p1() {
    // Problem 1 : insertion sort 

    // int arr[] = {4, 1, 3, 9, 7};
    int arr[] = {4, 1, 0};
    int size = sizeof(arr) / sizeof(arr[0]);

    insertSort(arr, 3);

    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    // Day 01 

    p1();


    return 0;
}