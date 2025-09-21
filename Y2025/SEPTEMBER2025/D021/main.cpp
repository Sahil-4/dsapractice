#include <bits/stdc++.h>

using namespace std;

class MovieRentingSystem {
public:
  typedef pair<int, int> P;

  unordered_map<int, set<P>> available; //movei -> set<{price, shop}>
  unordered_map<int, set<P>> movieToShopPrice; //movie -> set<shop, price>
  set<tuple<int, int, int>> rented; //{price, shop, movie}

  MovieRentingSystem(int n, vector<vector<int>>& entries) {
    for (auto& entry : entries) {
      int shop = entry[0];
      int movie = entry[1];
      int price = entry[2];
      available[movie].insert({ price, shop });
      movieToShopPrice[movie].insert({ shop, price });
    }
  }

  vector<int> search(int movie) {
    vector<int> result;
    int count = 0;
    if (!available.count(movie)) return result;

    for (auto& [_, shop] : available[movie]) {
      result.push_back(shop);
      count++;
      if (count >= 5) break;
    }

    return result;
  }

  void rent(int shop, int movie) {
    auto it = movieToShopPrice[movie].lower_bound({ shop, INT_MIN });
    int price = it->second;

    available[movie].erase({ price, shop });
    rented.insert({ price, shop, movie });
  }

  void drop(int shop, int movie) {
    auto it = movieToShopPrice[movie].lower_bound({ shop, INT_MIN });
    int price = it->second;

    available[movie].insert({ price, shop });
    rented.erase({ price, shop, movie });
  }

  vector<vector<int>> report() {
    vector<vector<int>> result;
    int count = 0;

    for (auto& [price, shop, movie] : rented) {
      result.push_back({ shop, movie });
      count++;
      if (count >= 5) break;
    }

    return result;
  }
};

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem* obj = new MovieRentingSystem(n, entries);
 * vector<int> param_1 = obj->search(movie);
 * obj->rent(shop,movie);
 * obj->drop(shop,movie);
 * vector<vector<int>> param_4 = obj->report();
 */

void p1() {
  // Problem 1 : POTD Leetcode 1912. Design Movie Rental System - https://leetcode.com/problems/design-movie-rental-system/description/?envType=daily-question&envId=2025-09-21 

  int n = 10;
  vector<vector<int>> entries = {
    {0,418,3},{9,5144,46},{2,8986,29},
    {6,1446,28},{3,8215,97},{7,9105,34},
    {6,9105,30},{5,1722,94},{9,528,40},
    {3,850,77},{3,7069,40},{8,1997,42},
    {0,8215,28},{7,4050,80},{4,7100,97},
    {4,9686,32},{4,2566,93},{2,8320,12},
    {2,5495,56}
  };
  MovieRentingSystem* mrs = new MovieRentingSystem(n, entries);

  mrs->search(7837);
  mrs->search(5495);
  mrs->rent(4, 7100);
  mrs->search(9105);
  mrs->search(1446);
  mrs->report();
  mrs->search(9869);
  mrs->drop(4, 7100);
}

class Solution2 {
private:
  vector<int> nextSmallRight(vector<int>& arr, int n) {
    vector<int> out(n, n - 1);
    stack<int> stk;

    for (int i = n - 1; i >= 0; i--) {
      while (!stk.empty() && arr[stk.top()] >= arr[i]) stk.pop();

      if (!stk.empty()) out[i] = stk.top() - 1;
      stk.push(i);
    }

    return out;
  }

  vector<int> nextSmallLeft(vector<int>& arr, int n) {
    vector<int> out(n, 0);
    stack<int> stk;

    for (int i = 0; i < n; i++) {
      while (!stk.empty() && arr[stk.top()] >= arr[i]) stk.pop();

      if (!stk.empty()) out[i] = stk.top() + 1;
      stk.push(i);
    }

    return out;
  }

  int largestHistogramRectangleArea(vector<int>& heights) {
    // ---- OLD CODE ---- 
    int n = heights.size();
    int ar = 0;
    vector<int> ns_l = nextSmallLeft(heights, n);
    vector<int> ns_r = nextSmallRight(heights, n);

    for (int i = 0; i < n; i++) {
      int e = heights[i], r = ns_r[i], l = ns_l[i];

      int ar_temp = (r - l + 1) * e;
      ar = max(ar, ar_temp);
    }

    return ar;
  }

  int solve(vector<vector<int>>& matrix) {
    int N = matrix.size(), M = matrix[0].size();

    vector<int> dp(M, 0);

    int marea = 0;

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if (matrix[i][j] == 1) {
          dp[j] = dp[j] + 1;
        } else {
          dp[j] = 0;
        }
      }

      // get max histo area 
      int harea = largestHistogramRectangleArea(dp);
      marea = max(marea, harea);
    }

    return marea;

    // Complexity analysis 
    // Time : O(N*M) ~ 
    // Space : O(M) ~ 
  }

public:
  int maxArea(vector<vector<int>>& mat) {
    // code here
    return solve(mat);
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Max rectangle - https://www.geeksforgeeks.org/problems/max-rectangle/1 

  Solution2* s2 = new Solution2();

  vector<vector<int>> v1 = {
    {0, 1, 1, 0},
    {1, 1, 1, 1},
    {1, 1, 1, 1},
    {1, 1, 0, 0}
  };
  cout << s2->maxArea(v1) << endl;

  vector<vector<int>> v2 = {
    {0, 1, 1},
    {1, 1, 1},
    {0, 1, 1}
  };
  cout << s2->maxArea(v2) << endl;
}

int main() {
  // Day 21 of September 2025

  p1();

  p2();

  return 0;
}
