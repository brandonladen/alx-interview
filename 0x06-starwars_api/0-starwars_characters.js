#!/usr/bin/node

const axios = require('axios').default;
movie_id = process.argv[2]
async function getCharacters () {
  try {
    const people = await axios.get(`https://swapi-api.alx-tools.com/api/films/${movie_id}/`); //returns a list -> people.data['characters']
    for(let i = 0; i < people.data['characters'].length; i++){
        const character = await axios.get(people.data['characters'][i]);
        console.log(character.data['name']);
    };
  } catch (error) {
    console.error(error);
  }
}
getCharacters()