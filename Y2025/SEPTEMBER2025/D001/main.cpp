#include <bits/stdc++.h>

using namespace std;

class Solution1 {
private:
  double maxAveragePassRatio = 0.0;

  void recursion(vector<vector<int>>& classes, int extraStudents, int index, double averagePassRatio) {
    if (index == classes.size()) {
      maxAveragePassRatio = max(maxAveragePassRatio, averagePassRatio / index);
      return;
    }

    for (int s = 0; s <= extraStudents; s++) {
      double pass = classes[index][0] + s;
      double total = classes[index][1] + s;
      double passRatio = pass / total;
      recursion(classes, extraStudents - s, index + 1, averagePassRatio + passRatio);
    }

    // Complexity analysis
    // Time : O(N ^ S)
    // Space : O(N) stack
  }

public:
  double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
    // classes = [[1,2],[3,5],[2,2]], extraStudents = 2
    // brute force (intuition building)
    // for each client i = 0, i < N
    // i try to assign them s = 0, s < extraStudents
    // at the end check pass ratio of all classes
    // find average pass ration
    // and update max average pass ratio
    // recursion(classes, extraStudents, 0, 0.0);

    // towards optimization
    // classes = [[1,2],[3,5],[2,2]], extraStudents = 2
    // passRatio = [0.5, 0.6, 1.0]
    // passRatio = [0.750, 0.714, 1.000], if 1 extraStudent added in ith
    // class averagePassRatio = (0.5 + 0.6 + 1.0) / 3 = 0.7 classes =
    // [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4 passRatio = [0.500,
    // 0.333, 0.800, 0.200] passRatio = [0.750, 0.538, 0.888, 0.285], if 1
    // extraStudent added in ith class difference = [0.250, 0.205, 0.088,
    // 0.085] steps for solution calculate initial passRatio use max heap
    // for storing difference (gain in passRatio) then for each
    // extraStudent, take out the class with maximum difference from heap
    // increase its pass and total students, recompute difference
    // add it back to heap
    // finally calculate maxAveragePassRatio by taking passRatio of all
    // classes heap structure { difference, passStudents, totalStudents }

    // this will return the difference (gain in passRatio)
    auto gain = [](int pass, int total) {
      return (double)(pass + 1) / (total + 1) - (double)pass / total;
      };

    priority_queue<pair<double, pair<int, int>>> pq;

    // initial pass ration gain -
    for (auto& c : classes) {
      pq.push({ gain(c[0], c[1]), {c[0], c[1]} });
    }

    while (extraStudents--) {
      auto [g, c] = pq.top(); pq.pop();
      int pass = c.first, total = c.second;
      pass++; total++;
      pq.push({ gain(pass, total), {pass, total} });
    }

    while (!pq.empty()) {
      auto [g, c] = pq.top(); pq.pop();
      maxAveragePassRatio += (double)c.first / c.second;
    }

    return maxAveragePassRatio / classes.size();

    // Complexity analysis
    // Time : O((N + S) * Log(N))
    // Space : O(N) priority queue
  }
};

void p1() {
  // Problem 1 : POTD Leetcode 1792. Maximum Average Pass Ratio - https://leetcode.com/problems/maximum-average-pass-ratio/description/?envType=daily-question&envId=2025-09-01

  Solution1* s1 = new Solution1();

  vector<pair<vector<vector<int>>, int>> tests = {
      { {{1,2}, {3,5}, {2,2}}, 2 },   // Example 1
      { {{2,4}, {3,9}, {4,5}, {2,10}}, 4 }, // Example 2
      { {{5,10}}, 5 },   // edge case: single class
      { {{1,3}, {2,4}}, 1 } // small custom
  };

  for (int i = 0; i < tests.size(); i++) {
    auto [classes, extraStudents] = tests[i];
    double out = s1->maxAverageRatio(classes, extraStudents);
    cout << "Test " << i + 1 << ": " << fixed << setprecision(5) << out << endl;
  }

  delete s1;
}

class Solution2 {
public:
  int sumOfModes(vector<int>& arr, int k) {
    // code here
    int sum = 0;

    int n = arr.size();

    unordered_map<int, int> freq;    // element -> frequency
    map<int, set<int>> freqToElems; // frequency -> set of elements

    int maxFreq = 0;
    int total = 0;

    for (int i = 0; i < n; i++) {
      int x = arr[i];
      int oldF = freq[x];
      int newF = oldF + 1;
      freq[x] = newF;

      if (oldF > 0) {
        freqToElems[oldF].erase(x);
        if (freqToElems[oldF].empty()) freqToElems.erase(oldF);
      }
      freqToElems[newF].insert(x);
      maxFreq = max(maxFreq, newF);

      // shrink window if needed
      if (i >= k) {
        int y = arr[i - k];
        int f = freq[y];
        freqToElems[f].erase(y);
        if (freqToElems[f].empty()) freqToElems.erase(f);

        freq[y]--;
        if (freq[y] > 0) {
          freqToElems[f - 1].insert(y);
        }
        if (freqToElems.find(maxFreq) == freqToElems.end()) {
          maxFreq--; // decrease if top freq set is empty
        }
      }

      // record mode once we have k elements
      if (i >= k - 1) {
        int mode = *freqToElems[maxFreq].begin(); // smallest with max frequency
        total += mode;
      }
    }

    return total;

    // Complexity analysis 
    // Time : O(N * Log(N)) 
    // Space : O(2N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Sum of Mode - https://www.geeksforgeeks.org/problems/sum-of-mode/1

  Solution2* s2 = new Solution2();

  vector<pair<vector<int>, int>> tests = {
    {{1, 2, 3, 2, 5, 2, 4, 4}, 3},
    {{1, 2, 1, 3, 5}, 2},
  };

  for (int i = 0; i < tests.size(); i++) {
    auto [arr, k] = tests[i];
    int out = s2->sumOfModes(arr, k);
    cout << "Test " << i + 1 << ": " << out << endl;
  }

  delete s2;
}

int main() {
  // Day 1 of September 2025

  p1();

  p2();

  return 0;
}
