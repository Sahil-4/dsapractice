const p1 = () => {
  // Problem 1 : POTD Leetcode 2818. Apply Operations to Maximize Score - https://leetcode.com/problems/apply-operations-to-maximize-score/description/?envType=daily-question&envId=2025-03-29

  // check main.cpp 
};

class DSU {
  constructor(size) {
      this.parent = Array(size + 1).fill(0).map((_, i) => i);
  }

  find(x) {
      if (this.parent[x] === x) return x;
      return this.parent[x] = this.find(this.parent[x]); // Path compression
  }

  union(x, y) {
      this.parent[this.find(x)] = this.find(y); // Merge sets
  }
}

class Problem2 {
  jobSequencing(deadline, profit) {
      // code here
      const N = deadline.length;

      const jobs = [];

      for (let i = 0; i < N; i++) {
          jobs.push([deadline[i], profit[i]]);
      }
      jobs.sort((a, b) => b[1] - a[1]);

      const lastDeadline = Math.max(...deadline);

      const dsu = new DSU(lastDeadline);

      let jobsCount = 0;
      let profitCount = 0;

      for (let [deadline_i, profit_i] of jobs) {
          // for this job 
          let availableSlot = dsu.find(deadline_i);

          if (availableSlot > 0) {
              // Mark not available slot 
              dsu.union(availableSlot, availableSlot - 1);
              jobsCount++;
              profitCount += profit_i;
          }
      }

      return [jobsCount, profitCount];

      // Complexity analysis 
      // Time : O(N*LOG(N)) + O(N*4ALPHA) 
      // Space : O(2N) + O(DEADLINE) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Job Sequencing Problem - https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1 

  console.log(new Problem2().jobSequencing([11, 2, 5, 8, 11, 10, 1, 6, 3, 8, 10], [321, 62, 456, 394, 424, 22, 393, 87, 118, 384, 83]));
};

(() => {
  // Day 29 of March 2025

  p1();

  p2();

})();
