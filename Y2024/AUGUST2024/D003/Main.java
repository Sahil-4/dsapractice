import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> list = new LinkedList<>();
        if (root == null)
            return list;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            int level = queue.size();
            List<Integer> subList = new LinkedList<>();

            for (int i = 0; i < level; i++) {
                TreeNode node = queue.remove();
                if (node.left != null)
                    queue.add(node.left);
                if (node.right != null)
                    queue.add(node.right);
                subList.add(node.val);
            }

            list.add(subList);
        }

        return list;
    }

    static void p1() {
        // Problem 1 : Leetcode 102. Binary Tree Level Order Traversal -
        // https://leetcode.com/problems/binary-tree-level-order-traversal/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/level-order-traversal/1

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
        // => [ 1 ], [ 2, 3], [ 4, 5 ]

        List<List<Integer>> list = levelOrder(root);
        for (List<Integer> l : list) {
            for (int e : l) {
                System.out.println(e);
            }
        }
    }

    public static void main(String[] args) {
        // Day 3 of August - Day 4 of Trees

        p1();
    }
}