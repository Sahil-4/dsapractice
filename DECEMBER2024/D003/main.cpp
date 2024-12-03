#include <bits/stdc++.h>

using namespace std;

#define ll long long

class Trie {
private:
    static const int __UPPER_BOUND__ = 63;

    typedef struct __TrieNode__ {
        __TrieNode__* links[__UPPER_BOUND__];
        int pref = 0;
        int end = 0;

        __TrieNode__() {
            std::fill_n(links, __UPPER_BOUND__, nullptr);
        }
    } __TrieNode__;

    int getCharKey(char ch) {
        int key = 62;

        if (ch >= 'a' && ch <= 'z') key = ch - 'a';
        else if (ch >= 'A' && ch <= 'Z') key = ch - 'A' + 26;
        else if (ch >= '0' && ch <= '9') key = ch - '0' + 26 + 26;

        return key;
    }

    bool nodeContainsKey(__TrieNode__* node, int index) {
        return ((node->links)[index] != NULL);
    }

    __TrieNode__* root;

public:
    Trie() { root = new __TrieNode__(); }

    void insert(string word) {
        __TrieNode__* temp = root;

        for (int i = 0, N = word.size(); i < N; i++) {
            int key = getCharKey(word[i]);

            if (!nodeContainsKey(temp, key)) {
                (temp->links)[key] = new __TrieNode__();
            }

            temp = (temp->links)[key];
            (temp->pref)++;
        }

        (temp->end)++;

        // Complexity analysis
        // Time : O(N)
        // Space : O(1)
    }

    bool search(string word) {
        __TrieNode__* temp = root;

        for (int i = 0, N = word.length(); i < N; i++) {
            int key = getCharKey(word[i]);
            if (!nodeContainsKey(temp, key)) return false;
            temp = (temp->links)[key];
        }

        return ((temp->end) > 0);

        // Complexity analysis
        // Time : O(N)
        // Space : O(1)
    }

    bool startsWith(string prefix) {
        __TrieNode__* temp = root;

        for (int i = 0, N = prefix.length(); i < N; i++) {
            int key = getCharKey(prefix[i]);
            if (!nodeContainsKey(temp, key)) return false;
            temp = (temp->links)[key];
        }

        return true;

        // Complexity analysis
        // Time : O(N)
        // Space : O(1)
    }

    int countWordsEqualsTo(string word) {
        __TrieNode__* temp = root;

        for (int i = 0, N = word.length(); i < N; i++) {
            int key = getCharKey(word[i]);
            if (!nodeContainsKey(temp, key)) return 0;
            temp = (temp->links)[key];
        }

        return (temp->end);

        // Complexity analysis
        // Time : O(N)
        // Space : O(1)
    }

    int countWordsStartsWith(string prefix) {
        __TrieNode__* temp = root;

        for (int i = 0, N = prefix.length(); i < N; i++) {
            int key = getCharKey(prefix[i]);
            if (!nodeContainsKey(temp, key)) return 0;
            temp = (temp->links)[key];
        }

        return (temp->pref);

        // Complexity analysis
        // Time : O(N)
        // Space : O(1)
    }

    void remove(string word) {
        // assure word exists 
        if (!(this->search(word))) return;

        __TrieNode__* temp = root;

        for (int i = 0, N = word.size(); i < N; i++) {
            int key = getCharKey(word[i]);
            temp = (temp->links)[key];
            (temp->pref)--;
        }

        (temp->end)--;

        // Complexity analysis
        // Time : O(N)
        // Space : O(1)
    }

    bool isAnswer(string word) {
        // for Leetcode 720 
        __TrieNode__* temp = root;

        for (int i = 0, N = word.size(); i < N; i++) {
            int key = getCharKey(word[i]);
            temp = (temp->links)[key];
            if ((temp->end) == 0) return false;
        }

        return ((temp->end) > 0);
    }
};


string solve(vector<string> words) {
    int N = words.size();

    // add words in trie 
    Trie* t = new Trie();
    for (int i = 0; i < N; i++) t->insert(words[i]);

    string ans = "";

    // traverse words and find largest word with all prefixes (except last char) 
    for (int i = 0; i < N; i++) {
        bool check = t->isAnswer(words[i]);
        if (!check) continue;
        if (ans.length() < words[i].length()) {
            // word bada hai 
            ans = words[i];
        }
        else if (ans.length() == words[i].length() && ans > words[i]) {
            // word ki len barabar hai aur lexicographically chhota hai 
            ans = words[i];
        }
    }

    return ans;

    // Complexity analysis 
    // Time : O(N * log(N)) + O(N) + O(N * len) + O(N * len) 
    // Space : O(N) copying input data + O(26^len) for trie 
}

string solve2(vector<string> words) {
    sort(words.begin(), words.end());
    unordered_set<string> built;
    string res;
    for (string w : words) {
        if (w.size() == 1 || built.count(w.substr(0, w.size() - 1))) {
            res = w.size() > res.size() ? w : res;
            built.insert(w);
        }
    }

    return res;

    // Complexity analysis 
    // Time : O(n * Log(n)) + (N) 
    // Space : O(N) copying input + set (N*len) ~ 
}

string longestWord(vector<string>& words) {
    // return solve(words);
    return solve2(words);
}

void p1() {
    // Problem 1 : Leetcode 720. Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/ 

    vector<string> words = { "b","br","bre","brea","break","breakf","breakfa","breakfas","breakfast","l","lu","lun","lunc","lunch","d","di","din","dinn","dinne","dinner" };
    string word = longestWord(words);
    cout << word << endl;
}

typedef struct SimpleTrie {
    SimpleTrie* links[26] = { nullptr };

    bool contains(char ch) {
        return links[ch - 'a'] != NULL;
    }

    void put(char ch) {
        links[ch - 'a'] = new SimpleTrie();
    }

    SimpleTrie* get(char ch) {
        return links[ch - 'a'];
    }
} SimpleTrie;

int __countDistinctSubstring__(string s) {
    int count = 1;
    SimpleTrie* root = new SimpleTrie();

    for (int i = 0, N = s.length(); i < N; i++) {
        SimpleTrie* temp = root;

        for (int j = i; j < N; j++) {
            if (!(temp->contains(s[j]))) {
                count++;
                temp->put(s[j]);
            }
            temp = temp->get(s[j]);
        }
    }

    return count;
    // TRIE gave MLE 
}

int countDistinctSubstring(string s) {
    // Your code here
    // return __countDistinctSubstring__(s);

    ll p = 31, mod = 1e17 + 7;
    unordered_set<ll> st;
    for (int i = 0; i < s.size(); i++) {
        ll hash = 0, p_pow = 1;
        for (int j = i; j < s.size(); j++) {
            hash = (hash + (s[j] - 'a' + 1) * p_pow) % mod;
            p_pow = (p_pow * p) % mod;
            st.insert(hash);
        }
    }

    return st.size() + 1;
}

void p2() {
    // Problem 2 : Geeksforgeeks Count of distinct substrings - https://www.geeksforgeeks.org/problems/count-of-distinct-substrings/1 

    cout << countDistinctSubstring("aaa") << endl;
    cout << countDistinctSubstring("abc") << endl;
}


int main() {
    // Day 3 of December - Trie 

    p1();

    p2();


    return 0;
}