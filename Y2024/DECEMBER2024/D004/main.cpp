#include <bits/stdc++.h>

using namespace std;


int XOR(int n, int m) {
    // code here
    return n ^ m;
}

int check(int a, int b) {
    // code here
    return (b >> a - 1) & 1;
}

int setBit(int c, int d) {
    // code here
    return d | (1 << c);
}

void p1() {
    // Problem 1 : Geeksforgeeks Bit's basic operations - https://www.geeksforgeeks.org/problems/bits-basic-operations/1 

    cout << "xor of 2, 5 :: " << XOR(2, 5) << endl;
    cout << "check of 2, 5 :: " << check(2, 5) << endl;
    cout << "setBit of 2, 5 :: " << setBit(2, 5) << endl;
}

class BinaryTrieNode {
private:
    BinaryTrieNode* links[2];

public:
    bool containsKey(int bit) {
        return links[bit] != NULL;
    }

    BinaryTrieNode* getNext(int bit) {
        return links[bit];
    }

    void put(int bit) {
        links[bit] = new BinaryTrieNode();
    }
};

class BinaryTrie {
private:
    BinaryTrieNode* root;

public:
    BinaryTrie() {
        root = new BinaryTrieNode();
    }

    void insert(int number) {
        BinaryTrieNode* temp = root;

        for (int i = 31; i >= 0; i--) {
            int bit = (number >> i) & 1;
            if (!(temp->containsKey(bit))) temp->put(bit);
            temp = temp->getNext(bit);
        }
    }

    int getMaximumXOR(int number) {
        int maximum = 0;

        BinaryTrieNode* temp = root;

        for (int i = 31; i >= 0; i--) {
            int bit = (number >> i) & 1;
            if ((temp->containsKey(!bit))) {
                maximum = maximum | (1 << i);
                temp = temp->getNext(!bit);
            }
            else {
                temp = temp->getNext(bit);
            }
        }

        return maximum;
    }
};

int TLE_wala(vector<int>& nums) {
    int maximum = 0;

    for (int i = 0, N = nums.size(); i < N; i++) {
        for (int j = i; j < N; j++) {
            int o = nums[i] ^ nums[j];
            maximum = max(maximum, o);
        }
    }

    return maximum;

    // Complexity analysis 
    // Time : O(N*N) 
    // Space : O(1) 
}

int trie_wala(vector<int>& nums) {
    int maximum = 0;

    BinaryTrie* bt = new BinaryTrie();

    // insert all numbers in trie 
    for (int n : nums) bt->insert(n);

    // find the largest XOR 
    for (int n : nums) {
        int x = bt->getMaximumXOR(n);
        maximum = max(maximum, x);
    }

    return maximum;

    // Complexity analysis 
    // Time : O(N * 32) + O(N * 32) 
    // Space : O(2^32) 
}

void p2() {
    // Problem 2 : Leetcode 421. Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/maximum-xor-of-two-numbers-in-an-array/1 

    vector<int> nums = { 3,10,5,25,2,8 };
    cout << trie_wala(nums) << endl;
}

vector<int> maximizeXor(vector<int>& nums, vector<vector<int>>& queries) {
    int N = nums.size(), M = queries.size();

    // sort array of numbers
    sort(nums.begin(), nums.end());

    // sort queries according to bound {bound, {number, index}}
    vector<pair<int, pair<int, int>>> qri;
    for (int i = 0; i < M; i++) {
        qri.push_back({ queries[i][1], { queries[i][0], i } });
    }
    sort(qri.begin(), qri.end());

    // for output
    vector<int> out(M, 0);
    BinaryTrie* bt = new BinaryTrie();
    int arr_ptr = 0;

    for (int i = 0; i < M; i++) {
        int bound = qri[i].first;
        int number = qri[i].second.first;
        int index = qri[i].second.second;

        while (arr_ptr < N && nums[arr_ptr] <= bound) {
            bt->insert(nums[arr_ptr]);
            arr_ptr++;
        }

        if (arr_ptr != 0) out[index] = bt->getMaximumXOR(number);
        else out[index] = -1;
    }

    return out;

    // Complexity analysis 
    // Time : O(N * Log(N)) + O(M) + O(M * Log(M)) + O(M * N * 2^32) 
    // Space : O(M) + O(2^32) 
}

void p3() {
    // Problem 3 : Leetcode 1707. Maximum XOR With an Element From Array - https://leetcode.com/problems/maximum-xor-with-an-element-from-array/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/maximum-xor-with-an-element-from-array/1 

    vector<int> nums = { 0,1,2,3,4 };
    vector<vector<int>> queries = { {3,1},{1,3},{5,6} };

    vector<int> out = maximizeXor(nums, queries);
    for (int n : out) cout << n << endl;
}


int main() {
    // Day 4 of December - Trie 

    p1();

    p2();

    p3();


    return 0;
}