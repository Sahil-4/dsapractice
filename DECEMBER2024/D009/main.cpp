#include <bits/stdc++.h>

using namespace std;

void fillZArray(vector<int>& zArr, string& str, int& N) {
    // z array - it simply contains the length of prefix matches with substring starting from i 

    /*
    // brute force way to generate z array - O(N^2)
    for (int i = 1; i < N; i++) {
        int j = i, k = 0;
        while (j < N && str[j] == str[k]) j++, k++;
        zArr[i] = k;
    } */

    // Efficient way to generate z array - O(N) 
    int l = 0, r = 0; // known boundary 
    for (int i = 1; i < N; i++) {
        if (i < r) {
            zArr[i] = zArr[i - l];
            // if it goes out of known boundary 
            if (zArr[i] + i > r) zArr[i] = r - i;
        }

        // match more chars - unknown boundary 
        while (zArr[i] + i < N && str[zArr[i]] == str[zArr[i] + i]) zArr[i]++;

        // now update the known boundary - if we have gone there 
        if (zArr[i] + i > r) r = zArr[i] + i, l = i;
    }

    // after moving to unknown boundary we are updating the known boundary 
    // so the time complexity will be around O(N) 
}

int z(string str, int plen) {
    int N = str.length();

    // build z array 
    vector<int> zArr(N, 0);
    fillZArray(zArr, str, N);

    for (int i = plen; i < N; i++) {
        if (zArr[i] >= plen) return i - plen - 1;
    }

    return -1;

    // Complexity analysis 
    // Time : O(N) + O(N) 
    // Space : O(copy string) + O(N) for z array 
}

int strStr(string haystack, string needle) {
    // solve using z algorithm 
    return z(needle + "$" + haystack, needle.length());
}

void p1() {
    // Problem1 : Leetcode 28. Find the Index of the First Occurrence in a String - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/ 
    // Geeksforgeeks - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/ 

    cout << strStr("randomstring", "and") << endl;
    cout << strStr("randomstring", "ing") << endl;
    cout << strStr("randomstring", "mst") << endl;
    cout << strStr("randomstring", "msp") << endl;
}


int main() {
    // Day 9 of December 

    p1();


    return 0;
}