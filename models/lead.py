from pydantic import BaseModel

class Lead(BaseModel): 
    email: str
    phone: str
    address: str
    firstname:str
    lastname:str