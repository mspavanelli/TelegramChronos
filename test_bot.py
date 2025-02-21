import pytest
from unittest import mock
import bot

@mock.patch('requests.post')
def test_group_name_format(mock_post):
    mock_post.return_value.status_code = 200
    bot.main()
    today = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
    meses = {
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
        5: "maio", 6: "junho", 7: "julho", 8: "agosto",
        9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }
    start_of_year = datetime.datetime(today.year, 1, 1, tzinfo=pytz.timezone('America/Sao_Paulo'))
    days_passed = (today - start_of_year).days + 1
    total_days_in_year = 366 if today.year % 4 == 0 and (today.year % 100 != 0 or today.year % 400 == 0) else 365
    percentage_of_year_passed = round((days_passed / total_days_in_year) * 100)
    formatted_name = f"{today.day} de {meses[today.month]} de {today.year} - {percentage_of_year_passed}% do ano"
    assert mock_post.call_args[1]['data']['title'] == formatted_name

@mock.patch('requests.post')
def test_api_call(mock_post):
    mock_post.return_value.status_code = 200
    bot.main()
    url = f"https://api.telegram.org/bot{bot.TOKEN}/setChatTitle"
    assert mock_post.call_args[0][0] == url
    assert mock_post.call_args[1]['data']['chat_id'] == bot.CHAT_ID
