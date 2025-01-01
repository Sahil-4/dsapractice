
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
        // Day 4 of BST

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 235. Lowest Common Ancestor of a Binary Search Tree -
        // https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1

        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);

        TreeNode lca = lowestCommonAncestor_Solution2(root, root.left.left, root.left.right);
        // TreeNode lca = lowestCommonAncestor(root, root.left.left, root.left.right);
        System.out.println(lca.val);
    }

    static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode curr = root;
        while (curr != null) {
            if (curr.val > p.val && curr.val > q.val) {
                curr = curr.left;
            } else if (curr.val < p.val && curr.val < q.val) {
                curr = curr.right;
            } else {
                break;
            }
        }

        return curr;
    }

    static TreeNode lowestCommonAncestor_Solution2(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null)
            return root;

        if (root.val > p.val && root.val > q.val) {
            return lowestCommonAncestor(root.left, p, q);
        }
        if (root.val < p.val && root.val < q.val) {
            return lowestCommonAncestor(root.right, p, q);
        }

        return root;
    }

    static void p2() {
        // Problem 2 : Leetcode 1008. Construct Binary Search Tree from Preorder Traversal -
        // https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/preorder-to-postorder4423/1

        int preorder[] = { 800, 500, 100, 700, 900, 1000 };
        TreeNode root = bstFromPreorder(preorder);
    }

    static int MAX_RANGE = 1000;

    static TreeNode bstFromPreorder(int[] preorder) {
        int index[] = { 0 };
        return bstFromPreorder(preorder, index, MAX_RANGE);
        // return bstFromPreorder(preorder, 0, preorder.length - 1);
    }

    static TreeNode bstFromPreorder(int[] preorder, int x, int y) {
        if (x > y)
            return null;

        TreeNode root = new TreeNode(preorder[x]);

        // m -> last index of element smaller then preorder[x]
        int m = x + 1;
        while (m <= y && preorder[m] < preorder[x])
            m++;

        root.left = bstFromPreorder(preorder, x + 1, m - 1);
        root.right = bstFromPreorder(preorder, m, y);

        return root;
    }

    static TreeNode bstFromPreorder(int[] preorder, int[] index, int bound) {
        if (index[0] >= preorder.length || preorder[index[0]] > bound)
            return null;

        TreeNode root = new TreeNode(preorder[index[0]++]);

        root.left = bstFromPreorder(preorder, index, root.val);
        root.right = bstFromPreorder(preorder, index, bound);

        return root;
    }
}