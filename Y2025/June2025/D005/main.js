class UnionSet {
  constructor() {
    this.parent = new Array(26);
    for (let i = 0; i < 26; i++) {
      this.parent[i] = i;
    }
  };

  union(u, v) {
    let parU = this.findParent(u);
    let parV = this.findParent(v);

    if (parU === parV) return;

    if (parU < parV) {
      this.parent[parV] = parU;
    } else {
      this.parent[parU] = parV;
    }
  };

  findParent(u) {
    if (this.parent[u] === u) return u;
    return this.parent[u] = this.findParent(this.parent[u]);
  };
};

/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} baseStr
 * @return {string}
 */
var smallestEquivalentString = function (s1, s2, baseStr) {
  // index <-> char 
  const resolveCharIndex = char => char.charCodeAt(0) - 'a'.charCodeAt(0);
  const resolveIndexChar = index => String.fromCharCode('a'.charCodeAt(0) + index);

  const us = new UnionSet();

  for (let i = 0; i < s1.length; i++) {
    us.union(resolveCharIndex(s1[i]), resolveCharIndex(s2[i]));
  }

  let out = [];

  for (let i = 0; i < baseStr.length; i++) {
    let cindex = resolveCharIndex(baseStr[i]);
    let pindex = us.findParent(cindex);
    let pchar = resolveIndexChar(pindex);
    out.push(pchar);
  }

  return out.join("");

  // Complexity analysis 
  // Time : O(slen * 4Alpha) + O(blen * 4Alpha) 
  // Space : O(26) 
};

const p1 = () => {
  // Problem 1 : POTD Leetcode 1061. Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/?envType=daily-question&envId=2025-06-05 

  console.log(smallestEquivalentString("parker", "morris", "parser"));
  console.log(smallestEquivalentString("hello", "world", "hold"));
  console.log(smallestEquivalentString("leetcode", "programs", "sourcecode"));
};

// User function Template for javascript
/**
 * @param {number[][]} edges
 * @param {number} V
 * @param {number} src
 * @param {number} dest
 * @returns {number}
 */

class Problem2 {
  // Function to count the number of paths from src to dest.
  countPaths(edges, V, src, dest) {
    // your code here

    // build adjacency list 
    const adj = Array.from({ length: V }, () => new Array());
    const indegree = new Array(V).fill(0);
    for (let [u, v] of edges) {
      adj[u].push(v);
      indegree[v]++;
    }

    // Kahn's 
    let topo = [];
    let queue = [];

    for (let i = 0; i < V; i++) {
      if (indegree[i] === 0) queue.push(i);
    }

    while (queue.length) {
      const u = queue.shift();
      topo.push(u);

      for (let v of adj[u]) {
        indegree[v]--;
        if (indegree[v] === 0) queue.push(v);
      }
    }

    // paths - using previous visited paths 
    const paths = new Array(V).fill(0);
    paths[src] = 1;

    for (let u of topo) {
      for (let v of adj[u]) {
        paths[v] += paths[u];
      }
    }

    // number of paths to reach dest node 
    return paths[dest];

    // Complexity analysis 
    // Time : O(3 * (V + E)) 
    // Space : O(4V) 
  }
}

const p2 = () => {
  // Problem 2 : POTD Geeksforgeeks Count the paths - https://www.geeksforgeeks.org/problems/count-the-paths4332/1 

  console.log(new Problem2().countPaths([[0, 1], [0, 3], [2, 0], [2, 1], [1, 3]], 4, 2, 3));
  console.log(new Problem2().countPaths([[0, 1], [1, 2], [1, 3], [2, 3]], 4, 0, 3));
};


(() => {
  // Day 5 of June 2025

  p1();

  p2();
})();
