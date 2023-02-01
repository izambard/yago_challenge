from typing import List
from models.rc_pro import AdvisedCover, CoverTypeEnum, DeductibleFormulaEnum, CoverageCeilingFormulaEnum


def nace_code_cover_advise(naceCodeList: List[str])-> AdvisedCover:
    # READ NACECODE FILE
    # READ MAPPING FILE
    # DO LOGIC
    return AdvisedCover(coverType=[CoverTypeEnum.legalExpenses], deductibleFormula=DeductibleFormulaEnum.small, coverageCeilingFormula=CoverageCeilingFormulaEnum.large)