#include <iostream>
#include <vector>

using namespace std;

long long computeHours(vector<int>& piles, int k) {
    long long hours = 0;

    for (int i = 0; i < piles.size(); i++) {
        if (piles[i] <= k) {
            hours += 1;
        } else {
            int e = (piles[i] % k) > 0 ? 1 : 0;
            hours += (piles[i] / k);
            hours += e;
        }
    }

    return hours;
}

int minEatingSpeed_solution1(vector<int>& piles, int h) {
    int array_max = piles[0];
    for (int i = 1; i < piles.size(); i++) if (array_max < piles[i]) array_max = piles[i];

    for (int k = 1; k <= array_max; k++) {
        long long hours = computeHours(piles, k);
        if (hours <= h) return k;
    }

    return array_max;
    // !TLE 
}

int minEatingSpeed(vector<int>& piles, int h) {
    int array_max = piles[0];
    for (int i = 1; i < piles.size(); i++) if (array_max < piles[i]) array_max = piles[i];

    int low = 1, high = array_max;
    int m = low + (high - low) / 2;

    int k = 0;

    while (low <= high) {
        long long hours = computeHours(piles, m);
        if (hours <= h) {
            k = m;
            high = m - 1;
        } else {
            low = m + 1;
        }

        m = low + (high - low) / 2;
    }

    return k;

    // Tc = O(n * log(max(piles[])) 
    // Sc = O(1) 
}

void p1() {
    // P1 LC 875. Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/ 

    vector<int> piles = {3,6,7,11};
    int h = 8;

    int k = minEatingSpeed(piles, h);

    cout << k << endl;
}

int main() {
    // Day 22 

    p1();


    return 0;
}