import requests
import pytest
from requests.auth import HTTPBasicAuth
import datetime

API_URL = 'http://127.0.0.1:8000'
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'
basicAuth = HTTPBasicAuth(ADMIN_PASSWORD, ADMIN_PASSWORD)


current_time = datetime.datetime.utcnow()

past_time_1_day = (current_time - datetime.timedelta(days=1)).isoformat() + 'Z'
past_time_4_minutes = (current_time - datetime.timedelta(minutes=4)).isoformat() + 'Z'
past_time_5_minutes = (current_time - datetime.timedelta(minutes=5)).isoformat() + 'Z'

future_time_1_day = (current_time + datetime.timedelta(days=1)).isoformat() + 'Z'
future_time_2_day = (current_time + datetime.timedelta(days=2)).isoformat() + 'Z'



database = {
    'normal_survey': {
        "title": "test_title",
        "description": "test_description",
        "beginning_date": current_time.isoformat() + 'Z',
        "completion_date": future_time_1_day,
    },
    'past_survey_1_day_ago': {
        "title": "test_title",
        "description": "test_description",
        "beginning_date": past_time_1_day,
        "completion_date": future_time_1_day,
    },
    'past_survey_5_minutes_ago': {
        "title": "test_title",
        "description": "test_description",
        "beginning_date": past_time_5_minutes,
        "completion_date": future_time_1_day,
    },
    'past_survey_4_minutes_ago': {
        "title": "test_title",
        "description": "test_description",
        "beginning_date": past_time_4_minutes,
        "completion_date": future_time_1_day,
    },
    'future_survey': {
        "title": "test_title",
        "description": "test_description",
        "beginning_date": future_time_1_day,
        "completion_date": future_time_2_day,
    },

}


id = {}

@pytest.fixture
def create_normal_survey():
    res = requests.post(API_URL + '/api/admin/create_survey/', auth=basicAuth, json=database['normal_survey'])
    assert res.status_code == 201
    data = res.json()
    id['normal_survey'] = data['id']
    yield
    rs = requests.delete(API_URL + '/api/admin/change_survey/%d' % id['normal_survey'], auth=basicAuth)
    assert rs.status_code == 204


@pytest.fixture
def create_past_survey_1_day_ago():
    res = requests.post(API_URL + '/api/admin/create_survey/', auth=basicAuth, json=database['past_survey_1_day_ago'])
    assert res.status_code == 500


@pytest.fixture
def create_past_survey_5_minutes_ago():
    res = requests.post(API_URL + '/api/admin/create_survey/', auth=basicAuth, json=database['past_survey_5_minutes_ago'])
    assert res.status_code == 500


@pytest.fixture
def create_past_survey_4_minutes_ago():
    res = requests.post(API_URL + '/api/admin/create_survey/', auth=basicAuth, json=database['past_survey_4_minutes_ago'])
    assert res.status_code == 201
    data = res.json()
    id['past_survey_4_minutes_ago'] = data['id']
    yield
    rs = requests.delete(API_URL + '/api/admin/change_survey/%d' % id['past_survey_4_minutes_ago'], auth=basicAuth)
    assert rs.status_code == 204


@pytest.fixture()
def create_future_survey():
    res = requests.post(API_URL + '/api/admin/create_survey/', auth=basicAuth, json=database['future_survey'])
    assert res.status_code == 201
    data = res.json()
    id['future_survey'] = data['id']
    yield
    rs = requests.delete(API_URL + '/api/admin/change_survey/%d' % id['future_survey'], auth=basicAuth)
    assert rs.status_code == 204






@pytest.mark.usefixtures('create_normal_survey','create_past_survey_1_day_ago',
                         'create_past_survey_5_minutes_ago','create_past_survey_4_minutes_ago',
                         'create_future_survey')
class TestDate():
    def test_get_current_survey(self):
        res = requests.get(API_URL + '/api/survey/%d' % id['normal_survey'])
        assert res.status_code == 200
        assert res.json()['title'] == database['normal_survey']['title']
        assert res.json()['description'] == database['normal_survey']['description']
        assert res.json()['beginning_date'] == database['normal_survey']['beginning_date']

    def test_get_future_survey(self):
        res = requests.get(API_URL + '/api/survey/%d' % id['future_survey'])
        assert res.status_code == 404

    '''def test_change_current_survey(self):
        current_survey = {
        "title": "test_title_change",
        "description": "test_description_change",
        "completion_date": future_time_1_day,
        }
        res = requests.patch(API_URL + '/api/admin/change_survey/%d' % id['normal_survey'],auth=basicAuth,
                             json=current_survey)
        assert res.status_code == 200
        assert res.json() == current_survey'''
