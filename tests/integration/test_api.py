import re

import pytest
from pytest_httpserver import HTTPServer

from modules.functions import get_time_from_web


def test_positive_endpoint(httpserver: HTTPServer):
    response_data = {'$id': '1', 'currentDateTime': '2021-10-11T16:47Z', 'utcOffset': '00:00:00',
                     'isDayLightSavingsTime': False, 'dayOfTheWeek': 'Monday', 'timeZoneName': 'UTC',
                     'currentFileTime': 132784444228669933, 'ordinalDate': '2021-284', 'serviceResponse': None}

    httpserver.expect_request("/time").respond_with_json(response_data, 200)
    url = httpserver.url_for("/time")
    assert type(get_time_from_web(url, url)) == dict


def test_faulty_endpoints(httpserver: HTTPServer):
    # response data from http://worldclockapi.com/api/json/utc/now
    response_data = {'$id': '1', 'currentDateTime': '2021-10-11T16:47Z', 'utcOffset': '00:00:00',
                     'isDayLightSavingsTime': False, 'dayOfTheWeek': 'Monday', 'timeZoneName': 'UTC',
                     'currentFileTime': 132784444228669933, 'ordinalDate': '2021-284', 'serviceResponse': None}

    httpserver.expect_request("/time").respond_with_json(response_data, 200)
    url = httpserver.url_for("/time")
    port = re.search(r':\d+', url).group()
    invalid_port = int(port.replace(':', '')) - 1
    invalid_url = url.replace(port, ':' + str(invalid_port))

    assert type(get_time_from_web(invalid_url, url)) == dict
    assert type(get_time_from_web(url, url)) == dict

    with pytest.raises(Exception):
        get_time_from_web(invalid_url, invalid_url)
