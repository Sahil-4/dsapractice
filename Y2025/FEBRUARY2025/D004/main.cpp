#include <bits/stdc++.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}

    ListNode* setNext(int val) {
        this->next = new ListNode(val);
        return this->next;
    }

    void printList() {
        ListNode* temp = this;
        while (temp != nullptr) {
            cout << temp->val << " ";
        } cout << endl;
    }
};

class Problem1 {
    TreeNode* fn(vector<int>& arr, int l, int h) {
        if (l > h) return nullptr;

        int m = l + (h - l) / 2;
        return new TreeNode(arr[m], fn(arr, l, m - 1), fn(arr, m + 1, h));
    }

public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return fn(nums, 0, nums.size() - 1);

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(log(N)) stack 
    }
};

void p1() {
    // Problem 1 : Leetcode 108. Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/array-to-bst4443/1 

    vector<int> nums = { 1,2,3,4,5,6,7 };
    TreeNode* root = Problem1().sortedArrayToBST(nums);
}

class Problem2 {
    bool comparator(int a, int b) {
        return a <= b;
    }

    void partition(ListNode* head, ListNode*& left, ListNode*& right) {
        ListNode* slow = head, * fast = head;

        while (fast->next != nullptr && fast->next->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        left = head;
        right = slow->next;
        slow->next = nullptr;
    }

    ListNode* merge(ListNode* left, ListNode* right) {
        if (left == nullptr) return right;
        if (right == nullptr) return left;

        ListNode* root = nullptr;

        if (comparator(left->val, right->val)) {
            root = left;
            root->next = merge(left->next, right);
        }
        else {
            root = right;
            root->next = merge(left, right->next);
        }

        return root;
    }

public:
    ListNode* sortList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;

        ListNode* left, * right;
        partition(head, left, right);

        return merge(sortList(left), sortList(right));

        // Complexity analysis 
        // Time : O(N * Log(N)) 
        // Space : O(log(N)) stack 
    }
};

void p2() {
    // Problem 2 : Leetcode 148. Sort List - https://leetcode.com/problems/sort-list/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/sort-a-linked-list/1 

    ListNode* head = new ListNode(0);
    head->setNext(4)->setNext(2)->setNext(1)->setNext(3);
    head->next->printList();

    head->next = Problem2().sortList(head->next);
    head->next->printList();
}


int main() {
    // Day 4 of February 

    p1();

    p2();


    return 0;
}