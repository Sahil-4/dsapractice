#include <bits/stdc++.h>

using namespace std;

class Trie {
    class TrieNode {
        // static const int CAP = 64;
        static const int CAP = 27;

        TrieNode* next[CAP] = { nullptr };
        bool endsWith;
        int prefixCount;

        int hash(char ch) {
            if (ch >= 'a' && ch <= 'z') return (ch - 'a') + 0;
            if (ch >= 'A' && ch <= 'Z') return (ch - 'A') + 0 + 26;
            if (ch >= '0' && ch <= '9') return (ch - '0') + 0 + 26 + 26;
            return 26 + 26 + 10 + 1;
        }

    public:
        TrieNode() {
            endsWith = false;
            prefixCount = 0;
        }

        bool getEndsWith() {
            return this->endsWith;
        }

        int getPrefixCount() {
            return this->prefixCount;
        }

        TrieNode* get(char ch) {
            return this->next[hash(ch)];
        }

        TrieNode* set(char ch) {
            if (this->next[hash(ch)] == nullptr) {
                this->next[hash(ch)] = new TrieNode();
            }
            return this->next[hash(ch)];
        }

        TrieNode* setEndsWith(bool flag = false) {
            this->endsWith = flag;
            return this;
        }

        TrieNode* incrementPrefixCount() {
            this->prefixCount++;
            return this;
        }

        TrieNode* decrementPrefixCount() {
            this->prefixCount--;
            return this;
        }
    };

    TrieNode* root;

public:
    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {
        TrieNode* temp = root;

        for (char s : word) {
            temp = temp->set(s);
            temp->incrementPrefixCount();
        }

        temp->setEndsWith(true);
    }

    bool search(string word) {
        TrieNode* temp = root;

        for (char s : word) {
            temp = temp->get(s);
            if (temp == nullptr) break;
        }

        return temp != nullptr && temp->getEndsWith();
    }

    bool startsWith(string prefix) {
        TrieNode* temp = root;

        for (char s : prefix) {
            temp = temp->get(s);
            if (temp == nullptr) return false;
        }

        return temp->getPrefixCount() > 0;
    }

    int countStartsWith(string prefix) {
        TrieNode* temp = root;

        for (char s : prefix) {
            temp = temp->get(s);
            if (temp == nullptr) return false;
        }

        return temp->getPrefixCount();
    }

    bool remove(string word) {
        if (!search(word)) return false;

        TrieNode* temp = root;

        for (char s : word) {
            temp = temp->get(s);
            temp->decrementPrefixCount();
        }

        temp->setEndsWith(false);

        return true;
    }
};

void p1() {
    // Problem 1 : Leetcode 208. Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/trie-insert-and-search0651/1 

    Trie* trie = new Trie();
    cout << trie->search("abcdef") << endl;
    cout << trie->startsWith("abc") << endl;
    cout << trie->countStartsWith("abc") << endl;
    trie->insert("abcdef");
    cout << trie->search("abcdef") << endl;
    cout << trie->startsWith("abc") << endl;
    cout << trie->countStartsWith("abc") << endl;
    trie->remove("abcdef");
    cout << trie->search("abcdef") << endl;
    cout << trie->startsWith("abc") << endl;
    cout << trie->countStartsWith("abc") << endl;
    trie->insert("abcd");
    trie->insert("abcx");
    cout << trie->search("abcd") << endl;
    cout << trie->search("abcx") << endl;
    cout << trie->startsWith("abc") << endl;
    cout << trie->countStartsWith("abc") << endl;
}

class WordDictionary {
    class TrieNode {
        // static const int CAP = 64;
        static const int CAP = 27;

        TrieNode* next[CAP] = { nullptr };
        bool endsWith;
        int prefixCount;

        int hash(char ch) {
            if (ch >= 'a' && ch <= 'z') return (ch - 'a') + 0;
            if (ch >= 'A' && ch <= 'Z') return (ch - 'A') + 0 + 26;
            if (ch >= '0' && ch <= '9') return (ch - '0') + 0 + 26 + 26;
            return 26 + 26 + 10 + 1;
        }

    public:
        TrieNode() {
            endsWith = false;
            prefixCount = 0;
        }

        bool getEndsWith() {
            return this->endsWith;
        }

        int getPrefixCount() {
            return this->prefixCount;
        }

        TrieNode* get(char ch) {
            return this->next[hash(ch)];
        }

        TrieNode* set(char ch) {
            if (this->next[hash(ch)] == nullptr) {
                this->next[hash(ch)] = new TrieNode();
            }
            return this->next[hash(ch)];
        }

        TrieNode* setEndsWith(bool flag = false) {
            this->endsWith = flag;
            return this;
        }

        TrieNode* incrementPrefixCount() {
            this->prefixCount++;
            return this;
        }

        TrieNode* decrementPrefixCount() {
            this->prefixCount--;
            return this;
        }
    };

