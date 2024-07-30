#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const wedgeAntillesId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;

  const wedgeAntillesCount = films.reduce((count, film) => {
    const hasWedgeAntilles = film.characters.some(characterUrl => 
      characterUrl.endsWith(`/api/people/${wedgeAntillesId}/`)
    );
    return hasWedgeAntilles ? count + 1 : count;
  }, 0);

  console.log(wedgeAntillesCount);
});
