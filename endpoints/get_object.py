import requests

from data_for_tests.urls import base_url
from endpoints.base_endpoint import Endpoint


class GetObject(Endpoint):

    def get_by_id(self, id):
        self.response = requests.get(f'{base_url}/{id}')
        self.response_json = self.response.json()

    def check_response_id(self, object_id):
        assert self.response_json['id'] == object_id

    def check_response_is_404(self):
        assert self.response.status_code == 404