    TrieNode* root;

public:
    WordDictionary() {
        root = new TrieNode();
    }

    void addWord(string word) {
        TrieNode* temp = root;

        for (char s : word) {
            temp = temp->set(s);
            temp->incrementPrefixCount();
        }

        temp->setEndsWith(true);
    }

    bool __search__(string& word, int i, TrieNode* temp) {
        if (i == word.length()) return temp->getEndsWith();
        if (word[i] != '.' && temp->get(word[i]) == nullptr) return false;

        bool flag = false;

        if (word[i] != '.') {
            flag = __search__(word, i + 1, temp->get(word[i]));
        }
        else {
            for (char ch = 'a'; ch <= 'z'; ch++) {
                if (temp->get(ch) == nullptr) continue;
                flag = flag || __search__(word, i + 1, temp->get(ch));
            }
        }

        return flag;
    }

    bool search(string word) {
        return __search__(word, 0, root);
    }

    // Complexity analysis 
    // Time : O(N) 
    // Space: used trie 
};

void p2() {
    // Problem 2 : Leetcode 211. Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/design-add-and-search-words-data-structure--154618/1 

    WordDictionary* wd = new WordDictionary();
    wd->addWord("axcdx");
    wd->addWord("aycdy");
    wd->addWord("azcdz");
    cout << wd->search("a.cdx") << endl;
    cout << wd->search("a.cd.") << endl;
}

class WordSearch2 {
    class TrieNode {
        // static const int CAP = 64;
        static const int CAP = 27;

        TrieNode* next[CAP] = { nullptr };
        bool endsWith;
        int prefixCount;

        int hash(char ch) {
            if (ch >= 'a' && ch <= 'z') return (ch - 'a') + 0;
            if (ch >= 'A' && ch <= 'Z') return (ch - 'A') + 0 + 26;
            if (ch >= '0' && ch <= '9') return (ch - '0') + 0 + 26 + 26;
            return 26 + 26 + 10 + 1;
        }

    public:
        TrieNode() {
            endsWith = false;
            prefixCount = 0;
        }

        bool getEndsWith() {
            return this->endsWith;
        }

        int getPrefixCount() {
            return this->prefixCount;
        }

        TrieNode* get(char ch) {
            return this->next[hash(ch)];
        }

        TrieNode* set(char ch) {
            if (this->next[hash(ch)] == nullptr) {
                this->next[hash(ch)] = new TrieNode();
            }
            return this->next[hash(ch)];
        }

        TrieNode* setEndsWith(bool flag = false) {
            this->endsWith = flag;
            return this;
        }

        TrieNode* incrementPrefixCount() {
            this->prefixCount++;
            return this;
        }

        TrieNode* decrementPrefixCount() {
            this->prefixCount--;
            return this;
        }
    };

    void insert(TrieNode* root, string& word) {
        TrieNode* temp = root;

        for (char s : word) {
            temp = temp->set(s);
            temp->incrementPrefixCount();
        }

        temp->setEndsWith(true);
    }

    // top, left, bottom, right 
    int D = 4;
    int DRC[4][2] = { {-1, 0}, {0, -1}, {+1, 0}, {0, +1} };
    char MARK = '$';

    void traverse(TrieNode* node, vector<vector<char>>& board, int r, int c, vector<string>& out, string word) {
        if (node->getEndsWith()) {
            out.push_back(word);
            node->setEndsWith(false);
        }
        if (r < 0 || c < 0 || r >= board.size() || c >= board[0].size()) return;
        if (board[r][c] == MARK) return;
        if (!node->get(board[r][c])) return;

        char temp = board[r][c];
        board[r][c] = MARK;
        word.push_back(temp);
        node = node->get(temp);

        for (int k = 0; k < D; k++) {
            int nr = r + DRC[k][0], nc = c + DRC[k][1];
            traverse(node, board, nr, nc, out, word);
        }

        word.pop_back();
        board[r][c] = temp;
    }

public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        // trie 
        TrieNode* root = new TrieNode();

        // build trie 
        for (string& word : words) insert(root, word);

        vector<string> out;

        // now traverse grid and find words existance 
        for (int r = 0; r < board.size(); r++) {
            for (int c = 0; c < board[0].size(); c++) {
                traverse(root, board, r, c, out, "");
            }
        }

        return out;
    }
};

void p3() {
    // Problem 3 : Leetcode 212. Word Search II - https://leetcode.com/problems/word-search-ii/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/word-search-ii/1 

    vector<vector<char>> board = { {'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'} };
    vector<string> words = { "oath","pea","eat","rain" };

    vector<string> res = WordSearch2().findWords(board, words);
    for (string s : res) cout << s << " ";
    cout << endl;
}


int main() {
    // Day 31 of January 2025 

    p1();

    p2();

    p3();


    return 0;
}