class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    static boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null)
            return true;
        if (p == null && q != null)
            return false;
        if (p != null && q == null)
            return false;

        if (p.val != q.val)
            return false;

        boolean left = isSameTree(p.left, q.left);
        boolean right = isSameTree(p.right, q.right);

        return left && right;
    }

    static void p1() {
        // Problem 1 : Leetcode 100. Same Tree -
        // https://leetcode.com/problems/same-tree/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1

        TreeNode t1 = new TreeNode(1);
        t1.left = new TreeNode(2);
        t1.right = new TreeNode(3);
        t1.left.left = new TreeNode(4);
        t1.left.right = new TreeNode(5);
        t1.right.left = new TreeNode(6);
        t1.right.right = new TreeNode(7);

        TreeNode t2 = new TreeNode(1);
        t2.left = new TreeNode(2);
        // t2.left.left = new TreeNode(4);
        t2.left.left = new TreeNode(7);
        t2.left.right = new TreeNode(5);
        t2.right = new TreeNode(3);
        t2.right.left = new TreeNode(6);
        t2.right.right = new TreeNode(7);

        boolean same = isSameTree(t1, t2);
        System.out.println(same);
    }

    public static void main(String[] args) {
        // Day 10 of binary trees

        p1();
    }
}