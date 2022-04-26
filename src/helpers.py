import requests
import json
from os.path import join, dirname
from jsonschema import validate


def sign_in(base_url, valid_credentials):
    sign_in_response = requests.post(f"{base_url}/sign-in/", json=valid_credentials)
    access_token = sign_in_response.json()["access_token"]

    return access_token


def assert_valid_schema(data, schema_file):
    """ Checks whether the given data matches the schema """

    schema = _load_json_schema(schema_file)
    return validate(data, schema)


def _load_json_schema(filename):
    """ Loads the given schema file """

    relative_path = join('schemas', filename)
    absolute_path = join(dirname(__file__), relative_path)

    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())
