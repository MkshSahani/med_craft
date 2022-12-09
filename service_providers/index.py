from fastapi import APIRouter 
import service_providers.services as service_providers_services
from service_providers.validators import OrganizationValidator, OrganizationLoginValidator, HospitalModel
from responses import responses
from .services import validate_access_token
import logger

service_providers_router = APIRouter(
    prefix="/providers",
    tags=["providers"]
)



@service_providers_router.post('/organization_register')
async def register_organization(organization_data: OrganizationValidator):
    try:
        organization_data = organization_data.dict()
        res = await  service_providers_services.register_organization(organization_data=organization_data)
        return res
    except Exception as e: 
        return responses.send_error(msg = "Error Occured While Execution", data = e)

@service_providers_router.post('/register_doctor')
async def register_doctors(): 
    pass


@service_providers_router.post('/register_hospital')
async def register_hospital(hospital_details : HospitalModel): 
    try: 
        print("--------------------");
        print(hospital_details.dict())
        hospital_details = hospital_details.dict()
        user_details = await validate_access_token(hospital_details['api_key'])
        if len(user_details) == 0:
            return responses.send_response(msg = "Invalid Access Token", data = "Invalid Access Token")
        print("================ use Details =================")
        print(user_details)
        print("===============================================")
        hospital_details['organization_id'] = user_details[0][0]
        reigster_hospital_response = await service_providers_services.hospital_registration(hospital_details)
        return responses.send_response(msg = "Hospital Created SuccessFully", data = "Hospital Created SuccessFully")
    except Exception as e: 
        logger.error(msg = str(e))
        return responses.send_error(msg = "Error Occured While Execution", data = "Error Occured")


@service_providers_router.post('/organization_login')
async def organization_login(organization_login_details : OrganizationLoginValidator):
    try: 
        organization_login_data = organization_login_details.dict() 
        res = service_providers_services.organization_login(organization_login_data)
        return res
    except Exception as e: 
        return responses.send_error(msg = "Error Occured While Execution", data = e)