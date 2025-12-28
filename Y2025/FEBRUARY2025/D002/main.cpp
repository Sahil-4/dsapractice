#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    void permutation(vector<int>& nums, int i, vector<vector<int>>& res) {
        if (i == nums.size()) {
            res.push_back(nums);
            return;
        }

        for (int ii = i; ii < nums.size(); ii++) {
            swap(nums[ii], nums[i]);
            permutation(nums, i + 1, res);
            swap(nums[ii], nums[i]);
        }
    }

public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;

        permutation(nums, 0, res);

        return res;

        // Complexity analysis 
        // Time : O(N^N) ~ 
        // Space : O(N) stack 
    }
};

void p1() {
    // Problem 1 : Leetcode 46. Permutations - https://leetcode.com/problems/permutations/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1 

    vector<int> nums = { 1, 2, 3 };
    vector<vector<int>> out = Problem1().permute(nums);
    for (vector<int> p : out) {
        for (int e : p) cout << e << " ";
        cout << endl;
    }
}

class Problem2 {
    void comsum(vector<int>& candidates, int i, vector<int>& com, int sum, int target, vector<vector<int>>& res) {
        if (i == candidates.size() || sum >= target) {
            if (sum == target) res.push_back(com);
            return;
        }

        // not pick 
        comsum(candidates, i + 1, com, sum, target, res);

        // pick - only if we can take it 
        if (target - sum >= candidates[i]) {
            com.push_back(candidates[i]); sum += candidates[i];
            comsum(candidates, i, com, sum, target, res);
            com.pop_back(); sum -= candidates[i];
        }
    }

public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;

        vector<int> com;
        int sum = 0;
        comsum(candidates, 0, com, sum, target, res);

        return res;

        // Complexity analysis 
        // Time : O(2^(N|target)) ~ 
        // Space : O(N | target) stack ~ 
    }
};

void p2() {
    // Problem 2 : Leetcode 39. Combination Sum - https://leetcode.com/problems/combination-sum/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/combination-sum-1587115620/1 

    vector<int> candidates = { 2, 3, 4, 5, 6, 7 };
    int target = 12;
    vector<vector<int>> res = Problem2().combinationSum(candidates, target);
    for (vector<int> p : res) {
        for (int e : p) cout << e << " ";
        cout << endl;
    }
}

class Problem3 {
    bool canIPlace(vector<vector<int>>& chessBoard, int N, int r, int c) {
        // check this entire row
        for (int ci = 0; ci < N; ci++) {
            if (chessBoard[r][ci] == 1) return false;
        }

        // check this entire col
        for (int ri = 0; ri < N; ri++) {
            if (chessBoard[ri][c] == 1) return false;
        }

        // check diagnols curr to top-left
        for (int ri = r, ci = c; ri >= 0 && ci >= 0; ri--, ci--) {
            if (chessBoard[ri][ci] == 1) return false;
        }

        // check diagnols curr to bottom-right
        for (int ri = r, ci = c; ri < N && ci < N; ri++, ci++) {
            if (chessBoard[ri][ci] == 1) return false;
        }

        // check diagnols curr to top-right
        for (int ri = r, ci = c; ri >= 0 && ci < N; ri--, ci++) {
            if (chessBoard[ri][ci] == 1) return false;
        }

        // check diagnols curr to bottom-left
        for (int ri = r, ci = c; ri < N && ci >= 0; ri++, ci--) {
            if (chessBoard[ri][ci] == 1) return false;
        }

        return true;
    }

    void placeQueens(int i, int N, vector<vector<int>>& chessBoard, vector<vector<int>>& out) {
        if (i == N) {
            vector<int> oout;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (chessBoard[i][j] == 1) {
                        oout.push_back(j + 1);
                    }
                }
            }
            out.push_back(oout);
            return;
        }

        for (int c = 0; c < N; c++) {
            if (!canIPlace(chessBoard, N, i, c)) continue;

            chessBoard[i][c] = 1;
            placeQueens(i + 1, N, chessBoard, out);
            chessBoard[i][c] = 0;
        }
    }

    void placeQueens(int i, int N, vector<vector<int>>& chessBoard, int& count) {
        if (i == N) {
            count++;
            return;
        }

        for (int c = 0; c < N; c++) {
            if (!canIPlace(chessBoard, N, i, c)) continue;

            chessBoard[i][c] = 1;
            placeQueens(i + 1, N, chessBoard, count);
            chessBoard[i][c] = 0;
        }
    }

public:
    int totalNQueens(int N) {
        vector<vector<int>> chessBoard(N, vector<int>(N, 0));

        int count = 0;
        vector<vector<int>> out;

        placeQueens(0, N, chessBoard, count);
        // placeQueens(0, N, chessBoard, out);

        return count;

        // Complexity analysis 
        // Time : O(N * N) 
        // Space : O(N) stack + O(N*N) board 
    }
};

void p3() {
    // Problem 3 : Leetcode 52. N-Queens II - https://leetcode.com/problems/n-queens-ii/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/n-queen-problem0315/1 

    cout << Problem3().totalNQueens(1) << endl;
    cout << Problem3().totalNQueens(3) << endl;
    cout << Problem3().totalNQueens(5) << endl;
    cout << Problem3().totalNQueens(9) << endl;
}


int main() {
    // Day 2 of February 2025 

    p1();

    p2();

    p3();


    return 0;
}