#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> stockBuySell(vector<int> A, int n){
    // code here 
    vector<vector<int>> ans;
    int buy = 0;
    int sell = 0;

    for (int i = 0; i < n - 1; i++) {
        if (A[i+1] > A[i]) sell++;
        else {
            if (buy < sell) ans.push_back({buy, sell});

            buy = i + 1;
            sell = i + 1;
        }
    }

    // one last sell - if profit 
    if (buy < sell) ans.push_back({buy, sell});

    return ans;
}

void p1() {
    // Problem 1 : Stock buy and sell - https://www.geeksforgeeks.org/problems/stock-buy-and-sell-1587115621/1 

    vector<int> prices = {100,180,260,310,40,535,695}; // prices of stocks 

    vector<vector<int>> ans = stockBuySell(prices, prices.size());

    for (int i = 0; i < ans.size(); i++) {
        cout << "buy : " << ans[i][0] << " sell : " << ans[i][1] << endl;
    }
}

int main() {
    // Day 021 

    p1();


    return 0;
}