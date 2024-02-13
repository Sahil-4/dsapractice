#include <iostream>
#include <vector>
#include <set>

using namespace std;

int doUnion1(int a[], int n, int b[], int m)  {
    //code here 
    // Time complexity : O(n + m) 
    // Space complexity : O(n + m) 
    // for sorted arrays only 

    int i = 0;
    int j = 0;
    vector<int> store;

    while (i < n && j < m) {
        if (a[i] == b[j]) {
            if (store.empty() || a[i] != store.back()) store.push_back(a[i]);
            i++;
            j++;
        } else if (a[i] < b[j]) {
            // insert a[i]
            if (store.empty() || a[i] != store.back()) store.push_back(a[i]);
            i++;
        } else {
            // insert b[j]
            if (store.empty() || b[j] != store.back()) store.push_back(b[j]);
            j++;
        }
    }

    while (i < n) {
        store.push_back(a[i++]);
    }

    while (j < m) {
        store.push_back(b[j++]);
    }

    for (int i = 0; i < store.size(); i++) {
        cout << store[i] << " ";
    }
    cout << endl;

    return store.size();
}

int doUnion2(int a[], int n, int b[], int m)  {
    //code here 
    // Time complexity : O(n + m) 
    // Space complexity : O(1) 
    // can handle only sorted array 

    int i = 0;
    int j = 0;
    int store = -1;
    int count = 0;

    while (i < n && j < m) {
        if (a[i] == b[j]) {
            if (store == -1 || a[i] != store) store = a[i];
            count++;
            i++;
            j++;
        } else if (a[i] < b[j]) {
            // insert a[i]
            if (store == -1 || a[i] != store) store = a[i];
            count++;
            i++;
        } else {
            // insert b[j]
            if (store == -1 || b[j] != store) store = b[j];
            count++;
            j++;
        }
    }

    while (i < n) {
        count++;
        i++;
    }

    while (j < m) {
        count++;
        j++;
    }

    return count;
}

int doUnion3(int a[], int n, int b[], int m)  {
    //code here 
    // Time complexity : O(n + m) 
    // Space complexity : O(n + m)
    // for sorted and un sorted array both 

    set<int> numberSet;

    for (int i = 0; i < n; i++) {
        numberSet.insert(a[i]);
    }

    for (int i = 0; i < m; i++) {
        numberSet.insert(b[i]);
    }

    return numberSet.size();
}

void p1() {
    // Problem 1 : Union of two arrays - https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1 

    // int a[] = {1, 2, 5, 7, 8};
    // int n = sizeof(a) / sizeof(a[0]);
    // int b[] = {1, 2, 3, 4};
    // int m = sizeof(b) / sizeof(b[0]);

    // int unionSize = doUnion1(a, n, b, m);
    // int unionSize = doUnion2(a, n, b, m);

    int a[] = {1, 2, 5, 7, 8};
    int n = sizeof(a) / sizeof(a[0]);
    int b[] = {4, 5, 3, 7};
    int m = sizeof(b) / sizeof(b[0]);

    int unionSize = doUnion3(a, n, b, m);
    
    cout << unionSize << endl;
}

int main() {
    // Day 13 

    p1();

    // Today's learning 
    // 1. one simple change can also change the entire approach and algorithm to solve the problem 
    // like changing sorted array to un sorted array 
    // 2. do not see constraints directly 
    // else we will think to jump directly on optimal solution 


    return 0;
}