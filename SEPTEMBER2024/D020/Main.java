
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 2 of BST - revisiting

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 235. Lowest Common Ancestor of a Binary Search Tree -
        // https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1

        TreeNode root = insertIntoBST(null, 5);
        insertIntoBST(root, 8);
        insertIntoBST(root, 3);
        insertIntoBST(root, 2);
        insertIntoBST(root, 2);
        insertIntoBST(root, 4);
        insertIntoBST(root, 1);

        TreeNode lca = lowestCommonAncestor(root, root.left.left, root.right);
        System.out.println("lca:: " + lca.val);
    }

    static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode lca = root;
        while ((lca.val < p.val && lca.val < q.val) || (lca.val > p.val && lca.val > q.val)) {
            if (lca.val < p.val && lca.val < q.val) {
                lca = lca.right;
            } else if (lca.val > p.val && lca.val > q.val) {
                lca = lca.left;
            }
        }

        return lca;
    }

    static void p2() {
        // Problem 2 : Leetcode 1008. Construct Binary Search Tree from Preorder Traversal -
        // https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/preorder-to-postorder4423/1

        int[] preorder = {};
        TreeNode root = bstFromPreorder(preorder);
        System.out.println(root.val);
    }

    static TreeNode bstFromPreorder(int[] preorder, int bound, int index[]) {
        if (index[0] == preorder.length)
            return null;
        if (preorder[index[0]] > bound)
            return null;

        TreeNode root = new TreeNode(preorder[index[0]++]);

        root.left = bstFromPreorder(preorder, root.val, index);
        root.right = bstFromPreorder(preorder, bound, index);

        return root;
    }

    static TreeNode bstFromPreorder(int[] preorder) {
        return bstFromPreorder(preorder, 1000, new int[1]);

        // Complexity analysis
        // Time : O(3n)
        // Space : O(1) + O(h) stack space for recursion
    }

    static TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null)
            return new TreeNode(val);

        TreeNode ptr = root;
        while (ptr != null) {
            if (ptr.val < val) {
                if (ptr.right == null) {
                    ptr.right = new TreeNode(val);
                    break;
                } else {
                    ptr = ptr.right;
                }
            } else {
                if (ptr.left == null) {
                    ptr.left = new TreeNode(val);
                    break;
                } else {
                    ptr = ptr.left;
                }
            }
        }

        return root;

        // Complexity analysis
        // Time : O(h), h = hight of tree
        // Space : O(1)
    }
}