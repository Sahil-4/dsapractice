#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    void generateValidParenthesis(int i, string& parens, int count, vector<string>& out) {
        if ((i == 0) || (count < 0)) {
            if (count == 0) out.push_back(parens);
            return;
        }

        parens.push_back('(');
        generateValidParenthesis(i - 1, parens, count + 1, out);
        parens.pop_back();
        parens.push_back(')');
        generateValidParenthesis(i - 1, parens, count - 1, out);
        parens.pop_back();
    }

public:
    vector<string> generateParenthesis(int n) {
        vector<string> out;

        string paren = "";
        generateValidParenthesis(2 * n, paren, 0, out);

        return out;

        // Complexity analysis 
        // Time : O(2^N) 
        // Space : O(N) stack + O(N) parens string 
    }
};

void p1() {
    // Problem 1 : Leetcode 22. Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/generate-all-possible-parentheses/1 

    vector<string> res = Problem1().generateParenthesis(5);
    for (string s : res) cout << s << endl;
}

class Problem2 {
    static const char MARK = '$';

    // top, right, bottom, left 
    int D = 4;
    int DArr[4][2] = { {-1, 0}, {0, +1}, {+1, 0}, {0, -1} };

    bool isValidIndex(int r, int c, int M, int N) {
        if (r < 0 || r >= M) return false;
        if (c < 0 || c >= N) return false;
        return true;
    }

    bool dfs(vector<vector<char>>& board, int r, int c, string& word, int i) {
        if (i == word.length()) return true;
        if (r < 0 || r >= board.size()) return false;
        if (c < 0 || c >= board[0].size()) return false;
        if (board[r][c] != word[i]) return false;

        bool check = false;

        char temp = board[r][c];
        board[r][c] = MARK;

        for (int k = 0; k < D; k++) {
            int nr = r + DArr[k][0], nc = c + DArr[k][1];
            check = check || dfs(board, nr, nc, word, i + 1);
        }

        board[r][c] = temp;

        return check;
    }

public:
    bool exist(vector<vector<char>>& board, string word) {
        int M = board.size(), N = board[0].size();

        for (int r = 0; r < M; r++) {
            for (int c = 0; c < N; c++) {
                if (board[r][c] != word[0]) continue;

                bool check = dfs(board, r, c, word, 0);
                if (check) return true;
            }
        }

        return false;

        // Complexity analysis 
        // Time : O(4^word_len) 
        // Space : O(word_len) stack 
    }
};

void p2() {
    // Problem 2 : Leetcode 79. Word Search - https://leetcode.com/problems/word-search/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/word-search/1 

    vector<vector<char>> board = { {'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'} };
    cout << Problem2().exist(board, "ASA") << endl;
    cout << Problem2().exist(board, "DEE") << endl;
}


int main() {
    // Day 3 of February 

    p1();

    p2();


    return 0;
}