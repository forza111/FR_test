import requests
import pytest
from requests.auth import HTTPBasicAuth


API_URL = 'http://127.0.0.1:8000'
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'
import datetime
basicAuth = HTTPBasicAuth(ADMIN_PASSWORD, ADMIN_PASSWORD)


current_time = datetime.datetime.now()
past_time_1 = current_time - datetime.timedelta(days=2)
past_time_2 = current_time - datetime.timedelta(days=2)
future_time_1 = current_time + datetime.timedelta(days=2)
future_time_2 = current_time + datetime.timedelta(days=4)



database = {
    'normal_survey': {
        "title": "test_title",
        "description": "test_description",
        "beginning_date": str(past_time_1),
        "completion_date": str(future_time_1),
    },
    'past_survey': {
        "title": "test_title",
        "description": "test_description",
        "beginning_date": str(future_time_2),
        "completion_date": str(future_time_1),
    },
    'future_survey': {
        "title": "test_title",
        "description": "test_description",
        "beginning_date": str(future_time_1),
        "completion_date": str(future_time_2),
    },

}


@pytest.fixture
def create_normal_survey():
    res = requests.post(API_URL + '/api/admin/create_survey/', auth=basicAuth, json=database['normal_survey'])
    assert res.status_code == 201
    data = res.json()
    id = data['id']
    yield
    rs = requests.delete(API_URL + '/api/admin/change_survey/%d' % id, auth=basicAuth)
    assert res.status_code == 201


@pytest.fixture
def create_past_survey():
    res = requests.post(API_URL + '/api/admin/create_survey/', auth=basicAuth, json=database['past_survey'])
    assert res.status_code == 201
    data = res.json()
    id = data['id']
    yield
    re = requests.delete(API_URL + '/api/admin/change_survey/%d' % id, auth=basicAuth)
    assert res.status_code == 201


@pytest.fixture()
def create_future_survey():
    res = requests.post(API_URL + '/api/admin/create_survey/', auth=basicAuth, json=database['future_survey'])
    assert res.status_code == 201
    data = res.json()
    id = data['id']
    yield
    re = requests.delete(API_URL + '/api/admin/change_survey/%d' % id, auth=basicAuth)
    assert res.status_code == 201






@pytest.mark.usefixtures('create_normal_survey','create_past_survey', 'create_future_survey')
class TestDate():
    def test_1(self):
        print('lol')