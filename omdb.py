"""
A minimalist Python wrapper for the Open Movie Database (OMDb) API (https://www.omdbapi.com/).
"""

import requests
import json


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

        response = requests.get(url=self._url, params=payload)

        return response


if __name__ == '__main__':
    # Get your free API key at https://www.omdbapi.com/apikey.aspx
    # You can use mine, but you'll be sharing it with other users of this library!
    omdb_api = Api(apikey='7b7c7bc4')
    result = omdb_api.search(search_string='terminator', release_year='1984')
    print(json.dumps(result.json(), indent=4))
