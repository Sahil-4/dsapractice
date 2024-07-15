#include <iostream>
#include <map>
#include <list>

using namespace std;

class LFUCache {
private:
    typedef struct {
        int key;
        int value;
        int useCount;
    } node;

    map<int, list<node>::iterator> index; // key -> list<node>::iterator 
    map<int, list<node>> freqTable; // freq -> list<node> 
    int capacity_left;

    void updateUseCount(int key) {
        node &n = *(index[key]);

        int val = n.value;
        int freq = n.useCount;

        freqTable[freq].erase(index[key]);
        if (freqTable[freq].empty()) freqTable.erase(freq);

        freq++;
        node n2 = { key, val, freq };
        freqTable[freq].push_front(n2);
        index[key] = freqTable[freq].begin();
    }

    void remove_LFU_or_LRU() {
        list<node> &ls = freqTable.begin()->second;
        int key = (ls.back()).key;

        ls.pop_back();
        if (ls.empty()) freqTable.erase(freqTable.begin()->first);

        index.erase(key);

        capacity_left++;
    }

public:
    LFUCache(int cap) { capacity_left = cap; }

    int get(int key) {
        if (index.find(key) == index.end()) return -1;

        node &n = *(index[key]);
        int value = n.value;

        updateUseCount(key);

        return value;
    }

    void put(int key, int value) {
        if (index.find(key) != index.end()) {
            // update 
            node &n = *(index[key]);

            n.value = value;

            updateUseCount(key);
        } else {
            // add 
            if (capacity_left == 0) remove_LFU_or_LRU();

            node n = { key, value, 1 };

            freqTable[1].push_front(n);
            index[key] = freqTable[1].begin();

            capacity_left--;
        }
    }
};

void p1() {
    // Problem 1 : Leetcode 460. LFU Cache - https://leetcode.com/problems/lfu-cache/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/lfu-cache-1665050355/1 

    LFUCache lc = LFUCache(2);
    cout << "1 --> " << lc.get(1) << endl;
    lc.put(1, 1);
    cout << "1 --> " << lc.get(1) << endl;
    lc.put(2, 2);
    cout << "1 --> " << lc.get(1) << endl;
    cout << "2 --> " << lc.get(2) << endl;
    lc.put(1, 100);
    cout << "1 --> " << lc.get(1) << endl;
    cout << "2 --> " << lc.get(2) << endl;
}

int main() {
    // Day 15 

    p1();


    return 0;
}