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


id = {}


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
    'type_question': {
        "текстовый": {"title": "текстовый"},
        "выбор": {"title": "выбор"},
        "мультивыбор": {"title": "мультивыбор"}
    },
    "questions": {
        "question_1": {
            "number_question": 1,
            "question_text": "question_text_1",
            "type_question": "",
            "survey": ""
        },
        "question_2": {
            "number_question": 2,
            "question_text": "question_text_2",
            "type_question": "",
            "survey": ""
            },
        "question_3": {
            "number_question": 3,
            "question_text": "question_text_3",
            "type_question": "",
            "survey": ""
            },
    }

}



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


@pytest.fixture()
def create_type_question():
    res1 = requests.post(API_URL + '/api/admin/create_type_question/', auth=basicAuth,
                         json=database['type_question']['текстовый'])
    assert res1.status_code == 201
    res2 = requests.post(API_URL + '/api/admin/create_type_question/', auth=basicAuth,
                         json=database['type_question']['выбор'])
    assert res1.status_code == 201
    res3 = requests.post(API_URL + '/api/admin/create_type_question/', auth=basicAuth,
                         json=database['type_question']['мультивыбор'])
    assert res1.status_code == 201

    data1 = res1.json()
    id['type_question_text'] = data1['id']
    data2 = res2.json()
    id['type_question_choice'] = data2['id']
    data3 = res3.json()
    id['type_question_multiselection'] = data3['id']

    yield

    rs1 = requests.delete(API_URL + '/api/admin/change_type_question/%d' % id['type_question_text'], auth=basicAuth)
    assert rs1.status_code == 204
    rs2 = requests.delete(API_URL + '/api/admin/change_type_question/%d' % id['type_question_choice'], auth=basicAuth)
    assert rs2.status_code == 204
    rs3 = requests.delete(API_URL + '/api/admin/change_type_question/%d' % id['type_question_multiselection'], auth=basicAuth)
    assert rs3.status_code == 204



@pytest.fixture()
def create_normal_question():
    database['questions']['question_1']['type_question'] = id['type_question_text'],
    database['questions']['question_2']['type_question'] = id['type_question_choice'],
    database['questions']['question_2']['type_question'] = id['type_question_multiselection'],


    res1 = requests.post(API_URL + '/api/admin/create_question/',auth=basicAuth,json=database['questions']['question_1'])
    assert res1.status_code == 201
    res2 = requests.post(API_URL + '/api/admin/create_question/',auth=basicAuth,json=database['questions']['question_2'])
    assert res2.status_code == 201
    res3 = requests.post(API_URL + '/api/admin/create_question/',auth=basicAuth,json=database['questions']['question_3'])
    assert res3.status_code == 201


    data1 = res1.json()
    id['question_1'] = data1['id']
    data2 = res2.json()
    id['question_2'] = data2['id']
    data3 = res3.json()
    id['question_3'] = data3['id']


    yield


    rs1 = requests.delete(API_URL + '/api/admin/change_question/%d' % id['question_1'], auth=basicAuth)
    assert rs1.status_code == 204
    rs2 = requests.delete(API_URL + '/api/admin/change_question/%d' % id['question_2'], auth=basicAuth)
    assert rs2.status_code == 204
    rs3 = requests.delete(API_URL + '/api/admin/change_question/%d' % id['question_3'], auth=basicAuth)
    assert rs3.status_code == 204






@pytest.mark.usefixtures('create_normal_survey','create_past_survey_1_day_ago',
                         'create_past_survey_5_minutes_ago','create_past_survey_4_minutes_ago',
                         'create_future_survey', 'create_type_question', 'create_normal_question')
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

    def test_change_title_current_survey(self):
        current_survey = {"title": "test_title_change"}
        res = requests.patch(API_URL + '/api/admin/change_survey/%d' % id['normal_survey'],auth=basicAuth,
                             json=current_survey)
        assert res.status_code == 200
        new_current_survey = {**res.json(), **current_survey}
        assert res.json() == new_current_survey

    def test_change_title_with_description_current_survey(self):
        current_survey = {
            "title": "test_title_change_2",
            "description": "test_description_change_2"}
        res = requests.patch(API_URL + '/api/admin/change_survey/%d' % id['normal_survey'],auth=basicAuth,
                             json=current_survey)
        assert res.status_code == 200
        new_current_survey = {**res.json(), **current_survey}
        assert res.json() == new_current_survey

    def test_change_title_description_beginningdate_current_survey(self):
        current_survey = {
            "title": "test_title_change_2",
            "description": "test_description_change_2",
            "beginning_date": past_time_4_minutes}
        res = requests.patch(API_URL + '/api/admin/change_survey/%d' % id['normal_survey'],auth=basicAuth,
                             json=current_survey)
        assert res.status_code == 200
        #new_current_survey - словарь с измененными title, descriptions, но первоначальным beginning_date
        new_current_survey = {**res.json(), **current_survey, **{'beginning_date': database['normal_survey']['beginning_date']}}
        assert res.json() == new_current_survey

    def test_change_title_description_beginningdate_completiondate_current_survey(self):
        current_survey = {
            "title": "test_title_change_2",
            "description": "test_description_change_2",
            "beginning_date": past_time_4_minutes,
            "completion_date": future_time_2_day}
        res = requests.patch(API_URL + '/api/admin/change_survey/%d' % id['normal_survey'],auth=basicAuth,
                             json=current_survey)
        assert res.status_code == 200
        #new_current_survey - словарь с измененными title, descriptions, completion_date но первоначальным beginning_date
        new_current_survey = {
            **res.json(),
            **current_survey,
            **{'beginning_date': database['normal_survey']['beginning_date']}
        }
        assert res.json() == new_current_survey


    def test_get_type_question(self):
        res1 = requests.get(API_URL + "/api/admin/type_question/%d" % id["type_question_text"], auth=basicAuth)
        assert res1.status_code == 200
        assert res1.json()["title"] == database["type_question"]["текстовый"]["title"]

        res2 = requests.get(API_URL + "/api/admin/type_question/%d" % id["type_question_choice"], auth=basicAuth)
        assert res2.status_code == 200
        assert res2.json()["title"] == database["type_question"]["выбор"]["title"]

        res3 = requests.get(API_URL + "/api/admin/type_question/%d" % id["type_question_multiselection"], auth=basicAuth)
        assert res3.status_code == 200
        assert res3.json()["title"] == database["type_question"]["мультивыбор"]["title"]


    def test_change_type_question(self):
        type_question = {"title": "text_change"}
        res = requests.patch(
            API_URL + '/api/admin/change_type_question/%d' % id['type_question_text'],
            auth=basicAuth,
            json=type_question)
        assert res.status_code == 200
        assert res.json()["title"] == type_question["title"]

"""
    def test_get_question(self):
        res1 = requests.get(API_URL + "/api/admin/question/%d" % id["question_1"], auth=basicAuth)
        assert res1.status_code == 200
        print(res1.json())


       res2 = requests.get(API_URL + "/api/admin/type_question/%d" % id["type_question_choice"], auth=basicAuth)
        assert res2.status_code == 200
        assert res2.json()["title"] == database["type_question"]["выбор"]["title"]

        res3 = requests.get(API_URL + "/api/admin/type_question/%d" % id["type_question_multiselection"], auth=basicAuth)
        assert res3.status_code == 200
        assert res3.json()["title"] == database["type_question"]["мультивыбор"]["title"]"""


