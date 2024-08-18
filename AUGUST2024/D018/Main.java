import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
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
    static void setParentPointers(Map<TreeNode, TreeNode> parent, TreeNode root) {
        Queue<TreeNode> que = new LinkedList<>();
        que.add(root);

        while (!que.isEmpty()) {
            TreeNode curr = que.remove();

            if (curr.left != null) {
                parent.put(curr.left, curr);
                que.add(curr.left);
            }
            if (curr.right != null) {
                parent.put(curr.right, curr);
                que.add(curr.right);
            }
        }
    }

    static List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        // get pointers node to its parent - bfs
        Map<TreeNode, TreeNode> parent = new HashMap<>();
        setParentPointers(parent, root);

        // radial traversal : up and down wards - bfs
        // keep track of distance and carry visited nodes set
        Map<TreeNode, Boolean> visited = new HashMap<>();
        Queue<TreeNode> que = new LinkedList<>();
        que.add(target);
        visited.put(target, true);

        int curr_level = 0;

        while (!que.isEmpty()) {
            if (curr_level == k)
                break;
            curr_level++;

            int size = que.size();

            for (int i = 0; i < size; i++) {
                TreeNode curr = que.remove();

                if (curr.left != null && visited.get(curr.left) == null) {
                    visited.put(curr.left, true);
                    que.add(curr.left);
                }
                if (curr.right != null && visited.get(curr.right) == null) {
                    visited.put(curr.right, true);
                    que.add(curr.right);
                }

                if (parent.get(curr) != null && visited.get(parent.get(curr)) == null) {
                    visited.put(parent.get(curr), true);
                    que.add(parent.get(curr));
                }
            }
        }

        List<Integer> out = new ArrayList<>();
        while (!que.isEmpty()) {
            TreeNode node = que.remove();
            out.add(node.val);
        }

        return out;
    }

    static void p1() {
        // Problem 1 : Leetcode 863. All Nodes Distance K in Binary Tree -
        // https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/nodes-at-given-distance-in-binary-tree/1

        int k = 2;
        TreeNode root = new TreeNode(0);
        root.left = new TreeNode(1);
        root.right = new TreeNode(1);
        root.left.left = new TreeNode(2);
        root.left.right = new TreeNode(3);
        root.right.right = new TreeNode(2);
        root.right.left = new TreeNode(3);

        List<Integer> list = distanceK(root, root.left, k);
        for (int e : list) {
            System.out.println(e);
        }
    }

    public static void main(String[] args) {
        // Day 19 of Binary Trees

        p1();
    }
}