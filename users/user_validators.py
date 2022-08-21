# filename : user_validators.py
from pydantic import BaseModel 
from typing import Optional

# * UserValidator -> Model for users 
class UserValidator(BaseModel): 

    username    : str
    firstname   : str 
    middle_name : Optional[str]
    lastname    : Optional[str]
    password    : str 
    email       : str 
    phone       : str 
    user_type   : int 


# * UserLoginValidator -> Model for user login 

class UserLoginValidator(BaseModel): 

    username    : str
    password    : str 

