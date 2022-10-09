from fastapi import APIRouter 
import service_providers.services as service_providers_services
from service_providers.validators import OrganizationValidator, OrganizationLoginValidator
from responses import responses

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
async def register_hospital(): 
    pass


@service_providers_router.post('/organization_login')
async def organization_login(organization_login_details : OrganizationLoginValidator):
    try: 
        organization_login_data = organization_login_details.dict() 
        res = service_providers_services.organization_login(organization_login_data)
        return res
    except Exception as e: 
        return responses.send_error(msg = "Error Occured While Execution", data = e)