import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    static void postOrder(List<Integer> list, TreeNode node) {
        // recursive
        if (node == null)
            return;
        postOrder(list, node.left);
        postOrder(list, node.right);
        list.add(node.val);
    }

    static List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        postOrder(list, root);
        return list;
    }

    static void p1() {
        // Problem 1 : Leetcode 145. Binary Tree Postorder Traversal -
        // https://leetcode.com/problems/binary-tree-postorder-traversal/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/postorder-traversal/1

        // Create the nodes
        TreeNode root = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(3);
        TreeNode node4 = new TreeNode(4);
        TreeNode node5 = new TreeNode(5);

        // Connect the nodes
        root.left = node2;
        root.right = node3;
        node2.left = node4;
        node2.right = node5;

        // The tree structure is now:
        // * 1
        // * / \
        // * 2 3
        // * / \
        // * 4 5
        // => 4 5 2 3 1

        List<Integer> list = postorderTraversal(root);
        for (int e : list) {
            System.out.println(e);
        }
    }

    public static void main(String[] args) {
        // Day 2 of August - Day 3 of Tree

        p1();
    }
}
