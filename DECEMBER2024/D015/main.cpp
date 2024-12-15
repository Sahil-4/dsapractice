#include <bits/stdc++.h>

using namespace std;

class Solution {
private:
    unordered_map<string, string> table; // hash -> URL 
    const int HASH_LENGTH = 8;
    const string cset = "1023aAb465BCcDEdFeGfHIghijJKLMNkl978mOPnoDQpRqrstuvTUVwxWyXzYZ";

    int random() {
        srand(time(0));
        return rand();
    }

    string hash() {
        // create 7 length digest 
        string digest = "";

        for (int i = 0; i < HASH_LENGTH; i++) {
            int ri = random() % 62;
            digest.push_back(cset[ri]);
        }

        return digest;

        // Complexity analysis 
        // Time : O(HASH_LENGTH) 
        // Space : O(1) 
    }

public:
    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        string digest = hash();
        table[digest] = longUrl;
        return digest;

        // Complexity analysis 
        // Time : O(1) 
        // Space : O(1) 
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return table[shortUrl];

        // Complexity analysis 
        // Time : O(1), DATASET_S = size of dataset 
        // Space : O(1) 
    }

    // Space : O(DATASET_S), DATASET_S = total number of URLs 
};


void p1() {
    // Problem 1 : Leetcode 535. Encode and Decode TinyURL - https://leetcode.com/problems/encode-and-decode-tinyurl/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/encode-and-decode-strings/1 

    Solution *s = new Solution();
    cout << s->decode(s->encode("https://leetcode.com/")) << endl;
}


int main() {
    // Day 15 of December 

    p1();


    return 0;
}