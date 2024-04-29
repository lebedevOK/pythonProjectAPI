import unittest
import requests
from data_for_tests.urls import typicode_url


class TestPostApi(unittest.TestCase):
    def setUp(self):
        body = {
            'title': 'fvjvyg uyguuy ioo',
            'body': 'tr yryuytry ouiudjchhb',
            'userId': 1
        }
        headers = {'Content-type': 'application/json'}
        response = requests.post(
            typicode_url,
            json=body,
            headers=headers
        )
        self.post_id = response.json()['id']

    def tearDown(self) -> None:
        requests.delete(f'{typicode_url}/{self.post_id}')

    def test_get_one_post(self):
        # post_id = self.new_post()
        response = requests.get(f'{typicode_url}/{self.post_id}').json()
        self.assertEqual(response['id'], self.post_id)

    def test_get_all_posts(self):
        response = requests.get(typicode_url).json()
        self.assertEqual(len(response), 100)

    def test_add_post(self):
        body = {
            'title': 'fvjvyg uyguuy ioo',
            'body': 'tr yryuytry ouiudjchhb',
            'userId': 1
        }
        headers = {'Content-type': 'application/json'}
        response = requests.post(
            typicode_url,
            json=body,
            headers=headers)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'], 101)

    # def test_create_post(self):
    #     pass
    #
    # def test_put_a_post(self):
    #     pass
    #
    # def test_patch_a_post(self):
    #     pass
    #
    # def test_delete_a_post(self):
    #     pass
