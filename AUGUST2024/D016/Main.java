import java.util.ArrayDeque;
import java.util.Deque;

class TreeNode {
    // int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        // this.val = val;
    }
}

class Pair {
    TreeNode node;
    int index;

    Pair(TreeNode n, int i) {
        node = n;
        index = i;
    }
}

public class Main {
    static int widthOfBinaryTree(TreeNode root) {
        if (root == null)
            return 0;

        int width = 0;

        Deque<Pair> dq = new ArrayDeque<>();
        dq.addLast(new Pair(root, 0));

        while (!dq.isEmpty()) {
            int level = dq.size();

            int m_min = dq.getFirst().index;

            int low = 0;
            int high = 0;

            for (int i = 0; i < level; i++) {
                TreeNode node = dq.getFirst().node;
                int curi = dq.getFirst().index - m_min;
                dq.removeFirst();

                if (i == 0)
                    low = curi;
                if (i == level - 1)
                    high = curi;

                if (node.left != null) {
                    dq.addLast(new Pair(node.left, curi * 2 + 1));
                }

                if (node.right != null) {
                    dq.addLast(new Pair(node.right, curi * 2 + 2));
                }
            }

            width = Math.max(width, high - low + 1);
        }

        return width;
    }

    static int getMaxWidth(TreeNode root) {
        // Your code here
        if (root == null)
            return 0;

        int width = 0;

        Deque<TreeNode> dq = new ArrayDeque<>();
        dq.addLast(root);

        while (!dq.isEmpty()) {
            int level = dq.size();

            width = Math.max(width, level);

            for (int i = 0; i < level; i++) {
                TreeNode node = dq.removeFirst();

                if (node.left != null) {
                    dq.addLast(node.left);
                }
                if (node.right != null) {
                    dq.addLast(node.right);
                }
            }
        }

        return width;
    }

    static void p1() {
        // Problem 1 : Leetcode 662. Maximum Width of Binary Tree -
        // https://leetcode.com/problems/maximum-width-of-binary-tree/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/maximum-width-of-tree/1

        TreeNode root = new TreeNode(0);
        root.left = new TreeNode(1);
        root.left.left = new TreeNode(2);
        root.left.right = new TreeNode(3);
        root.right = new TreeNode(1);
        root.right.right = new TreeNode(2);
        root.right.left = new TreeNode(3);

        System.out.println("maximum width (between nodes) : " + widthOfBinaryTree(root));
        System.out.println("width : " + getMaxWidth(root));
    }

    public static void main(String[] args) {
        // Day 17 of Binary Trees

        p1();
    }
}