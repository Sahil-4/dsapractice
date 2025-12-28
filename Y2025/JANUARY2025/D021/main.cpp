#include <bits/stdc++.h>

using namespace std;

class TreeNode {
public:

    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}

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
    int countDepth1(TreeNode* root) {
        if (root == nullptr) return 0;

        int l = countDepth1(root->left);
        int r = countDepth1(root->right);

        return max(l, r) + 1;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(D) 
    }

    int countDepth2(TreeNode* root) {
        if (root == nullptr) return 0;

        int depth = 0;

        deque<TreeNode*> dq;
        dq.push_back(root);

        while (!dq.empty()) {
            depth++;
            int N = dq.size();
            for (int i = 0; i < N; i++) {
                TreeNode* node = dq.front();
                dq.pop_front();
                if (node->left) dq.push_back(node->left);
                if (node->right) dq.push_back(node->right);
            }
        }

        return depth;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(H) 
    }

public:
    int maxDepth(TreeNode* root) {
        // ways to solve 
        // 1. count depth using recursion 
        // 2. use level order traversal 

        // return countDepth1(root);

        return countDepth2(root);
    }
};

void p1() {
    // Problem 1 : Leetcode 104. Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/maximum-depth-of-binary-tree/0 

    TreeNode* root = new TreeNode(0);
    root->left = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);
    root->right->left->right = new TreeNode(4);

    cout << Problem1().maxDepth(root);
}

class Problem2 {
    bool isSamePreOrder(TreeNode* p, TreeNode* q) {
        if (p == nullptr && q == nullptr) return true;

        if (p == nullptr && q != nullptr) return false;
        if (p != nullptr && q == nullptr) return false;

        if (p->val != q->val) return false;

        bool checkl = isSamePreOrder(p->left, q->left);
        if (!checkl) return checkl;

        return isSamePreOrder(p->right, q->right);

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(D) 
    }

public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // we can solve it using any traversal 
        // just we have to traverse both trees together 

        return isSamePreOrder(p, q);
    }
};

void p2() {
    // Problem 2 : Leetcode 100. Same Tree - https://leetcode.com/problems/same-tree/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1 

    TreeNode* root1 = new TreeNode(0);
    root1->left = new TreeNode(1);
    root1->right = new TreeNode(2);
    root1->right->left = new TreeNode(3);
    root1->right->left->right = new TreeNode(4);
    TreeNode* root2 = new TreeNode(0);
    root2->right = new TreeNode(2);
    root2->right->left = new TreeNode(3);
    root2->right->left->right = new TreeNode(4);

    cout << Problem2().isSameTree(root1, root1);
    cout << Problem2().isSameTree(root1, root2);
}

class Problem3 {
public:
    TreeNode* invertTree(TreeNode* root) {
        // better to use pre order to ease the things 

        if (root == nullptr) return root;

        TreeNode* tright = root->right;
        root->right = invertTree(root->left);
        root->left = invertTree(tright);

        return root;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(D) 
    }
};

void p3() {
    // Problem 3 : Leetcode 226. Invert Binary Tree - https://leetcode.com/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/mirror-tree/0 

    TreeNode* root = new TreeNode(0);
    root->left = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);
    root->right->left->right = new TreeNode(4);
    TreeNode::print(root);

    Problem3().invertTree(root);
    TreeNode::print(root);
}

class Problem4 {
    bool isSymmetricDFS(TreeNode* p, TreeNode* q) {
        if (p == nullptr && q == nullptr) return true;

        if (p == nullptr && q != nullptr) return false;
        if (p != nullptr && q == nullptr) return false;

        if (p->val != q->val) return false;

        bool checkA = isSymmetricDFS(p->left, q->right);
        if (!checkA) return checkA;

        return isSymmetricDFS(p->right, q->left);

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(H) 
    }

    int MARK = -10001;

    bool isSymmetricBFS(TreeNode* root) {
        deque<TreeNode*> dq;
        dq.push_back(root);

        while (!dq.empty()) {
            int S = dq.size();

            vector<int> vals;

            for (int i = 0; i < S; i++) {
                TreeNode* n = dq.front(); dq.pop_front();

                if (n->left) {
                    vals.push_back(n->left->val);
                    dq.push_back(n->left);
                }
                else {
                    vals.push_back(MARK);
                }

                if (n->right) {
                    vals.push_back(n->right->val);
                    dq.push_back(n->right);
                }
                else {
                    vals.push_back(MARK);
                }
            }

            int l = 0, r = vals.size() - 1;
            while (l < r) {
                if (vals[l] != vals[r]) return false;
                l++, r--;
            }
        }

        return true;

        // Complexity analysis 
        // Time : O(2N) 
        // Space : O(2H) 
    }

public:
    bool isSymmetric(TreeNode* root) {
        // return isSymmetricDFS(root->left, root->right);

        return isSymmetricBFS(root);
    }
};

void p4() {
    // Problem 4 : Leetcode 101. Symmetric Tree - https://leetcode.com/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/symmetric-tree/1 

    TreeNode* root = TreeNode::construct({ 1,2,2,3,4,4,3,5,6,-10000,7,-10000,7,6,5 }, -10000);
    TreeNode::print(root);
    cout << Problem4().isSymmetric(root) << endl;
}


int main() {
    // Day 21 of January 

    p1();

    p2();

    p3();

    p4();


    return 0;
}
