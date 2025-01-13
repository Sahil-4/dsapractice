#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    bool isValidIndex(int N, int M, int i, int j) {
        if ((i >= 0 && i < N) && (j >= 0 && j < M)) return true;
        return false;
    }

    int getNextStateOfCell1(vector<vector<int>>& board, int N, int M, int i, int j) {
        vector<vector<int>> neighbours = {
            {i - 1, j - 1}, {i - 1, j}, {i - 1, j + 1},
            {i, j - 1}, {i, j + 1},
            {i + 1, j - 1}, {i + 1, j}, {i + 1, j + 1}
        };

        int livingCount = 0;
        int deadCount = 0;

        for (vector<int> coord : neighbours) {
            int r = coord[0], c = coord[1];
            if (!isValidIndex(N, M, r, c)) continue;

            if (board[r][c] == 1) livingCount++;
            else deadCount++;
        }

        if (board[i][j] == 0 && livingCount == 3) return 1;
        else if (board[i][j] == 1 && livingCount < 2) return 0;
        else if (board[i][j] == 1 && livingCount >= 2 && livingCount <= 3) return 1;
        else if (board[i][j] == 1 && livingCount > 3) return 0;
        return 0;
    }

    void solve1(vector<vector<int>>& board) {
        int N = board.size(), M = board[0].size();

        vector<vector<int>> grid(N, vector<int>(M, 0));
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                grid[i][j] = getNextStateOfCell1(board, N, M, i, j);
            }
        }

        // copy
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                board[i][j] = grid[i][j];
            }
        }

        // Complexity analysis
        // Time : O(N*M * 8) + O(N*M)
        // Space : O(N*M)
    }

    // maps to store state mapping // [0 1 2 3]
    int getOld[4] = { 0, 1, 0, 1 };
    int getNew[4] = { 0, 0, 1, 1 };
    // map<int, int> getOld = { {0, 0}, {1, 1}, {2, 0}, {3, 1} }; // mark state to old cell value
    // map<int, int> getNew = { {0, 0}, {1, 0}, {2, 1}, {3, 1} }; // mark state to new cell value
    int getMark[2][2] = { {0, 2}, {1, 3} };

    int getNextStateOfCell(vector<vector<int>>& board, int N, int M, int i, int j) {
        vector<vector<int>> neighbours = {
            {i - 1, j - 1}, {i - 1, j}, {i - 1, j + 1},
            {i, j - 1}, {i, j + 1},
            {i + 1, j - 1}, {i + 1, j}, {i + 1, j + 1}
        };

        int livingCount = 0;
        int deadCount = 0;

        for (vector<int> coord : neighbours) {
            int r = coord[0], c = coord[1];
            if (!isValidIndex(N, M, r, c)) continue;

            if (getOld[board[r][c]] == 1) livingCount++;
            else deadCount++;
        }

        int cell = getOld[board[i][j]];
        if (cell == 0 && livingCount == 3) return 1;
        else if (cell == 1 && livingCount < 2) return 0;
        else if (cell == 1 && livingCount >= 2 && livingCount <= 3) return 1;
        else if (cell == 1 && livingCount > 3) return 0;
        return 0;
    }

    void solve2(vector<vector<int>>& board) {
        /*
            # state mapping #
            # Old   # New   # Mark
            # 0     # 0     # 0
            # 1     # 0     # 1
            # 0     # 1     # 2
            # 1     # 1     # 3

            earliear was 0 and then became 1 then i would mark it as 2
            # 0     # 1     # 2
        */

        int N = board.size(), M = board[0].size();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                int cellOld = getOld[board[i][j]];
                int nayaValue = getNextStateOfCell(board, N, M, i, j);
                int cellNew = getMark[cellOld][nayaValue];
                board[i][j] = cellNew;
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                board[i][j] = getNew[board[i][j]];
            }
        }

        // Complexity analysis 
        // Time : O(N*M * 8) + O(N*M) 
        // Space : O(1) 
    }

public:
    void gameOfLife(vector<vector<int>>& board) {
        // return solve1(board);

        return solve2(board);
    }
};


void p1() {
    // Problem 1 : Leetcode 289. Game of Life - https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150 

    vector<vector<int>> board = { {0,1,0,1,0},{0,0,1,0,1},{1,1,0,1,1},{0,1,0,1,0},{0,0,1,0,1},{1,1,0,1,1} };
    Problem1().gameOfLife(board);

    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            cout << board[i][j] << " ";
        } cout << endl;
    }
}

