omdbpy

---

`omdbpy` is a minimalist Python wrapper for the Open Movie Database (OMDb) API (https://www.omdbapi.com/).

# Usage

### Search by `search_terms`
```
>>> import omdb
>>> import json
>>> omdb_api = omdb.Api(apikey='123xyz')
>>> result = omdb_api.search(search_terms='terminator', release_year='1984')
>>> print(json.dumps(result.json(), indent=4))
{
    "Search": [
        {
            "Title": "The Terminator",
            "Year": "1984",
            "imdbID": "tt0088247",
            "Type": "movie",
            "Poster": "https://m.media-amazon.com/images/M/MV5BYTViNzMxZjEtZGEwNy00MDNiLWIzNGQtZDY2MjQ1OWViZjFmXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg"
        },
        {
            "Title": "The Making of 'Terminator'",
            "Year": "1984",
            "imdbID": "tt0267719",
            "Type": "movie",
            "Poster": "https://m.media-amazon.com/images/M/MV5BMTQ3MzE5NTI0Nl5BMl5BanBnXkFtZTgwNDE1OTk1MDE@._V1_SX300.jpg"
        }
    ],
    "totalResults": "2",
    "Response": "True"
}
```

---

### Search by `title`
```
>>> import omdb
>>> import json
>>> omdb_api = omdb.Api(apikey='123xyz')
>>> result = omdb_api.search(title='terminator', release_year='1984')
>>> print(json.dumps(result.json(), indent=4))
{
    "Title": "The Terminator",
    "Year": "1984",
    "Rated": "R",
    "Released": "26 Oct 1984",
    "Runtime": "107 min",
    "Genre": "Action, Sci-Fi",
    "Director": "James Cameron",
    "Writer": "James Cameron, Gale Anne Hurd, William Wisher (additional dialogue)",
    "Actors": "Arnold Schwarzenegger, Michael Biehn, Linda Hamilton, Paul Winfield",
    "Plot": "A cyborg is sent from the future on a deadly mission. He has to kill Sarah Connor, a young woman whose life will have a great significance in years to come. Sarah has only one protector - Kyle Reese - also sent from the future. The Terminator uses his exceptional intelligence and strength to find Sarah, but is there any way to stop the seemingly indestructible cyborg ?",
    "Language": "English, Spanish",
    "Country": "UK, USA",
    "Awards": "6 wins & 6 nominations.",
    "Poster": "https://m.media-amazon.com/images/M/MV5BYTViNzMxZjEtZGEwNy00MDNiLWIzNGQtZDY2MjQ1OWViZjFmXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg",
    "Ratings": [
        {
            "Source": "Internet Movie Database",
            "Value": "8.0/10"
        },
        {
            "Source": "Rotten Tomatoes",
            "Value": "100%"
        },
        {
            "Source": "Metacritic",
            "Value": "84/100"
        }
    ],
    "Metascore": "84",
    "imdbRating": "8.0",
    "imdbVotes": "734,748",
    "imdbID": "tt0088247",
    "Type": "movie",
    "DVD": "03 Sep 1997",
    "BoxOffice": "N/A",
    "Production": "Orion Pictures Corporation",
    "Website": "http://www.terminator1.com/",
    "Response": "True"
}
```

---

#### Search by `imdb_id`
```
>>> import omdb
>>> import json
>>> omdb_api = omdb.Api(apikey='123xyz')
>>> result = omdb_api.search(imdb_id='tt0088247', release_year='1984')
>>> print(json.dumps(result.json(), indent=4))
{
    "Title": "The Terminator",
    "Year": "1984",
    "Rated": "R",
    "Released": "26 Oct 1984",
    "Runtime": "107 min",
    "Genre": "Action, Sci-Fi",
    "Director": "James Cameron",
    "Writer": "James Cameron, Gale Anne Hurd, William Wisher (additional dialogue)",
    "Actors": "Arnold Schwarzenegger, Michael Biehn, Linda Hamilton, Paul Winfield",
    "Plot": "A cyborg is sent from the future on a deadly mission. He has to kill Sarah Connor, a young woman whose life will have a great significance in years to come. Sarah has only one protector - Kyle Reese - also sent from the future. The Terminator uses his exceptional intelligence and strength to find Sarah, but is there any way to stop the seemingly indestructible cyborg ?",
    "Language": "English, Spanish",
    "Country": "UK, USA",
    "Awards": "6 wins & 6 nominations.",
    "Poster": "https://m.media-amazon.com/images/M/MV5BYTViNzMxZjEtZGEwNy00MDNiLWIzNGQtZDY2MjQ1OWViZjFmXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg",
    "Ratings": [
        {
            "Source": "Internet Movie Database",
            "Value": "8.0/10"
        },
        {
            "Source": "Rotten Tomatoes",
            "Value": "100%"
        },
        {
            "Source": "Metacritic",
            "Value": "84/100"
        }
    ],
    "Metascore": "84",
    "imdbRating": "8.0",
    "imdbVotes": "734,748",
    "imdbID": "tt0088247",
    "Type": "movie",
    "DVD": "03 Sep 1997",
    "BoxOffice": "N/A",
    "Production": "Orion Pictures Corporation",
    "Website": "http://www.terminator1.com/",
    "Response": "True"
}
```

---

## Important Notes about OMDb API
Although `search_terms`, `imdb_id`, and `title` are all optional, at least one must be chosen or an error will be returned.
Through testing, it appears that there is a priority order. In other words, if one query parameter is provided, it will take priority over the others
that are provided. This theory can be tested easily by providing three different examples and verifying the results. 
The priority is as follows: `search_terms` > `title` > `imdb_id`. Keep in mind that the `release_year` greatly affects the results as well. 

For example, if you search via `title` with  `title="terminator"` and the `release_year="1984"`, you will get `The Terminator (imdb_id=tt0088247)`:
```
>>> import omdb
>>> import json
>>> omdb_api = omdb.Api(apikey='123xyz')
>>> result = omdb_api.search(title='terminator', release_year='1984')
>>> print(json.dumps(result.json(), indent=4))
{
    "Title": "The Terminator",
    "Year": "1984",
    "Rated": "R",
    "Released": "26 Oct 1984",
    "Runtime": "107 min",
    "Genre": "Action, Sci-Fi",
    "Director": "James Cameron",
    "Writer": "James Cameron, Gale Anne Hurd, William Wisher (additional dialogue)",
    "Actors": "Arnold Schwarzenegger, Michael Biehn, Linda Hamilton, Paul Winfield",
    "Plot": "A cyborg is sent from the future on a deadly mission. He has to kill Sarah Connor, a young woman whose life will have a great significance in years to come. Sarah has only one protector - Kyle Reese - also sent from the future. The Terminator uses his exceptional intelligence and strength to find Sarah, but is there any way to stop the seemingly indestructible cyborg ?",
    "Language": "English, Spanish",
    "Country": "UK, USA",
    "Awards": "6 wins & 6 nominations.",
    "Poster": "https://m.media-amazon.com/images/M/MV5BYTViNzMxZjEtZGEwNy00MDNiLWIzNGQtZDY2MjQ1OWViZjFmXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg",
    "Ratings": [
        {
            "Source": "Internet Movie Database",
            "Value": "8.0/10"
        },
        {
            "Source": "Rotten Tomatoes",
            "Value": "100%"
        },
        {
            "Source": "Metacritic",
            "Value": "84/100"
        }
    ],
    "Metascore": "84",
    "imdbRating": "8.0",
    "imdbVotes": "734,748",
    "imdbID": "tt0088247",
    "Type": "movie",
    "DVD": "03 Sep 1997",
    "BoxOffice": "N/A",
    "Production": "Orion Pictures Corporation",
    "Website": "http://www.terminator1.com/",
    "Response": "True"
}
``` 

However, if you search via `search_terms` with `search_terms="terminator"` with `release_year="1985"`, you will get `Ninja Terminator (imdb_id=tt0199849)`:
```
>>> import omdb
>>> import json
>>> omdb_api = omdb.Api(apikey='123xyz')
>>> result = omdb_api.search(search_terms='terminator', release_year='1985')
>>> print(json.dumps(result.json(), indent=4))
{
    "Search": [
        {
            "Title": "Ninja Terminator",
            "Year": "1985",
            "imdbID": "tt0199849",
            "Type": "movie",
            "Poster": "https://m.media-amazon.com/images/M/MV5BMGZiNTczNWItOTdmYy00OTFjLWIwOWUtMmE3Y2QyNzBmZDJkXkEyXkFqcGdeQXVyNzg3NjQyOQ@@._V1_SX300.jpg"
        }
    ],
    "totalResults": "1",
    "Response": "True"
}
```

Often, you will receive more than one object as the result of a search. For example, if you search via `search_terms` with `search_terms="terminator"` with the `release_year="2002"`, you will get
`The Terminator: Dawn of Fate (imdb_id=tt0320595)` and `Terminator: A Short Film About JT LeRoy (imdb_id=tt7108520)`:
```
>>> import omdb
>>> import json
>>> omdb_api = omdb.Api(apikey='123xyz')
>>> result = omdb_api.search(search_terms='terminator', release_year='2002')
>>> print(json.dumps(result.json(), indent=4))
{
    "Search": [
        {
            "Title": "The Terminator: Dawn of Fate",
            "Year": "2002",
            "imdbID": "tt0320595",
            "Type": "game",
            "Poster": "https://m.media-amazon.com/images/M/MV5BYjEyNWU3Y2ItMGI4MS00OGY2LTk2ZTUtNWQyNDY3MTRmM2I1XkEyXkFqcGdeQXVyMzM4MjM0Nzg@._V1_SX300.jpg"
        },
        {
            "Title": "Terminator: A Short Film About JT LeRoy",
            "Year": "2002",
            "imdbID": "tt7108520",
            "Type": "movie",
            "Poster": "N/A"
        }
    ],
    "totalResults": "2",
    "Response": "True"
}
```

If there are no results, you will get a response with a message like this one:
```
>>> import omdb
>>> import json
>>> omdb_api = omdb.Api(apikey='123xyz')
>>> result = omdb_api.search(search_terms='terminator', release_year='32')
>>> print(json.dumps(result.json(), indent=4))
{
    "Response": "False",
    "Error": "Movie not found!"
}
```

Finally, if the request doesn't make sense, you will get a response with a message like this one:
```
>>> import omdb
>>> import json
>>> omdb_api = omdb.Api(apikey='123xyz')
>>> result = omdb_api.search(release_year='32')
>>> print(json.dumps(result.json(), indent=4))
{
    "Response": "False",
    "Error": "Something went wrong."
}
```