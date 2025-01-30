#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    vector<int> getCoords(int cell, int N) {
        int row = (N - 1) - ((cell - 1) / N);
        int col = (cell - 1) % N;
        if ((N & 1 && row & 1) || (!(N & 1) && !(row & 1))) col = (N - 1) - col;
        return { row, col };
    }

    vector<int> getCoords(int cell, int N, int M) {
        int row = N - 1 - ((cell - 1) / M);
        int col = (cell - 1) % M;
        if (row & 1) col = M - 1 - col;

        return { row, col };
    }

public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        int N = n * n;

        int steps = 0;

        vector<bool> visited(N + 1, false);
        queue<int> que;

        que.push(1);
        visited[1] = true;

        while (!que.empty()) {
            int level = que.size();

            for (int i = 0; i < level; i++) {
                int curr = que.front(); que.pop();

                if (curr == N) return steps;

                for (int k = 1; k <= 6; k++) {
                    int next = curr + k;

                    if (next > N) break;

                    if (visited[next]) continue;
                    visited[next] = true;

                    vector<int> coords = getCoords(next, n);
                    if (board[coords[0]][coords[1]] != -1) {
                        next = board[coords[0]][coords[1]];
                    }
                    que.push(next);
                }
            }
            steps++;
        }

        return -1;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(N) 
    }

    int minThrow(int NSL, int arr[]) {
        // code here 

        int N = 5, M = 6;

        // create board 
        vector<vector<int>> board(N, vector<int>(M, -1));

        // place snakes and ladders 
        for (int i = 0; i < NSL; i++) {
            int start = arr[2 * i];
            int end = arr[2 * i + 1];

            vector<int> coords = getCoords(start, N, M);
            board[coords[0]][coords[1]] = end;
        }

        return snakesAndLadders(board);
        // return -1;
    }
};

void p1() {
    // Problem 1 : Leetcode 909. Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/snake-and-ladder-problem4816/1 

    vector<vector<int>> board = { {-1,-1,-1,-1,-1,-1},{-1,-1,-1,-1,-1,-1},{-1,-1,-1,-1,-1,-1},{-1,35,-1,-1,13,-1},{-1,-1,-1,-1,-1,-1},{-1,15,-1,-1,-1,-1} };
    cout << Problem1().snakesAndLadders(board) << endl;
}

class Problem2 {
    int diff(string& a, string& b) {
        int diff = 0;

        for (int i = 0; i < 8; i++) {
            diff += (a[i] != b[i]);
        }

        return diff;
    }

public:
    int minMutation(string start, string end, vector<string>& bank) {
        int K = bank.size();

        int steps = 0;

        unordered_set<string> visited;
        queue<string> que;

        visited.insert(start);
        que.push(start);

        while (!que.empty()) {
            int N = que.size();

            for (int i = 0; i < N; i++) {
                string curr = que.front(); que.pop();

                if (curr == end) return steps;

                for (int k = 0; k < K; k++) {
                    string next = bank[k];

                    if (visited.find(next) != visited.end()) continue;
                    if (diff(curr, next) != 1) continue;

                    visited.insert(next);
                    que.push(next);
                }
            }

            steps++;
        }

        return -1;

        // Complexity analysis 
        // Time : O(8*K) 
        // Space : O(K) + O(K) 
    }
};

void p2() {
    // Problem 2 : Leetcode 433. Minimum Genetic Mutation - https://leetcode.com/problems/minimum-genetic-mutation/?envType=study-plan-v2&envId=top-interview-150 

    string start = "AACCGGTT";
    string end = "AAACGGTA";
    vector<string> bank = { "AACCGGTA","AACCGCTA","AAACGGTA" };
    cout << Problem2().minMutation(start, end, bank) << endl;
}

class Problem3 {
    int diff(string& a, string& b) {
        int diff = 0;

        for (int i = 0; i < a.length(); i++) {
            diff += a[i] != b[i];
        }

        return diff;
    }

public:
    int ladderLength(string start, string end, vector<string>& bank) {
        int K = bank.size();

        int steps = 1;

        unordered_set<string> visited;
        queue<string> que;

        visited.insert(start);
        que.push(start);

        while (!que.empty()) {
            int N = que.size();

            for (int i = 0; i < N; i++) {
                string curr = que.front(); que.pop();

                if (curr == end) return steps;

                for (int k = 0; k < K; k++) {
                    string next = bank[k];

                    if (visited.find(next) != visited.end()) continue;
                    if (diff(curr, next) != 1) continue;

                    visited.insert(next);
                    que.push(next);
                }
            }

            steps++;
        }

        return 0;

        // Complexity analysis 
        // Time : O(8*K) 
        // Space : O(K) + O(K) 
    }
};

void p3() {
    // Problem 3 : Leetcode 127. Word Ladder - https://leetcode.com/problems/word-ladder/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/word-ladder/1 

    string start = "abc";
    string end = "aaa";
    vector<string> bank = { "aba","abb","aaa" };
    cout << Problem2().minMutation(start, end, bank) << endl;
    Problem3().ladderLength(start, end, bank);
}


int main() {
    // Day 30 of January 

    p1();

    p2();

    p3();


    return 0;
}
