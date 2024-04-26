import requests


class DeleteObject():
    response = None
    response_json = None

    def delete_by_id(self, object_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
        self.response_json = self.response.json()

    def check_response_is_200(self):
        assert self.response.status_code == 200

    def check_response_is_404(self):
        assert self.response.status_code == 404
