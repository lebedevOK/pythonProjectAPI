import requests

from data_for_tests.urls import base_url
from endpoints.base_endpoint import Endpoint


class DeleteObject(Endpoint):

    def delete_by_id(self, object_id):
        self.response = requests.delete(f'{base_url}/{object_id}')
        self.response_json = self.response.json()

    def check_response_is_404(self):
        assert self.response.status_code == 404
