#include <bits/stdc++.h>

using namespace std;

class Problem1 {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> out;

        // difference one function 
        auto diff1 = [&](int a, int b) {
            return ((long long)a - b) == 1;
            };

        int N = nums.size();
        int i = 1;
        int start = 0, end = 0;

        while (i <= N) {
            if (i == N || !diff1(nums[i], nums[end])) {
                string s = to_string(nums[start]);
                if (start != end) s += "->" + to_string(nums[end]);
                out.push_back(s);
                start = i, end = i;
            }
            end = i;
            i++;
        }

        return out;

        // Complexity analysis 
        // Time : O(N * nstr_len) 
        // Space : O(1) 
    }
};

void p1() {
    // Problem 1 : Leetcode 228. Summary Ranges - https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150 

    vector<int> nums = { -2147483648,0,1,2147483647 };
    vector<string> ranges = Problem1().summaryRanges(nums);
    for (string s : ranges) cout << s << endl;
}

class Problem2 {
public:
    vector<vector<int>> merge(vector<vector<int>> intervals) {
        auto compare = [&](vector<int> v1, vector<int> v2) {
            return v1[0] < v2[0];
            };
        sort(intervals.begin(), intervals.end(), compare);

        vector<vector<int>> out;

        int start = intervals[0][0], end = intervals[0][1];

        for (int i = 1, N = intervals.size(); i <= N; i++) {
            if (i == N) {
                out.push_back({ start, end });
                break;
            }

            int starti = intervals[i][0], endi = intervals[i][1];
            if (end < starti) {
                out.push_back({ start, end });
                start = starti;
            }

            end = max(end, endi);
        }

        return out;

        // Complexity analysis
        // Time : O(N * Log(N)) + O(N)
        // Space : O(N) copying input data
    }
};

void p2() {
    // Problem 2 : Leetcode 56. Merge Intervals - https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/overlapping-intervals--170633/0 

    vector<vector<int>> intervals = { {1,4},{0,4},{2,8},{0,8} };
    vector<vector<int>> mergedIntervals = Problem2().merge(intervals);
    for (vector<int> interval : mergedIntervals) {
        cout << interval[0] << "->" << interval[1] << endl;
    }
}

class Problem3 {
    vector<vector<int>> solve1(vector<vector<int>> intervals, vector<int>& newInterval) {
        // add at the end then merge overlapping intervals
        intervals.push_back(newInterval);

        auto compare = [&](vector<int> v1, vector<int> v2) {
            return v1[0] < v2[0];
            };
        sort(intervals.begin(), intervals.end(), compare);

        vector<vector<int>> out;

        int start = intervals[0][0], end = intervals[0][1];

        for (int i = 1, N = intervals.size(); i <= N; i++) {
            if (i == N) {
                out.push_back({ start, end });
                break;
            }

            int starti = intervals[i][0], endi = intervals[i][1];
            if (end < starti) {
                out.push_back({ start, end });
                start = starti;
            }

            end = max(end, endi);
        }

        return out;

        // Complexity analysis
        // Time : O(N * Log(N)) + O(N)
        // Space : O(N) copying input data
    }

    vector<vector<int>> solve2(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> out;

        int start = newInterval[0], end = newInterval[1];

        int i = 0, N = intervals.size();

        while (i < N) {
            if (intervals[i][1] >= start) break;
            out.push_back(intervals[i]);
            i++;
        }

        while (i < N) {
            if (intervals[i][0] > end) break;
            start = min(start, intervals[i][0]);
            end = max(end, intervals[i][1]);
            i++;
        }
        out.push_back({ start, end });

        while (i < N) {
            out.push_back(intervals[i]);
            i++;
        }

        return out;

        // Complexity analysis
        // Time : O(N)
        // Space : O(1)
    }

public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        // return solve1(intervals, newInterval);

        return solve2(intervals, newInterval);
    }
};

void p3() {
    // Problem 3 : Leetcode 57. Insert Interval - https://leetcode.com/problems/insert-interval/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/insert-interval-1666733333/0 

    vector<vector<int>> intervals = { {0,1}, {2,3}, {3,4}, {8,12} };
    vector<int> newInterval = { 2,5 };
    vector<vector<int>> nintervals = Problem3().insert(intervals, newInterval);
    for (vector<int> interval : nintervals) {
        cout << interval[0] << "->" << interval[1] << endl;
    }
}

class Problem4 {
public:
    int findMinArrowShots(vector<vector<int>> points) {
        sort(points.begin(), points.end());

        int arrows = 0;
        int range[] = { points[0][0], points[0][1] };

        for (int i = 1, N = points.size(); i <= N; i++) {
            if (i == N || range[1] < points[i][0]) {
                arrows++;
                if (i == N) break;
                range[0] = points[i][0];
                range[1] = points[i][1];
            }
            else {
                // update range
                range[0] = max(range[0], points[i][0]);
                range[1] = min(range[1], points[i][1]);
            }
        }

        return arrows;

        // Complexity analysis 
        // Time : O(N*Log(N)) + O(N) 
        // Space : O(N) 
    }
};

void p4() {
    // Problem 4 : Leetcode 452. Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=top-interview-150 

    vector<vector<int>> points = { {10,16},{2,8},{1,6},{7,12} };
    cout << Problem4().findMinArrowShots(points) << endl;
}


int main() {
    // Day 15 of January 

    p1();

    p2();

    p3();

    p4();


    return 0;
}