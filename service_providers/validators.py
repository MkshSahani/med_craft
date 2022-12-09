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

class HospitalModel(BaseModel):
    api_key                 : str
    hospital_name           : str 
    hospital_addr           : str 
    phone                   : str 
    organization_id         : int
    hospital_state          : str
    hospital_country        : str
    hospital_pincode        : str



class DoctorModel(BaseModel): 
    pass

class OrganizationLoginValidator(BaseModel): 
    
    organization_email      : str
    organization_password   : str