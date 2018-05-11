$(function () {
  $.get('https://swapi.co/api/films/?format=json', function (data, status) {
    if (status === 'success') {
      let movies = data.results;
      for (let i in movies) {
        let movie = $('<li></li>').text(movies[i]['title']);
        $('ul#list_movies').append(movie);
      }
    }
  });
});
