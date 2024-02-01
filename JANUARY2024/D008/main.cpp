#include <iostream>
#include <string>

using namespace std;

void p1() {
    // Problem 1 : Search in a Rotated Array - https://www.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1 

    // we have given a sorted and rotated array 
    // we have to find an element in this element 


    // int arr[] = {5};
    // int l = 0, h = 0, key = 5;
    // int arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
    // int l = 0, h = 8, key = 10;
    // int arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
    // int l = 0, h = 8, key = 3;
    int arr[] = {5, 6, 7, 8,  8, 9, 10, 1, 2, 3};
    int l = 0, h = 9, key = 4;
    int m = l + (h-l)/2;
    int ans = -1;

    while (l <= h) { // binary search 
        // check for mid if it mathces with target key 
        if (arr[m] == key) {
            ans = m;
            break;
        } else {
            // if does not mathes 
            // check which part is sorted 
            // so that we can check in which part target can be present 
            if (arr[l] <= arr[m]) {
                // left part is sorted 
                // check where can be the target present according to left part 
                // we are just checking whether key is present in this sorted part or not 
                if (arr[l] <= key && arr[m] >= key) {
                    h = m-1;
                } else {
                    l = m+1;
                }
            } else {
                // right part is sorted 
                // check where can be the target present according to right part 
                // we are just checking whether key is present in right sorted part or not 
                if (arr[m] <= key && arr[h] >= key) {
                    l = m+1;
                } else {
                    h = m-1;
                }
            }
        }

        m = l + (h-l)/2;
    }

    cout << ans << endl;
}


int main() {
    // Day 008 

    p1();


    return 0;
}