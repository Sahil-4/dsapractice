#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

bool isCollisionPossible(int l, int r) {
    // collision is possible only when left asteroid is moving towards right(+) and right is moving towards left(-) 
    if (l > 0 && r < 0) return true;
    return false;
}

int getCollisionResult(int l, int r) {
    // collision - both having same size, destroy each other 
    if (l + r == 0) return 0;

    // collision - smaller will explode 
    if (abs(l) > abs(r)) return l;
    else return r;
}

vector<int> asteroidCollision_solution1(vector<int>& asteroids_arr) {
    int n = asteroids_arr.size();
    stack<int> col_stack;

    for (int i = n - 1; i >= 0; i--) {
        if (col_stack.empty()) {
            col_stack.push(asteroids_arr[i]);
        } else {
            int l = asteroids_arr[i]; // left asteroid 
            while (!col_stack.empty() && isCollisionPossible(l, col_stack.top())) {
                int r = col_stack.top(); col_stack.pop();
                l = getCollisionResult(l, r);
            }

            if (l != 0) col_stack.push(l);
        }
    }

    vector<int> res;
    while (!col_stack.empty()) {
        res.push_back(col_stack.top()); col_stack.pop();
    }

    return res;

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(2N) 
}

vector<int> asteroidCollision(vector<int>& asteroids_arr) {
    int n = asteroids_arr.size();
    vector<int> col_stack;

    for (int i = n - 1; i >= 0; i--) {
        if (col_stack.empty()) {
            col_stack.push_back(asteroids_arr[i]);
        } else {
            int l = asteroids_arr[i]; // left asteroid 
            while (!col_stack.empty() && isCollisionPossible(l, col_stack.back())) {
                int r = col_stack.back(); col_stack.pop_back();
                l = getCollisionResult(l, r);
            }

            if (l != 0) col_stack.push_back(l);
        }
    }

    reverse(col_stack.begin(), col_stack.end());
    return col_stack;

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(N) 
}

void p1() {
    // Problem 1 : Leetcode 735. Asteroid Collision - https://leetcode.com/problems/asteroid-collision/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/asteroid-collision/1 

    vector<int> asteroids_arr = {1, -1, 2, 2, 2, 3, -2, 2, 4};
    vector<int> collision_result = asteroidCollision(asteroids_arr);
}


int main() {
    // Day 10 

    p1();


    return 0;
}