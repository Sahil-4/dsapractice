#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

void p1() {
    // Problem 1 : Second Largest Number - https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960 

    // brute force O(2n) 
    // traverse the array two times 
    // find largest and smallest 
    // find second largest and second smallest 

    // optimal 
    // traverse the array only one time 
    // take largest = arr[0], smallest = arr[0]
    // assume second_largest = INT_MIN
    // second_smallest = INT_MAX
    // just to be on safe side 
    // while traversing array 
    // for second largest 
    // 1. check arr[i] > second_largest && arr[i] < largest 
    // if true update second_largest = arr[i]
    // 2. check arr[i] > second_largest && arr[i] > largest 
    // update second_largest = largest, largest = arr[i] 
    // 3. check arr[i] < second_smallest && arr[i] > smallest 
    // if true update second_smallest = arr[i]
    // 4. check arr[i] < second_smallest && arr[i] < smallest 
    // update second_smallest = smallest, smallest = arr[i] 
    // O(n) 

    vector<int> a = {1};
    int l = a[0], s = a[0];

    vector<int> ans = {INT_MIN, INT_MAX};

    for (int i = 1; i < a.size(); i++) {
        // for second largest 
        if (a[i] > ans[0] && a[i] < l) ans[0] = a[i];
        if (a[i] > ans[0] && a[i] > l) {
            ans[0] = l;
            l = a[i];
        }

        // for second smallest 
        if (a[i] < ans[1] && a[i] > s) ans[1] = a[i];
        if (a[i] < ans[1] && a[i] < s) {
            ans[1] = s;
            s = a[i];
        }
    }

    cout << "l : " << ans[0] << " s : " << ans[1] << endl;
}


int main() {
    // Day 019 

    p1();


    return 0;
}