import pytest
from unittest import mock
import helper

@mock.patch('requests.get')
def test_group_validation(mock_get):
    mock_response = {
        "ok": True,
        "result": {
            "id": 12345,
            "title": "Test Group",
            "type": "supergroup"
        }
    }
    mock_get.return_value.json.return_value = mock_response
    helper.TOKEN = "test_token"
    helper.main()
    assert mock_get.called
    assert mock_get.call_args[0][0] == f"https://api.telegram.org/bot{helper.TOKEN}/getChat?chat_id=12345"
