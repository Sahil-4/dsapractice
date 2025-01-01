#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class StockSpanner {
public:
    stack<pair<int, int>> spans;

    StockSpanner() {}

    int next(int price) {
        if (spans.empty() || spans.top().first > price) {
            spans.push({price, 1});
            return 1;
        } else {
            int count = 1;

            while (!spans.empty() && spans.top().first <= price) {
                pair<int, int> span = spans.top();
                count += span.second;
                spans.pop();
            }

            spans.push({price, count});
            return count;
        }
    }
};

//Function to calculate the span of stock price for all n days.
vector<int> calculateSpan(int prices[], int n) {
    vector<int> ans;
    stack<pair<int, int>> spans;

    for (int i = 0; i < n; i++) {
        if (spans.empty() || spans.top().first > prices[i]) {
            spans.push({prices[i], 1});
        } else {
            int count = 1;

            while (!spans.empty() && spans.top().first <= prices[i]) {
                pair<int, int> span = spans.top();
                count += span.second;
                spans.pop();
            }

            spans.push({prices[i], count});
        }

        ans.push_back(spans.top().second);
    }

    return ans;
}

void p1() {
    // Problem 1 : Leetcode 901. Online Stock Span - https://leetcode.com/problems/online-stock-span/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1 

    StockSpanner sp = StockSpanner();
    vector<int> arr = {100, 50, 10, 50, 100};
    for (int i = 0; i < arr.size(); i++) {
        cout << sp.next(arr[i]) << " ";
    } cout << endl;
}


int main() {
    // Day 21 

    p1();


    return 0;
}