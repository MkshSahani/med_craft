from fastapi import APIRouter 
import service_providers.services as service_providers_services
from service_providers.validators import OrganizationValidator

service_providers_router = APIRouter(
    prefix="/providers",
    tags=["providers"]
)



@service_providers_router.post('/organization_register')
async def register_organization(organization_data: OrganizationValidator):
    organization_data = organization_data.dict()
    res = await  service_providers_services.register_organization(organization_data=organization_data)
    return res


@service_providers_router.post('/register_doctor')
async def register_doctors(): 
    pass


@service_providers_router.post('/register_hospital')
async def register_hospital(): 
    pass
