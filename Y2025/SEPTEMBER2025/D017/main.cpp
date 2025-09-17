#include <bits/stdc++.h>

using namespace std;

class FoodRatings {
  class Food {
  public:
    string food;
    string cuisine;
    int rating;

    Food(string food, string cuisine, int rating) {
      this->food = food;
      this->cuisine = cuisine;
      this->rating = rating;
    }
  };

  vector<Food> items;
  unordered_map<string, int> food2Food;             // { food, items index }
  unordered_map<string, vector<int>> cuisine2Foods; // { cuisine, vector<items index> }

public:
  FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
    // Initializes the system
    int N = foods.size();
    for (int i = 0; i < N; i++) {
      items.push_back(Food(foods[i], cuisines[i], ratings[i]));
      food2Food[foods[i]] = i;
      cuisine2Foods[cuisines[i]].push_back(i);
    }

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) 
  }

  void changeRating(string food, int newRating) {
    // Changes the rating of the food item with the name food.
    int index = food2Food[food];
    items[index].rating = newRating;

    // Complexity analysis 
    // Time : O(1) 
    // Space : O(1) 
  }

  string highestRated(string cuisine) {
    // Returns the name of the food item
    // that has the highest rating for the given type of cuisine.
    // If there is a tie,
    // return the item with the lexicographically smaller name.
    int ratings = -1;
    string food = "";

    vector<int> indices = cuisine2Foods[cuisine];
    for (int& index : indices) {
      bool check = items[index].rating > ratings;
      check |= (items[index].rating == ratings && items[index].food < food);
      if (check) {
        ratings = items[index].rating;
        food = items[index].food;
      }
    }

    return food;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) 
  }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */

void p1() {
  // Problem 1 : POTD Leetcode 2353. Design a Food Rating System - https://leetcode.com/problems/design-a-food-rating-system/description/?envType=daily-question&envId=2025-09-17

  vector<string> foods = { "kimchi","miso","sushi","moussaka","ramen","bulgogi" };
  vector<string> cuisines = { "korean","japanese","japanese","greek","japanese","korean" };
  vector<int> ratings = { 9,12,8,15,14,7 };

  FoodRatings* system = new FoodRatings(foods, cuisines, ratings);
  cout << system->highestRated("korean") << endl;
  cout << system->highestRated("japanese") << endl;
  system->changeRating("sushi", 16);
  cout << system->highestRated("japanese") << endl;
  system->changeRating("ramen", 16);
  cout << system->highestRated("japanese") << endl;
}

class Solution2 {
private:
  string repeat(string s, int k) {
    string out = "";
    for (int i = 0; i < k; i++) {
      out += s;
    }

    return out;
  }

public:
  string decodedString(string& s) {
    // code here
    int N = s.size();

    stack<int> stackNum;
    stack<string> stackStr;

    int currNum = 0;
    string currStr = "";

    for (auto& ch : s) {
      if (ch == '[') {
        stackNum.push(currNum);
        stackStr.push(currStr);
        currNum = 0;
        currStr = "";
      }
      else if (ch == ']') {
        int times = stackNum.top(); stackNum.pop();
        string str = stackStr.top(); stackStr.pop();
        currStr = str + repeat(currStr, times);
      }
      else if (ch >= '0' && ch <= '9') {
        currNum = (currNum * 10) + (ch - '0');
      }
      else {
        currStr.push_back(ch);
      }
    }

    return currStr;

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Decode the string - https://www.geeksforgeeks.org/problems/decode-the-string2444/1

  vector<string> testcases = {
    "3[b2[ca]]",
    "3[ab]",
    "3[a3[b]1[ab]]",
    "3[a1[12[b]]]",
    "a1[5[aa]]",
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << "INPUT: " << tc << endl;
    cout << "OUTPUT: " << s2->decodedString(tc) << endl << endl;
  }
}

int main() {
  // Day 17 of September 2025

  p1();

  p2();

  return 0;
}
