#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2]; // The movie ID is the first argument
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.error(error);
  }
});
