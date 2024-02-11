#include <iostream>

using namespace std;

int remove_duplicate(int arr[],int n){
    // code here 
    int c = 0;

    for (int j = 1; j < n; j++) {
        if (arr[c] != arr[j]) {
            arr[++c] = arr[j];
        }
    }

    return c + 1;
}

void p1() {
    // Problem 1 : Remove duplicate elements from sorted Array - https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1 

    int arr[] = {1, 2, 2, 3, 5};
    int n = 5;

    int m = remove_duplicate(arr, n);

    for (int i = 0; i < m; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    // Day 11 

    p1();


    return 0;
}
