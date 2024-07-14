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


int main() {
    // Day 14 

    p1();


    return 0;
}