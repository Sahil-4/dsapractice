#include <iostream>
#include <vector>

using namespace std;

int numberOfSubstrings_Solution1(string s) {
    int substringsCount = 0;

    for (int it = 0; it < s.length(); it++) {
        int freq[3] = {0}; // freq of a b c 

        for (int it2 = it; it2 < s.length(); it2++) {
            freq[s[it2] - 'a']++;

            if (freq[0] && freq[1] && freq[2]) {
                substringsCount += s.length() - it2;
                break;
            }
        }
    }

    return substringsCount;

    // Complexity 
    // TIme : O(n ^ 2) 
    // Space : O(1) 
}

int minOf3s(vector<int> arr) {
    int out = arr[0];
    for (int i = 0; i < 3; i++) out = min(out, arr[i]);
    return out;
}

int numberOfSubstrings(string s) {
    int substringsCount = 0; // ans 

    int freq[3] = { -1, -1, -1 }; // last seen index of a b c 

    for (int r = 0; r < s.length(); r++) {
        freq[s[r] - 'a'] = r;

        if (freq[0] != -1 && freq[1] != -1 && freq[2] != -1) {
            // found a valid substr 
            // find min index 
            int idx = minOf3s({freq[0], freq[1], freq[2]});
            // add 1 (for current) and add it in answer 
            substringsCount += idx + 1;
        }
    }

    return substringsCount;

    // Complexity 
    // TIme : O(n) 
    // Space : O(1) 
}

void p1() {
    // Problem 1 : Leetcode 1358. Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/count-substring/1 

    string s = "acbca";
    // int subStrs = numberOfSubstrings(s);
    // cout << "ans :: " << subStrs << endl;
}

int main() {
    // Day 30 

    p1();


    return 0;
}