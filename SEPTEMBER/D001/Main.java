
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
        // Day 1 of September - Overall Day 245

        p1();

        p2();

        p3();
    }

    static void p1() {
        // Problem 1 : Leetcode 700. Search in a Binary Search Tree -
        // https://leetcode.com/problems/search-in-a-binary-search-tree/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/search-a-node-in-bst/1

        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);

        TreeNode res = searchBST(root, 1);
        System.out.println(res.val == 1);
    }

    static TreeNode searchBST(TreeNode root, int val) {
        if (root == null || root.val == val)
            return root;
        if (val < root.val)
            return searchBST(root.left, val);
        return searchBST(root.right, val);
    }

    static void p2() {
        // Problem 2 : Leetcode 98. Validate Binary Search Tree -
        // https://leetcode.com/problems/validate-binary-search-tree/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/binary-search-trees/1

        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);

        boolean check = isValidBST(root);
        System.out.println(check);
    }

    static boolean isValidBST(TreeNode root, long min, long max) {
        if (root == null)
            return true;
        if (root.val <= min || root.val >= max)
            return false;

        return isValidBST(root.left, min, root.val) && isValidBST(root.right, root.val, max);
    }

    static boolean isValidBST(TreeNode root) {
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    static void p3() {
        // Problem 3 : GeeksforGeeks Minimum element in BST -
        // https://www.geeksforgeeks.org/problems/minimum-element-in-bst/1

        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);

        int res = minValue(root);
        System.out.println(res == 1);
    }

    static int minValue(TreeNode root) {
        // code here
        if (root == null)
            return -1;
        if (root.left == null)
            return root.val;
        return minValue(root.left);
    }
}
