#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    int solve1(int x) {
        int ans = 0;

        for (int i = 0; ((long long)i * i) <= x; i++) {
            ans = i;
        }

        return ans;

        // Complexity analysis 
        // Time : O(sqrt(X)) 
        // Space : O(1) 
    }

    int solve2(int x) {
        int l = 0, r = x;

        while (l <= r) {
            int mid = l + (r - l) / 2;

            if (((long long)mid * mid) == x) {
                return mid;
            }
            else if (((long long)mid * mid) < x) {
                l = mid + 1;
            }
            else {
                r = mid - 1;
            }
        }

        return r;

        // Complexity analysis 
        // Time : O(log(X)) 
        // Space : O(1) 
    }

public:
    int mySqrt(int x) {
        // return solve1(x);

        return solve2(x);
    }
};

void p1() {
    // Problem 1 : Leetcode 69. Sqrt(x) - https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/square-root/1 

    cout << Problem1().mySqrt(0) << endl;
    cout << Problem1().mySqrt(1) << endl;
    cout << Problem1().mySqrt(2) << endl;
    cout << Problem1().mySqrt(3) << endl;
    cout << Problem1().mySqrt(4) << endl;
    cout << Problem1().mySqrt(12) << endl;
    cout << Problem1().mySqrt(2147483647) << endl;
}

class Problem2 {
    double power(double x, long long n) {
        if (n == 0) return 1.0;
        if (n == 1) return x;

        double sub = power(x, n / 2);

        if (n & 1) return x * sub * sub;
        return sub * sub;
    }

public:
    double myPow(double x, int n) {
        double out = power(x, abs((long long)n));

        if (n >= 0) return out;
        return 1 / out;

        // Complexity analysis 
        // Time : O(Log(N)) 
        // Space : O(log(N)) 
    }
};

void p2() {
    // Problem 2 : Leetcode 50. Pow(x, n) - https://leetcode.com/problems/powx-n/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks -  https://www.geeksforgeeks.org/problems/powx-n/0 

    cout << Problem2().myPow(2.02, 2) << endl;
    cout << Problem2().myPow(2.02, -2) << endl;
}

class Problem3 {
    int solve1(vector<vector<int>>& points) {
        int mpoints = 1;

        for (int i = 0, n = points.size(); i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int pointsCount = 2;

                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];

                for (int k = 0; k < n; k++) {
                    if (k == i || k == j) continue;

                    int _dx = points[k][0] - points[i][0];
                    int _dy = points[k][1] - points[i][1];

                    if (dx * _dy == dy * _dx) pointsCount++;
                }

                mpoints = max(mpoints, pointsCount);
            }
        }

        return mpoints;

        // Complexity analysis 
        // Time : O(N^3) 
        // Space : O(1) 
    }

    int solve2(vector<vector<int>>& points) {
        int mpoints = 1;

        for (int i = 0, n = points.size(); i < n; i++) {
            unordered_map<double, int> thetaFreq;

            for (int j = 0; j < n; j++) {
                if (j == i) continue;

                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];

                double theta = atan2(dy, dx);

                thetaFreq[theta]++;
            }

            for (auto& it : thetaFreq) {
                mpoints = max(mpoints, it.second + 1);
            }
        }

        return mpoints;

        // Complexity analysis 
        // Time : O(N*(2*N)) 
        // Space : O(N) 
    }

public:
    int maxPoints(vector<vector<int>>& points) {
        // return solve1(points);

        return solve2(points);
    }
};

void p3() {
    // Problem 3 : Leetcode 149. Max Points on a Line - https://leetcode.com/problems/max-points-on-a-line/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/points-in-straight-line/1 Geeksforgeeks - https://www.geeksforgeeks.org/problems/points-in-straight-line/1 

    vector<vector<int>> points = { {1, 1} };
    cout << Problem3().maxPoints(points) << endl;
}


int main() {
    // Day 13 of February 

    p1();

    p2();

    p3();


    return 0;
}