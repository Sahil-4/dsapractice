#include <iostream>
#include <list>
#include <unordered_map>

using namespace std;

class LRUCache {
private:
    int cap;
    list<int> keys;
    // map<int, pair<list<int>::iterator,int>> nodes; // !TLE 
    unordered_map<int, pair<list<int>::iterator,int>> nodes;

    void makeRecent(int key) {
        keys.erase(nodes[key].first);

        keys.push_front(key);

        nodes[key].first = keys.begin();
    }

public:
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        if (nodes.find(key) == nodes.end()) return -1;

        makeRecent(key);

        return nodes[key].second;
    }
    
    void put(int key, int value) {
        if (nodes.find(key) == nodes.end()) {
            keys.push_front(key);
            nodes[key] = { keys.begin(), value };

            if (keys.size() > cap) {
                nodes.erase(keys.back());
                keys.pop_back();
            }
        } else {
            nodes[key].second = value;
            makeRecent(key);
        }
    }
};

void p1() {
    // Problem 1 : Leetcode 146. LRU Cache - https://leetcode.com/problems/lru-cache/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/lru-cache/1 

    LRUCache lc = LRUCache(2);
    lc.put(1, 1);
    lc.put(2, 2);
    cout << lc.get(1) << " ";
    lc.put(3, 3);
    cout << lc.get(2) << " ";
    lc.put(4, 4);
    cout << lc.get(1) << " ";
    cout << lc.get(3) << " ";
    cout << lc.get(4) << " ";
    cout << endl;
}

string getSmallestString(string s) {
    int n = s.length();

    for (int i = 0; i < n; i++) {
        if (i == n - 1) break;

        int a = s[i] - '0';
        int b = s[i + 1] - '0';

        if (((a & 1) == (b & 1)) && a > b) {
            swap(s[i], s[i + 1]); break;
        }
    }

    return s;
}

void p2() {
    // P2 : Leetcode 3216. Lexicographically Smallest String After a Swap - https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/ 

    // cout << getSmallestString("3210") << endl;
    cout << getSmallestString("4210") << endl;
}


int main() {
    // Day 14 

    p1();

    p2();


    return 0;
}