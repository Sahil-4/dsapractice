#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

void p1() {
    // Problem 1 : 349. Intersection of Two Arrays - https://leetcode.com/problems/intersection-of-two-arrays/ 

    vector<int> arr1 = {1,2,2,1};
    vector<int> arr2 = {2, 2};

    unordered_set<int> set1;
    vector<int> ans;

    for (int e : arr1) {
        set1.insert(e);
    }

    for (int e : arr2) {
        if (set1.find(e) != set1.end()) {
            set1.erase(e);
            ans.push_back(e);
        }
    }

    for (int e : ans) {
        cout << e << " ";
    }
    cout << endl;
}

void p2() {
    // Problem 2 : Bitonic Point - https://www.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1 

    int arr[] = {1,15,25,45,42,21,17,12,11};
    int n = 9;

    int low = 0, high = n-1;
    int mid = low + (high - low) / 2;
    
    while (low < high) {
        if (arr[mid-1] < arr[mid] && arr[mid] > arr[mid+1]) {
            cout << arr[mid] << endl;
            break;
        }
        
        if (arr[mid-1] < arr[mid] && arr[mid] < arr[mid+1]) {
            low = mid+1;
        } else {
            high = mid;
        }
        
        mid = low + (high-low)/2;
    }
    
    cout << arr[mid] << endl;
}


int main() {
    // Day 005 

    p1();

    p2();


    return 0;
}