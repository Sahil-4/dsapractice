#include <iostream>

using namespace std;


void sort012(int a[], int n) {
    // code here 

    // keeping pointers on position 
    int i = 0, j = n - 1;
    int k = 0;

    // running loop to check element at k and replace it with others at its correct position 
    while (k <= j) {
        if (a[k] == 0) {
            // if value at k is zero 
            // then i is its correct place 
            int temp = a[i];
            a[i++] = a[k];
            a[k++] = temp;
        } else if (a[k] == 2) {
            // if value at k is 2 
            // then h is its correct place 
            int temp = a[j];
            a[j--] = a[k];
            a[k] = temp;
        } else k++;
        // if value at k is 1 
        // and its the correct place for it 
    }
}

void p1() {
    // Problem 1 : Sort an array of 0s, 1s and 2s - https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1 

    // int arr[] = {0, 2, 1, 2, 0};
    int arr[] = {0, 2, 1};
    int n = sizeof(arr) / sizeof(arr[0]);

    sort012(arr, n);

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    // Day 018 

    p1();


    return 0;
}