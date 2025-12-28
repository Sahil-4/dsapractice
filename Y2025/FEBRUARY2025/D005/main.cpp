#include <bits/stdc++.h>

using namespace std;

// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;

    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }

    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }

    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }

    void print() {
        vector<vector<int>> v;
        queue<Node*> que;
        que.push(this);

        while (!que.empty()) {
            Node* temp = que.front(); que.pop();

            v.push_back({ temp->val, temp->isLeaf });

            if (temp->topLeft) que.push(temp->topLeft);
            if (temp->topRight) que.push(temp->topRight);
            if (temp->bottomLeft) que.push(temp->bottomLeft);
            if (temp->bottomRight) que.push(temp->bottomRight);
        }

        for (vector<int> e : v) cout << e[1] << " " << e[0] << endl;
    }
};

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
    Node* construct(vector<vector<int>>& grid, int istart, int iend, int jstart, int jend) {
        if (istart > iend || jstart > jend) return nullptr;
        if (istart == iend && jstart == jend) {
            return new Node(grid[istart][jstart], true);
        }

        bool allZeroes = true;
        bool allOnes = true;

        for (int i = istart; i <= iend; i++) {
            for (int j = jstart; j <= jend; j++) {
                allZeroes = allZeroes && grid[i][j] == 0;
                allOnes = allOnes && grid[i][j] == 1;
            }
        }

        if (allZeroes || allOnes) {
            return new Node(allOnes, true);
        }

        Node* node = new Node(-1, false);

        int imid = istart + ((iend - istart) / 2);
        int jmid = jstart + ((jend - jstart) / 2);

        node->topLeft = construct(grid, istart, imid, jstart, jmid);
        node->topRight = construct(grid, istart, imid, jmid + 1, jend);
        node->bottomLeft = construct(grid, imid + 1, iend, jstart, jmid);
        node->bottomRight = construct(grid, imid + 1, iend, jmid + 1, jend);

        return node;
    }

public:
    Node* construct(vector<vector<int>>& grid) {
        int N = grid.size();
        return construct(grid, 0, N - 1, 0, N - 1);

        // Complexity analysis 
        // Time : O((N^2) + 4^log4(N)) 
        // Space : O(log4(N)) 
    }
};

void p1() {
    // Problem 1 : Leetcode 427. Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/?envType=study-plan-v2&envId=top-interview-150 

    vector<vector<int>> grid = { {1,1,1,1,0,0,0,0},{1,1,1,1,0,0,0,0},{1,1,1,1,1,1,1,1},{1,1,1,1,1,1,1,1},{1,1,1,1,0,0,0,0},{1,1,1,1,0,0,0,0},{1,1,1,1,0,0,0,0},{1,1,1,1,0,0,0,0} };
    Node* root = Problem1().construct(grid);
    root->print();
}

class Problem2 {
    bool canTraverse(vector<ListNode*>& lists) {
        for (ListNode* node : lists) {
            if (node != nullptr) return true;
        }
        return false;
    }

    ListNode* mergeKLists1(vector<ListNode*>& lists) {
        // vector<ListNode*> copy(lists);

        ListNode* dummy = new ListNode(-1);
        ListNode* temp = dummy;

        while (canTraverse(lists)) {
            int mini = -1;
            for (int i = 0; i < lists.size(); i++) {
                if (lists[i] != nullptr && (mini == -1 || lists[i]->val < lists[mini]->val)) {
                    mini = i;
                }
            }

            temp->next = lists[mini];
            temp = temp->next;
            lists[mini] = lists[mini]->next;
        }

        return dummy->next;

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(1) 
    }

    struct Compare {
        bool operator()(ListNode* l1, ListNode* l2) {
            return l1->val > l2->val;
        }
    };

    ListNode* mergeKLists2(vector<ListNode*>& lists) {
        ListNode* dummy = new ListNode(-1);
        ListNode* temp = dummy;

        priority_queue<ListNode*, vector<ListNode*>, Compare> pq;
        for (ListNode* list : lists) {
            if (list != nullptr) pq.push(list);
        }

        while (!pq.empty()) {
            ListNode* node = pq.top(); pq.pop();

            temp->next = node;
            temp = temp->next;

            if (node->next != nullptr) pq.push(node->next);
        }

        return dummy->next;

        // Complexity analysis 
        // Time : O(N*log(N)) 
        // Space : O(O(L)) 
    }

public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // return mergeKLists1(lists);

        return mergeKLists2(lists);
    }
};

void p2() {
    // Problem 2 : Leetcode 23. Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1 

    // [[1,4,5],[1,3,4],[2,6]]
    ListNode* l1 = new ListNode(1);
    l1->setNext(4)->setNext(5);
    ListNode* l2 = new ListNode(1);
    l2->setNext(3)->setNext(4);
    ListNode* l3 = new ListNode(2);
    l3->setNext(6);

    vector<ListNode*> lists = { l1, l2, l3 };

    // [1,1,2,3,4,4,5,6]
    ListNode* l = Problem2().mergeKLists(lists);
    l->print();
}


int main() {
    // Day 5 of February 

    p1();

    p2();


    return 0;
}