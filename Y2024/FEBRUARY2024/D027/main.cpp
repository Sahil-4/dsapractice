#include <iostream>
#include <vector>

using namespace std;

int lmi(vector<long long> v, long long x) {
    int ans = -1;

    int low = 0;
    int high = v.size() - 1;
    int mid = low + (high - low) / 2;

    while (low <= high) {
        if (v[mid] == x) {
            // possible answer save it 
            ans = mid;

            // to find left side indices we will have to move left 
            high = mid - 1;
        } else if (v[mid] > x) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }

        mid = low + (high - low) / 2;
    }

    return ans;
}

int rmi(vector<long long> v, long long x) {
    int ans = -1;

    int low = 0;
    int high = v.size() - 1;
    int mid = low + (high - low) / 2;

    while (low <= high) {
        if (v[mid] == x) {
            // possible answer save it 
            ans = mid;

            // to find right side indices we will have to move right 
            low = mid + 1;
        } else if (v[mid] > x) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }

        mid = low + (high - low) / 2;
    }

    return ans;
}

pair<long,long> indexes(vector<long long> v, long long x) {
    // code here
    return {lmi(v, x), rmi(v, x)};
}

void p1() {
    // Problem 1 : Left most and right most index - https://www.geeksforgeeks.org/problems/find-first-and-last-occurrence-of-x0849/1 

    // vector<long long> arr = {1, 1, 3, 3, 3, 5, 7, 12, 12, 15, 16};
    vector<long long> arr = {1, 1, 3, 3, 3, 5, 7, 12, 12, 15};
    long long key = 3;

    pair<long,long> ans = indexes(arr, key);
    cout << "first : " << ans.first << " second : " << ans.second << endl;
}

int main() {
    // Day 27 

    p1();

    // test case types 
    // array having odd / even elements 
    // array having only one elements or two or three or near to given range hint 


    return 0;
}