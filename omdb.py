"""
A minimalist Python wrapper for the Open Movie Database (OMDb) API (https://www.omdbapi.com/).
"""

import requests


class Api:

    def __init__(self, apikey, api_version='1'):
        self._apikey = apikey
        self._api_version = api_version
        self._url = 'https://www.omdbapi.com/'

    def search(self, search_string=None, imdb_id=None, title=None, result_type=None, release_year=None, plot='full', return_type='json', page=None, callback=None, season=None, episode=None):
        """

        :param string search_string: Any search phrase that might identify a possible movie title. [optional]
        :param string imdb_id: A valid IMDb ID (e.g. tt1285016). [optional]
        :param string title: Movie title to search for. [optional]
        :param string result_type: Type of result to return. [optional]. Valid Options: [`movie`, `series`, `episode`]
        :param string release_year: Year of release. [optional]
        :param string plot: Return short or full plot. Default value: short. Valid Options: [`short`, `full`]
        :param string return_type: The data type to return. Default value: json. Valid Options: [`json`, `xml`]
        :param int page: Page number to return (for paginated results). [optional]
        :param string callback: JSONP callback name. [optional]
        :param string api_version: API version (reserved for future use). Default value: 1
        :param int season: Season to return a `series` result for.
        :param int episode: Episode to return a `series` result for.
        :return: A list of IMDb objects that match the search.

        Important Notes: Although `search_string`, `imdb_id`, and `title` are all optional, at least one must be chosen or an error will be returned.
        Through testing, it appears that there is a priority order. In other words, if one is provided, it will take priority of the others that are provided.
        This theory can be tested easily by providing three different examples and verifying the results. The priority is as follows: `search_string` > `title` > `imdb_id`.
        Keep in mind that the `release_year` greatly affects the results as well. For example, if you search "terminator" and the year "1984",
        you will get "The Terminator" (`imdb_id` = tt0088247). However, if you search "terminator" with the year "1985", you will get "Ninja Terminator" (`imdb_id` = tt0199849)

        Finally, you can receive more than one object as the result of a search. For example, if you search "terminator" with the year "2002", you will get
        "The Terminator: Dawn of Fate" (`imdb_id` = tt0320595) and "Terminator: A Short Film About JT LeRoy" (`imdb_id` = tt7108520)
        """

        payload = {
            'apikey': self._apikey,
            's': search_string,
            'i': imdb_id,
            't': title,
            'type': result_type,
            'Season': season,
            'Episode': episode,
            'y': release_year,
            'plot': plot,
            'r': return_type,
            'callback': callback,
            'v': self._api_version
        }

        response = requests.get(url=self._api_url, params=payload)

        return response
