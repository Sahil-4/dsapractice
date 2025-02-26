class ATM {
  constructor() {
    this.denominations = [20, 50, 100, 200, 500];
    this.notesCount = [0, 0, 0, 0, 0];
    this.t = 5;
  }

  /**
   * @param {number[]} banknotesCount
   * @return {void}
   */
  deposit(banknotesCount) {
    banknotesCount.forEach((e, i) => {
      this.notesCount[i] += e;
    });

    // Complexity analysis
    // Time : O(5)
    // Space : O(1)
  }

  /**
   * @param {number} amount
   * @return {number[]}
   */
  withdraw(amount) {
    let rnotes = [0, 0, 0, 0, 0];
    let i = this.t - 1;

    for (let i = this.t - 1; i >= 0; i--) {
      const need = Math.min(Math.floor(amount / this.denominations[i]), this.notesCount[i]);
      rnotes[i] = need;
      amount -= this.denominations[i] * need;
    }

    if (amount !== 0) return [-1];

    rnotes.forEach((e, i) => {
      this.notesCount[i] -= e;
    });

    return rnotes;

    // Complexity analysis
    // Time : O(2 * 5)
    // Space : O(1)
  }
}

const p1 = () => {
  // Problem 1 : Leetcode 2241. Design an ATM Machine - https://leetcode.com/problems/design-an-atm-machine/description/?envType=problem-list-v2&envId=2vp6ojv1

  const atm = new ATM();
  console.log(atm.withdraw(500));
  atm.deposit([0, 0, 1, 2, 1]);
  console.log(atm.withdraw(600));
  console.log(atm.withdraw(20));
  console.log(atm.withdraw(100));
  console.log(atm.withdraw(200));
};

class ParkingSystem {
  /**
   * @param {number} big
   * @param {number} medium
   * @param {number} small
   */
  constructor(big, medium, small) {
    this.slots = { 1: big, 2: medium, 3: small };
  }

  /**
   * @param {number} carType
   * @return {boolean}
   */
  addCar(carType) {
    if (this.slots[carType] === 0) return false;
    this.slots[carType]--;
    return true;
  }
}

const p2 = () => {
  // Problem 2 : Leetcode 1603. Design Parking System - https://leetcode.com/problems/design-parking-system/?envType=problem-list-v2&envId=2vp6ojv1

  const system = new ParkingSystem(0, 0, 1);
  console.log(system.addCar(1));
  console.log(system.addCar(2));
  console.log(system.addCar(3));
  console.log(system.addCar(3));
};

(() => {
  // Day 26 of February 2025

  p1();

  p2();
})();
