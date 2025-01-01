import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
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
    static int infecttionTime = 0;

    static TreeNode search(TreeNode root, int data) {
        if (root == null)
            return null;

        if (root.val == data)
            return root;

        TreeNode f = search(root.left, data);
        if (f != null)
            return f;

        return search(root.right, data);
    }

    static void setChild2Parent(Map<TreeNode, TreeNode> child2Parent, TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            int lev = q.size();

            for (int i = 0; i < lev; i++) {
                TreeNode node = q.remove();

                if (node.left != null) {
                    q.add(node.left);
                    child2Parent.put(node.left, node);
                }
                if (node.right != null) {
                    q.add(node.right);
                    child2Parent.put(node.right, node);
                }
            }
        }
    }

    static void burn(TreeNode curr, Map<TreeNode, TreeNode> child2Parent, Map<TreeNode, Boolean> visited, int time) {
        // update burn out time
        infecttionTime = Math.max(infecttionTime, time);

        // parent
        TreeNode parent = child2Parent.get(curr);
        if (parent != null && visited.get(parent) == null) {
            visited.put(parent, true);
            burn(parent, child2Parent, visited, time + 1);
        }

        // left
        TreeNode left = curr.left;
        if (left != null && visited.get(left) == null) {
            visited.put(left, true);
            burn(left, child2Parent, visited, time + 1);
        }

        // right
        TreeNode right = curr.right;
        if (right != null && visited.get(right) == null) {
            visited.put(right, true);
            burn(right, child2Parent, visited, time + 1);
        }
    }

    static int amountOfTime(TreeNode root, int start) {
        // set time to default
        infecttionTime = 0;

        // search target node
        TreeNode target = search(root, start);

        // create child to parent pointer mapping
        Map<TreeNode, TreeNode> child2Parent = new HashMap<>();
        setChild2Parent(child2Parent, root);

        // perform radial traversal and calculate burning time
        Map<TreeNode, Boolean> visited = new HashMap<>();
        visited.put(target, true);
        burn(target, child2Parent, visited, 0);

        return infecttionTime;

        // Same as burn tree
    }

    static void p1() {
        // Problem 1 : Leetcode 2385. Amount of Time for Binary Tree to Be Infected -
        // https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/burning-tree/1

        TreeNode root = new TreeNode(0);
        root.left = new TreeNode(1);
        root.right = new TreeNode(2);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(4);
        root.right.right = new TreeNode(5);
        root.right.left = new TreeNode(6);

        int t = amountOfTime(root, 5);
        System.out.println(t);
    }

    public static void main(String[] args) {
        // Day 20 of binary trees

        p1();
    }
}