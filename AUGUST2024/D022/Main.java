
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

class Codec {
    private final int flagA = -100000; // leetcode
    private final int flagB = 0; // gfg

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder("");
        if (root == null)
            return sb.toString();

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            int level = q.size();

            for (int i = 0; i < level; i++) {
                TreeNode node = q.remove();

                if (node.val != flagA) {
                    sb.append(node.val).append(",");
                } else {
                    sb.append("N,");
                    continue;
                }

                if (node.left != null) {
                    q.add(node.left);
                } else {
                    q.add(new TreeNode(flagA));
                }

                if (node.right != null) {
                    q.add(node.right);
                } else {
                    q.add(new TreeNode(flagA));
                }
            }
        }

        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.length() == 0)
            return null;

        StringBuilder sb = new StringBuilder(data);

        TreeNode root = new TreeNode(Integer.parseInt(sb.substring(0, sb.indexOf(","))));
        sb.delete(0, sb.indexOf(",") + 1);

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            int level = q.size();

            for (int i = 0; i < level; i++) {
                TreeNode node = q.remove();

                TreeNode left = null;
                TreeNode right = null;

                // create left node
                if (sb.charAt(0) != 'N') {
                    left = new TreeNode(Integer.parseInt(sb.substring(0, sb.indexOf(","))));
                    q.add(left);
                }
                sb.delete(0, sb.indexOf(",") + 1);

                // create right node
                if (sb.charAt(0) != 'N') {
                    right = new TreeNode(Integer.parseInt(sb.substring(0, sb.indexOf(","))));
                    q.add(right);
                }
                sb.delete(0, sb.indexOf(",") + 1);

                node.left = left;
                node.right = right;
            }
        }

        return root;
    }

    // Function to serialize a tree and return a list containing nodes of tree.
    public ArrayList<Integer> serialize2(TreeNode root) {
        // code here
        ArrayList<Integer> list = new ArrayList<>();
        if (root == null)
            return list;

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            int level = q.size();

            for (int i = 0; i < level; i++) {
                TreeNode node = q.remove();

                list.add(node.val);

                if (node.val == flagB)
                    continue;

                if (node.left != null) {
                    q.add(node.left);
                } else {
                    q.add(new TreeNode(flagB));
                }

                if (node.right != null) {
                    q.add(node.right);
                } else {
                    q.add(new TreeNode(flagB));
                }
            }
        }

        return list;
    }

    // Function to deserialize a list and construct the tree.
    public TreeNode deSerialize2(ArrayList<Integer> list) {
        // code here
        if (list.isEmpty())
            return null;

        TreeNode root = new TreeNode(list.get(0));
        list.remove(0);

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            int level = q.size();

            for (int i = 0; i < level; i++) {
                TreeNode node = q.remove();

                TreeNode left = null;
                TreeNode right = null;

                // create left node
                if (list.get(0) != 0) {
                    left = new TreeNode(list.get(0));
                    q.add(left);
                }
                list.remove(0);

                // create right node
                if (list.get(0) != 0) {
                    right = new TreeNode(list.get(0));
                    q.add(right);
                }
                list.remove(0);

                node.left = left;
                node.right = right;
            }
        }

        return root;
    }
}

public class Main {
    static void p1() {
        // Problem 1 : Leetcode 297. Serialize and Deserialize Binary Tree -
        // https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
        // GeeksForGeeks -
        // https://www.geeksforgeeks.org/problems/serialize-and-deserialize-a-binary-tree/1

        TreeNode root = null;

        Codec cd = new Codec();
        System.out.println(cd.serialize(root));
        // System.out.println(cd.serialize2(root).toString());
    }

    public static void main(String[] args) {
        // Day 23 of Binary Trees

        p1();
    }
}