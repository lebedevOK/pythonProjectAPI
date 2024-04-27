import requests
from endpoints.base_endpoint import Endpoint


class UpdateObject(Endpoint):

    def update_by_id(self, object_id, payload_new):
        self.response = requests.put(
            f'https://api.restful-api.dev/objects/{object_id}',
            json=payload_new
        )
        self.response_json = self.response.json()

    def check_response_name(self, name):
        assert self.response_json['name'] == name
