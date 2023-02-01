import logging
import requests as rq
import json
import models.rc_pro as rc_pro
import params as params

PATH_RC_PRO = '/quotes/professional-liability/'

LOGGER = logging.getLogger(__name__)

def post_rc_pro_quote(rc_pro_rfq: rc_pro.RCProRFQ)-> rc_pro.RCProQuote:
    headers={'X-Api-Key':params.YAGO_API_KEY, 'Content-Type':'application/json'}
    r= rq.post(params.YAGO_API_URL_ROOT+PATH_RC_PRO, data= rc_pro_rfq.json(exclude_none=True), headers=headers)
          
    if r.status_code != rq.codes.ok:
        raise Exception(f'Error calling Yago server. Code: {r.status_code} - content: {r.content} - data: {rc_pro_rfq.json(exclude_none=True)}, headers: {headers}')
    
    resp: dict = json.loads(r.text)

    if not resp.get("success"):
        message = resp.get('message')
        data = resp.get('data')
        raise Exception(f'Unsuccessfull call to Yago server. Message: {message} - data: {data}')
    
    data = resp.get('data')
    LOGGER.debug(f'RC PRO Response from Yago server - {data}')

    return rc_pro.RCProQuote(**data)

