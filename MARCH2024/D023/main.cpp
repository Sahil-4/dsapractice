#include <iostream>
#include <vector>

using namespace std;

int makeBouquets(vector<int>& bloomDay, int k, int d) {
    int bqts = 0;
    int flwrs = 0;
    for (int i = 0; i < bloomDay.size(); i++) {
        if (bloomDay[i] <= d) {
            flwrs++;

            if (flwrs == k) {
                // we can make a bouquet 
                bqts++;
                flwrs = 0;
            }
        } else {
            flwrs = 0;
        }
    }

    return bqts;
}

int minDays_solution1(vector<int>& bloomDay, int m, int k) {
    int minD = bloomDay[0];
    int maxD = bloomDay[0];
    for (int i = 1; i < bloomDay.size(); i++) {
        minD = min(minD, bloomDay[i]);
        maxD = max(maxD, bloomDay[i]);
    }

    // search space for binary search minD to maxD 
    for (int d = minD; d <= maxD; d++) {
        int bqts = makeBouquets(bloomDay, k, d);
        if (bqts >= m) return d;
    }

    return -1;
}

int minDays(vector<int>& bloomDay, int m, int k) {
    int minD = bloomDay[0];
    int maxD = bloomDay[0];
    for (int i = 1; i < bloomDay.size(); i++) {
        minD = min(minD, bloomDay[i]);
        maxD = max(maxD, bloomDay[i]);
    }

    // search space for binary search minD to maxD 
    int l = minD, h = maxD;
    int mid = l + (h - l) / 2;

    int ans = -1;

    while (l <= h) {
        int bqts = makeBouquets(bloomDay, k, mid);
        if (bqts >= m) {
            ans = mid;
            h = mid - 1;
        } else {
            l = mid + 1;
        }

        mid = l + (h - l) / 2;
    }

    return ans;
}

void p1() {
    // Problem 1 : LC 1482. Minimum Number of Days to Make m Bouquets -  https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/  

    // problem statement : 
    // given an array bloomday[], of size n 
    // and an integer m says how many bouquets we have to make 
    // and another integer k tells how many flowers we have to put in each bouquet 
    // in the array bloomday[], ith element bloomday[i] shows after how many days this ith flower (it is only one flower not i flowers) will bloom 
    // we have to find minimum number of days it will take to make m bouquets of k flowers 

    // vector<int> bloomDay = {1,10,3,10,2};
    // int k = 1, m = 3;
    vector<int> bloomDay = {7,7,7,7,12,7,7};
    int k = 3, m = 2;

    int days = minDays(bloomDay, m, k);

    cout << days << endl;
}

int main() {
    // Day 23 

    p1();


    return 0;
}