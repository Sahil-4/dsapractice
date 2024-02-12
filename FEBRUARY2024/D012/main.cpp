#include <iostream>

using namespace std;

void rotateArr(int arr[], int d, int n){
    // code here 
    // dont perform unnecessary operations 
    d = d % n;

    // same array 
    if (d == 0 || n == 1) return;

    // now rotation - optimal solution 
    // reverse from 0 to <d 
    for (int i = 0; i < d/2; i++) {
        int temp = arr[i];
        arr[i] = arr[d - 1 - i];
        arr[d - 1 - i] = temp;
    }

    // reverse from d to <n 
    for (int i = d; i < (n + d)/2; i++) {
        int temp = arr[i];
        arr[i] = arr[n + d - 1 - i];
        arr[n + d - 1 - i] = temp;
    }

    // reverse entire array 
    for (int i = 0; i < n/2; i++) {
        int temp = arr[i];
        arr[i] = arr[n - 1 - i];
        arr[n - 1 - i] = temp;
    }
}

void p1() {
    // Problem 1 : Rotate Array - https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1 

    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
    int n = sizeof(arr)/sizeof(arr[0]);
    int d = 7;

    rotateArr(arr, d, n);

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}


int main() {
    // Day 12 

    p1();

    // 1. try to run code on small and big test cases also 
    // 2. handle < and > conditions carefully 


    return 0;
}