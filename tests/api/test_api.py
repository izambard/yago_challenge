from fastapi.testclient import TestClient
import json

from service.api import app, YagoChallengeApp
from models.rc_pro import RCProQuote
import tests.models.test_rc_pro as test_rc_pro

client = TestClient(app)
headers = {'Authorization': 'dummyToken'}
        
def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

def _validate_resp(response):
    assert response.status_code == 200
    assert response.apparent_encoding == 'ascii'
    assert response.headers.get('content-type') ==  'application/json'
    assert validateJSON(response.content)   

def test_get_root():
    response = client.get('/', headers=headers)
    _validate_resp(response)

def test_get_rc_pro_quote(mocker):
    mocker.patch('clients.yago_client.post_rc_pro_quote', return_value=RCProQuote(**test_rc_pro.RCPRO_RESPONSE_EXAMPLE))
    payload = {'lead': test_rc_pro.LEAD_EXAMPLE, 'rfq': test_rc_pro.RCPRO_RFQ_EXAMPLE}
    response = client.post(YagoChallengeApp.PATH_RC_PRO, json=payload, headers=headers)
    _validate_resp(response)


def test_get_rc_pro_quote_no_mock():
    payload = {'lead': test_rc_pro.LEAD_EXAMPLE, 'rfq': test_rc_pro.RCPRO_RFQ_EXAMPLE}
    response = client.post(YagoChallengeApp.PATH_RC_PRO, json=payload, headers=headers)
    _validate_resp(response)

def test_get_leads():
    response = client.get(YagoChallengeApp.PATH_LEADS, headers=headers)
    _validate_resp(response)    
