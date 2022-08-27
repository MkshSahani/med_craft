from pydantic import BaseModel 


class OrganizationValidator(BaseModel): 

    organization_name       : str
    organization_address    : str
    organization_country    : str 
    organization_state      : str 
    organization_city       : str
    organization_phone      : str 
    organization_email      : str
    organization_password   : str