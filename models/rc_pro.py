from typing import List, Optional
from pydantic import BaseModel, validator

from enum import Enum

from models.lead import Lead

class CoverageCeilingFormulaEnum(str, Enum):
    small = 'small'
    large = 'large'

class DeductibleFormulaEnum(str, Enum):
    small = 'small'
    medium = 'medium'
    large = 'large'

class RCProRFQ(BaseModel): 
    annualRevenue: float
    enterpriseNumber: str # VAT number
    legalName: str
    naturalPerson: bool
    nacebelCodes: List[str] # 5 digits strings
    deductibleFormula: Optional[DeductibleFormulaEnum]  # enum small, medium, large, default medium
    coverageCeilingFormula: Optional[CoverageCeilingFormulaEnum] # enum small, large, default small

    @validator('annualRevenue')
    def annualRevenue_strictly_positive(cls, v):
        if v <= 0 :
            raise ValueError('must be higher than zero')
        return v

    @validator('nacebelCodes')
    def nacebelCodes_five_digits(cls, v):
        return v

    @validator('enterpriseNumber')
    def enterpriseNumber_vat_code(cls, v):
        return v
    
class RCProLeadRFQ(BaseModel):
    lead: Lead
    rfq: RCProRFQ

class RCProPremiums(BaseModel):
    afterDelivery: float # 
    publicLiability: float # 
    professionalIndemnity: float # 
    entrustedObjects: float # 
    legalExpenses: float # 

class RCProQuote(BaseModel):
    available: bool
    coverageCeiling: int
    deductible: int
    quoteId: str
    grossPremiums: RCProPremiums

class CoverTypeEnum(str, Enum):
    afterDelivery='afterDelivery'
    publicLiability='publicLiability'
    professionalIndemnity='professionalIndemnity'
    entrustedObjects='entrustedObjects'
    legalExpenses='legalExpenses'

COVERTYPE_DESCRIPTION_DICT = {
    CoverTypeEnum.afterDelivery: "Covers damage arising after delivery of or completion of work (ex: new machines recently installed at the client's office start a fire).",
    CoverTypeEnum.publicLiability: 'Cover compensation claims for injury or damage (ex: you spill a cup of coffee over a client’s computer equipment).',
    CoverTypeEnum.professionalIndemnity: 'Cover compensation claims for a mistake that you make during your work (ex: accidentally forwarded confidential client information to third parties).',
    CoverTypeEnum.entrustedObjects: "Objects that don't belong to you, and are entrusted to you. You are obviously liable for any damage to these goods. (ex: you break the super expensive computer that was provided to you as an IT consultant).",
    CoverTypeEnum.legalExpenses:"Also known as legal insurance, is an insurance which facilitates access to law and justice by providing legal advice and covering legal costs of a dispute. (ex: a client asks you for a financial compensation for a mistake you made in your work and you consider it's absolutely not you fault considering the context and you thus want to hire a lawyer to defend you).",
}

class AdvisedCover(BaseModel):
    coverType: List[CoverTypeEnum]
    deductibleFormula: Optional[DeductibleFormulaEnum]  # enum small, medium, large, default medium
    coverageCeilingFormula: Optional[CoverageCeilingFormulaEnum] # enum small, large, default small    

class RCProRFQResponse(BaseModel):
    advisedCover: AdvisedCover
    quote: RCProQuote
