import requests


def test_delete(new_post_id):
    # print('test')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}')
    # assert response.status_code == 200