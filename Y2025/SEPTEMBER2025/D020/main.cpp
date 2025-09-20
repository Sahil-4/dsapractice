#include <bits/stdc++.h>

using namespace std;

class Router {
private:
  int T;
  queue<string> storage;
  unordered_map<string, vector<int>> packets;
  unordered_map<int, vector<int>> destination2Timestamp;

  string getPacketKey(int source, int destination, int timestamp) {
    string hash = "";

    hash += to_string(source) + ".";
    hash += to_string(destination) + ".";
    hash += to_string(timestamp);

    return hash;
  }

public:
  Router(int memoryLimit) {
    // init 
    this->T = memoryLimit;
  }

  bool addPacket(int source, int destination, int timestamp) {
    string key = getPacketKey(source, destination, timestamp);

    if (packets.find(key) != packets.end()) return false;
    if (storage.size() >= T) forwardPacket();

    storage.push(key);
    packets[key] = { source, destination, timestamp };
    destination2Timestamp[destination].push_back(timestamp);

    return true;
  }

  vector<int> forwardPacket() {
    if (storage.empty()) return {};

    string key = storage.front(); storage.pop();
    vector<int> packet = packets[key]; packets.erase(key);
    int d = packet[1];
    destination2Timestamp[d].erase(destination2Timestamp[d].begin());

    return packet;
  }

  int getCount(int destination, int startTime, int endTime) {
    auto it = destination2Timestamp.find(destination);

    if (it == destination2Timestamp.end() || it->second.empty()) {
      return 0;
    }

    int l = lower_bound(it->second.begin(), it->second.end(), startTime) - it->second.begin();
    int r = lower_bound(it->second.begin(), it->second.end(), endTime + 1) - it->second.begin();

    return r - l;
  }
};

/**
 * Your Router object will be instantiated and called as such:
 * Router* obj = new Router(memoryLimit);
 * bool param_1 = obj->addPacket(source,destination,timestamp);
 * vector<int> param_2 = obj->forwardPacket();
 * int param_3 = obj->getCount(destination,startTime,endTime);
 */

void p1() {
  // Problem 1 : POTD Leetcode 3508. Implement Router - https://leetcode.com/problems/implement-router/description/?envType=daily-question&envId=2025-09-20

  Router* router = new Router(3);
  router->addPacket(1, 4, 90);
  router->addPacket(2, 5, 90);
  router->addPacket(1, 4, 90);
  router->addPacket(3, 5, 95);
  router->addPacket(4, 5, 105);
  vector<int> packet = router->forwardPacket();
  for (int e : packet) cout << e << " ";
  cout << endl;
  router->addPacket(5, 2, 110);
  router->getCount(5, 100, 11);
}

class Solution2 {
  int solve1(vector<int>& arr) {
    // build all subarray 
    // take valid subarrays 
    // find its length 
    // update answer 

    int lslen = 0;

    for (int i = 0, N = arr.size(); i < N; i++) {
      int maxx = arr[i];
      int len = 1;
      for (int j = i; j < N; j++, len++) {
        maxx = max(maxx, arr[j]);
        if (maxx <= len) lslen = max(lslen, len);
      }
    }

    return lslen;

    // Complexity analysis 
    // Time : O(N * N) 
    // Space : O(1) 
  }

  vector<int> get_fgtl(vector<int>& arr, int N) {
    vector<int> output(N, -1);
    stack<int> stk;

    for (int i = 0; i < N; i++) {
      while (!stk.empty() && arr[i] >= arr[stk.top()]) {
        stk.pop();
      }

      if (!stk.empty()) {
        output[i] = stk.top();
      }

      stk.push(i);
    }

    return output;
  }

  vector<int> get_fgtr(vector<int>& arr, int N) {
    vector<int> output(N, N);
    stack<int> stk;

    for (int i = N - 1; i >= 0; i--) {
      while (!stk.empty() && arr[i] >= arr[stk.top()]) {
        stk.pop();
      }

      if (!stk.empty()) {
        output[i] = stk.top();
      }

      stk.push(i);
    }

    return output;
  }

public:
  int longestSubarray(vector<int>& arr) {
    // code here
    // arr[]  = [4,1,2,3]
    // fgtl[]  = [-1,0,0,0]
    // fgtr[]  = [4,2,3,4]
    // len[]  = [4,1,2,3] (r - l - 1) 
    // output = 4
    // arr[]    = [6, 4, 2, 5]
    // fgtl[]   = [-1, 0, 1, 0]
    // fgtr[]   = [4, 3, 3, 4]
    // len[]    = [4, 2, 1, 3] 

    int N = arr.size();

    vector<int> fgtl = get_fgtl(arr, N);
    vector<int> fgtr = get_fgtr(arr, N);

    int llen = 0;

    for (int i = 0; i < N; i++) {
      int len = fgtr[i] - fgtl[i] - 1;
      if (len >= arr[i]) llen = max(llen, len);
    }

    return llen;

    // Complexity analysis 
    // Time : O(2N + 2N + N) 
    // Space : O(2N) 
  }
};

void p2() {
  // Problem 2 : POTD Geeksforgeeks Longest Subarray Length - https://www.geeksforgeeks.org/problems/longest-subarray-length--202010/1

  vector<vector<int>> testcases = {
    {1, 2, 3},
    {6, 4, 2, 5},
    {6, 4, 2, 1},
    {4, 1, 2, 3},
  };

  Solution2* s2 = new Solution2();
  for (auto& tc : testcases) {
    cout << "InPUT: ";
    for (auto& e : tc) cout << e << " ";
    cout << endl;
    int out = s2->longestSubarray(tc);
    cout << "OUTPUT: " << out << endl << endl;
  }
}

int main() {
  // Day 20 of September 2025

  p1();

  p2();

  return 0;
}
