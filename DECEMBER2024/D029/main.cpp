#include <bits/stdc++.h>

using namespace std;

int sol1(string& s) {
    set<string> st;

    st.insert("");
    for (int i = 0; i < s.size(); i++) {
        string sub = "";
        for (int j = i; j < s.size(); j++) {
            sub.push_back(s[j]);
            st.insert(sub);
        }
    }

    return st.size();

    // Complexity analysis 
    // Time : O(N*N*LOG(M)) 
    // Space : O(N*N * N) ~ 
}

class TrieNode {
    TrieNode* links[26];

public:
    bool containsKey(char ch) {
        return (links[ch - 'a'] != NULL);
    }

    void put(char ch) {
        links[ch - 'a'] = new TrieNode();
    }

    TrieNode* get(char ch) {
        return links[ch - 'a'];
    }
};

int sol2(string& s) {
    int noOfDisSubstr = 1;

    TrieNode* root = new TrieNode();

    for (int startI = 0; startI < s.size(); startI++) {
        TrieNode* n = root;
        for (int endI = startI; endI < s.size(); endI++) {
            if (!(n->containsKey(s[endI]))) {
                noOfDisSubstr++;
                n->put(s[endI]);
            }
            n = n->get(s[endI]);
        }
    }

    return noOfDisSubstr;

    // Complexity analysis 
    // Time : O(N*N) 
    // Space : O(26^N) ~ 
}

/*You are required to complete this method */
int countDistinctSubstring(string s) {
    // Your code here 

    // return sol1(s);

    return sol2(s);
}

void p1() {
    // Problem 1 : Geeksforgeeks Count of distinct substrings - https://www.geeksforgeeks.org/problems/count-of-distinct-substrings/1 

    cout << countDistinctSubstring("abc") << endl;
    cout << countDistinctSubstring("abcab") << endl;
    cout << countDistinctSubstring("aaa") << endl;
}


class BinaryTrieNode {
    static const int bound = 2;
    BinaryTrieNode* links[bound];

public:
    bool containsKey(int b) {
        return (links[b] != NULL);
    }

    void put(int b) {
        links[b] = new BinaryTrieNode();
    }

    BinaryTrieNode* get(int b) {
        return links[b];
    }
};

class Trie {
    BinaryTrieNode* root;

public:
    Trie() {
        root = new BinaryTrieNode();
    }

    void insert(int n) {
        BinaryTrieNode* node = root;

        for (int s = 31; s >= 0; s--) {
            int bit = (n >> s) & 1;
            if (!node->containsKey(bit)) node->put(bit);
            node = node->get(bit);
        }
    }

    int getMaxXOR(int xi) {
        BinaryTrieNode* node = root;

        int out = 0;

        for (int s = 31; s >= 0; s--) {
            int bit = (xi >> s) & 1;

            if (node->containsKey(!bit)) {
                out = out | (1 << s);
                node = node->get(!bit);
            }
            else {
                node = node->get(bit);
            }
        }

        return out;
    }
};

class Problem2 {
    vector<int> sol1(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> out;

        for (vector<int> query : queries) {
            int xi = query[0], mi = query[1];

            int ans = -1;

            for (int e : nums) {
                if (e > mi) continue;
                int XOR = e ^ xi;
                ans = max(ans, XOR);
            }

            out.push_back(ans);
        }

        return out;

        // Complexity analysis
        // Time : O(Q * N)
        // Space : O(1)
    }

    static bool custom_sort(vector<int>& q1, vector<int>& q2) {
        return q1[1] < q2[1];
    }

    vector<int> sol2(vector<int> nums, vector<vector<int>> queries) {
        int N = nums.size(), Q = queries.size();

        // output
        vector<int> out(Q, -1);

        // queries[qi][2] = qi; // adding index for offline queries
        for (int qi = 0; qi < Q; qi++) queries[qi].push_back(qi);

        // now sort given nums array acs
        sort(nums.begin(), nums.end());
        sort(queries.begin(), queries.end(), custom_sort);

        // we have prepared offline queries

        // crete Trie
        Trie* root = new Trie();

        int ei = 0; // pointer to point at current index of nums array
        // add elements in trie starting from ei index

        for (vector<int>& query : queries) {
            int xi = query[0], mi = query[1], qi = query[2];

            // put all elements <= mi in trie
            while (ei < N) {
                if (nums[ei] > mi) break;
                // add nums[ei] in trie
                root->insert(nums[ei]);
                ei++;
            }

            // get max xor from trie and add max xor at out[qi]
            if (ei != 0) out[qi] = root->getMaxXOR(xi);
        }

        return out;
    }

public:
    vector<int> maximizeXor(vector<int>& nums, vector<vector<int>>& queries) {
        // return sol1(nums, queries);

        return sol2(nums, queries);
    }
};

void p2() {
    // Problem 2 : Leetcode 1707. Maximum XOR With an Element From Array - https://leetcode.com/problems/maximum-xor-with-an-element-from-array/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/maximum-xor-with-an-element-from-array/0 

    vector<int> nums = { 0, 1, 2, 3, 4 };
    vector<vector<int>> queries = { {3, 1}, {1, 3}, {5, 6} };

    vector<int> out = Problem2().maximizeXor(nums, queries);
    for (int e : out) cout << e << " ";
    cout << endl;
}


int main() {
    // Day 29 of December 

    p1();

    p2();


    return 0;
}