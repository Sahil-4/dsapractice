#include <bits/stdc++.h>

using namespace std;

class MyHashSet {
private:
    const int BOUND = 1e6 + 1;
    const int LF = 1000; // root of BOUND 
    vector<list<int>> set;

    int hash(int key) {
        int index = key % LF;
        return index;
    }

public:
    MyHashSet() {
        set.resize(LF, list<int>{});
    }

    void add(int key) {
        int index = hash(key);
        auto pos = find(set[index].begin(), set[index].end(), key);
        if (pos == set[index].end()) set[index].push_back(key);
    }

    void remove(int key) {
        int index = hash(key);
        auto pos = find(set[index].begin(), set[index].end(), key);
        if (pos != set[index].end()) set[index].erase(pos);
    }

    bool contains(int key) {
        int index = hash(key);
        auto pos = find(set[index].begin(), set[index].end(), key);
        return (pos != set[index].end());
    }

    // Complexity analysis 
    // Time : O(root of BOUND) 
    // Space : O(BOUND) 
};


void p1() {
    // Problem 1 : Leetcode 705. Design HashSet - https://leetcode.com/problems/design-hashset/ 

    MyHashSet* hs = new MyHashSet();
    hs->add(5);
    hs->add(5);
    cout << hs->contains(55) << endl;
    cout << hs->contains(5) << endl;
    hs->add(10000);
    cout << hs->contains(10000) << endl;
    hs->remove(10000);
    cout << hs->contains(10000) << endl;
    cout << hs->contains(5) << endl;
}

class MyHashMap {
private:
    const int BOUND = 1e6 + 1;
    const int LF = 1000;
    vector<list<pair<int, int>>> mp;

    int hash(int key) {
        int index = key % LF;
        return index;
    }

public:
    MyHashMap() {
        mp.resize(LF, list<pair<int, int>>{});
    }

    void put(int key, int value) {
        int index = hash(key);

        list<pair<int, int>>& branch = mp[index];

        for (auto& it : branch) {
            if (it.first == key) {
                it.second = value;
                return;
            }
        }

        branch.emplace_back(key, value);
    }

    int get(int key) {
        int index = hash(key);

        list<pair<int, int>>& branch = mp[index];

        for (auto& it : branch) {
            if (it.first == key) return it.second;
        }

        return -1;
    }

    void remove(int key) {
        int index = hash(key);

        list<pair<int, int>>& branch = mp[index];

        for (auto it = branch.begin(); it != branch.end(); it++) {
            if (it->first == key) {
                branch.erase(it);
                return;
            }
        }
    }

    // Complexity analysis 
    // Time : O(LF) for init, O(LF) for put, get, and remove operation 
    // Space : O(BOUND) 
};


void p2() {
    // Problem 2 : Leetcode 706. Design HashMap - https://leetcode.com/problems/design-hashmap/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/design-hashmap/1 

    MyHashMap* hm = new MyHashMap();
    cout << hm->get(5) << endl;
    hm->put(5, 55);
    cout << hm->get(5) << endl;
    hm->put(5, 555);
    cout << hm->get(5) << endl;
    hm->remove(5);
    cout << hm->get(5) << endl;
}

int main() {
    // Day 12 of December 

    p1();

    p2();


    return 0;
}