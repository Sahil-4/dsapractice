#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode *detectCycle_Solution1(ListNode *head) {
    map<ListNode*, bool> table;

    while (head != NULL && head->next != NULL) {
        if (table[head]) return head;

        table[head] = true;

        head = head->next;
    }

    return NULL;

    // Complexity analysis 
    // Time : O(n) 
    // Space : O(n) 
}

ListNode *detectCycle(ListNode *head) {
    ListNode *slow = head;
    ListNode *fast = head;
    bool loop = false;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            loop = true;
            break;
        }
    }

    ListNode *temp = head;
    while (loop) {
        if (temp == slow) return slow;

        temp = temp->next;
        slow = slow->next;
    }

    return NULL;

    // Complexity analysis 
    // Time : O(n) 
    // Space : O(1) 
}

void p1() {
    // Probelm 1 : Leetcode 142. Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1 

    ListNode *head_node = new ListNode(3);
    ListNode *node2 = new ListNode(2);
    head_node->next = node2;
    ListNode *node3 = new ListNode(5);
    node2->next= node3;
    ListNode *node4 = new ListNode(4);
    node3->next = node4;

    node4->next = node3; // cycle 
    // node4->next = NULL; // no cycle 

    ListNode *start = detectCycle(head_node);
    if (start != NULL) cout << "cycle starts at : " << start->val << endl;
    else cout << "no cycle" << endl; 
}

bool isPalindrome_Solution1(ListNode* head) {
    string str = "";
    string copy = "";

    ListNode *temp = head;

    while (temp != NULL) {
        str += '0' + temp->val;
        temp = temp->next;
    }

    copy = str;
    reverse(str.begin(), str.end());

    return str == copy;

    // Complexity analysis 
    // Time : O(n) 
    // Space : O(n), string 
}

ListNode* middle(ListNode *head) {
    ListNode *slow = head;
    ListNode *fast = head;

    while (fast->next != NULL && fast->next->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    return slow;
}

ListNode* reverse(ListNode *head) {
    ListNode *curr = head;
    ListNode *prev = NULL;
    ListNode *next = head;

    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    return prev;
}

bool checkPalindrome(ListNode *head1, ListNode *head2) {
    while (head1 != NULL && head2 != NULL) {
        if (head1->val != head2->val) return false;

        head1 = head1->next;
        head2 = head2->next;
    }

    return true;
}

bool isPalindrome(ListNode* head) {
    if (head->next == NULL) return true;

    ListNode *mid = middle(head);
    ListNode *l2 = reverse(mid->next);
    mid->next = NULL;

    bool check = checkPalindrome(head, l2);

    ListNode *l2r = reverse(l2);
    mid->next = l2r;

    return check;
}

void p2() {
    // Problem 2 : Leetcode 234. Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1 

    ListNode *head_node = new ListNode(3);
    ListNode *n2 = new ListNode(2);
    head_node->next = n2;
    ListNode *n3 = new ListNode(2);
    n2->next= n3;
    ListNode *n4 = new ListNode(3);
    n3->next = n4;

    bool check = isPalindrome(head_node);
    cout << "isPalindrome ::" << check << endl;
}

int main() {
    // Day 26 

    p1();

    p2();


    return 0;
}