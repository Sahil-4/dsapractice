#include <iostream>
#include <bits/stdc++.h>
#include <cmath>

using namespace std;

void merge_1(long long arr1[], long long arr2[], int n, int m) {
    // code here 
    
    int l = n-1;
    int r = 0;

    // move small elements in arr1 
    // and big elements in arr2 
    while (l >= 0 && r < m) {
        if (arr1[l] > arr2[r]) {
            swap(arr1[l], arr2[r]);
            l--;
            r++;
        } else {
            break;
        }
    }

    // sort both the arrays 
    sort(arr1, arr1+n);
    sort(arr2, arr2+m);

    // Time = O(min(n, m)) + O(n * log(n)) + O(m * log(m))
    // O(max(O(n * log(n)), O(m * log(m))))
}

void merge(long long arr1[], long long arr2[], int n, int m) {
    // code here 
    // gap technique - derived from shell sort 
    int t_len = n + m;
    int gap = (t_len / 2) + (t_len % 2);

    // Tc = O(log(n + m))
    while (gap > 0) {
        int l = 0;
        int r = gap;

        // Tc = O(n + m)
        while (r < t_len) {
            if (l < n && r < n) {
                // l is on arr1 and r is also on arr1 
                if (arr1[l] > arr1[r]) swap(arr1[l], arr1[r]);
            } else if (l >= n && r >= n) {
                // l is on arr2 and r is also on arr2 
                if (arr2[l - n] > arr2[r - n]) swap(arr2[l - n], arr2[r - n]);
            } else {
                // l is on arr1 and r is on arr2 
                if (arr1[l] > arr2[r - n]) swap(arr1[l], arr2[r - n]);
            }

            // it is not possible thatl is on arr2 and r is also on arr1 

            // update pointers 
            l++;
            r++;
        }

        // update gap 
        if (gap == 1) break;
        gap = (gap / 2) + (gap % 2);
    }

    // Tc = O((n+m) * log(n + m)) 
    // Space = 1 
}

void p1() {
    // problem 1 : Merge Without Extra Space - https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1 

    long long arr1[] = {0, 1, 2};
    int n = sizeof(arr1) / sizeof(arr1[0]);
    long long arr2[] = {0, 1, 2, 3};
    int m = sizeof(arr2) / sizeof(arr2[0]);

    // merge_1(arr1, arr2, n, m);
    merge(arr1, arr2, n, m);

    for (int i = 0; i < n; i++) {
        cout << arr1[i] << " ";
    }
    for (int i = 0; i < m; i++) {
        cout << arr2[i] << " ";
    }
    cout << endl;
}

int main() {
    // Day 26 

    p1();


    return 0;
}