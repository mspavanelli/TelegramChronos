import pytest
from unittest import mock
import chat_info

@mock.patch('requests.get')
def test_group_info_retrieval(mock_get):
    mock_response = {
        "ok": True,
        "result": {
            "id": 12345,
            "title": "Test Group",
            "username": "testgroup",
            "type": "supergroup",
            "description": "This is a test group",
            "invite_link": "https://t.me/joinchat/testlink"
        }
    }
    mock_get.return_value.json.return_value = mock_response
    chat_info.TOKEN = "test_token"
    chat_info.CHAT_ID = "test_chat_id"
    chat_info.main()
    assert mock_get.called
    assert mock_get.call_args[0][0] == f"https://api.telegram.org/bot{chat_info.TOKEN}/getChat?chat_id={chat_info.CHAT_ID}"
