#!/usr/bin/node

const id = process.argv[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (error, response, body) {
  if (error) {
    return;
  }
  const result = JSON.parse(body).characters;
  orderChars(result, 0);
});

function orderChars (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        orderChars(characters, index + 1);
      }
    }
  });
}
