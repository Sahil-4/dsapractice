#include <iostream>
#include <vector>

using namespace std;

int maxProfit(vector<int>& prices) {
    int profit = 0;
    int buyPrice = 0, sellPrice = 0;

    for (int i = 0; i < prices.size(); i++) {
        if (prices[i] < prices[buyPrice]) {
            buyPrice = i, sellPrice = i;
        } else if (prices[i] >= prices[sellPrice]) {
            sellPrice = i;
            profit = max(profit, prices[sellPrice] - prices[buyPrice]);
        }
    }

    return profit;

    // Complexity analysis - sliding window : find low and high (buy and sell) price then find the profit 
    // Time : O(n) 
    // Space : O(1) 
}

vector<vector<int>> stockBuySell(vector<int> A, int n) {
    // code here
    vector<vector<int>> profitDays;
    int prevBuy = 0, prevSell = 0;
    int prevProfit = 0;

    for (int i = 0; i < n; i++) {
        prevSell = i;
        if (A[i] <= A[prevBuy]) {
            prevBuy = i;
            prevProfit = 0;
        } else {
            int tempProfit = A[prevBuy] - A[prevSell];
            if (tempProfit > prevProfit) {
                prevProfit = tempProfit;
            } else {
                profitDays.push_back({prevBuy, prevSell});
                prevBuy = i;
                prevProfit = 0;
            }
        }
    }

    return profitDays;
    // Complexity analysis 
    // Time : O(n) 
    // Space : O(1) 
}

void p1() {
    // P1 Leetcode 121. Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/stock-buy-and-sell-1587115621/1 

    vector<int> prices = {100,180,260,310,40,535,695};
    int profit = maxProfit(prices);
    cout << "profit :: " << profit << endl;

    vector<vector<int>> allProfitableTrades = stockBuySell(prices, prices.size());
    for (int i = 0; i < allProfitableTrades.size(); i++) {
        cout << "buy :: " << allProfitableTrades[i][0] << " sell :: " << allProfitableTrades[i][1] << endl;
    }
}

int main() {
    // Day 8 

    p1();


    return 0;
}