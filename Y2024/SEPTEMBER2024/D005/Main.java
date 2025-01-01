
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

    public BSTIterator(TreeNode root) {
        this.stack = new Stack<>();
        pushLeftsIntoStack(root);
    }

    private void pushLeftsIntoStack(TreeNode root) {
        while (root != null) {
            stack.push(root);
            root = root.left;
        }
    }

    public int next() {
        if (!hasNext())
            return -1;
        TreeNode top = stack.pop();
        pushLeftsIntoStack(top.right);
        return top.val;
    }

    public boolean hasNext() {
        return !stack.isEmpty();
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 5 of BST

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Geeksforgeeks Inorder Successor in BST -
        // https://www.geeksforgeeks.org/problems/inorder-successor-in-bst/1

        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);

        TreeNode successor = inorderSuccessor(root, root.left.left);
        if (successor != null) {
            System.out.println(successor.val);
        }
    }

    static TreeNode inorderSuccessor(TreeNode root, TreeNode x) {
        if (root == null || x == null)
            return null;

        TreeNode succ = null;
        TreeNode curr = root;
        while (curr != null) {
            if (curr.val <= x.val) {
                curr = curr.right;
            } else {
                succ = curr;
                curr = curr.left;
            }
        }

        return succ;
    }

    static void p2() {
        // Problem 2 : Leetcode 173. Binary Search Tree Iterator -
        // https://leetcode.com/problems/binary-search-tree-iterator/

        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);

        BSTIterator bstI = new BSTIterator(root);
        System.out.println(bstI.hasNext());
        System.out.println(bstI.next());
        System.out.println(bstI.hasNext());
        System.out.println(bstI.next());
        System.out.println(bstI.hasNext());
        System.out.println(bstI.next());
    }
}
