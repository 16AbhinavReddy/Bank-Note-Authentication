from pydantic import BaseModel

class Bank_Note(BaseModel) :
    variance : float
    skewness : float
    curtosis : float
    entropy : float