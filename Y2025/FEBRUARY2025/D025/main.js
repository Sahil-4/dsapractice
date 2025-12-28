class TravelTimeNode {
  constructor(sum, count) {
    this.sum = sum;
    this.count = count;
    this.avg = sum / count;
  }

  updateAvg() {
    this.avg = this.sum / this.count;
  }
}

class CheckIn {
  constructor(startStation, t) {
    this.startStation = startStation;
    this.t = t;
  }
}

class UndergroundSystem {
  constructor() {
    // travelTimes[startStation][endStation] = new TravelTimeNode()
    this.travelTimes = new Map();
    // checkIns[cardId] = new checkIn()
    this.checkIns = new Map();
  }

  /**
   * @param {number} id
   * @param {string} stationName
   * @param {number} t
   * @return {void}
   */
  checkIn(id, stationName, t) {
    this.checkIns[id] = new CheckIn(stationName, t);

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @param {number} id
   * @param {string} stationName
   * @param {number} t
   * @return {void}
   */
  checkOut(id, stationName, t) {
    const checkIn = this.checkIns[id];
    const travelTime = t - checkIn.t;
    const startStation = checkIn.startStation;
    const endStation = stationName;

    if (!this.travelTimes[startStation]) {
      this.travelTimes[startStation] = new Map();
    }

    if (!this.travelTimes[startStation][endStation]) {
      this.travelTimes[startStation][endStation] = new TravelTimeNode(0, 0);
    }

    this.travelTimes[startStation][endStation].sum += travelTime;
    this.travelTimes[startStation][endStation].count += 1;

    this.travelTimes[startStation][endStation].updateAvg();

    delete this.checkIns[id];

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @param {string} startStation
   * @param {string} endStation
   * @return {number}
   */
  getAverageTime(startStation, endStation) {
    if (!this.travelTimes[startStation] || !this.travelTimes[startStation][endStation]) {
      return 0;
    }

    return this.travelTimes[startStation][endStation].avg;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }
}

const p1 = () => {
  // Problem 1 : Leetcode 1396. Design Underground System - https://leetcode.com/problems/design-underground-system/description/?envType=problem-list-v2&envId=2vp6ojv1

  const system = new UndergroundSystem();
  system.checkIn(100, "A", 1200);
  system.checkOut(100, "B", 1210);
  console.log(system.getAverageTime("A", "B"));
  system.checkIn(200, "A", 1400);
  system.checkOut(200, "B", 1215);
  console.log(system.getAverageTime("A", "B"));
};

class DLLNode {
  constructor(data) {
    this.data = data;
    this.next = null;
    this.prev = null;
  }
}

class BrowserHistory {
  /**
   * @param {string} homepage
   */
  constructor(homepage) {
    this.head = new DLLNode(homepage);
    this.pointer = this.head;
  }

  /**
   * @param {string} url
   * @return {void}
   */
  visit(url) {
    // forward history is deleted
    delete this.pointer.next;

    // create new page
    const node = new DLLNode(url);
    node.prev = this.pointer; // update prev pointer of new page

    // add into browser history stack
    this.pointer.next = node;

    // update current page pointer
    this.pointer = this.pointer.next;

    // Complexity analysis
    // Time : O(1)
    // Space : O(1)
  }

  /**
   * @param {number} steps
   * @return {string}
   */
  back(steps) {
    while (steps-- && this.pointer.prev) {
      this.pointer = this.pointer.prev;
    }
    return this.pointer.data;

    // Complexity analysis
    // Time : O(K) k = steps
    // Space : O(1)
  }

  /**
   * @param {number} steps
   * @return {string}
   */
  forward(steps) {
    while (steps-- && this.pointer.next) {
      this.pointer = this.pointer.next;
    }
    return this.pointer.data;

    // Complexity analysis
    // Time : O(K) k = steps
    // Space : O(1)
  }
}

const p2 = () => {
  // Problem 2 : Leetcode 1472. Design Browser History - https://leetcode.com/problems/design-browser-history/description/?envType=problem-list-v2&envId=2vp6ojv1
  // Geeksforgeeks - https://www.geeksforgeeks.org/problems/design-browser-history/0

  const tab = new BrowserHistory("/");
  console.log(tab.forward(1));
  console.log(tab.back(1));
  tab.visit("/about");
  tab.visit("/profile");
  tab.visit("/settings");
  console.log(tab.back(0));
  console.log(tab.forward(0));
  console.log(tab.back(5));
  console.log(tab.forward(5));
  console.log(tab.back(5));
  tab.visit("/dashboard");
  console.log(tab.forward(0));
  console.log(tab.forward(1));
  console.log(tab.forward(5));
};

(() => {
  // Day 25 of February 2025

  p1();

  p2();
})();
