#!/usr/bin/node
window.$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const dict of data.results) {
    const txt2 = window.$('<li></li>').text(dict.title);
    window.$('#list_movies').append(txt2);
  }
});
