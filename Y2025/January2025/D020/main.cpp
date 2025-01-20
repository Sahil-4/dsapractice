#include <bits/stdc++.h>

using namespace std;

class ListNode {
public:
    int val;
    ListNode* next;

    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}

    ListNode* setNext(int x) {
        this->next = new ListNode(x);
        this->next;
    }

    void print() {
        ListNode* temp = this;
        cout << "printing linked list" << endl;
        while (temp != nullptr) {
            cout << temp->val << " ";
            temp = temp->next;
        }
        cout << endl;
    }
};


class Problem1 {
    int MARK = -10000;

public:
    ListNode* partitionSEG(ListNode* head, int x) {
        // [ ...smalls, ...equals, ...greater ] 

        ListNode* d1 = new ListNode(MARK);
        ListNode* d2 = new ListNode(MARK);
        ListNode* d3 = new ListNode(MARK);

        ListNode* d1t = d1;
        ListNode* d2t = d2;
        ListNode* d3t = d3;

        while (head != nullptr) {
            ListNode* next = head->next;
            head->next = nullptr;

            if (head->val < x) {
                d1t->next = head;
                d1t = d1t->next;
            }
            else if (head->val == x) {
                d2t->next = head;
                d2t = d2t->next;
            }
            else {
                d3t->next = head;
                d3t = d3t->next;
            }

            head = next;
        }

        d1t->next = d2->next;
        d2t->next = d3->next;
        d3t->next = nullptr;

        return d1->next;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

    ListNode* partition(ListNode* head, int x) {
        // [ ...smalls, ...rest ] 

        ListNode* d1 = new ListNode(MARK);
        ListNode* d2 = new ListNode(MARK);

        ListNode* d1t = d1;
        ListNode* d2t = d2;

        while (head != nullptr) {
            ListNode* next = head->next;
            head->next = nullptr;

            if (head->val < x) {
                d1t->next = head;
                d1t = d1t->next;
            }
            else {
                d2t->next = head;
                d2t = d2t->next;
            }

            head = next;
        }

        d1t->next = d2->next;

        return d1->next;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }
};

void p1() {
    // Problem 1:  Leetcode 86. Partition List - https://leetcode.com/problems/partition-list/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/partition-a-linked-list-around-a-given-value/1 

    ListNode* head = new ListNode(0);
    head->setNext(1)->setNext(2)->setNext(1)->setNext(3)->setNext(4)->setNext(5);
    head->print();

    ListNode* nhead = Problem1().partition(head, 1);
    nhead->print();
}

class LRUCache {
    // number of keys we can have
    int capacity = 0;

    list<int> keys; // to store keys according to use time
    // most recently used will be in front and least recently used will be at last

    unordered_map<int, pair<list<int>::iterator, int>> key2AddrVal; // key to <address of key in dll:list, value corresponds to key>

    void makeItRecentlyUsed(int key) {
        // first remove this key from list 
        keys.erase(key2AddrVal[key].first);

        // put it at the beginning - to make it most recent 
        keys.push_front(key);

        // then update address of key in list in map 
        key2AddrVal[key].first = keys.begin();
    }

    void removeLRU() {
        // remove very last used or least recently used 
        key2AddrVal.erase(keys.back());
        keys.pop_back();
        capacity++;
    }

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }

    int get(int key) {
        if (key2AddrVal.find(key) == key2AddrVal.end()) return -1;
        makeItRecentlyUsed(key);
        return key2AddrVal[key].second;
    }

    void put(int key, int value) {
        if (key2AddrVal.find(key) == key2AddrVal.end()) {
            if (capacity == 0) removeLRU();
            keys.push_front(key);
            key2AddrVal[key] = { keys.begin(), value };
            capacity--;
        }
        else {
            key2AddrVal[key].second = value;
            makeItRecentlyUsed(key);
        }
    }
};

void p2() {
    // Problem 2 : Leetcode 146. LRU Cache - https://leetcode.com/problems/lru-cache/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/lru-cache/1 

    LRUCache* lru = new LRUCache(2);
    lru->put(1, 1);
    assert(lru->get(1) == 1);
    assert(lru->get(2) == -1);
    lru->put(2, 2);
    assert(lru->get(2) == 2);
    lru->put(3, 3);
    lru->put(4, 4);
    assert(lru->get(2) == -1);
    assert(lru->get(1) == -1);
}


int main() {
    // Day 20 of January 2025 

    p1();

    p2();


    return 0;
}