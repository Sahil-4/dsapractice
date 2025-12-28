class Movie {
  constructor(movieId, shop, price) {
    this.movieId = movieId;
    this.shop = shop;
    this.price = price;
  }
}

function movieComparator(m1, m2) {
  if (m1[2] != m2[2]) return m1[2] - m2[2];
  if (m1[0] != m2[0]) return m1[0] - m2[0];
  return m1[1] - m2[1];
}

class MovieRentingSystem {
  /**
   * @param {number} n
   * @param {number[][]} entries
   */
  constructor(n, entries) {
    this.resultLength = 5;

    const sortedEntries = entries.sort(movieComparator);

    this.movies = sortedEntries.reduce((moviesMap, [shopId, movieId]) => {
      if (!moviesMap[movieId]) moviesMap[movieId] = [];
      moviesMap[movieId].push(shopId);
      return moviesMap;
    }, {});

    this.shops = sortedEntries.reduce((shopsMap, [shop, movieId, price]) => {
      if (!shopsMap[shop]) shopsMap[shop] = {};
      shopsMap[shop][movieId] = { price };
      return shopsMap;
    }, {});

    this.rentedMovies = [];
  }

  /**
   * @param {number} movieId
   * @return {number[]}
   */
  search(movieId) {
    let results = [];
    const shops = this.movies[movieId];

    for (let i = 0, SN = shops?.length; i < SN && results.length < this.resultLength; i++) {
      let shop = shops[i];
      if (!this.shops[shop][movieId].isRented) results.push(shop);
    }

    return results;
  }

  /**
   * @param {number} shop
   * @param {number} movieId
   * @return {void}
   */
  rent(shop, movieId) {
    if (!this.shops[shop][movieId].isRented) {
      const meta = [shop, movieId, this.shops[shop][movieId].price];
      this.rentedMovies.push(meta);
      this.shops[shop][movieId].isRented = meta;
    }
  }

  /**
   * @param {number} shop
   * @param {number} movieId
   * @return {void}
   */
  drop(shop, movieId) {
    if (this.shops[shop][movieId].isRented) {
      const meta = this.shops[shop][movieId].isRented;
      this.rentedMovies.splice(this.rentedMovies.indexOf(meta), 1);
      delete this.shops[shop][movieId].isRented;
    }
  }

  /**
   * @return {number[][]}
   */
  report() {
    const result = this.rentedMovies.sort(movieComparator).slice(0, this.resultLength);
    return result.map((movie) => [movie[0], movie[1]]);
  }
}

const p1 = () => {
  // Problem 1 : Leetcode 1912. Design Movie Rental System - https://leetcode.com/problems/design-movie-rental-system/description/?envType=problem-list-v2&envId=2vp6ojv1

  const movies = [
    [0, 1, 5],
    [0, 2, 6],
    [0, 3, 7],
    [1, 1, 4],
    [1, 2, 7],
    [2, 1, 5],
  ];

  const rentalSystem = new MovieRentingSystem(6, movies);
  console.log(rentalSystem.search(2));
  console.log(rentalSystem.report());
  rentalSystem.rent(0, 2);
  console.log(rentalSystem.search(2));
  console.log(rentalSystem.report());
  console.log(rentalSystem.search(1));
  rentalSystem.rent(0, 1);
  console.log(rentalSystem.report());
  rentalSystem.drop(0, 1);
  rentalSystem.drop(0, 2);
  console.log(rentalSystem.report());
};

class FoodRatings {
  constructor(foods, cuisines, ratings) {
    this.food2Rating = new Map(); // food -> rating
    this.food2Cuisine = new Map(); // food -> cuisine
    this.cuisine2Foods = new Map(); // cuisine -> Set of {rating, food}

    for (let i = 0; i < foods.length; i++) {
      const food = foods[i];
      const cuisine = cuisines[i];
      const rating = ratings[i];

      this.food2Rating.set(food, rating);
      this.food2Cuisine.set(food, cuisine);

      if (!this.cuisine2Foods.has(cuisine)) {
        this.cuisine2Foods.set(cuisine, new Set());
      }

      this.cuisine2Foods.get(cuisine).add(this._createKey(rating, food));
    }
  }

  _createKey(rating, food) {
    return `${-rating.toString().padStart(5, "0")}:${food}`;
  }

  _parseKey(key) {
    const [ratingStr, food] = key.split(":");
    return { rating: -parseInt(ratingStr), food };
  }

  changeRating(food, newRating) {
    const cuisine = this.food2Cuisine.get(food);
    const oldRating = this.food2Rating.get(food);

    const foods = this.cuisine2Foods.get(cuisine);
    foods.delete(this._createKey(oldRating, food));

    foods.add(this._createKey(newRating, food));
    this.food2Rating.set(food, newRating);
  }

  highestRated(cuisine) {
    const foods = Array.from(this.cuisine2Foods.get(cuisine));
    foods.sort(); // Sort by rating (descending) and food name (ascending)
    return this._parseKey(foods[0]).food;
  }
}

const p2 = () => {
  // Problem 2 : Leetcode 2353. Design a Food Rating System - https://leetcode.com/problems/design-a-food-rating-system/description/?envType=problem-list-v2&envId=2vp6ojv1

  // ! TLE

  const food = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"];
  const cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"];
  const ratings = [9, 12, 8, 15, 14, 7];
  const system = new FoodRatings(food, cuisines, ratings);
  system.highestRated("japanese");
  system.changeRating("ramen", 18);
};

(() => {
  // Day 27 of February 2025

  p1();

  p2();
})();
