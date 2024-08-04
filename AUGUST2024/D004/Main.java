import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;

class TreeNode {
    int val;

    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Main {
    static void preorderTraversal(List<Integer> list, TreeNode root) {
        // recursion
        if (root == null)
            return;
        list.add(root.val);
        preorderTraversal(list, root.left);
        preorderTraversal(list, root.right);
    }

    static List<Integer> preorderTraversal(TreeNode root) {
        // pre order -> root left right
        List<Integer> list = new ArrayList<>();
        if (root == null)
            return list;

        // preorderTraversal(list, root);

        Stack<TreeNode> nodes = new Stack<>();
        nodes.add(root);

        while (!nodes.isEmpty()) {
            TreeNode top = nodes.pop();

            list.add(top.val);

            if (top.right != null) {
                nodes.add(top.right);
            }
            if (top.left != null) {
                nodes.add(top.left);
            }
        }

        return list;
    }

    static void inorderTraversal(List<Integer> list, TreeNode root) {
        // recursion
        if (root == null)
            return;

        inorderTraversal(list, root.left);
        list.add(root.val);
        inorderTraversal(list, root.right);
    }

    static List<Integer> inorderTraversal(TreeNode root) {
        // left root right
        List<Integer> list = new ArrayList<>();
        if (root == null)
            return list;

        // inorderTraversal(list, root);

        Stack<TreeNode> nodes = new Stack<>();
        TreeNode curr = root;

        while (curr != null || !nodes.isEmpty()) {
            while (curr != null) {
                nodes.add(curr);
                curr = curr.left;
            }

            curr = nodes.pop();
            list.add(curr.val);
            curr = curr.right;
        }

        return list;
    }

    static void postorderTraversal(List<Integer> list, TreeNode root) {
        if (root == null)
            return;

        postorderTraversal(list, root.left);
        postorderTraversal(list, root.right);
        list.add(root.val);
    }

    static List<Integer> postorderTraversal(TreeNode root) {
        // left right root

        List<Integer> list = new ArrayList<>();
        if (root == null)
            return list;
        // postorderTraversal(list, root);

        Stack<TreeNode> nodes = new Stack<>();
        TreeNode curr = root;

        while (curr != null || !nodes.isEmpty()) {
            if (curr != null) {
                nodes.add(curr);
                curr = curr.left;
            } else {
                TreeNode temp = nodes.peek().right;
                if (temp == null) {
                    temp = nodes.pop();
                    list.add(temp.val);
                    while (!nodes.isEmpty() && temp == nodes.peek().right) {
                        temp = nodes.pop();
                        list.add(temp.val);
                    }
                } else {
                    curr = temp;
                }
            }
        }

        return list;
    }

    static List<Integer> run(String type) {
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

        // The tree structure now :
        // * 1
        // * / \
        // * 2 3
        // * / \
        // * 4 5
        return switch (type) {
            case "pre" -> preorderTraversal(root);
            case "in" -> inorderTraversal(root);
            default -> postorderTraversal(root);
        };
    }

    static void p1() {
        // Problem 1 : Leetcode 144. Binary Tree Preorder Traversal -
        // https://leetcode.com/problems/binary-tree-preorder-traversal/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/preorder-traversal/1

        List<Integer> list = run("pre");
        for (int e : list) {
            System.out.println(e);
        }
    }

    static void p2() {
        // Problem 2 : Leetcode 94. Binary Tree Inorder Traversal -
        // https://leetcode.com/problems/binary-tree-inorder-traversal/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/inorder-traversal/1

        List<Integer> list = run("in");
        for (int e : list) {
            System.out.println(e);
        }
    }

    static void p3() {
        // Problem 3 : Leetcode 145. Binary Tree Postorder Traversal -
        // https://leetcode.com/problems/binary-tree-postorder-traversal/
        // GeeksForGeeks - https://www.geeksforgeeks.org/problems/postorder-traversal/1

        List<Integer> list = run("post");
        for (int e : list) {
            System.out.println(e);
        }
    }

    static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> list = new LinkedList<>();
        if (root == null)
            return list;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            int level = queue.size();
            ArrayList<Integer> sub = new ArrayList<>();

            for (int i = 0; i < level; i++) {
                TreeNode top = queue.remove();
                sub.add(top.val);

                if (top.left != null) {
                    queue.add(top.left);
                }
                if (top.right != null) {
                    queue.add(top.right);
                }
            }

            list.add(sub);
        }

        return list;
    }

    static void p4() {
        // Problem 4 : Leetcode 102. Binary Tree Level Order Traversal -
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

        // The tree structure now :
        // * 1
        // * / \
        // * 2 3
        // * / \
        // * 4 5

        List<List<Integer>> list = levelOrder(root);
        for (List<Integer> sub : list) {
            for (int e : sub) {
                System.out.println(e);
            }
        }
    }

    public static void main(String[] args) {
        // Day 4 of August - day 5 of trees - revisiting tree traversal 

        p1();

        p2();

        p3();

        p4();
    }
}