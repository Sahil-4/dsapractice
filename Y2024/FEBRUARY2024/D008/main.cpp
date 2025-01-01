#include <iostream>
#include <vector>
#include <stack>

using namespace std;

vector<long long> nextLargerElement(vector<long long> arr, int n) {
    // Your code here
    int l = n - 1; // last index of given array 
    vector<long long> ans; // array to store answer 
    stack<long long> stk;

    for (int i = l; i >= 0; i--) {
        if (stk.empty()) {
            stk.push(arr[i]);
            ans.push_back(-1);
            continue;
        }

        if (arr[i] < stk.top()) {
            ans.push_back(stk.top());
            stk.push(arr[i]);
        } else {
            while (!stk.empty()) {
                if (arr[i] < stk.top()) break;
                stk.pop();
            }

            if (stk.empty()) ans.push_back(-1);
            else ans.push_back(stk.top());
            stk.push(arr[i]);
        }
    }

    // reverse the array 
    for (int i = 0; i < ans.size()/2; i++) {
        long long temp = ans[i];
        ans[i] = ans[ans.size() - 1 - i];
        ans[ans.size() - 1 - i] = temp;
    }

    return ans;
}

void p1() {
    // Problem 1 : NGE - https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1 

    // using stacks 

    // vector<long long> arr = {6, 8, 0, 1, 3};
    vector<long long> arr = { 11345835571, 16031708126, 19102954416, 18091714480, 12925897971, 
                                                21144197529, 30055749465, 11717150235, 19765593085, 4438987805, 
                                                19711278440, 19744854766, 20216898408, 14469421428, 16357595996 };
    int n = arr.size();

    vector<long long> nges = nextLargerElement(arr, n);

    cout << endl << "elements " << endl;
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl << "nges " << endl;
    for (int i = 0; i < nges.size(); i++) {
        cout << nges[i] << " ";
    }
}

int main() {
    // Day 008 

    p1();


    return 0;
}
