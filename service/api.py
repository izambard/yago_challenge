import logging
import time
import math

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


import params as params
import models.rc_pro as rc_pro
import clients.yago_client as yago_client
from utils import FileStore
from business import nace_code_cover_advise

LOGGER = logging.getLogger(__name__)

class YagoChallengeApp(FastAPI):
    PATH_RC_PRO = '/quotes/professional-liability/'
    PATH_LEADS = '/leads/'

    def __init__(self):
        super().__init__()

        self.add_middleware(
            CORSMiddleware,
            allow_origins=params.CORS_ORIGIN,
            allow_methods=['*'],
            allow_headers=['*'],
        )

app = YagoChallengeApp()
storage = FileStore()

@app.get('/')
def get_root():    
    return {'Hello': 'World'}

@app.post(YagoChallengeApp.PATH_RC_PRO, response_model=rc_pro.RCProRFQResponse)
def post_rc_pro_quote(lead_rfq: rc_pro.RCProLeadRFQ):
    lead = lead_rfq.lead
    rfq = lead_rfq.rfq

    advised_cover = nace_code_cover_advise(rfq.nacebelCodes)

    if not rfq.deductibleFormula:
        rfq.deductibleFormula=advised_cover.deductibleFormula

    if not rfq.coverageCeilingFormula:
        rfq.coverageCeilingFormula=advised_cover.coverageCeilingFormula
    
    try:
        quote= yago_client.post_rc_pro_quote(rfq)
        resp = rc_pro.RCProRFQResponse(advisedCover=advised_cover, quote=quote)

        if resp and rfq and lead:
            storage.save(quote.quoteId, {'lead':lead.json(exclude_none=True), 'rfq': rfq.json(exclude_none=True), 'resp': resp.json(exclude_none=True)})

        return resp
    except Exception as e:
        LOGGER.exception(e)
        raise e

@app.get(YagoChallengeApp.PATH_LEADS)
def get_leads():
    return storage.get_all()