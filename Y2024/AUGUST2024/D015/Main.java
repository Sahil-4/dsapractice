import java.util.LinkedList;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    static boolean getPathToNode(TreeNode root, TreeNode node, LinkedList<TreeNode> path) {
        if (root == null)
            return false;

        path.addLast(root);

        if (root.val == node.val)
            return true;

        boolean a = getPathToNode(root.left, node, path);
        if (a)
            return true;

        a = getPathToNode(root.right, node, path);
        if (a)
            return true;

        path.removeLast();

        return false;
    }

    static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode lca = null;

        LinkedList<TreeNode> pPath = new LinkedList<>();
        LinkedList<TreeNode> qPath = new LinkedList<>();
        getPathToNode(root, p, pPath);
        getPathToNode(root, q, qPath);

        while (!pPath.isEmpty() && !qPath.isEmpty()) {
            if (pPath.getFirst().val != qPath.getFirst().val)
                break;
            lca = pPath.getFirst();
            pPath.removeFirst();
            qPath.removeFirst();
        }

        return lca;
    }

    static void p1() {
        // Problem 1 : Leetcode 236. Lowest Common Ancestor of a Binary Tree -
        // https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1

        TreeNode root = new TreeNode(0);
        root.left = new TreeNode(1);
        root.left.left = new TreeNode(2);
        root.left.right = new TreeNode(3);
        root.right = new TreeNode(1);
        root.right.right = new TreeNode(2);
        root.right.left = new TreeNode(3);

        TreeNode lca = lowestCommonAncestor(root, root.left.right, root.right.left);
        System.out.println(lca.val);
    }

    public static void main(String[] args) {
        // Day 16 of Binary Trees

        p1();
    }
}