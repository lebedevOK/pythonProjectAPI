import pytest
import requests

from data_for_tests.payloads import payload_base, payload_new
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject


def test_create_object():
    new_object_endpoint = CreateObject()

    new_object_endpoint.new_object(payload_base)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_name(payload_base['name'])


def test_get_object(obj_id):
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id)
    get_obj_endpoint.check_response_is_200()
    get_obj_endpoint.check_response_id(obj_id)


def test_update_object(obj_id):
    update_obj_endpoint = UpdateObject()

    update_obj_endpoint.update_by_id(obj_id, payload_new)
    update_obj_endpoint.check_response_is_200()
    update_obj_endpoint.check_response_name(payload_new['name'])


def test_delete_object(obj_id):
    delete_obj_endpoint = DeleteObject()
    delete_obj_endpoint.delete_by_id(obj_id)
    delete_obj_endpoint.check_response_is_200()
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id)
    get_obj_endpoint.check_response_is_404()
