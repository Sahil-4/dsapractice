#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <list>

using namespace std;

//Function to find if there is a celebrity in the party or not.
int celebrity_Solution1(vector<vector<int>>& M, int n) {
    // code here 
    int celeb = -1; // celebrity 

    // code here 
    map<int, int> mp;
    vector<int> possiblyCelebs;

    // create a map of persons and number of other people who knows him 
    for (int row = 0; row < n; row++) {
        int temp = 0;
        for (int col = 0; col < n; col++) {
            if (M[row][col] != 1) continue;
            temp++;
            mp[col]++;
        }
        if (temp == 0) possiblyCelebs.push_back(row);
    }

    // find the person who is known by N - 1 persons 
    for (auto person : possiblyCelebs) {
        if (mp[person] == n - 1) celeb = person;
    }

    return celeb;
    // ! TLE 
    // T : O(n * n)
    // S : O(2n)
}

//Function to find if there is a celebrity in the party or not.
int celebrity(vector<vector<int>>& M, int n) {
    // code here 
    int possiblyCelebs = -1;

    // find the person who knows no one in the party 
    for (int row = 0; row < n; row++) {
        int temp = 0;
        for (int col = 0; col < n; col++) temp += M[row][col];

        if (temp == 0) {
            possiblyCelebs = row;
            break;
        }
    }

    // find how many other knows possiblyCelebs person 
    for (int row = 0; row < n; row++) {
        if (row != possiblyCelebs && M[row][possiblyCelebs] == 0) return -1;
    }

    return possiblyCelebs;
    // T : O(n * n) 
}

//Function to find if there is a celebrity in the party or not.
int celebrity(vector<vector<int>>& M, int n) {
    // code here 
    int celeb = -1;

    // stack to store persons 
    stack<int> stk;

    for (int it = n - 1; it >= 0; it--) stk.push(it);

    // check whether they know each other or not one by one 
    while (!stk.empty()) {
        if (stk.size() == 1) {
            celeb = stk.top(); stk.pop();
            break;
        }

        int p1 = stk.top(); stk.pop();
        int p2 = stk.top(); stk.pop();

        // if M[p1][p2] == 1 && M[p2][p1] == 1
        // no one can be celebrity as they both know each other, so dont do anything 
        // if M[p1][p2] == 0 && M[p2][p1] == 0
        // no one can be celebrity as they both dont know each other, so dont do anything 

        if (M[p1][p2] == 1 && M[p2][p1] == 0) {
            // p2 can be celebrity as p1 knows him but p2 dont know p1 
            stk.push(p2);
        } else if (M[p1][p2] == 0 && M[p2][p1] == 1) {
            // p1 can be celebrity as p2 knows him but p1 dont know p2 
            stk.push(p1);
        }
    }

    if (celeb == -1) return -1;

    // verify whether or not celeb is a celebrity 
    for (int it = 0; it < n; it++) {
        if (celeb != it && M[celeb][it] == 1) return -1;
        if (celeb != it && M[it][celeb] == 0) return -1;
    }

    return celeb;
}

void p1() {
    // Problem 1 : The Celebrity Problem - https://www.geeksforgeeks.org/problems/the-celebrity-problem/1 

    int n = 3;
    vector<vector<int>> M = {
        {0, 1, 0},
        {0, 0, 0},
        {0, 1, 0}};

    int cl = celebrity(M, n);
    cout << "cl :: " << cl << endl;
}

class LRUCache {
public:
    vector<pair<int, int>> cache;
    int n;

    LRUCache(int capacity) {
        n = capacity;
    }

    int get(int key) {
    for (int i = 0; i < cache.size(); i++) {
        if (cache[i].first == key) {
            pair<int, int> out = cache[i];
            cache.erase(cache.begin() + i);
            cache.push_back(out);
            return out.second;
        }
    }
    }

    void put(int key, int value) {
        if (get(key) != -1) cache.pop_back();
        cache.push_back({key, value});

        if (cache.size() > n) cache.erase(cache.begin());
    }

    // TLE 
};

class LRUCache {
public:
    int n;
    map<int, pair<list<int>::iterator, int>> keyToNode; // to store key to node (address of node, value of node) 
    list<int> dll; // to store keys 

    LRUCache(int capacity) {
        // assign max capacity 
        n = capacity;
    }

    void makeRecentlyUsed(int key) {
        // erase key from dll 
        dll.erase(keyToNode[key].first);

        // push key at front in dll 
        dll.push_front(key);

        // update address of key in keyToNode map 
        keyToNode[key].first = dll.begin();
    }

    int get(int key) {
        // if key not found in map return -1 
        if (keyToNode.find(key) == keyToNode.end()) return -1;

        // move this key at front (mark it recently used)
        makeRecentlyUsed(key);

        // return value of key 
        return keyToNode[key].second;
    }

    void put(int key, int value) {
        if (keyToNode.find(key) != keyToNode.end()) {
            // update value 
            keyToNode[key].second = value;

            // mark it recently used
            makeRecentlyUsed(key);
        } else {
            dll.push_front(key);
            keyToNode[key] = {dll.begin(), value};
        }

        if (dll.size() > n) {
            // delete last key (least recently used)
            keyToNode.erase(dll.back());
            dll.pop_back();
        }
    }
};

void p2() {
    // Problem 2 : Leetcode 146. LRU Cache - https://leetcode.com/problems/lru-cache/ 

    int capacity = 5;
    cout << "Initialised :: " << endl;
    LRUCache lru = LRUCache(capacity);

    lru.put(1, 1);
    lru.put(2, 2);
    cout << "get 2 :: " << lru.get(2) << " ";
    lru.put(3, 3);
    cout << "get 1 :: " << lru.get(1) << " ";
    cout << "get 3 :: " << lru.get(3) << " ";
    cout << "get 2 :: " << lru.get(2) << " ";
    lru.put(2, 5);
    cout << "get 1 :: " << lru.get(1) << " ";
    cout << "get 3 :: " << lru.get(3) << " ";
    cout << "get 2 :: " << lru.get(2) << " ";
}

int main() {
    // Day 22 

    p1();

    p2();
    

    return 0;
}