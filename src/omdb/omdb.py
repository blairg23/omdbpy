"""
A minimalist Python wrapper for the Open Movie Database (OMDb) API (https://www.omdbapi.com/).
"""

import requests


class Api:
    def __init__(self, apikey, api_version="1"):
        """

        :param str apikey: Valid OMDb API key credentials.
        :param str api_version: API version (reserved for future use). Default value: 1
        """
        self._apikey = apikey
        self._api_version = api_version
        self._url = "https://www.omdbapi.com/"

    def search(
        self,
        search_terms=None,
        imdb_id=None,
        title=None,
        result_type=None,
        release_year=None,
        plot="full",
        return_type="json",
        page=None,
        callback=None,
        season=None,
        episode=None,
    ):
        """

        :param str search_terms: Any search phrase that might identify a possible movie title. [optional]
        :param str imdb_id: A valid IMDb ID (e.g. tt1285016). [optional]
        :param str title: Movie title to search for. [optional]
        :param str result_type: Type of result to return. [optional]. Valid Options: [`movie`, `series`, `episode`]
        :param str release_year: Year of release. [optional]
        :param str plot: Return short or full plot. Default value: short. Valid Options: [`short`, `full`]
        :param str return_type: The data type to return. Default value: json. Valid Options: [`json`, `xml`]
        :param int page: Page number to return (for paginated results). [optional]
        :param str callback: JSONP callback name. [optional]
        :param int season: Season to return a `series` result for.
        :param int episode: Episode to return a `series` result for.
        :return: An HTTP `requests` response object containing a list of IMDb objects that match the search criteria.

        """

        payload = {
            "apikey": self._apikey,
            "s": search_terms,
            "i": imdb_id,
            "t": title,
            "type": result_type,
            "Season": season,
            "Episode": episode,
            "y": release_year,
            "plot": plot,
            "r": return_type,
            "callback": callback,
            "v": self._api_version,
        }

        response = requests.get(url=self._url, params=payload)

        return response
