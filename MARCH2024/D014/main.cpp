#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> generate(int numRows) {
    if (numRows == 0) return { };

    vector<vector<int>> pascal;

    for (int i = 1; i <= numRows; i++) {
        vector<int> temp;

        for (int j = 0; j < i; j++) {
            if (j == 0 || j == i - 1) temp.push_back(1);
            else temp.push_back(pascal[i - 2][j] + pascal[i - 2][j - 1]);
        }

        pascal.push_back(temp);
    }

    return pascal;
}

void p1() {
    // Problem 1 : Pascal's triangle - https://leetcode.com/problems/pascals-triangle/ 

    vector<vector<int>> pascal = generate(5);

    for (int i = 0; i < pascal.size(); i++) {
        for (int j = 0; j < pascal[i].size(); j++) {
            cout << pascal[i][j] << " ";
        }
        cout << endl;
    }

}


int main() {
    // Day 14 

    p1();


    return 0;
}