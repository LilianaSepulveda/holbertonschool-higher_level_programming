$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  data.results.forEach(movie => {
    $('#list_movies').append(`<li>${movie.title}</li>`);
  });
});
