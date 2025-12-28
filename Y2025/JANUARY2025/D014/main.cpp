#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    vector<vector<string>> solve1(vector<string>& strs) {
        map<string, vector<string>> mp;

        for (int i = 0; i < strs.size(); i++) {
            string s = string(strs[i]);
            sort(s.begin(), s.end());
            mp[s].push_back(strs[i]);
        }

        vector<vector<string>> out;
        for (auto it : mp) out.push_back(it.second);

        return out;

        // Complexity analysis 
        // Time : O(N * (Log(str[i]) * str[i])) 
        // Space : O(N) 
    }

    vector<vector<string>> solve2(vector<string>& strs) {
        map<string, int> mp;
        int mindex = 0;

        for (int i = 0; i < strs.size(); i++) {
            string s = string(strs[i]);
            sort(s.begin(), s.end());
            if (mp.find(s) != mp.end()) continue;
            mp[s] = mindex++;
        }

        vector<vector<string>> out(mindex);
        for (int i = 0; i < strs.size(); i++) {
            string s = string(strs[i]);
            sort(s.begin(), s.end());
            int mindex = mp[s];
            out[mindex].push_back(strs[i]);
        }

        return out;

        // Complexity analysis 
        // Time : O(2 * (N * (Log(str_len) * str_len))) 
        // Space : O(nunique(strs[])) 
    }

    string getHash(string s) {
        string hash = "";
        int freq[26] = { 0 };
        for (char ch : s) freq[ch - 'a']++;
        for (int f : freq) hash += to_string(f) + "/";
        return hash;
    }

    vector<vector<string>> solve3(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;

        for (const string& str : strs) mp[getHash(str)].push_back(str);

        vector<vector<string>> out;
        for (auto it : mp) out.push_back(it.second);

        return out;

        // Complexity analysis 
        // Time : O(N * str_len) 
        // Space : O(N) 
    }

public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // return solve1(strs);

        // return solve2(strs);

        return solve3(strs);
    }
};

void p1() {
    // Problem 1 : Leetcode 49. Group Anagrams - https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/print-anagrams-together/1 

    vector<string> strs = { "eat","tea","tan","ate","nat","bat" };
    vector<vector<string>> out = Problem1().groupAnagrams(strs);
    for (vector<string> vs : out) {
        for (string s : vs) cout << s << " ";
        cout << endl;
    }
}

class Problem2 {
    vector<int> brute(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                int sum = nums[i] + nums[j];
                if (sum == target) return { i, j };
            }
        }

        return { -1, -1 };

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(1) 
    }

    vector<int> better(vector<int>& nums, int target) {
        unordered_map<int, int> mp;

        for (int i = 0; i < nums.size(); i++) {
            int need = target - nums[i];
            if (mp.find(need) != mp.end()) return { i, mp[need] };
            mp[nums[i]] = i;
        }

        return { -1, -1 };

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(N) 
    }

public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // return brute(nums, target);

        return better(nums, target);
    }
};

void p2() {
    // Problem 2 : Leetcode 1. Two Sum - https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150 

    vector<int> nums = { 2,7,11,15 };
    int target = 9;
    vector<int> indices = Problem2().twoSum(nums, target);
    cout << nums[indices[0]] + nums[indices[1]] << endl;
}

class Problem3 {
    int squareSum(int n) {
        int squareSum = 0;

        while (n > 1) {
            int d = n % 10;
            squareSum += (d * d);
            n /= 10;
        }

        squareSum += (n * n);

        return squareSum;
    }

    bool solve1(int n) {
        unordered_set<int> st;

        while (!st.count(n)) {
            st.insert(n);
            n = squareSum(n);
        }

        return n == 1;

        // Complexity analysis 
        // Time : O(1000) ~ 
        // Space : O(1000) ~ 
    }

    bool solve2(int n) {
        int slow = n, fast = n;

        do {
            slow = squareSum(slow);
            fast = squareSum(fast);
            fast = squareSum(fast);
        } while (slow != fast);

        return slow == 1;

        // Complexity analysis 
        // Time : O(1000) 
        // Space : O(1) 
    }

public:
    bool isHappy(int n) {
        // return solve1(n);

        return solve2(n);
    }
};

void p3() {
    // Problem 3 : Leetcode 202. Happy Number - https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/happy-number1408/0 

    cout << Problem3().isHappy(1) << endl;
    cout << Problem3().isHappy(2) << endl;
    cout << Problem3().isHappy(12) << endl;
    cout << Problem3().isHappy(19) << endl;
    cout << Problem3().isHappy(91) << endl;
    cout << Problem3().isHappy(911) << endl;
}

class Problem4 {
    bool brute(vector<int>& nums, int k) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] == nums[j] && abs(i - j) <= k) {
                    return true;
                }
            }
        }

        return false;

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(1) 
    }

    bool better(vector<int>& nums, int k) {
        unordered_map<int, int> mp;

        for (int i = 0; i < nums.size(); i++) {
            int need = nums[i];
            if ((mp.find(need) != mp.end()) && (i - mp[need] <= k)) return true;
            mp[need] = i;
        }

        return false;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(N) 
    }

public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        // return brute(nums, k);

        return better(nums, k);
    }
};

void p4() {
    // Problem 4 : Leetcode 219. Contains Duplicate II - https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150 

    vector<int> nums = { 0, 1, 5, 1, 3, 5, 1, 1 };
    int k = 1;
    cout << Problem4().containsNearbyDuplicate(nums, k) << endl;
}

class Problem5 {
public:
    int longestConsecutive(vector<int> nums) {
        int mlen = 0;

        unordered_map<int, bool> mp;
        for (int n : nums) mp[n] = false;

        for (int n : nums) {
            // already visited 
            if (mp[n]) continue;

            int slen = 1;
            int it = n;
            mp[n] = true;

            // forward 
            it = n + 1;
            while (mp.find(it) != mp.end()) {
                mp[it++] = true; slen++;
            }

            // backward 
            it = n - 1;
            while (mp.find(it) != mp.end()) {
                mp[it--] = true; slen++;
            }

            mlen = max(mlen, slen);
        }

        return mlen;

        // Complexity analysis 
        // Time : O(N) + O(N) 
        // Space : O(N) 
    }
};

void p5() {
    // Problem 5 : Leetcode 128. Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/0 

    vector<int> nums = { 1,3,2,1,3,4,2,1,3,2,1,3,2 };
    cout << Problem5().longestConsecutive(nums) << endl;
}


int main() {
    // Day 14 of January 

    p1();

    p2();

    p3();

    p4();

    p5();


    return 0;
}