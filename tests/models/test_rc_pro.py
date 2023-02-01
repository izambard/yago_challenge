from pydantic.error_wrappers import ValidationError
from models.rc_pro import RCProRFQ, RCProQuote, RCProRFQResponse, AdvisedCover


LEAD_EXAMPLE = {
    'email': 'jane.doe@dummy.com',
    'phone': '+00 123 89 65 23',
    'address': 'Main dead end 3, Bottleneck Gulch',
    'firstname': 'Jane',
    'lastname': 'Doe',
}

RCPRO_RFQ_EXAMPLE={
	'annualRevenue': 80000,
	'enterpriseNumber': '0649885171',
	'legalName': 'example SA',
	'naturalPerson': True,
	'nacebelCodes': ['62010', '62020', '62030', '62090', '63110']
}

RCPRO_RESPONSE_EXAMPLE={
  'available': True,
  'coverageCeiling': 100000,
  'deductible': 5000,
  'quoteId': 12604234942544,
  'grossPremiums': {
    'afterDelivery': 53.00, 
    'publicLiability': 150.00, 
    'professionalIndemnity': 270.00, 
    'entrustedObjects': 12.92, 
		'legalExpenses': 20.87, 
  }
}

RCPRO_ADVISED_COVER = {
   'coverType': ['professionalIndemnity','legalExpenses'],
   'deductibleFormula': 'small',
   'coverageCeilingFormula':'small',
}   

def test_valid_RCProRequestModel():
    rfq=RCProRFQ(**RCPRO_RFQ_EXAMPLE)
    assert rfq.annualRevenue==RCPRO_RFQ_EXAMPLE['annualRevenue']

def test_unvalid_annualRevenue_RCProRequestModel():
    RCPRO_RFQ_EXAMPLE['annualRevenue'] = 0
    try:
      rfq=RCProRFQ(**RCPRO_RFQ_EXAMPLE)
    except Exception as e:
       assert type(e) == ValidationError

def test_unvalid_annualRevenue_RCProRequestModel2():
    RCPRO_RFQ_EXAMPLE['annualRevenue'] = -2
    try:
      rfq=RCProRFQ(**RCPRO_RFQ_EXAMPLE)
    except Exception as e:
       assert type(e) == ValidationError     

def test_valid_RCProResponseModel():
    resp=RCProQuote(**RCPRO_RESPONSE_EXAMPLE)
    assert resp.coverageCeiling==RCPRO_RESPONSE_EXAMPLE['coverageCeiling']   

def test_valid_RCProRFQResponsel():
    adCover=AdvisedCover(**RCPRO_ADVISED_COVER)
    quote=RCProQuote(**RCPRO_RESPONSE_EXAMPLE)
    resp=RCProRFQResponse(advisedCover=adCover, quote=quote)
    assert resp.quote.deductible==RCPRO_RESPONSE_EXAMPLE['deductible']
      

