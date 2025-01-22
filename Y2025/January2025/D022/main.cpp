#include <bits/stdc++.h>

using namespace std;


class TreeNode {
public:
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode* next;

    // TreeNode() : val(0), left(nullptr), right(nullptr) {}
    // TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}

    TreeNode() : val(0), left(NULL), right(NULL), next(NULL) {}
    TreeNode(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}
    TreeNode(int _val, TreeNode* _left, TreeNode* _right, TreeNode* _next)
        : val(_val), left(_left), right(_right), next(_next) {
    }

    static void print(TreeNode* node) {
        // pre order traversal 
        if (node == nullptr) {
            cout << endl;
            return;
        }

        cout << node->val << " ";

        print(node->left);
        print(node->right);
    }

    static void printNext(TreeNode* root) {
        if (root == nullptr) return;
        stack<TreeNode*> stk;
        stk.push(root);

        while (!stk.empty()) {
            int L = stk.size();
            TreeNode* temp = stk.top();

            for (int i = 0; i < L; i++) {
                TreeNode* node = stk.top(); stk.pop();
                if (node->right != nullptr) stk.push(node->right);
                if (node->left != nullptr) stk.push(node->left);
            }

            while (temp != nullptr) {
                cout << temp->val << " ";
                temp = temp->next;
            }
        }
    }

    // v = preorder traversal 
    static TreeNode* construct(vector<int> v, int MARK) {
        if (v.size() == 0 || v[0] == MARK) return nullptr;

        TreeNode* root = new TreeNode(v[0]);

        deque<TreeNode*> dq;
        dq.push_back(root);

        for (int i = 1; i < v.size();) {
            TreeNode* r = dq.front(); dq.pop_front();
            if (v[i] != MARK) {
                r->left = new TreeNode(v[i]);
                dq.push_back(r->left);
            }
            i++;
            if (v[i] != MARK) {
                r->right = new TreeNode(v[i]);
                dq.push_back(r->right);
            }
            i++;
        }

        return root;
    }
};

class Problem1 {
    TreeNode* buildTree(vector<int>& preorder, unordered_map<int, int>& inorderE2IMap, int pi, int pj, int ii, int ij) {
        if (pi > pj || ii > ij) return nullptr;

        TreeNode* root = new TreeNode(preorder[pi]);

        // number of nodes on left 
        int ln = inorderE2IMap[preorder[pi]] - ii;

        root->left = buildTree(preorder, inorderE2IMap, pi + 1, pi + ln, ii, ii + ln);
        root->right = buildTree(preorder, inorderE2IMap, pi + ln + 1, pj, ii + ln + 1, ij);

        return root;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(H) 
    }

public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int nodes = preorder.size();

        // element to index map for inorder 
        unordered_map<int, int> inorderE2IMap;
        for (int i = 0; i < inorder.size(); i++) inorderE2IMap[inorder[i]] = i;

        return buildTree(preorder, inorderE2IMap, 0, nodes - 1, 0, nodes - 1);
    }
};

void p1() {
    // Problem 1 : Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal - https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/construct-tree-1/1 

    vector<int> pre = { 3,9,20,15,7 };
    vector<int> in = { 9,3,15,20,7 };

    TreeNode* root = Problem1().buildTree(pre, in);
    TreeNode::print(root);
}

class Problem2 {
    TreeNode* buildTree(vector<int>& postorder, unordered_map<int, int>& inorderE2IMap, int pi, int pj, int ii, int ij) {
        if (pi > pj || ii > ij) return nullptr;

        TreeNode* root = new TreeNode(postorder[pj]);

        // number of nodes on left
        int ei = inorderE2IMap[postorder[pj]];
        int ln = ei - ii;

        root->left = buildTree(postorder, inorderE2IMap, pi, pi + ln - 1, ii, ei - 1);
        root->right = buildTree(postorder, inorderE2IMap, pi + ln, pj - 1, ei + 1, ij);

        return root;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(H) 
    }

public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int nodes = postorder.size();

        // element to index map for inorder 
        unordered_map<int, int> inorderE2IMap;
        for (int i = 0; i < inorder.size(); i++) inorderE2IMap[inorder[i]] = i;

        return buildTree(postorder, inorderE2IMap, 0, nodes - 1, 0, nodes - 1);
    }
};

void p2() {
    // Problem 2 : Leetcode 106. Construct Binary Tree from Inorder and Postorder Traversal - https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/tree-from-postorder-and-inorder/1 

    vector<int> post = { 9,3,15,20,7 };
    vector<int> in = { 9,15,7,20,3 };

    TreeNode* root = Problem2().buildTree(post, in);
    TreeNode::print(root);
}

class Problem3 {
public:
    TreeNode* connect(TreeNode* root) {
        deque<TreeNode*> dq;

        if (root != nullptr) dq.push_front(root);

        while (!dq.empty()) {
            int L = dq.size();

            TreeNode* prev = nullptr;
            TreeNode* curr = nullptr;

            for (int i = 0; i < L; i++) {
                curr = dq.front(); dq.pop_front();

                if (prev != nullptr) prev->next = curr;

                if (curr->left) dq.push_back(curr->left);
                if (curr->right) dq.push_back(curr->right);

                prev = curr;
            }
        }

        return root;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(W) 
    }
};

void p3() {
    // Problem 3 : Leetcode 117. Populating Next Right Pointers in Each Node II - https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/connect-nodes-at-same-level/1 

    TreeNode* root = TreeNode::construct({ 1, 2, 4, 5, 3, 6, -1 }, -1);

    Problem3().connect(root);

    TreeNode::print(root);
    TreeNode::printNext(root);
}

class Problem4 {
    void traverse(TreeNode* root, vector<TreeNode*>& ls) {
        if (root == nullptr) return;

        ls.push_back(root);

        traverse(root->left, ls);
        traverse(root->right, ls);
    }

    void solve1(TreeNode* root) {
        vector<TreeNode*> ls;

        // preorder traversal 
        traverse(root, ls);

        TreeNode* temp = root;

        for (int i = 1; i < ls.size(); i++) {
            temp->right = ls[i];
            temp->left = nullptr;
            temp = temp->right;
        }

        // Complexity analysis 
        // Time : O(N) + O(N) 
        // Space : O(N) + O(H) 
    }

    void solve2(TreeNode* root) {
        TreeNode* temp = root;

        while (temp != nullptr) {
            if (temp->left == nullptr) {
                temp = temp->right;
            }
            else {
                // find most right node on left of temp node 
                TreeNode* rightest = temp->left;
                while (rightest->right != nullptr) rightest = rightest->right;

                // connect rightest->right to temp->right 
                rightest->right = temp->right;

                // update/change links 
                temp->right = temp->left;
                temp->left = nullptr;

                // move to left (pointer is changed to right) 
                temp = temp->right;
            }
        }

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

public:
    void flatten(TreeNode* root) {
        // return solve1(root);

        return solve2(root);
    }
};

void p4() {
    // Problem 4 : Leetcode 114. Flatten Binary Tree to Linked List - https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/flatten-binary-tree-to-linked-list/1 

    TreeNode* root = TreeNode::construct({ 1, 2, 3, 4, 5, -1, 6 }, -1);

    TreeNode::print(root);

    Problem4().flatten(root);

    TreeNode::print(root);
}


int main() {
    // Day 22 of January 2025 

    p1();

    p2();

    p3();

    p4();


    return 0;
}