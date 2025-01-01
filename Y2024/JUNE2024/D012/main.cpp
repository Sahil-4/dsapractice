#include <iostream>
#include <vector>

using namespace std;

void traverseLToR(vector<int> &ans, vector<vector<int>>& matrix, int ri, int ci, int rl, int cl) {
    for (ci; ci <= cl; ci++) {
        ans.push_back(matrix[ri][ci]);
    }
}

void traverseTToB(vector<int> &ans, vector<vector<int>>& matrix, int ri, int ci, int rl, int cl) {
    for (ri; ri <= rl; ri++) {
        ans.push_back(matrix[ri][cl]);
    }
}

void traverseRToL(vector<int> &ans, vector<vector<int>>& matrix, int ri, int ci, int rl, int cl) {
    for (cl; cl >= ci; cl--) {
        ans.push_back(matrix[rl][cl]);
    }
}

void traverseBToT(vector<int> &ans, vector<vector<int>>& matrix, int ri, int ci, int rl, int cl) {
    for (rl; rl >= ri; rl--) {
        ans.push_back(matrix[rl][ci]);
    }
}

vector<int> spiralOrder(vector<vector<int>>& matrix) {
    // store answer 
    vector<int> ans;

    // boundaries 
    int ri = 0, ci = 0;
    int rl = matrix.size() - 1, cl = matrix[0].size() - 1;

    while (ri <= rl && ci <= cl) {
        traverseLToR(ans, matrix, ri, ci, rl, cl);
        ri++;
        traverseTToB(ans, matrix, ri, ci, rl, cl);
        cl--;
        if (ri > rl || ci > cl) break;
        traverseRToL(ans, matrix, ri, ci, rl, cl);
        rl--;
        traverseBToT(ans, matrix, ri, ci, rl, cl);
        ci++;
    }

    return ans;
}

void p1() {
    // Problem 1 : Leetcode 54. Spiral Matrix - https://leetcode.com/problems/spiral-matrix/ 

    vector<vector<int>> matrix = {{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15}};
    vector<int> ans = spiralOrder(matrix);
}

int findK(vector<vector<int>> &matrix, int n, int m, int k) {
    // Your code goes here
    vector<int> ans = spiralOrder(matrix);
    return ans[k - 1];
}

void p2() {
    // Problem 2 : GeeksForGeeks Spiral Matrix - https://www.geeksforgeeks.org/problems/spiral-matrix--141631/1 

    vector<vector<int>> matrix = {{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15}};
    int k = 8;
    int ans = findK(matrix, matrix.size(), matrix[0].size(), k);
}

int main() {
    // Day 12 

    p1();

    p2();


    return 0;
}