class Problem2 {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int freq[26] = { 0 };

        for (char ch : ransomNote) freq[ch - 'a']++;
        for (char ch : magazine) freq[ch - 'a']--;

        bool check = true;
        for (int f : freq) check = check && !(f > 0);

        return check;

        // Complexity analysis 
        // Time : O(N+M+26) 
        // Space : O(26) 
    }
};

void p2() {
    // Problem 2 : Leetcode 383. Ransom Note - https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150 

    cout << Problem2().canConstruct("ransom", "somerandomtext") << endl;
    cout << Problem2().canConstruct("ransom", "random") << endl;
}

class Problem3 {

public:
    bool isIsomorphic(string s, string t) {
        if (s.length() != t.length()) return false;

        unordered_map<char, char> s2t;
        unordered_map<char, char> t2s;

        for (int i = 0; i < s.length(); i++) {
            char sc = s[i], tc = t[i];

            if (s2t.find(sc) != s2t.end() && s2t[sc] != tc) return false;
            if (t2s.find(tc) != t2s.end() && t2s[tc] != sc) return false;

            s2t[sc] = tc;
            t2s[tc] = sc;
        }

        return true;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(2 * 256) 
    }
};

void p3() {
    // Problem 3 : Leetcode 205. Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1 

    cout << Problem3().isIsomorphic("abcd", "kick") << endl;
    cout << Problem3().isIsomorphic("abcd", "efgh") << endl;
    cout << Problem3().isIsomorphic("abc", "efgh") << endl;
}

class Problem4 {
    bool solve1(string pattern, string s) {
        vector<string> words;
        for (int l = 0, r = 0; r <= s.length(); r++) {
            if (r == s.length() || s[r] == ' ') {
                words.push_back(s.substr(l, r - l));
                l = r + 1;
            }
        }

        if (words.size() != pattern.length()) return false;

        unordered_map<char, string> char2word;
        unordered_map<string, char> word2char;

        for (int i = 0; i < pattern.length(); i++) {
            char ch = pattern[i];
            string word = words[i];

            if (char2word.find(ch) != char2word.end() && char2word[ch] != word) return false;
            if (word2char.find(word) != word2char.end() && word2char[word] != ch) return false;

            char2word[ch] = word;
            word2char[word] = ch;
        }

        return true;

        // Complexity analysis 
        // Time : O(SN) + O(PN) 
        // Space : O(words) + O(chars) + O(words) 
    }

    bool solve2(string pattern, string s) {
        unordered_map<char, string> char2word;
        unordered_map<string, char> word2char;

        int i = 0, l = 0, r = 0;

        while (r <= s.length() && i < pattern.length()) {
            if (r == s.length() || s[r] == ' ') {
                char ch = pattern[i];
                string word = s.substr(l, r - l);

                if (char2word.find(ch) != char2word.end() && char2word[ch] != word) return false;
                if (word2char.find(word) != word2char.end() && word2char[word] != ch) return false;

                char2word[ch] = word;
                word2char[word] = ch;
                l = r + 1;
                i++;
            }
            r++;
        }

        return ((i >= pattern.length()) && (r >= s.length()));

        // Complexity analysis 
        // Time : O(SN) 
        // Space : O(chars) + O(words) 
    }

public:
    bool wordPattern(string pattern, string s) {
        // return solve1(pattern, s);

        return solve2(pattern, s);
    }
};

void p4() {
    // Problem 4 : Leetcode 290. Word Pattern - https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150 

    cout << Problem4().wordPattern("abba", "dog cat cat dog") << endl;
}

class Problem5 {
public:
    bool isAnagram(string s, string t) {
        int freq[26] = { 0 };

        for (char ch : s) freq[ch - 'a']++;
        for (char ch : t) freq[ch - 'a']--;

        bool check = true;
        for (int f : freq) check = check && (f == 0);

        return check;

        // Complexity analysis 
        // Time : O(N+M+26) 
        // Space : O(26) 
    }
};

void p5() {
    // Problem 5 : Leetcode 242. Valid Anagram - https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/anagram-1587115620/1

    cout << Problem5().isAnagram("random", "mondar") << endl;
    cout << Problem5().isAnagram("random", "mondor") << endl;
}


int main() {
    // Day 13 of January 2025 

    p1();

    p2();

    p3();

    p4();

    p5();


    return 0;
}