#include <bits/stdc++.h>

using namespace std;


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
};

void test() {
    vector<string> operations = { "Trie", "insert", "search", "search", "startsWith", "insert", "search", "insert", "countWordsEqualsTo", "countStartsWith", "remove", "countWordsEqualsTo", "countStartsWith" };
    vector<vector<string>> arguments = { {}, {"apple"}, {"apple"}, {"app"}, {"app"}, {"app"}, {"app"}, {"apple"}, {"apple"}, {"app"}, {"app"}, {"app"}, {"app"} };
    vector<string> output;

    Trie* t = new Trie();

    for (int i = 1, N = operations.size(); i < N; i++) {
        if (operations[i] == "insert") {
            t->insert(arguments[i][0]);
            output.push_back("inserted " + arguments[i][0]);
        } else if (operations[i] == "search") {
            bool out = t->search(arguments[i][0]);
            if (out) output.push_back("yes found " + arguments[i][0]);
            else output.push_back("not found " + arguments[i][0]);
        } else if (operations[i] == "startsWith") {
            bool out = t->startsWith(arguments[i][0]);
            if (out) output.push_back("yes starts with " + arguments[i][0]);
            else output.push_back("no starts with " + arguments[i][0]);
        } else if (operations[i] == "countWordsEqualsTo") {
            int out = t->countWordsEqualsTo(arguments[i][0]);
            output.push_back("equals to " + arguments[i][0] + " " + to_string(out));
        } else if (operations[i] == "countStartsWith") {
            int out = t->countWordsStartsWith(arguments[i][0]);
            output.push_back("starts with " + arguments[i][0] + " " + to_string(out));
        } else if (operations[i] == "remove") {
            t->remove(arguments[i][0]);
            output.push_back("removed " + arguments[i][0]);
        }
    }

    for (string out : output) cout << out << endl;
}

void p1() {
    // Problem 1 : Leetcode 208. Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/trie-insert-and-search0651/1 

    test();
}


int main() {
    // Day 2 of December - started with Trie 

    p1();


    return 0;
}