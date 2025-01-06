#include <bits/stdc++.h>

using namespace std;

class TrieNode {
private:
    TrieNode* links[26] = { nullptr }; // child pointers
    int ns = 0;                      // number of string

public:
    void put(char ch) {
        if (links[ch - 'a'] == nullptr) links[ch - 'a'] = new TrieNode();
        links[ch - 'a']->ns++;
    }

    TrieNode* get(char ch) {
        return links[ch - 'a'];
    }

    int getN(char ch) {
        return links[ch - 'a'] ? links[ch - 'a']->ns : 0;
    }

    // Destructor to prevent memory leaks
    ~TrieNode() {
        for (int i = 0; i < 26; i++) {
            delete links[i];
        }
    }
};

class Trie {
private:
    TrieNode* head = nullptr;

public:
    Trie() {
        head = new TrieNode();
    }

    void putString(const string& s) {
        TrieNode* root = head;
        for (int i = 0; i < s.length(); i++) {
            root->put(s[i]);
            root = root->get(s[i]);
        }
    }

    int lcsLen(const string& s, int N) {
        TrieNode* root = head;
        int len = 0;

        for (int i = 0; i < s.length(); i++) {
            if (!root || root->getN(s[i]) != N) break;
            len++;
            root = root->get(s[i]);
        }

        return len;
    }

    ~Trie() {
        delete head;
    }
};

class Problem1 {
    string btute(vector<string> arr) {
        string lcp = "";

        // sort all strings in ascending/lexicographical order
        sort(arr.begin(), arr.end());

        // find the smallest word
        int slen = arr[0].length();
        for (int i = 1; i < arr.size(); i++) {
            if (slen < arr[i].length()) slen = arr[i].length();
        }

        // run a loop to check slen chars of each strings
        // and check whether or not they are equal
        for (int si = 0; si < slen; si++) { // all chars
            bool flag = true;
            for (int ai = 1; ai < arr.size() && flag != false; ai++) { // all strings
                if (arr[ai][si] != arr[0][si]) flag = false;
            }

            if (!flag) break;
            lcp += arr[0][si];
        }

        return lcp;

        // Complexity analysis
        // Time : O(N*Log(N)) sorting + O(N) + O(slen * N)
        // Space : O(N) copying given dataset
    }

    string better(vector<string> arr) {
        string lcp = "";

        // sort all strings in ascending/lexicographical order
        sort(arr.begin(), arr.end());

        // now array is like ["aaaa", "aaabc", "aabca", "abc"] sorted
        // so if we want to find the maximum difference then we will have to
        // loop 0th and (n-1)th string int z = 0, n1 = arr.size()-1;
        for (int i = 0, n = arr.size(); i < arr[0].length() && i < arr[n - 1].length(); i++) {
            // if (arr[z][i] != arr[n1][i]) break;
            if (arr[0][i] != arr[n - 1][i]) break;
            lcp += arr[0][i];
        }

        return lcp;

        // Complexity analysis
        // Time : O(N*Log(N)) sorting + O(slen)
        // Space : O(N) copying given dataset
    }

    string optimal(vector<string>& strs) {
        // init trie
        Trie* tr = new Trie();

        // put all s in trie
        for (string s : strs) tr->putString(s);

        // now find length of lcs
        int lcsLen = tr->lcsLen(strs[0], strs.size());

        // build lcs of len lcsLen 
        string lcs = "";
        for (int i = 0; i < lcsLen; i++) lcs += strs[0][i];

        return lcs;

        // Complexity analysis
        // Time : O(N*strlen) put string + O(lcsLen) find length of lcs + O(lcsLen) build lcs 
        // Space : O(26 ^ N) for trie 
    }

public:
    string longestCommonPrefix(vector<string>& strs) {
        // return btute(strs);

        // return better(strs);

        return optimal(strs);
    }
};

void p1() {
    // Problem 1 : Leetcode 14. Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1 

    vector<string> strs = {};
    cout << Problem1().longestCommonPrefix(strs) << endl;
}

class Problem2 {
    string solve1(string s) {
        string ns = "";

        for (int i = s.length() - 1; i >= 0; i--) {
            // skip all spaces at last 
            while (i >= 0 && s[i] == ' ') i--;
            int end = i;

            // collect all non spaces 
            while (i >= 0 && s[i] != ' ') i--;
            int start = i + 1;

            // add word 
            if (start <= end) {
                if (ns != "") ns += " ";
                ns += s.substr(start, end - start + 1);
            }
        }

        return ns;

        // Complexity analysis 
        // Time : O(N*N) ~ 
        // Space : O(N) for output string 
    }

    string solve2(string s) {
        int n = s.length();

        vector<string> sv;
        string ss = "";

        for (int i = 0; i <= n; i++) {
            if (i != n && s[i] != ' ') ss += s[i];
            else if (ss != "") {
                sv.push_back(ss);
                ss = "";
            }
        }

        string ns = "";

        for (int n = sv.size(), i = n - 1; i >= 0; i--) {
            ns = ns + sv[i];
            if (i != 0) ns += ' ';
        }

        return ns;

        // Complexity analysis 
        // Time : O(N) ~ 
        // Space : O(N) for output string + O(N) for tokens 
    }

    string solve3(string s) {
        // two pointers 

        int n = s.length();
        int i = 0;
        int l = 0, r = 0;

        // reverse entire string 
        reverse(s.begin() + 0, s.begin() + n);

        while (i < n) {
            // collect non space chars 
            while (i < n && s[i] != ' ') s[r++] = s[i++];

            // reverse l to r 
            if (l < r) {
                reverse(s.begin() + l, s.begin() + r);
                s[r++] = ' ';
                l = r;
            }

            i++;
        }

        return s.substr(0, r - 1);

        // Complexity analysis 
        // Time : O(3N) ~ 
        // Space : O(N) for copying input string for output 
    }

public:
    string reverseWords(string s) {
        // return solve1(s);

        // return solve2(s);

        return solve3(s);
    }
};

void p2() {
    // Problem 2 : Leetcode 151. Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1 

    cout << Problem2().reverseWords("    h   el    lo     wordld      ") << endl;
}


int main() {
    // Day 6 of January 

    p1();

    p2();


    return 0;
}