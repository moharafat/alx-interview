#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Base URL for the Star Wars API
const baseUrl = 'https://swapi-api.alx-tools.com/api';

// Function to make a GET request to the API
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// Function to get and print character names
async function getAndPrintCharacters(movieId) {
  try {
    // Get the movie data
    const movieUrl = `${baseUrl}/films/${movieId}/`;
    const movieData = await makeRequest(movieUrl);

    // Get the character URLs
    const characterUrls = movieData.characters;

    // Fetch and print each character's name
    for (const characterUrl of characterUrls) {
      const characterData = await makeRequest(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Call the function with the provided movie ID
getAndPrintCharacters(movieId);