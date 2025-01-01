import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Disjoint set data structure
 */
class DisjointSet {
    int[] parent;
    int[] rank;
    int[] size;

    DisjointSet(int N) {
        parent = new int[N + 1];
        rank = new int[N + 1];
        size = new int[N + 1];

        for (int i = 0; i < N + 1; i++) {
            size[i] = 1;
            rank[i] = 0;
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
        // Day 27 of October

        p1();
    }

    static void p1() {
        // Problem 1 : Leetcode 721. Accounts Merge -
        // https://leetcode.com/problems/accounts-merge/
        // Geeksforgeeks - 
        // https://www.geeksforgeeks.org/problems/account-merge/1 

        List<List<String>> accounts = new ArrayList<>();
        accounts.add(new ArrayList<>(Arrays.asList("John","johnsmith@mail.com","john_newyork@mail.com")));
        accounts.add(new ArrayList<>(Arrays.asList("John","johnsmith@mail.com","john00@mail.com")));
        accounts.add(new ArrayList<>(Arrays.asList("Mary","mary@mail.com")));
        accounts.add(new ArrayList<>(Arrays.asList("John","johnnybravo@mail.com")));

        List<List<String>> mergedAccounts = accountsMerge(accounts);
        for (List<String> ua : mergedAccounts) {
            System.out.println(ua.toString());
        }
    }

    static List<List<String>> accountsMerge(List<List<String>> accounts) {
        int N = accounts.size();
        DisjointSet ds = new DisjointSet(N);

        // map - mail to number or id or index
        Map<String, Integer> emails = new HashMap<>();
        for (int i = 0; i < N; i++) {
            for (int j = 1; j < accounts.get(i).size(); j++) {
                String mail = accounts.get(i).get(j);
                if (emails.containsKey(mail)) {
                    ds.unionBySize(i, emails.get(mail));
                } else {
                    emails.put(mail, i);
                }
            }
        }

        // now we have mail to name index mapping
        // and in disjoint set we have all indexes and their ultimate parent

        // map mail to user - merge users make one account
        List<List<String>> indexedMails = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            indexedMails.add(new ArrayList<>());
        }
        for (Map.Entry<String, Integer> e : emails.entrySet()) {
            String mail = e.getKey();
            int user = ds.findParent(e.getValue());
            indexedMails.get(user).add(mail);
        }

        // now all users have their emails, some user list might be empty because of
        // redundant or extra accounts
        // sort individual email list and add user name at the beginning
        for (int i = 0; i < N; i++) {
            if (indexedMails.get(i).isEmpty()) {
                continue;
            }

            Collections.sort(indexedMails.get(i));
            indexedMails.get(i).add(0, accounts.get(i).get(0));
        }

        // remove empty user mails lists
        for (int i = N - 1; i >= 0; i--) {
            if (indexedMails.get(i).isEmpty()) {
                indexedMails.remove(i);
            }
        }

        return indexedMails;

        // Complexity analysis
        // Time : O(N) + O(T_Mails * 4ALPHA) + O(N) = O(T_Mails * 4ALPHA) + O(N *
        // LOG(M_Mails)) + O(N + N)
        // Space : O(3N) + O(T_Mails)
    }
}
