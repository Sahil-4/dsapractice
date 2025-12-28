#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    vector<int> solve1(string s, vector<string>& words) {
        // if string length is smaller then the permutation string
        if (s.length() < words.size() * words[0].length()) return {};

        // we will store starting index of a substring and match = 1, not match = -1
        unordered_map<int, int> memory;

        // map to store freq of each word in words[]
        unordered_map<string, int> freq, copyMap;
        for (string word : words) freq[word]++;

        int N = words.size();
        int M = s.length();
        int wordLen = words[0].length();
        int windowLen = wordLen * N;

        vector<int> indices;
        // start position - words in s can be of different length
        for (int starti = 0; starti < wordLen; starti++) {
            int i = starti;

            // check each word in s
            do {
                copyMap = freq;   // copy kar lo map ko
                bool flag = true; // say that there is an answer at i

                // sabhi words ko find karne ki kosis
                for (int it = 0; it < N; it++) {
                    // ith word se it times next word ko pakdo
                    string subWord = s.substr(i + (it * wordLen), wordLen);

                    if (copyMap.find(subWord) == copyMap.end() ||
                        copyMap[subWord] == 0) {
                        flag = false;
                        break;
                    }
                    copyMap[subWord]--;
                }

                // add i as answer
                if (flag) indices.push_back(i);

                // update i - point to next word - shifting window to next word
                i += wordLen;
            } while (i + windowLen - 1 < M);
        }

        return indices;

        // Complexity analysis 
        // Time : O(M * N) ~ (substring operation will be adding 
        // + map operations take constant time) 
        // Space : O(2N) two copies of map of words with freq 
    }

    bool checkSubstring(unordered_map<string, int> wordCount, string s, int wordLen) {
        for (int j = 0; j < s.length(); j += wordLen) {
            string w = s.substr(j, wordLen);
            if (wordCount.find(w) != wordCount.end()) {
                if (--wordCount[w] == -1) return false;
            }
            else return false;
        }
        return true;
    }

    vector<int> solve2(string s, vector<string>& words) {
        vector<int> indices;

        int N = words.size();
        int M = s.length();
        int wordLen = words[0].length();
        int windowLen = wordLen * N;

        unordered_map<string, int> wordCount;
        for (int i = 0; i < N; i++) {
            wordCount[words[i]]++;
        }

        int i = 0;
        while (i + windowLen <= M) {
            if (checkSubstring(wordCount, s.substr(i, windowLen), wordLen)) {
                indices.push_back(i);
            }
            i++;
        }

        return indices;

        // Complexity analysis 
        // Time : O(M * M) ~ 
        // Space : O(N) 
    }

public:
    vector<int> findSubstring(string s, vector<string>& words) {
        // return solve1(s, words);

        return solve2(s, words);
    }
};


void p1() {
    // Problem 1 : Leetcode 30. Substring with Concatenation of All Words - https://leetcode.com/problems/substring-with-concatenation-of-all-words/?envType=study-plan-v2&envId=top-interview-150 

    string s = "foobarbazfoobazbar";
    vector<string> words = { "foo","bar","baz" };

    vector<int>  out = Problem1().findSubstring(s, words);
}

class Problem2 {
    static const int BOUND = 53;

    int getIndex(char ch) {
        if (ch >= 'A' && ch <= 'Z') return (ch - 'A');
        if (ch >= 'a' && ch <= 'z') return (ch - 'a' + 26);
        return 52;
    }

public:
    string minWindow(string s, string t) {
        // for output 
        int mwl = 0; // length of min window 
        int mwi = -1; // start of min window - to get the substring 

        // frequency of each char in t 
        int tmap[BOUND] = { 0 };
        int tchars = 0; // count of unique chars 
        for (char ch : t) {
            tmap[getIndex(ch)]++;
            if (tmap[getIndex(ch)] == 1) tchars++;
        }

        // frequency of each char in s 
        for (int l = 0, r = 0; r < s.size(); r++) {
            tmap[getIndex(s[r])]--;
            if (tmap[getIndex(s[r])] == 0) tchars--;

            while (tchars == 0) {
                if (mwl == 0 || mwl > r - l + 1) {
                    mwi = l, mwl = r - l + 1;
                }

                tmap[getIndex(s[l])]++;
                if (tmap[getIndex(s[l])] == 1) tchars++;
                l++;
            }
        }

        if (mwl == 0) return "";
        return s.substr(mwi, mwl);

        // Complexity analysis 
        // Time : O(tn + 2sn) 
        // Space : O(52) map will store frequency of each char 
    }
};

void p2() {
    // Problem 2 : Leetcode 76. Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/?envType=study-plan-v2&envId=top-interview-150 

    cout << Problem2().minWindow("abaabcddddffedef", "abcddffe") << endl;
}

class Problem3 {

public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // validate all rows 
        for (int r = 0; r < 9; r++) {
            int freq[10] = { 0 }; // freq of e 1 to 9 
            for (int ci = 0; ci < 9; ci++) {
                if (board[r][ci] == '.') continue;

                int idx = board[r][ci] - '0';
                freq[idx]++;
                if (freq[idx] > 1) return false;
            }
        }

        // validate all cols 
        for (int c = 0; c < 9; c++) {
            int freq[10] = { 0 }; // freq of e 1 to 9 
            for (int ri = 0; ri < 9; ri++) {
                if (board[ri][c] == '.') continue;
                int idx = board[ri][c] - '0';
                freq[idx]++;
                if (freq[idx] > 1) return false;
            }
        }

        // validate each sub grid 
        for (int ri = 0; ri < 9; ri += 3) {
            for (int ci = 0; ci < 9; ci += 3) {
                int freq[10] = { 0 }; // freq of e 1 to 9 
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        int r = i + ri, c = j + ci;
                        if (board[r][c] == '.') continue;
                        int idx = board[r][c] - '0';
                        freq[idx]++;
                        if (freq[idx] > 1) return false;
                    }
                }
            }
        }

        // if everything pass 
        return true;

        // Complexity analysis 
        // Time : O(3 * 9 * 9) 
        // Space : O(10) freq array 
    }
};

void p3() {
    // Problem 3 : Leetcode 36. Valid Sudoku - https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/is-sudoku-valid4820/1 

    vector<vector<char>> board = {
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}
    };
    cout << Problem3().isValidSudoku(board) << endl;
}


int main() {
    // Day 11 of January 2025 

    p1();

    p2();

    p3();


    return 0;
}