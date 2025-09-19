#include <bits/stdc++.h>

using namespace std;

class Spreadsheet {
private:
  int T = 0;
  int INITIAL_VALUE = 0;
  unordered_map<string, int> sheet;

  int resolve(string str) {
    if (str[0] >= 'A' && str[0] <= 'Z') {
      // cell reference
      return getCell(str);
    } else {
      // non neg integer
      return stoi(str);
    }
  }

public:
  Spreadsheet(int rows) { this->T = rows; }

  void setCell(string cell, int value) { this->sheet[cell] = value; }

  void resetCell(string cell) { setCell(cell, INITIAL_VALUE); }

  int getCell(string cell) {
    if (this->sheet.find(cell) != this->sheet.end()) {
      return this->sheet[cell];
    }
    return 0;
  }

  int getValue(string formula) {
    // index of operator '+'
    int mid = formula.find('+');

    // left and right operand
    string left = formula.substr(1, mid - 1);
    string right = formula.substr(mid + 1);

    // resolve value of ref value
    int X = resolve(left);
    int Y = resolve(right);

    // return sum
    return X + Y;
  }
};

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet* obj = new Spreadsheet(rows);
 * obj->setCell(cell,value);
 * obj->resetCell(cell);
 * int param_3 = obj->getValue(formula);
 */

void p1() {
  // Problem 1 : POTD Leetcode 3484. Design Spreadsheet - https://leetcode.com/problems/design-spreadsheet/description/?envType=daily-question&envId=2025-09-19

  Spreadsheet* sheet = new Spreadsheet(3);
  cout << sheet->getCell("=5+7") << endl;
  sheet->setCell("A1", 10);
  cout << sheet->getCell("=A1+6") << endl;
  sheet->setCell("B2", 15);
  cout << sheet->getCell("=A1+B2") << endl;
  sheet->resetCell("A1");
  cout << sheet->getCell("=A1+B2") << endl;
  cout << sheet->getCell("=A3+B3") << endl;
}

class Solution2 {
public:
  int minParentheses(string& s) {
    // code here
    int count = 0;   // number of insertions needed for unmatched ')'
    int balance = 0; // current open '(' waiting to be closed

    for (char& ch : s) {
      // update balance between '(', ')'
      balance += (ch == '(') ? 1 : -1;

      if (balance < 0) {
        count++; // need to add extra '('
        balance++;
      }
    }

    //  + balance, possible that remaing are '('
    return count + balance;

    // Complexity analysis
    // Time : O(N)
    // Space : O(1)
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Min Add to Make Parentheses Valid - https://www.geeksforgeeks.org/problems/min-add-to-make-parentheses-valid/1

  vector<string> testcases = {
      "(()(", ")))", ")()()", "(((", "()()()",
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << "INPUT: " << tc << endl;
    cout << "OUTPUT: " << s2->minParentheses(tc) << endl << endl;
  }
}

int main() {
  // Day 19 of September 2025

  p1();

  p2();

  return 0;
}
