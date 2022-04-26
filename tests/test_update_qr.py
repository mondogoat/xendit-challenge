import json
import requests
from src.helpers import assert_valid_schema, sign_in

# use the helper to get access token
session_token = sign_in()


def test_update_qr_successfully(base_url, valid_qr_id, valid_req_body, accepted_response_time):
    send_update_qr_req = requests.patch(f"{base_url}/qr_codes/{valid_qr_id}",
                                        headers=f"Bearer + {session_token}",
                                        json=valid_req_body)

    response = send_update_qr_req.json()

    assert send_update_qr_req.status_code == 200
    assert send_update_qr_req.elapsed.total_seconds() <= accepted_response_time
    assert response == valid_req_body


def test_update_qr_no_auth(base_url, valid_qr_id, valid_req_body):
    send_update_qr_req = requests.patch(f"{base_url}/qr_codes/{valid_qr_id}",
                                        json=valid_req_body)

    response = send_update_qr_req.json()

    assert send_update_qr_req.status_code == 401
    # add some assertion for authentication here. Not defined currently in api doc


def test_update_qr_invalid_credentials(base_url, valid_qr_id, valid_req_body):
    send_update_qr_req = requests.patch(f"{base_url}/qr_codes/{valid_qr_id}", headers={f"Bearer XYZ"},
                                        json=valid_req_body)

    response = send_update_qr_req.json()

    assert send_update_qr_req.status_code == 403


def test_update_qr_qrid_does_not_exist(base_url, non_existent_qr_id, valid_req_body):
    send_update_qr_req = requests.patch(f"{base_url}/qr_codes/{non_existent_qr_id}",
                                        headers=f"Bearer + {session_token}",
                                        json=valid_req_body)

    response = send_update_qr_req.json()

    assert send_update_qr_req.status_code == 404
    assert response["ErrorCodes"] == ["QR_CODE_NOT_FOUND_ERROR"]


def test_update_qr_already_used(base_url, already_used_qr_id, valid_req_body):
    send_update_qr_req = requests.patch(f"{base_url}/qr_codes/{already_used_qr_id}",
                                        headers=f"Bearer + {session_token}",
                                        json=valid_req_body)

    response = send_update_qr_req.json()

    assert send_update_qr_req.status_code == 422
    assert response["ErrorCodes"] == ["QR_CODE_IN_USE"]


def test_update_qr_amount_less_than_1500(base_url, valid_qr_id, less_than_1500_req_body):
    send_update_qr_req = requests.patch(f"{base_url}/qr_codes/{valid_qr_id}",
                                        headers=f"Bearer + {session_token}",
                                        json=less_than_1500_req_body)

    response = send_update_qr_req.json()

    assert send_update_qr_req.status_code == 422
    assert response["ErrorCodes"] == ["API_VALIDATION_ERROR"]


def test_update_qr_amount_more_than_5M(base_url, valid_qr_id, more_than_5m_req_body):
    send_update_qr_req = requests.patch(f"{base_url}/qr_codes/{valid_qr_id}",
                                        headers=f"Bearer + {session_token}",
                                        json=more_than_5m_req_body)

    response = send_update_qr_req.json()

    assert send_update_qr_req.status_code == 422
    assert response["ErrorCodes"] == ["API_VALIDATION_ERROR"]


def test_update_qr_validate_json_schema(base_url, valid_qr_id, valid_req_body):
    send_update_qr_req = requests.patch(f"{base_url}/qr_codes/{valid_qr_id}",
                                        headers=f"Bearer + {session_token}",
                                        json=valid_req_body)

    json_data = send_update_qr_req.json()
    assert_valid_schema(json_data, 'update_qr_schema.json')


def test_update_qr_validate_missing_fields(base_url, valid_qr_id, empty_req_body):
    """All fields required"""
    send_update_qr_req = requests.patch(f"{base_url}/qr_codes/{valid_qr_id}",
                                        headers=f"Bearer + {session_token}",
                                        json=empty_req_body)

    response = send_update_qr_req.json()
    assert_valid_schema(response, 'update_qr_schema.json')

    assert send_update_qr_req.status_code == 400
    assert response["ErrorCodes"] == ["API_VALIDATION_ERROR"]
