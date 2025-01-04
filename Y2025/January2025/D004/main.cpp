#include <bits/stdc++.h>

using namespace std;


class RandomizedSet {
    vector<int> keys;              // { key }
    unordered_map<int, int> map; // {key -> index }

    int getRandomIndex() {
        return rand() % keys.size();
    }

public:
    RandomizedSet() {}

    bool insert(int key) {
        if (map.find(key) != map.end()) return false;

        map.insert({ key, keys.size() });
        keys.push_back(key);

        return true;
    }

    bool remove(int dkey) {
        if (map.find(dkey) == map.end()) return false;

        // swap index of key with last key in keys 
        // key is to be deleted 
        // instead of deleting key from between of the vector 
        // we will swap key with last element in vector 
        // and then delete the last element 
        // with this we will have to update index in map also 
        // new index of map[lkey] will be map[key] 

        // update index of lkey in map 
        int lkey = keys.back();
        map[lkey] = map[dkey]; // key = dkey, key to be deleted 

        // put lkey at dkey's place 
        keys[map[dkey]] = lkey;

        keys.pop_back();
        map.erase(dkey);

        return true;
    }

    int getRandom() {
        int index = getRandomIndex();
        return keys[index];
    }

    // Complexity analysis 
    // Time : O(1) average / O(N) for map in worst case 
    // Space : O(1) + O(3N) storage 
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */

void p1() {
    // Problem 1 : Leetcode 380. Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150 

    RandomizedSet* rs = new RandomizedSet();

    cout << rs->remove(1) << endl; // false 
    cout << rs->insert(1) << endl; // true 
    cout << rs->getRandom() << endl; // 1 
    cout << rs->remove(1) << endl; // true 
    cout << rs->insert(1) << endl; // true 
    cout << rs->getRandom() << endl; // 1 
    cout << rs->insert(5) << endl; // true 
    cout << rs->insert(2) << endl; // true 
    cout << rs->insert(2) << endl; // false 
    cout << rs->insert(8) << endl; // true 
    cout << rs->getRandom() << endl; // any(1, 2, 5, 8) 
}

class Problem2 {
    vector<int> brute(vector<int>& nums) {
        vector<int> answer;

        for (int i = 0; i < nums.size(); i++) {
            int prod = 1;
            for (int j = 0; j < nums.size(); j++) {
                if (i != j) prod *= nums[j];
            }
            answer.push_back(prod);
        }

        return answer;

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(1) 
    }

    vector<int> optimal(vector<int>& nums) {
        int prod = 1;
        int zeroes = 0; // contains zero 
        for (int j = 0; j < nums.size(); j++) {
            if (nums[j] == 0) zeroes++;
            else prod *= nums[j];
        }

        vector<int> answer(nums.size(), 0);
        for (int i = 0; i < nums.size() && zeroes == 1; i++) {
            if (nums[i] == 0) answer[i] = prod;
        }
        for (int i = 0; i < nums.size() && zeroes == 0; i++) {
            answer[i] = prod / nums[i];
        }

        return answer;

        // Complexity analysis 
        // Time : O(2N) 
        // Space : O(1) 
    }

public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // return brute(nums);

        return optimal(nums);
    }
};

void p2() {
    // Problem 2 : Leetcode 238. Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/product-array-puzzle4525/1 

    // vector<int> nums = { 1, 2, 2, 5, 4 };
    // vector<int> nums = { 1, 2, 0, 5, 4 };
    vector<int> nums = { 1, 2, 0, 5, 0 };
    vector<int> answer = Problem2().productExceptSelf(nums);
    for (int e : answer) cout << e << " ";
    cout << endl;
}

class Problem3 {
    int brute(vector<int>& gas, vector<int>& cost) {
        int N = gas.size(); // number of stations 

        for (int si = 0; si < N; si++) {
            int i = si; // we are currently at 
            int tank = gas[i]; // refuel tank 

            // move to next station till we dont reach to si 
            do {
                // if we have much fuel to move from i to i+1 
                if (tank < cost[i]) break;

                // reduce fuel 
                tank -= cost[i];

                // move to next station 
                i = ((i + 1) % N);

                // refuel 
                tank += gas[i];

                // if we reached to si again after moving circularly 
                if (i == si) return si;
            } while (i != si);
        }

        return -1;

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(1) 
    }

    int greedy(vector<int>& gas, vector<int>& cost) {
        // check whether answer is possible or not 
        int tgas = accumulate(gas.begin(), gas.end(), 0);
        int tcost = accumulate(cost.begin(), cost.end(), 0);
        if (tgas < tcost) return -1;

        // if answer is possible - 

        int N = gas.size();

        int tank = 0; // currently fuel 
        int si = 0; // index to start with 

        for (int i = 0; i < N; i++) {
            // add gas and reduce cost to reach to ith station 
            tank += gas[i] - cost[i];

            // in si was not correct answer 
            if (tank < 0) {
                tank = 0;
                si = i + 1;
            }
        }

        return si;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        // return brute(gas, cost);

        return greedy(gas, cost);
    }
};

void p3() {
    // Problem 3 : Leetcode 134. Gas Station - https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/circular-tour-1587115620/1 

    vector<int> gas = { 1,1,1,3 };
    vector<int> cost = { 2,1,2,1 };

    cout << Problem3().canCompleteCircuit(gas, cost) << endl;
}

class Problem4 {
    int greedy1(vector<int>& ratings) {
        // greed factor :
        // first compare children with its left
        // then in second itereation compare with its right
        // finally sum up all candies and return

        int N = ratings.size();
        // vector<int> candies(N, 0);
        vector<int> candies(N, 1);

        // give one candy to first child
        // as there is no one on its left
        // candies[0] = 1;

        for (int i = 1; i < N; i++) {
            // give one candy if it has less rating then its left child
            // candies[i] = 1;
            // give more candies then its left child if its rating it more
            if (ratings[i] > ratings[i - 1]) candies[i] += candies[i - 1];
        }

        for (int i = N - 2; i >= 0; i--) {
            // give more candies then its right child if its rating it more and
            // has less candies
            if (ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1]) {
                candies[i] = candies[i + 1] + 1;
            }
        }

        // sum up all candies
        int candiesSum = 0;
        for (int c : candies) candiesSum += c;

        return candiesSum;

        // Complexity analysis
        // Time : O(3N)
        // Space : O(N)
    }

    int greedy2(vector<int>& ratings) {
        int N = ratings.size();

        int candies = N;

        int i = 1;
        while (i < N) {
            if (ratings[i] == ratings[i - 1]) {
                i++;
                continue;
            }

            // peak
            int peak = 0;
            while (ratings[i] > ratings[i - 1]) {
                i++;
                peak++;
                candies += peak;
                if (i == N) return candies;
            }

            // valley
            int valley = 0;
            while (i < N && ratings[i] < ratings[i - 1]) {
                i++;
                valley++;
                candies += valley;
            }

            candies -= min(peak, valley);
        }

        return candies;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

public:
    int candy(vector<int>& ratings) {
        // return greedy1(ratings);

        return greedy2(ratings);
    }
};

void p4() {
    // Problem 4 : Leetcode 135. Candy - https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/candy/1 

    vector<int> ratings = { 2, 5, 4, 3, 1, 2, 0, 5, 7 };

    cout << Problem4().candy(ratings) << endl;
}


int main() {
    // Day 4 of January 

    p1();

    p2();

    p3();

    p4();


    return 0;
}