import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

/**
 * Disjoint set data structure
 */
class DisjointSet {
    int[] parent;
    int[] size;

    DisjointSet(int N) {
        parent = new int[N];
        size = new int[N];

        for (int i = 0; i < N; i++) {
            size[i] = 1;
            parent[i] = i;
        }
    }

    int findParent(int node) {
        if (parent[node] != node) {
            parent[node] = findParent(parent[node]);
        }

        return parent[node];
    }

    void unionBySize(int u, int v) {
        int pu = findParent(u);
        int pv = findParent(v);

        if (pu == pv) {
            return;
        }

        int spu = size[pu];
        int spv = size[pv];

        if (spu < spv) {
            parent[pu] = pv;
            size[pv] += size[pu];
        } else {
            parent[pv] = pu;
            size[pu] += size[pv];
        }
    }
}

public class Main {
    public static void main(String[] args) {
        // Day 13 of October

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 721. Accounts Merge -
        // https://leetcode.com/problems/accounts-merge/
        // Geeksforgeeks -
        // https://www.geeksforgeeks.org/problems/account-merge/1

        List<List<String>> accounts = new ArrayList<>();
        String l1[] = { "John", "johnsmith@mail.com", "john_newyork@mail.com" };
        String l2[] = { "John", "johnsmith@mail.com", "john00@mail.com" };
        String l3[] = { "Mary", "mary@mail.com" };
        String l4[] = { "John", "johnnybravo@mail.com" };

        accounts.add(Arrays.asList(l1));
        accounts.add(Arrays.asList(l2));
        accounts.add(Arrays.asList(l3));
        accounts.add(Arrays.asList(l4));

        List<List<String>> out = accountsMerge(accounts);
        for (List<String> p : out) {
            System.out.println(p.toString());
        }
    }

    static List<List<String>> accountsMerge(List<List<String>> accounts) {
        int N = accounts.size();

        DisjointSet ds = new DisjointSet(N);

        Map<String, Integer> mailsToOwner = new TreeMap<>();
        for (int i = 0; i < N; i++) { // total members
            List<String> mails = accounts.get(i);
            int m = mails.size();

            for (int j = 1; j < m; j++) {
                String mail = mails.get(j);

                if (!mailsToOwner.containsKey(mail)) {
                    mailsToOwner.put(mail, i);
                } else {
                    int p = mailsToOwner.get(mail);
                    ds.unionBySize(p, i);
                }
            }
        }

        ArrayList<String>[] mergedMails = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            mergedMails[i] = new ArrayList<>();
        }

        for (Map.Entry<String, Integer> it : mailsToOwner.entrySet()) {
            String mail = it.getKey();
            int banda = it.getValue();

            int asliBanda = ds.findParent(banda);

            mergedMails[asliBanda].add(mail);
        }

        // for answer/output
        List<List<String>> ans = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            if (mergedMails[i].isEmpty()) {
                continue;
            }

            // sort all emails
            Collections.sort(mergedMails[i]);

            List<String> nameMails = new ArrayList<>();
            nameMails.add(accounts.get(i).get(0)); // add name
            nameMails.addAll(mergedMails[i]); // add all mails

            ans.add(nameMails);
        }

        return ans;

        // Complexity analysis 
        // Time : O(N) + O(N * m - N) + O(N) + O(N * m - N) + O(N * (m * LOG(m) + m)) 
        // Space : O(2N) + O(N * m) + O(N * m) 
    }
}
