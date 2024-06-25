#include <iostream>
#include <vector>

using namespace std;

vector<int> getMinMaxFreq(int arr[]) {
    // return {minFreq, maxFreq} 
    int min = -1, max = -1;
    for (int i = 0; i < 26; i++) {
        if (arr[i] == 0) continue;

        if (min == -1 || arr[min] > arr[i]) min = i;
        if (max == -1 || arr[max] < arr[i]) max = i;
    }

    if (min == max || min == -1 || max == -1) return {0, 0};
    return {arr[min], arr[max]};

    // Complexity analysis 
    // Time : O(26) => O(1) 
    // Space : O(1) 
}

int beautySum(string s) {
    int n = s.length();
    int sumOfBeauty = 0;

    for (int i = 0; i < n; i++) {
        // freq array 
        int charFreq[26] = {0};

        for (int j = i; j < n; j++) {
            // update freq 
            charFreq[s[j] - 'a']++;

            // calculate most and least freq 
            vector<int> freq = getMinMaxFreq(charFreq);

            // find beauty 
            int beauty = freq[1] - freq[0];

            // sum up 
            sumOfBeauty += beauty;
        }
    }

    return sumOfBeauty;

    // Complexity analysis 
    // Time : O(n ^ 2) 
    // Space : O(26) => O(1) 
}

void p1() {
    // Problem 1 : Leetcode 1781 Sum of Beauty of All Substrings - https://leetcode.com/problems/sum-of-beauty-of-all-substrings/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/sum-of-beauty-of-all-substrings-1662962118/1 

    string s = "something";
    int beauty = beautySum(s);
    cout << "beauty of " << s << " is ::" << beauty << endl;
}

int main() {
    // Day 25 

    p1();


    return 0;
}