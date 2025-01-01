#include <iostream>
#include <vector>

using namespace std;

vector<int> spiralOrder(vector<vector<int>>& vc) {
    vector<int> ans;
    int top = 0, right = vc[0].size() - 1, left = 0, bottom = vc.size() - 1;

    while (top <= bottom && left <= right) {
        for (int i = left; i <= right; i++) {
            ans.push_back(vc[top][i]);
        }
        top++;

        for (int i = top; i <= bottom; i++) {
            ans.push_back(vc[i][right]);
        }
        right--;

        if (top <= bottom) {
            for (int i = right; i >= left; i--) {
                ans.push_back(vc[bottom][i]);
            }
            bottom--;
        }

        if (left <= right) {
            for (int i = bottom; i >= top; i--) {
                ans.push_back(vc[i][left]);
            }
            left++;
        }
    }


    return ans;
}

void p1() {
    // P1 Spiral matrix - https://leetcode.com/problems/spiral-matrix/description/ 

    // vector<vector<int>> matrix = {{1,2,3},{4,5,6},{7,8,9}};
    // vector<vector<int>> matrix = {{1,2,3,4},{5,6,7,8},{9,10,11,12}};
    // vector<vector<int>> matrix = {{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};
    vector<vector<int>> matrix = {{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16},{17,18,19,20}};

    vector<int> ans = spiralOrder(matrix);

    for (int i = 0; i < ans.size(); i++) cout << ans[i] << " ";
    cout << endl;
}

int main() {
    // Day 12 

    p1();

    // Learning : Observation is the key to solve any DSA question 


    return 0;
}