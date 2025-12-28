#include <bits/stdc++.h>

using namespace std;

struct Node {
    int u;
    int v;
    int sum;

    Node(int u, int v) {
        this->u = u;
        this->v = v;
        this->sum = u + v;
    }

    // indices 
    Node(int sum, int ui, int vi) {
        this->u = ui;
        this->v = vi;
        this->sum = sum;
    }
};

struct sortNode {
    bool operator()(const Node& n1, const Node& n2) {
        return n1.sum > n2.sum;
    }
};

class Problem1 {
    vector<vector<int>> solve1(vector<int>& nums1, vector<int>& nums2, int k) {
        // generate all pairs 
        // put them into min heap 
        // take out top k pairs 
        // return top k pairs 

        int n = nums1.size();
        int m = nums2.size();

        priority_queue<Node, vector<Node>, sortNode> pq;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                pq.push({ nums1[i], nums2[j] });
                if (pq.size() > k) pq.pop();
            }
        }

        vector<vector<int>> out;

        for (int i = 0; i < k; i++) {
            Node top = pq.top(); pq.pop();
            out.push_back({ top.u, top.v });
        }

        return out;

        // Complexity analysis 
        // Time : O(N*M* K*Log(K)) + O(K) 
        // Space : O(N*M) 
    }

    vector<vector<int>> solve2(vector<int>& nums1, vector<int>& nums2, int k) {
        // intuition : 
        // we have given two sorted arrays 
        // if we have to pick one element from each array so that their sum is minimum 
        // we will have to pick first elements of both arrays 
        // then for next minimum sum pair we have two options (i, j+1) and (i+1, j) 

        // for output 
        vector<vector<int>> out;

        // length of both arrays 
        int n = nums1.size();
        int m = nums2.size();

        // hold the { sum, uindex, vindex } 
        priority_queue<Node, vector<Node>, sortNode> pq;

        // holds visited pair of indices { uindex, vindex } 
        set<pair<int, int>> visited;

        // first smallest pair 
        pq.push({ nums1[0] + nums2[0], 0, 0 });
        visited.insert({ 0, 0 });

        while (k-- && !pq.empty()) {
            Node top = pq.top(); pq.pop();

            int ui = top.u;
            int vi = top.v;

            // add this pair in output 
            out.push_back({ nums1[ui], nums2[vi] });

            // visit next possible pair of indices 

            if (ui + 1 < n && visited.find({ ui + 1, vi }) == visited.end()) {
                pq.push({ nums1[ui + 1] + nums2[vi], ui + 1, vi });
                visited.insert({ ui + 1, vi });
            }

            if (vi + 1 < m && visited.find({ ui, vi + 1 }) == visited.end()) {
                pq.push({ nums1[ui] + nums2[vi + 1], ui, vi + 1 });
                visited.insert({ ui, vi + 1 });
            }
        }

        return out;

        // Complexity analysis 
        // Time : O(K* K*Log(K)) 
        // Space : O(K) + O(K) 
    }

public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        // return solve1(nums1, nums2, k);

        return solve2(nums1, nums2, k);
    }
};

void p1() {
    // Problem 1 : Leetcode 373. Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/?envType=study-plan-v2&envId=top-interview-150 

    vector<int> nums1 = { 1, 5, 7 };
    vector<int> nums2 = { 1, 2, 5 };

    vector<vector<int>> result = Problem1().kSmallestPairs(nums1, nums2, 5);
    for (vector<int> res : result) {
        for (int e : res) cout << e << " ";
        cout << endl;
    }
}

class MedianFinder {
    priority_queue<int> pq1;
    priority_queue<int, vector<int>, greater<int>> pq2;

public:
    MedianFinder() {}

    void addNum(int num) {
        if (pq1.empty() || num < pq1.top()) {
            pq1.push(num);
        }
        else {
            pq2.push(num);
        }

        if (abs((int)pq1.size() - (int)pq2.size()) > 1) {
            pq2.push(pq1.top());
            pq1.pop();
        }
        else if (pq1.size() < pq2.size()) {
            pq1.push(pq2.top());
            pq2.pop();
        }
    }

    double findMedian() {
        if (pq1.size() == pq2.size()) {
            return (double)(pq1.top() + pq2.top()) / 2;
        }
        return pq1.top();
    }
};

void p2() {
    // Problem 2 : Leetcode 295. Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/find-median-in-a-stream-1587115620/1 

    MedianFinder mf = MedianFinder();
    mf.addNum(1);
    cout << mf.findMedian() << endl;
    mf.addNum(2);
    cout << mf.findMedian() << endl;
    mf.addNum(1);
    mf.addNum(3);
    mf.addNum(5);
    cout << mf.findMedian() << endl;
}


int main() {
    // Day 10 of February 2025 

    p1();

    p2();


    return 0;
}