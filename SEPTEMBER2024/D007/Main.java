
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
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

    public int top() {
        if (!hasNext())
            return -1;
        TreeNode top = stack.peek();
        return top.data;
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
        // Day 7 of BST

        p1();

        p2();
    }

    static void p1() {
        // Problem 1 : Leetcode 1932. Merge BSTs to Create Single BST -
        // https://leetcode.com/problems/merge-bsts-to-create-single-bst/

        TreeNode root1 = new TreeNode(25);
        root1.left = new TreeNode(12);
        root1.right = new TreeNode(30);

        TreeNode root2 = new TreeNode(30);
        root2.left = new TreeNode(2);
        root2.left.left = new TreeNode(1);

        List<TreeNode> treeList = new ArrayList<>();
        treeList.add(root1);
        treeList.add(root2);

        TreeNode newRoot = canMerge(treeList);
        if (newRoot == null)
            return;

        System.out.println(newRoot.val);
    }

    static boolean traverse(TreeNode root, Map<Integer, TreeNode> map, int min, int max) {
        if (root == null)
            return true;
        if (root.val <= min || root.val >= max)
            return false;

        if (root.left == null && root.right == null) {
            if (map.containsKey(root.val) && root != map.get(root.val)) {
                TreeNode next = map.get(root.val);
                root.left = next.left;
                root.right = next.right;
                map.remove(root.val);
            }
        }

        return traverse(root.left, map, min, root.val) && traverse(root.right, map, root.val, max);
    }

    static TreeNode canMerge(List<TreeNode> trees) {
        Set<Integer> leaves = new HashSet<>();
        Map<Integer, TreeNode> map = new HashMap<>();

        for (TreeNode tree : trees) {
            map.put(tree.val, tree);

            if (tree.left != null) {
                leaves.add(tree.left.val);
            }

            if (tree.right != null) {
                leaves.add(tree.right.val);
            }
        }

        TreeNode result = null;
        for (TreeNode tree : trees) {
            if (!leaves.contains(tree.val)) {
                result = tree;
                break;
            }
        }

        if (result == null) {
            return null;
        }

        return traverse(result, map, Integer.MIN_VALUE, Integer.MAX_VALUE) && map.size() == 1 ? result : null;
    }

    static void p2() {
        // Problem 2 : GeeksForGeeks Merge two BST 's -
        // https://www.geeksforgeeks.org/problems/merge-two-bst-s/1

        TreeNode root1 = new TreeNode(12);
        root1.left = new TreeNode(5);
        root1.right = new TreeNode(55);
        root1.left.left = new TreeNode(2);
        TreeNode root2 = new TreeNode(18);
        root2.left = new TreeNode(5);
        root2.right = new TreeNode(22);
        root2.right.left = new TreeNode(20);

        List<Integer> list = merge(root1, root2);
        for (int e : list) {
            System.out.println(e);
        }
    }

    static List<Integer> merge(TreeNode root1, TreeNode root2) {
        // Write your code here
        BSTIterator bstitr1 = new BSTIterator(root1);
        BSTIterator bstitr2 = new BSTIterator(root2);

        List<Integer> list = new ArrayList<>();

        while (bstitr1.hasNext() && bstitr2.hasNext()) {
            if (bstitr1.top() <= bstitr2.top()) {
                list.add(bstitr1.next());
            } else {
                list.add(bstitr2.next());
            }
        }

        while (bstitr1.hasNext()) {
            list.add(bstitr1.next());
        }

        while (bstitr2.hasNext()) {
            list.add(bstitr2.next());
        }

        return list;
    }
}