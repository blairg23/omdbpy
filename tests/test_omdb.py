from unittest import mock, TestCase

import faker

module_under_test = 'src.omdb'
fake = faker.Faker()


class ApiTestCase(TestCase):
    def setUp(self):
        self.mock_api_patch = mock.patch(f'{module_under_test}.Api', autospec=True)
        self.mock_api = self.mock_api_patch.start()

    def tearDown(self):
        self.mock_api_patch.stop()

    def test_initialization(self):
        apikey = fake.word
        api_version = fake.pyint
        omdb_api = self.mock_api_patch(apikey=apikey, api_version=api_version)
        self.assertIsInstance(omdb_api, self.mock_api_patch)
        self.assertEquals(self.mock_api_patch._apikey, apikey)
        self.assertEquals(self.mock_api_patch._api_version, api_version)

    def test_search_by_search_string(self):
        response = self.mock_api.search(search_string=fake.words, release_year=fake.year)
        self.mock_api.search.assert_called_once()

    def test_search_by_title(self):
        response = self.mock_api.search(title=fake.words, release_year=fake.year)
        self.mock_api.search.assert_called_once()

    def test_search_by_imdb_id(self):
        response = self.mock_api.search(imdb_id=fake.words, release_year=fake.year)
        self.mock_api.search.assert_called_once()



