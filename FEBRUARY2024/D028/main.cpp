#include <iostream>

using namespace std;

int search(int A[], int l, int h, int key){
    // l: The starting index
    // h: The ending index, you have to search the key in this range
    
    //complete the function here

    int mid = l + (h - l) / 2;
    int f = -1;

    while (l <= h) {
        if (A[mid] == key) return mid;
        else {
            if (A[l] <= A[mid]) {
                // left part is sorted 
                if (A[l] <= key && key < A[mid]) {
                    // key is on left side 
                    h = mid;
                } else {
                    // key is on right side 
                    l = mid + 1;
                }
            } else {
                // right (mid + 1 to h) part is sorted 
                if (A[mid] <= key && key <= A[h]) {
                    // key is on right side 
                    l = mid;
                } else {
                    // key is on left side 
                    h = mid - 1;
                }
            }
        }

        mid = l + (h - l) / 2;
    }

    return f;
}

void p1() {
    // Problem 1 : Search in a Rotated Array - https://www.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1 

    // int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3, 4};
    int size = sizeof(arr) / sizeof(arr[0]);

    for (int i = 0; i < size; i++) {
        int key = arr[i];
        int f = search(arr, 0, size - 1, key);
        cout << f << endl;
    }
}


int main() {
    // Day 28 

    p1();


    return 0;
}