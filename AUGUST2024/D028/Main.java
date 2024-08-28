import java.util.ArrayList;
import java.util.Collections;
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
    public static void main(String[] args) {
        // Day 29 of Binary Trees - revisiting 

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 103. Binary Tree Zigzag Level Order Traversal -
        // https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/zigzag-tree-traversal/1

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.left.left.left = new TreeNode(6);

        List<List<Integer>> list = zigzagLevelOrder(root);
        for (List<Integer> l : list) {
            for (int e : l) {
                System.out.println(e);
            }
        }
    }

    static List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> list = new ArrayList<>();
        if (root == null)
            return list;

        Queue<TreeNode> stack = new LinkedList<>();
        stack.add(root);
        int h = 0;

        while (!stack.isEmpty()) {
            int level = stack.size();
            List<Integer> subList = new ArrayList<>();

            for (int i = 0; i < level; i++) {
                TreeNode node = stack.remove();

                if (node.left != null)
                    stack.add(node.left);
                if (node.right != null)
                    stack.add(node.right);

                subList.add(node.val);
            }

            if (h++ % 2 == 1)
                Collections.reverse(subList);
            list.add(subList);
        }

        return list;
    }
}
