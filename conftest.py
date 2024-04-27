import pytest

from data_for_tests.payloads import payload_base
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject


@pytest.fixture
def obj_id():
    create_object = CreateObject()

    create_object.new_object(payload_base)
    yield create_object.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_by_id(create_object.response_json['id'])
