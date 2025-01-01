#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
    set<int> nonuniques;

    for (int i = 0; i < nums1.size(); i++) {
        for (int j = 0; j < nums2.size(); j++) {
            if (nums1[i] == nums2[j]) nonuniques.insert(nums1[i]);
        }
    }

    return {nonuniques.begin(), nonuniques.end()};
}

vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
    set<int> nonuniques;

    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());

    int p1 = 0, p2 = 0;
    while (p1 < nums1.size() && p2 < nums2.size()) {
        if (nums1[p1] == nums2[p2]) {
            nonuniques.insert(nums1[p1]);
            p1++, p2++;
        } else if (nums1[p1] < nums2[p2]) p1++;
        else p2++;
    }

    return {nonuniques.begin(), nonuniques.end()};

    // Complexity analysis 
    // Time : O(n * log(n)) + O(m * log(m)) + O(n + n)
    // Space : O(2(min(n, m))) 
}

void p1() {
    // Problem 1 : Leetcode 349. Intersection of Two Arrays - https://leetcode.com/problems/intersection-of-two-arrays/ 

    vector<int> nums1 = {4,9,5};
    vector<int> nums2 = {9,4,9,8,4};

    vector<int> intersec = intersection(nums1, nums2);
    for (int i = 0; i < intersec.size(); i++) cout << intersec[i] << " ";
    cout << endl;
}

int doUnion(int a[], int n, int b[], int m)  {
    //code here
    set<int> st;

    int p = 0;
    while (p < n || p < m) {
        if (p < n) st.insert(a[p]);
        if (p < m) st.insert(b[p]);
        p++;
    }

    return st.size();

    // Complexity analysis 
    // Time : O(max(n, m))
    // Space : O(n + m) 
}

void p2() {
    // Problem 2 : GeeksForGeeks Union of two array - https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1 

    int a[] = {4,9,5};
    int n = 3;
    int b[] = {9,4,9,8,4};
    int m = 5;

    int unionCount = doUnion(a, n, b, m);
    cout << "unionCount :: " << unionCount << endl;
}

int main() {
    // Day 6 

    p1();

    p2();


    return 0;
}