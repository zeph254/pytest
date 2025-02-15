import pytest
import unittest.mock as mock
import requests
import source.service as service  # Ensure 'source' is the correct module path

@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    """
    Tests that get_user_from_db correctly returns a mocked value.
    """
    mock_get_user_from_db.return_value = "Mocked John"
    user_name = service.get_user_from_db(1)
    assert user_name == "Mocked John"

@mock.patch("requests.get")
def test_get_users(mock_get):
    """
    Tests that get_users correctly fetches data and returns JSON.
    """
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "name": "John"}]
    mock_get.return_value = mock_response

    users = service.get_users()
    assert users == [{"id": 1, "name": "John"}]
    mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users")
    mock_response.json.assert_called_once()

@mock.patch("requests.get")
def test_get_users_error(mock_get):
    """
    Tests that get_users raises HTTPError when the response status is not 200.
    """
    mock_response = mock.Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.HTTPError("404 Client Error")
    mock_get.return_value = mock_response

    with pytest.raises(requests.HTTPError, match="404 Client Error"):
        service.get_users()
