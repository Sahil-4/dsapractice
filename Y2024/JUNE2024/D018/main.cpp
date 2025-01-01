#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool placeBalls(vector<int>& basketPositions, int balls, int minForce) {
    // this will check if we are able to place all balls while maintaining minimum given force 
    // if we are able to place balls with this force we will increase the force and chekc again 
    // else we will decrease the force 

    int prevPlace = 0;
    balls--;

    for (int i = 1; i < basketPositions.size(); i++) {
        if (basketPositions[i] - basketPositions[prevPlace] >= minForce) {
            balls--, prevPlace = i;
            if (balls == 0) return true;
        }
    }

    return false;
}

int maxDistance(vector<int>& basketPositions, int balls) {
    int maxMinForce = 0;

    sort(basketPositions.begin(), basketPositions.end());

    int n = basketPositions.size();

    int leastForce = 1, maxForce = basketPositions[n - 1] - basketPositions[0];
    int mForce = leastForce + (maxForce - leastForce) / 2;

    while (leastForce <= maxForce) {
        bool check = placeBalls(basketPositions, balls, mForce);

        if (check) {
            maxMinForce = max(maxMinForce, mForce);
            leastForce = mForce + 1;
        } else {
            maxForce = mForce - 1;
        }

        mForce = leastForce + (maxForce - leastForce) / 2;
    }

    return maxMinForce;
}

void p1() {
    // Problem 1 : Leetcode 1552. Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/aggressive-cows/0 

    vector<int> positions = {1, 2, 4, 8, 9};
    int balls = 5;
    int d = maxDistance(positions, 5);
    cout << "d :: " << d << endl;
}

int main() {
    // Day 18 

    p1();


    return 0;
}