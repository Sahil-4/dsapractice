#include <bits/stdc++.h>

using namespace std;

class Solution1 {
public:
  string fractionToDecimal(int numerator, int denominator) {
    if (numerator == 0) return "0";

    // output string - decimal 
    string decimal = "";

    // negative answer (decimal value) 
    if ((numerator < 0) ^ (0 > denominator)) decimal += '-';

    long long lnumerator = abs((long long)numerator);
    long long ldenominator = abs((long long)denominator);

    // common factor 
    int g = gcd(lnumerator, ldenominator);
    // remove common factors from lnumerator & ldenominator 
    lnumerator = lnumerator / g;
    ldenominator = ldenominator / g;

    long long int quotient = lnumerator / ldenominator;
    long long int remainder = lnumerator % ldenominator;

    decimal += to_string(quotient);

    if (remainder != 0) {
      decimal += "."; // starting fraction part 

      // check terminating or not 
      int factor_2_5 = ldenominator;
      while (factor_2_5 % 2 == 0) factor_2_5 /= 2;
      while (factor_2_5 % 5 == 0) factor_2_5 /= 5;

      bool isTerminating = (factor_2_5 == 1);
      unordered_map<int, int> lastSeenIndex;

      // build fraction part 
      while (remainder != 0) {
        if (!isTerminating && lastSeenIndex[remainder]) {
          decimal.insert(decimal.begin() + lastSeenIndex[remainder], '(');
          decimal.push_back(')');
          break;
        }

        // save info - remainder was seen at decimal.size() 
        lastSeenIndex[remainder] = decimal.size();

        remainder = remainder * 10;
        decimal.push_back('0' + remainder / ldenominator);
        remainder = remainder % ldenominator;
      }
    }

    // return final output 
    return decimal;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) 
    // N = number of digits, <= 10^4
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 166. Fraction to Recurring Decimal - https://leetcode.com/problems/fraction-to-recurring-decimal/description/?envType=daily-question&envId=2025-09-24 

  Solution1* s1 = new Solution1();
  cout << "1, 2 -> " << s1->fractionToDecimal(1, 2) << endl;
  cout << "2, 1 -> " << s1->fractionToDecimal(2, 1) << endl;
  cout << "4, 333 -> " << s1->fractionToDecimal(4, 333) << endl;
  cout << "1, 7 -> " << s1->fractionToDecimal(1, 7) << endl;
  cout << "7, 7 -> " << s1->fractionToDecimal(7, 7) << endl;
  cout << "3, 9 -> " << s1->fractionToDecimal(3, 9) << endl;
  cout << "1, -1 -> " << s1->fractionToDecimal(1, -1) << endl;
  cout << "-1, -2147483648 -> " << s1->fractionToDecimal(-1, -2147483648) << endl;

  delete s1;
}

class SpecialQueue {
  // 1, 2, 3, 2, 4, 1
  // 1, 1, (for min)
  // 4, 1, (for max)
  // 9, 7, 8
  // 7, 
  // 9, 7

private:
  queue<int> q;
  deque<int> minn;
  deque<int> maxx;

public:
  void enqueue(int x) {
    // Insert element into the queue
    while (!minn.empty() && minn.back() > x) minn.pop_back();
    while (!maxx.empty() && maxx.back() < x) maxx.pop_back();
    q.push(x);
    minn.push_back(x);
    maxx.push_back(x);
  }

  void dequeue() {
    // Remove element from the queue
    if (q.front() == minn.front()) minn.pop_front();
    if (q.front() == maxx.front()) maxx.pop_front();
    q.pop();
  }

  int getFront() {
    // Get front element
    return q.front();
  }

  int getMin() {
    // Get minimum element
    return minn.front();
  }

  int getMax() {
    // Get maximum element
    return maxx.front();
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Design MinMax Queue - https://www.geeksforgeeks.org/problems/design-minmax-queue/1 

  SpecialQueue* sque = new SpecialQueue();

  sque->enqueue(9);
  sque->enqueue(7);
  sque->enqueue(8);
  cout << sque->getMax() << endl;
  sque->dequeue();
  cout << sque->getFront() << endl;
  cout << sque->getMin() << endl;
  cout << sque->getMax() << endl;
  cout << sque->getFront() << endl;

  delete sque;
}

int main() {
  // Day 24 of September 2025

  p1();

  p2();

  return 0;
}
