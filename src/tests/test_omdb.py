from unittest import mock, TestCase

import faker
import omdb

module_under_test = "omdb"

fake = faker.Faker()


class ApiTestCase(TestCase):
    def setUp(self):
        self.mock_requests_patch = mock.patch(
            f"{module_under_test}.omdb.requests", autospec=True
        )
        self.mock_requests = self.mock_requests_patch.start()

        self._apikey = fake.word
        self._api_version = str(fake.pyint)
        self._omdb_api = omdb.Api(apikey=self._apikey, api_version=self._api_version)

    def tearDown(self):
        self.mock_requests_patch.stop()

    def test_initialization(self):
        self.assertIsInstance(self._omdb_api, omdb.Api)
        self.assertEqual(self._omdb_api._apikey, self._apikey)
        self.assertEqual(self._omdb_api._api_version, self._api_version)

    def test_search_by_search_terms(self):
        self._omdb_api.search(search_terms=fake.words, release_year=fake.year)
        self.mock_requests.get.assert_called_once()

    def test_search_by_title(self):
        self._omdb_api.search(title=fake.words, release_year=fake.year)
        self.mock_requests.get.assert_called_once()

    def test_search_by_imdb_id(self):
        self._omdb_api.search(imdb_id=fake.words, release_year=fake.year)
        self.mock_requests.get.assert_called_once()
