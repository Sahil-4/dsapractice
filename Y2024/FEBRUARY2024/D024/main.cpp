#include <iostream>
#include <vector>

using namespace std;

vector<long long> nthRowOfPascalTriangle(int row);

void p3() {
    // Problem 3 : given n print the pascal's triangle till n row 

    // we can use same algo of p2 
    // and add a loop for changing row 

    int n = 7;

    vector<vector<long long>> ans;
    for (int row_number = 0; row_number < n; row_number++) {
        vector<long long> temp = nthRowOfPascalTriangle(row_number);
        ans.push_back(temp);
    }

    for (int i = 0; i < ans.size(); i++) {
        for (int j = 0; j < ans[i].size(); j++) {
            cout << ans[i][j] << " ";
        }
        cout << endl;
    }
}

vector<long long> nthRowOfPascalTriangle(int row) {
    // code here 
    vector<long long> ans;
    long long val = 1;

    for (int col_number = 0; col_number < row; col_number++) {
        if (col_number == 0 || col_number == row - 1) {
            ans.push_back(1);
        } else {
            val = val * (row - col_number) / col_number;
            ans.push_back(val);
        }
    }

    return ans;
}

void p2() {
    // Problem 2 Pascals triangle - https://www.geeksforgeeks.org/problems/pascal-triangle0652/1 

    // given row number r 
    // print this row of pascal's triangle 
    // assumptions 
    // - rth row must have r elements 
    // means a loop from 1 to <= r 
    // - first and last or 0th or (r-1)th element will be 1 
    // means we can save two calculations 
    // we can use the nCr formula here 
    // but it will give us time complexity of O(col * r) 
    // Optimization 
    // second element will be row - 1 
    // that we can say (row - 1) / 2 - 1 
    // third element will be [(row - 1) / 2 - 1] * [(row - 2) / 3 - 1] 
    // and so on 
    // by here we can say that if we know prev element we can easily get current element 
    // by multiplying it (row - c) / c 
    // c is column having 0 based indexes 
    // 0 based indexing for denominator in second : 2 - 1, third : 3 - 1

    // int row = 8;
    int row = 142;
    vector<long long> ans = nthRowOfPascalTriangle(row);

    for (int i = 0; i < ans.size(); i++) {
        // cout << ans[i] << " ";
    }
    cout << endl;
}

void p1() {
    // Problem 1 : given row, col print the value present at it in pascal's triangle 

    // we can do this using nCr 
    // n = row - 1, r = col - 1 
    // (row - 1)C(col-1) 
    // rCc = r! / (c! * (r - c)!)
    // but it will give us time complexity of O(row) + O(col) + O(row - col) 
    // we can optimise this by doing some observation on pascal's triangle 
    // r! = x * .. * (r - c)! 
    // and we can cancel (r - c)! by denominator 
    // by this we can say that to canculate rCc 
    // we can do this r/c * ((r-1) / (c-1)) * ((r-2) / (c-2)) * ... * ((r-c) / 1) 
    // by this time complexity will be O(col) 

    // int row = 3, col = 2;
    int row = 5, col = 3;
    long long val = 1;
    
    // nCr logic 
    row -= 1;
    col -= 1;

    // optimal nCr logic 
    for (int c_index = 0; c_index < col; c_index++) {
        val = val * (row - c_index);
        val = val / (c_index + 1);
    }

    cout << val << endl;
}

int main() {
    // Day 24 

    // p1();

    // p2();

    // p3();


    return 0;
}