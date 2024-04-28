import requests

from data_for_tests.urls import base_url
from endpoints.base_endpoint import Endpoint


class CreateObject(Endpoint):

    def new_object(self, payload_base):
        self.response = requests.post(base_url, json=payload_base)
        self.response_json = self.response.json()

    def check_name(self, name):
        assert self.response_json['name'] == name
