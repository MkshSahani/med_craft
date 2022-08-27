from .validators import OrganizationValidator
from sql_services.services import execute_query
import logger.logging as logger
import secrets
from responses import responses

async def register_organization(organization_data: OrganizationValidator): 
    try:
        if await validate_email(organization_data['organization_email']) == False: 
            return responses.send_error(msg = "Email Already Registered", data = {})
        access_token = secrets.token_hex(25)
        sql_query = "INSERT INTO organizations(org_name, org_address, org_country,"
        sql_query += "org_state, org_city, phone, email, passwd, access_token)"; 
        sql_query += f"VALUES('{organization_data['organization_name']}', '{organization_data['organization_address']}',"
        sql_query += f"'{organization_data['organization_country']}', '{organization_data['organization_state']}', '{organization_data['organization_city']}',"
        sql_query += f"'{organization_data['organization_phone']}', '{organization_data['organization_email']}',"
        sql_query += f"'{organization_data['organization_password']}', '{access_token}')"
        await execute_query(api_refrence="register organization", sql_query=sql_query, commit_operation=True)
        return responses.send_response(msg = "Organization Created SuccessFully", data = {
            'access_token': access_token
        })
    except Exception as e:
        logger.error(api_refrence="register organization", msg = "Error While Execution", data = e)
        raise e
        
async def validate_email(email: str): 
    try: 
        if email == '':
            logger.log(api_refrence="validate email", msg = "Blank Email Address", data = {})
            return False ## not valid. 
        sql_query = f"SELECT organization_id FROM organizations WHERE email = '{email}'"
        print(sql_query)
        sql_response = await execute_query(api_refrence="validate email", sql_query=sql_query)
        print(sql_response)
        if len(sql_response) == 0:
            return True 
        else:
            return False
    except Exception as e: 
        logger.error(api_refrence="validate email", msg = "Error While validating Email", data = e)
        raise e 