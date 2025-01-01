#include <iostream>
#include <list>
#include <map>

using namespace std;

class LFUCache {
private:
typedef struct {
    int key;
    int value;
    int usedCount;
} node;

public:
    map<int, list<node>::iterator> indexTable; // <key, address of node in dll> 
    map<int, list<node>> freq2DLLTable; // <freq, list<node>> // list<node> dll 
    int leftOutSpace;

    LFUCache(int capacity) {
        leftOutSpace = capacity;
    }

    void updateFreq(int key) {
        node &n = *(indexTable[key]);

        int value = n.value;
        int freq = n.usedCount;

        freq2DLLTable[freq].erase(indexTable[key]);
        if (freq2DLLTable[freq].empty()) freq2DLLTable.erase(freq);

        freq++;
        node n2 = {key, value, freq};

        freq2DLLTable[freq].push_front(n2);
        indexTable[key] = freq2DLLTable[freq].begin();
    }

    void removeLast() {
        list<node> &ls = freq2DLLTable.begin()->second;
        int keyToDelete = (ls.back()).key;

        ls.pop_back();
        if (ls.empty()) freq2DLLTable.erase(freq2DLLTable.begin()->first);

        indexTable.erase(keyToDelete);

        leftOutSpace++;
    }

    int get(int key) {
        if (indexTable.find(key) == indexTable.end()) return -1;

        node &n = *(indexTable[key]);

        int value = n.value;

        updateFreq(key);

        return value;
    }

    void put(int key, int value) {
        if (indexTable.find(key) != indexTable.end()) {
            node &n = *(indexTable[key]);

            n.value = value;

            updateFreq(key);
        } else {
            if (leftOutSpace == 0) removeLast();

            node n = {key, value, 1};

            freq2DLLTable[1].push_front(n);
            indexTable[key] = freq2DLLTable[1].begin();

            leftOutSpace--;
        }
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

void p1() {
    // Problem 1 : Leetcode 460. LFU Cache - https://leetcode.com/problems/lfu-cache/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/lfu-cache-1665050355/1 

    LFUCache* obj = new LFUCache(3);
    cout << "1 :: " << obj->get(1) << " ";
    obj->put(1,1);
    cout << "1 :: " << obj->get(1) << " ";
    obj->put(1,11);
    cout << "1 :: " << obj->get(1) << " ";
    obj->put(2,2);
    cout << "2 :: " << obj->get(2) << " ";
    obj->put(3,3);
    cout << "3 :: " << obj->get(3) << " ";
    obj->put(2,200);
    cout << "2 :: " << obj->get(2) << " ";
}

int main() {
    // Day 23 

    p1();


    return 0;
}