#include <bits/stdc++.h>

using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }

    Node* setNext(int x) {
        this->next = new Node(x);
        this->next;
    }

    void print() {
        Node* temp = this;
        cout << "printing linked list" << endl;
        while (temp != nullptr) {
            cout << temp->val << " ";
            temp = temp->next;
        }
        cout << endl;
    }
};

struct ListNode {
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
    bool detectCycle1(ListNode* head) {
        ListNode* node = head;
        set<ListNode*> st;

        while (node != nullptr) {
            if (!st.insert(node).second) break;
            node = node->next;
        }

        return node != nullptr;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(N) 
    }

    bool detectCycle2(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast != nullptr) {
            slow = slow->next;
            fast = fast->next;
            if (fast != nullptr) fast = fast->next;
            if (slow == fast) break;
        }

        return fast != nullptr;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

public:
    bool hasCycle(ListNode* head) {
        // return detectCycle1(head);

        return detectCycle1(head);
    }
};

void p1() {
    // Problem 1 : Leetcode 141. Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1 

    ListNode* head = new ListNode(1);
    head->setNext(2)->setNext(3)->setNext(4)->setNext(5);

    cout << Problem1().hasCycle(head) << endl;

    // add cycle 
    head->next->next->next->next = head->next->next;

    cout << Problem1().hasCycle(head) << endl;
}

class Problem2 {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* temp = head;
        int carry = 0;

        while (l1 != nullptr && l2 != nullptr) {
            int sum = l1->val + l2->val + carry;

            int c = sum % 10;
            carry = sum / 10;

            temp->next = new ListNode(c);

            l1 = l1->next;
            l2 = l2->next;
            temp = temp->next;
        }

        while (l1 != nullptr) {
            int sum = l1->val + carry;

            int c = sum % 10;
            carry = sum / 10;

            temp->next = new ListNode(c);

            l1 = l1->next;
            temp = temp->next;
        }

        while (l2 != nullptr) {
            int sum = l2->val + carry;

            int c = sum % 10;
            carry = sum / 10;

            temp->next = new ListNode(c);

            l2 = l2->next;
            temp = temp->next;
        }

        while (carry != 0) {
            int sum = carry;

            int c = sum % 10;
            carry = sum / 10;

            temp->next = new ListNode(c);

            temp = temp->next;
        }

        return head->next;

        // Complexity analysis 
        // Time : O(max(N,M)) 
        // Space : O(1) 
    }
};

void p2() {
    // Problem 2 : Leetcode 2. Add Two Numbers - https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1 

    ListNode* l1 = new ListNode(1);
    l1->setNext(2)->setNext(3);
    ListNode* l2 = new ListNode(1);
    l2->setNext(2)->setNext(3);

    ListNode* sum = Problem2().addTwoNumbers(l1, l2);
    sum->print();
}

class Problem3 {
    ListNode* solve1(ListNode* h1, ListNode* h2) {

        ListNode* head = new ListNode();
        ListNode* temp = head;

        while (h1 != nullptr && h2 != nullptr) {
            if (h1->val <= h2->val) {
                temp->next = h1;
                h1 = h1->next;
                temp = temp->next;
            }
            else {
                temp->next = h2;
                h2 = h2->next;
                temp = temp->next;
            }
        }

        while (h1 != nullptr) {
            temp->next = h1;
            h1 = h1->next;
            temp = temp->next;
        }

        while (h2 != nullptr) {
            temp->next = h2;
            h2 = h2->next;
            temp = temp->next;
        }

        return head->next;

        // Complexity analysis 
        // Time : O(max(N, M))
        // Space : O(1) 
    }

    ListNode* solve2(ListNode* h1, ListNode* h2) {
        if (h1 == nullptr) return h2;
        if (h2 == nullptr) return h1;

        if (h1->val <= h2->val) {
            h1->next = solve2(h1->next, h2);
            return h1;
        }
        else {
            h2->next = solve2(h1, h2->next);
            return h2;
        }

        // Complexity analysis 
        // Time : O(min(N, M))
        // Space : O(min(N, M)) 
    }

public:
    ListNode* mergeTwoLists(ListNode* h1, ListNode* h2) {
        // return solve1(h1, h2);

        return solve2(h1, h2);
    }
};

void p3() {
    // Problem 3 : Leetcode 21. Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1 

    ListNode* l1 = new ListNode();
    l1->setNext(1)->setNext(5)->setNext(8)->setNext(12);
    ListNode* l2 = new ListNode();
    l2->setNext(1)->setNext(3)->setNext(4)->setNext(5);

    ListNode* head = Problem3().mergeTwoLists(l1, l2);
    head->print();
}

class Problem4 {
public:
    Node* copyRandomList(Node* head) {
        Node* nhead = new Node(0);

        Node* temp = nullptr;
        Node* ntemp = nhead;

        // create duplicate nodes 
        temp = head;
        while (temp != nullptr) {
            Node* nnode = new Node(temp->val);
            nnode->next = temp->next;
            temp->next = nnode;
            temp = temp->next->next;
        }

        // set random pointers 
        temp = head;
        while (temp != nullptr) {
            if (temp->random != nullptr) {
                temp->next->random = temp->random->next;
            }
            temp = temp->next->next;
        }

        // seperate both lists 
        temp = head;
        while (temp != nullptr) {
            ntemp->next = temp->next;
            temp->next = temp->next->next;
            ntemp = ntemp->next;
            temp = temp->next;
        }

        return nhead->next;
    }
};

void p4() {
    // Problem 4 : Leetcode 138. Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/0 

    Node* head = new Node(1);
    head->setNext(2)->setNext(3)->setNext(5);

    Node* h = Problem4().copyRandomList(head);
    h->print();
}

class Problem5 {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (head == nullptr || head->next == nullptr) return head;

        ListNode* dummy = new ListNode(0, head);

        ListNode* prev = dummy;
        for (int i = 1; i < left; i++) prev = prev->next;

        ListNode* curr = prev->next;

        for (int i = 1; i <= right - left; i++) {
            ListNode* next = prev->next;
            prev->next = curr->next;
            curr->next = curr->next->next;
            prev->next->next = next;
        }

        return dummy->next;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }
};

void p5() {
    // Problem 5 : Leetcode 92. Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/reverse-a-sublist-of-a-linked-list/0 

    ListNode* head = new ListNode(0);
    head->setNext(1)->setNext(2)->setNext(3)->setNext(4)->setNext(5);

    ListNode* nhead = Problem5().reverseBetween(head, 2, 3);
    nhead->print();
}


int main() {
    // Day 18 of January 2025 

    p1();

    p2();

    p3();

    p4();

    p5();


    return 0;
}
