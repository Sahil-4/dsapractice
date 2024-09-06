
import java.util.Stack;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

class BSTIterator {
    private final Stack<TreeNode> stack;
    int mode; // 1 for inorder 2 for reversed inorder

    public BSTIterator(TreeNode root, int mode) {
        this.stack = new Stack<>();
        this.mode = mode;
        pushAllIntoStack(root);
    }

    private void pushAllIntoStack(TreeNode root) {
        if (mode == 1) {
            pushAllLeftsIntoStack(root);
        } else {
            pushAllRightsIntoStack(root);
        }
    }

    private void pushAllLeftsIntoStack(TreeNode root) {
        while (root != null) {
            stack.push(root);
            root = root.left;
        }
    }

    private void pushAllRightsIntoStack(TreeNode root) {
        while (root != null) {
            stack.push(root);
            root = root.right;
        }
    }

    public int next() {
        if (!hasNext())
            return -1;

        TreeNode top = stack.pop();
        if (mode == 1) {
            pushAllLeftsIntoStack(top.right);
        } else {
            pushAllRightsIntoStack(top.left);
        }

        return top.val;
    }

    public boolean hasNext() {
        return !stack.isEmpty();
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 6 of BST

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 653. Two Sum IV - Input is a BST -
        // https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/find-a-pair-with-given-target-in-bst/1

        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);

        int k = 9;

        boolean check = findTarget(root, k);
        System.out.println(check);
    }

    static boolean findTarget(TreeNode root, int k) {
        BSTIterator itr = new BSTIterator(root, 1);
        BSTIterator revItr = new BSTIterator(root, 2);

        int a = itr.next();
        int b = revItr.next();

        while (a < b) {
            if (a + b == k)
                return true;

            if (a + b < k) {
                a = itr.next();
            } else {
                b = revItr.next();
            }
        }

        return false;
    }
}