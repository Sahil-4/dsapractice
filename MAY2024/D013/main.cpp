#include <iostream>
#include <stack>
#include <string>
#include <vector>
#include <map>

using namespace std;

string postToInfix(string postfixExpression) {
    // postfixExpression = "ab+ef/*" 
    // infix = "((a + b) * (e / f)) "

    stack<string> stk;

    for (int i = 0; i < postfixExpression.length(); i++) {
        if (postfixExpression[i] >= 'a' && postfixExpression[i] <= 'z' || 
        postfixExpression[i] >= 'A' && postfixExpression[i] <= 'Z' || 
        postfixExpression[i] >= '0' && postfixExpression[i] <= '9') {
            // an operand 
            stk.push(string(1, postfixExpression[i]));
        } else {
            // an operator 
            string oprnd2 = stk.top(); stk.pop();
            string oprnd1 = stk.top(); stk.pop();
            string newExpression = "(" + oprnd1 + postfixExpression[i] + oprnd2 + ")";
            stk.push(newExpression);
        }
    }

    return stk.top();
}

string preToInfix(string pre_exp) {
    stack<string> stk;

    for (int i = pre_exp.length() - 1; i >= 0; i--) {
        if (pre_exp[i] >= 'a' && pre_exp[i] <= 'z' || 
        pre_exp[i] >= 'A' && pre_exp[i] <= 'Z' || 
        pre_exp[i] >= '0' && pre_exp[i] <= '9') {
            // an operand 
            stk.push(string(1, pre_exp[i]));
        } else {
            // an operator 
            string oprnd1 = stk.top(); stk.pop();
            string oprnd2 = stk.top(); stk.pop();
            string newExpression = "(" + oprnd1 + pre_exp[i] + oprnd2 + ")";
            stk.push(newExpression);
        }
    }

    return stk.top();
}

void p1() {
    // Problem 1 : Geeksforgeeks - Prefix to Infix Conversion - https://www.geeksforgeeks.org/problems/prefix-to-infix-conversion/1 

    string prefixExpression = "*-A/BC-/AKL";
    string infixExpression = preToInfix(prefixExpression);
    cout << "prefixExpression :: " << prefixExpression << endl;
    cout << "infixExpression :: " << infixExpression << endl;
}

vector<int> nextGreaterElement_solution1(vector<int>& nums1, vector<int>& nums2) {
    vector<int> ans(nums1.size());

    for (int it = 0; it < nums1.size(); it++) {
        int indexOfNumsIT = nums2.size();
        ans[it] = -1;

        for (int it2 = 0; it2 < nums2.size(); it2++) {
            if (nums2[it2] == nums1[it]) {
                indexOfNumsIT = it2;
                break;
            }
        }

        for (int it2 = indexOfNumsIT + 1; it2 < nums2.size(); it2++) {
            if (nums1[it] < nums2[it2]) {
                ans[it] = nums2[it2];
                break;
            }
        }
    }

    return ans;
}

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    vector<int> ans;
    stack<int> stk;
    map<int, int> ngeIndexTable;

    ngeIndexTable.insert({nums2[nums2.size() - 1], -1});
    stk.push(nums2[nums2.size() - 1]);

    for (int it = nums2.size() - 2; it >= 0; it--) {
        if (nums2[it] < nums2[it + 1]) {
            ngeIndexTable.insert({nums2[it], nums2[it + 1]});
        } else {
            while (!stk.empty() && stk.top() < nums2[it]) stk.pop();

            if (stk.empty()) ngeIndexTable.insert({nums2[it], -1});
            else ngeIndexTable.insert({nums2[it], stk.top()});
        }

        if (stk.empty() || nums2[it] < stk.top()) stk.push(nums2[it]);
    }

    for (int it = 0; it < nums1.size(); it++) {
        ans.push_back(ngeIndexTable[nums1[it]]);
    }

    return ans;
}

void p2() {
    // Problem 2 : Leetcode 496. Next Greater Element I - https://leetcode.com/problems/next-greater-element-i/ 

    vector<int> nums1 = {2,4};
    vector<int> nums2 = {1,4,2,6,8,3,12,16};

    vector<int> ans = nextGreaterElement(nums1, nums2);
    for (int i = 0; i < ans.size(); i++) cout << ans[i] << endl;
}

int main() {
    // Day 13 

    p1();

    p2();


    return 0;
}