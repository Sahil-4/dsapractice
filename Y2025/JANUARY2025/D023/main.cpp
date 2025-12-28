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
public:
    bool hasPathSum(TreeNode* root, int sum) {
        // dfs 
        if (root == NULL) return false;
        if (root->left == NULL && root->right == NULL) return sum == root->val;

        bool lc = hasPathSum(root->left, sum - root->val);
        bool rc = hasPathSum(root->right, sum - root->val);

        return lc | rc;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(H) 
    }
};

void p1() {
    // Problem 1 : Leetcode 112. Path Sum - https://leetcode.com/problems/path-sum/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/root-to-leaf-path-sum/1 

    TreeNode* root = TreeNode::construct({ 1,2,2,1,-10000,5 }, -10000);
    TreeNode::print(root);
    Problem1().hasPathSum(root, 8);
}

class Problem2 {
public:
    int sumNumbers(TreeNode* root, int number = 0) {
        // dfs 

        if (root == NULL) return 0;

        number = ((number * 10) + root->val);

        if (root->left == NULL && root->right == NULL) return number;
        return sumNumbers(root->left, number) + sumNumbers(root->right, number);

        // Complexity analysis 
        // Time : O(N) + multiplication operations 
        // Space : O(H) 
    }
};

void p2() {
    // Problem 2 : Leetcode 129. Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/root-to-leaf-paths-sum/1 

    TreeNode* root = TreeNode::construct({ 9,9,9,-1,9,-1,9,-1,9,-1,9,-1,9,-1,9,-1,9,-1,9,-1,9,-1,9,-1,9,-1 }, -1);
    TreeNode::print(root);
    cout << Problem2().sumNumbers(root) << endl;
}

class Problem3 {
    int helper(TreeNode* root, int& msum) {
        if (root == NULL) return 0;

        int lsum = helper(root->left, msum);
        int rsum = helper(root->right, msum);

        // case 1 : lrum + rsum + root->val gives max sum
        int a = lsum + rsum + root->val;

        // case 2 : max of (lrum, rsum) + root->val gives max sum
        int b = max(lsum, rsum) + root->val;

        // case 3 : root->val gives max sum
        int c = root->val;

        // update maximum path sum 
        msum = max({ msum, a, b, c });

        // return any one straight path 
        return max(b, c);

        // Complexity analysis 
        // Time : O(N) + multiplication operations 
        // Space : O(H) 
    }

public:
    int maxPathSum(TreeNode* root) {
        int msum = INT_MIN;
        helper(root, msum);

        return msum;
    }
};

void p3() {
    // Problem 3 : Leetcode 124. Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/maximum-path-sum-from-any-node/1 

    TreeNode* root = TreeNode::construct({ 9,9,9,-1,9,-1,9,-1,9,-1,9,-1,9,-1,9,-1,9,-1,9,-1,9,-1,9,-1,9,-1 }, -1);
    TreeNode::print(root);
    cout << Problem3().maxPathSum(root) << endl;
}


int main() {
    // Day 23 of January 2025 

    p1();

    p2();

    p3();


    return 0;
}