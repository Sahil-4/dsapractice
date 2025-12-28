#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    void traverseF(vector<vector<int>>& matrix, int ri, int ci, int rn, int cn, vector<int>& out) {
        for (int i = ri; i <= rn; i++) {
            for (int j = ci; j <= cn; j++) {
                out.push_back(matrix[i][j]);
            }
        }
    }

    void traverseR(vector<vector<int>>& matrix, int ri, int ci, int rn, int cn, vector<int>& out) {
        for (int i = ri; i >= rn; i--) {
            for (int j = ci; j >= cn; j--) {
                out.push_back(matrix[i][j]);
            }
        }
    }

public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> out;

        // go step by step 

        int r = 0, rn = matrix.size() - 1;
        int c = 0, cn = matrix[0].size() - 1;

        while (r <= rn && c <= cn) {
            traverseF(matrix, r, c, r, cn, out);
            r++;
            traverseF(matrix, r, cn, rn, cn, out);
            cn--;

            if (r > rn || c > cn) break;

            traverseR(matrix, rn, cn, rn, c, out);
            rn--;
            traverseR(matrix, rn, c, r, c, out);
            c++;
        }

        return out;

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(1) 
    }
};

void p1() {
    // Problem 1 : Leetcode 54. Spiral Matrix - https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/spiral-matrix--141631/0 

    vector<vector<int>> matrix = { {1,2,3,4,5,6,7,8},{9,10,11,12,13,14,15,16} };
    vector<int> out = Problem1().spiralOrder(matrix);
    for (int e : out) cout << e << " ";
    cout << endl;
}

class Problem2 {
public:
    void rotate(vector<vector<int>>& matrix) {
        int N = matrix.size();

        // swap [i][j] and [j][i] 
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }

        // then reverse each row - for clock wise 
        for (int i = 0; i < N; i++) {
            int l = 0, r = N - 1;
            while (l < r) {
                swap(matrix[i][l], matrix[i][r]);
                l++, r--;
            }
        }

        // or reverse each col - for anti clock wise 
        // for (int i = 0; i < N; i++) {
        //     int l = 0, r = N-1;
        //     while (l < r) {
        //         swap(matrix[l][i], matrix[r][i]);
        //         l++, r--;
        //     }
        // }

        // Complexity analysis 
        // Time : O(2*N*N) 
        // Space : O(1) 
    }
};


void p2() {
    // Problem 2 : Leetcode 48. Rotate Image - https://leetcode.com/problems/rotate-image/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/rotate-by-90-degree0356/0 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/0 

    vector<vector<int>> matrix = { {1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16} };

    Problem2().rotate(matrix);

    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix.size(); j++) {
            cout << matrix[i][j] << " ";
        } cout << endl;
    }
}

class Problem3 {
    void solve1(vector<vector<int>>& matrix) {
        int N = matrix.size(), M = matrix[0].size();

        set<int> rows; // rows containing zero 
        set<int> cols; // cols containing zero 

        // find rows and cols which having zero 
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (matrix[i][j] == 0) {
                    rows.insert(i);
                    cols.insert(j);
                }
            }
        }

        // pick each row one by one and make all e zero in that row 
        for (int r : rows) {
            for (int c = 0; c < M; c++) matrix[r][c] = 0;
        }
        for (int c : cols) {
            for (int r = 0; r < N; r++) matrix[r][c] = 0;
        }

        // Complexity analysis 
        // Time : O(3*N*M) 
        // Space : O(N+M) 
    }

    void solve2(vector<vector<int>>& matrix) {
        int N = matrix.size(), M = matrix[0].size();

        bool r0 = false, c0 = false;

        // find zeroes and mark row and col 
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (matrix[i][j] == 0) {
                    if (i == 0) r0 = true;
                    if (j == 0) c0 = true;
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }

        // traverse matrix - if row0 or col0 ontains zero then mark [i][j] also 0 
        for (int i = 1; i < N; i++) {
            for (int j = 1; j < M; j++) {
                if (matrix[0][j] == 0 || matrix[i][0] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        // for row0 if row0 contains zero make all cols zero 
        for (int c = 0; c < M && r0; c++) matrix[0][c] = 0;

        // for col0 if col0 contains zero make all cols zero 
        for (int r = 0; r < N && c0; r++) matrix[r][0] = 0;

        // Complexity analysis 
        // Time : O(2 * N*M) 
        // Space : O(1) 
    }

public:
    void setZeroes(vector<vector<int>>& matrix) {
        // solve1(matrix);

        solve2(matrix);
    }
};

void p3() {
    // Problem 3 : Leetcode 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/set-matrix-zeroes/0 

    vector<vector<int>> matrix = { {1,2,3,4},{5,6,7,0},{9,10,0,12},{13,14,15,16} };

    Problem3().setZeroes(matrix);

    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix.size(); j++) {
            cout << matrix[i][j] << " ";
        } cout << endl;
    }
}


int main() {
    // Day 12 of January 2025 

    p1();

    p2();

    p3();


    return 0;
}