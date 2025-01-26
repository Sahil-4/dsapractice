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
        if (node == nullptr) return;

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
    int prev;
    int mindiff;

    int __getMinimumDifference__(TreeNode* root) {
        // left | root | right ... 

        if (root == nullptr) return mindiff;

        __getMinimumDifference__(root->left);

        if (prev != INT_MAX) mindiff = min(mindiff, root->val - prev);
        prev = root->val;

        __getMinimumDifference__(root->right);

        return mindiff;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(H) 
    }

public:
    int getMinimumDifference(TreeNode* root) {
        prev = INT_MAX;
        mindiff = INT_MAX;

        return __getMinimumDifference__(root);
    }
};

void p1() {
    // Problem 1 : Leetcode 530. Minimum Absolute Difference in BST - https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/minimum-absolute-difference-in-bst-1665139652/0 

    TreeNode* root = TreeNode::construct({ 236,104,701,-1,227,-1,911 }, -1);
    cout << Problem1().getMinimumDifference(root) << endl;
}

class Problem2 {
    int kth;
    int k;

    void __kthSmallest__(TreeNode* root) {
        if (root == nullptr) return;

        __kthSmallest__(root->left);

        k--;
        if (k == 0) {
            kth = root->val;
            return;
        }

        __kthSmallest__(root->right);
    }

public:
    int kthSmallest(TreeNode* root, int K) {
        kth = 0;
        k = K;

        __kthSmallest__(root);

        return kth;
    }
};

void p2() {
    // Problem 2 : Leetcode 230. Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/find-k-th-smallest-element-in-bst/1 

    TreeNode* root = TreeNode::construct({ 100,50,200,25,75,150,250,10,30,60,80,125,175,215,275 }, -1);
    cout << Problem2().kthSmallest(root, 1) << endl;
    cout << Problem2().kthSmallest(root, 5) << endl;
    cout << Problem2().kthSmallest(root, 3) << endl;
}

class Problem3 {
public:
    bool isValidBST(TreeNode* root, long long low = -2147483649, long long high = 2147483648) {
        if (root == nullptr) return true;
        if (root->val >= high || root->val <= low) return false;

        bool lcheck = isValidBST(root->left, low, root->val);
        bool rcheck = isValidBST(root->right, root->val, high);

        return (lcheck && rcheck);

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(H) 
    }
};

void p3() {
    // Problem 3 : Leetcode 98. Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/check-for-bst/1 

    TreeNode* root = TreeNode::construct({ 100,50,200,25,75,150,250,10,30,60,80,125,175,215,275 }, -1);
    cout << Problem3().isValidBST(root) << endl;
}


int main() {
    // Day 26 of January 

    p1();

    p2();

    p3();


    return 0;
}