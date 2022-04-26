import pytest


@pytest.fixture
def base_url():
    return 'https://www.something.com'


@pytest.fixture
def valid_credentials():
    return {
        'username': 'xendit_user',
        'password': 'ThisIsTheP@ssw0rd'
    }


@pytest.fixture
def accepted_response_time():
    return 1


@pytest.fixture
def valid_req_body():
    return {
        "description": "send money to wallet",
        "callback_url": "https://walletnotif.com",
        "amount": 2000
    }


@pytest.fixture
def empty_response_body():
    return {}


@pytest.fixture
def less_than_1500_req_body():
    return {
        "description": "send money to wallet",
        "callback_url": "https://walletnotif.com",
        "amount": 1499
    }


@pytest.fixture
def more_than_5m_req_body():
    return {
        "description": "send money to wallet",
        "callback_url": "https://walletnotif.com",
        "amount": 5000001
    }


@pytest.fixture
def valid_qr_id():
    """
    for the sake of a mock, we just return some integer as qr_id. Realistically, this would be a setup that generates
    different qr_ids since the api doc defined it to be a one-off use.
    """
    return 1


@pytest.fixture
def non_existent_qr_id():
    return 34


@pytest.fixture
def already_used_qr_id():
    return 59
