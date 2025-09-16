#include <bits/stdc++.h>

using namespace std;

class Solution1 {
private:
  int gcd(int a, int b) {
    if (a < b) return gcd(b, a);
    if (b == 0) return a;
    return gcd(b, a % b);
  }

  int lcm(int a, int b) {
    return (((long long)a * (long long)b) / (long long)gcd(a, b));
  }

  bool nonCoPrime(int a, int b) {
    return gcd(a, b) > 1;
  }

public:
  vector<int> replaceNonCoprimes(vector<int>& nums) {
    // simulate whatever is given in problem statement
    // keep a stack-like list (answer)
    // for each num in nums,
    // compare num with the last element in answer.
    // if they are coprime, keep both
    // else, pop the last element and replace the current number with the LCM of both
    // repeat this merging until
    // the last element and the current one become coprime (or stack is empty)
    // at the end, 
    // the stack contains the final sequence
    // where all adjacent numbers are coprime
    // this is our output

    vector<int> answer;

    for (int i = 0; i < nums.size(); i++) {
      int curr = nums[i];
      bool flag = true;

      while (flag) {
        int prev = answer.size() ? answer.back() : -1;

        if (prev < 0 || !nonCoPrime(prev, curr)) {
          answer.push_back(curr);
          flag = false;
        } else {
          answer.pop_back();
          curr = lcm(prev, curr);
        }
      }
    }

    return answer;

    // Complexity analysis 
    // Time : O(2N * Log(num)) 
    // Space : O(1) 
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 2197. Replace Non-Coprime Numbers in Array - https://leetcode.com/problems/replace-non-coprime-numbers-in-array/description/?envType=daily-question&envId=2025-09-16 

  vector<vector<int>> testcases = {
    { 6, 4, 3, 2, 7, 6, 2 },
    { 2, 2, 1, 1, 3, 3, 3 },
    { 15, 16, 17, 13, 1418, 5, 61, 3, 4, 211, 12, 17, 8, 9, 10, 9, 20 },
    { 31, 97561, 97561, 97561,  97561,  97561,  97561,  97561,  97561 },
  };

  Solution1* s1 = new Solution1();
  for (auto& tc : testcases) {
    cout << "INPUT: ";
    for (auto& e : tc) cout << e << " ";
    cout << endl;
    vector<int> answer = s1->replaceNonCoprimes(tc);
    cout << "OUTPUT: ";
    for (auto& e : answer) cout << e << " ";
    cout << endl;
    cout << endl;
  }
}

class Solution2 {
private:
  bool isOperator(string s) {
    return (s == "+" || s == "-" || s == "*" || s == "/" || s == "^");
  }

  int add(int a, int b) {
    return a + b;
  }

  int subtract(int a, int b) {
    return a - b;
  }

  int multiply(int a, int b) {
    return a * b;
  }

  int divide(int a, int b) {
    return floor((double)a / (double)b);
  }

  int power(int a, int b) {
    return pow(a, b);
  }

  string performOperation(string s1, string s2, string op) {
    int a = stoi(s1);
    int b = stoi(s2);

    int output = 0;

    if (op == "+") {
      output = add(a, b);
    } else if (op == "-") {
      output = subtract(a, b);
    } else if (op == "*") {
      output = multiply(a, b);
    } else if (op == "/") {
      output = divide(a, b);
    } else if (op == "^") {
      output = power(a, b);
    }

    return to_string(output);
  }

public:
  int evaluatePostfix(vector<string>& arr) {
    // code here
    // "2", "3", "1", "*", "+", "9", "-"
    // using stack (traverse arr from i = 0 to i < N)
    // keep(2)
    // keep(3)
    // keep(1)
    // operator(*) received take out last two
    // 3, 1
    // perform operation (3, 1, *)
    // keep(result)

    stack<string> stk;

    for (int i = 0; i < arr.size(); i++) {
      if (isOperator(arr[i])) {
        string s2 = stk.top(); stk.pop();
        string s1 = stk.top(); stk.pop();
        string res = performOperation(s1, s2, arr[i]);
        stk.push(res);
      } else {
        stk.push(arr[i]);
      }
    }

    return stoi(stk.top());

    // Complexity analysis 
    // Time : O(N * operation) 
    // Space : O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Postfix Evaluation - https://www.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1 

  vector<vector<string>> testcases = {
    { "2", "3", "1", "*", "+", "9", "-" },
    { "2", "1", "1", "*", "+", "9", "/" },
    { "2", "3", "^", "1", "+" },
    { "2", "32", "^" },
    { "1", "-6", "/" },
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << "INPUT: ";
    for (auto& e : tc) cout << e << " ";
    cout << endl;
    int value = s2->evaluatePostfix(tc);
    cout << "OUTPUT: " << value << endl << endl;
  }
}

int main() {
  // Day 16 of September 2025

  p1();

  p2();

  return 0;
}
