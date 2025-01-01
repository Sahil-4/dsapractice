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
    private final Stack<TreeNode> nodes;
    private final boolean reverse;

    public BSTIterator(TreeNode r, boolean rev) {
        nodes = new Stack<>();
        reverse = rev;

        if (reverse) {
            pushRight(r);
        } else {
            pushLeft(r);
        }
    }

    private void pushLeft(TreeNode n) {
        while (n != null) {
            nodes.push(n);
            n = n.left;
        }
    }

    private void pushRight(TreeNode n) {
        while (n != null) {
            nodes.push(n);
            n = n.right;
        }
    }

    public boolean hasNext() {
        return !nodes.isEmpty();
    }

    public int top() {
        if (!hasNext()) return -1;
        return nodes.peek().val;
    }

    public int next() {
        if (!hasNext()) return -1;

        TreeNode node = nodes.pop();

        if (reverse) {
            pushRight(node.left);
        } else {
            pushLeft(node.right);
        }

        return node.val;
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 3 of BST - revisiting 

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 653. Two Sum IV - Input is a BST -
        // https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/find-a-pair-with-given-target-in-bst/1

        TreeNode root = new TreeNode(12);
        root.left = new TreeNode(8);
        root.left.left = new TreeNode(5);
        root.left.left.left = new TreeNode(4);
        root.left.right = new TreeNode(10);
        root.right = new TreeNode(24);

        boolean check = findTarget(root, 12);
        System.out.println("is 12 present ::" + check);
    }

    static boolean findTarget(TreeNode root, int k) {
        BSTIterator bitr_l = new BSTIterator(root, false);
        BSTIterator bitr_r = new BSTIterator(root, true);

        int a = bitr_l.next();
        int b = bitr_r.next();

        while (a < b) {
            if (a + b == k) {
                return true;
            } else if (a + b < k) {
                a = bitr_l.next();
            } else {
                b = bitr_r.next();
            }
        }

        return false;

        // Complexity analysis
        // Time : O(h)
        // Space : O(h)
    }

    static void p2() {
        // Problem 2 : Leetcode 99. Recover Binary Search Tree -
        // https://leetcode.com/problems/recover-binary-search-tree/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/fixed-two-nodes-of-a-bst/1

        TreeNode root = new TreeNode(12);
        root.left = new TreeNode(8);
        root.left.left = new TreeNode(10);
        root.left.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right = new TreeNode(24);

        recoverTree(root);
    }

    static TreeNode first;
    static TreeNode middle;
    static TreeNode last;
    static TreeNode prev;

    static void detect(TreeNode root) {
        if (root == null) return;

        detect(root.left);

        if (root.val < prev.val) {
            // problem
            if (first == null) {
                first = prev;
                middle = root;
            } else {
                last = root;
            }
        }

        prev = root;
        detect(root.right);
    }

    static void recoverTree(TreeNode root) {
        // for swapped nodes
        first = middle = last = null;
        prev = new TreeNode(Integer.MIN_VALUE);

        // find swapped nodes
        detect(root);

        // swap values - fix nodes
        if (first != null && last != null) {
            int temp = first.val;
            first.val = last.val;
            last.val = temp;
        } else if (first != null && middle != null) {
            int temp = first.val;
            first.val = middle.val;
            middle.val = temp;
        }
    }
}