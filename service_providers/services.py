from .validators import OrganizationValidator


async def register_organization(organization_data: OrganizationValidator): 
    sql_query = "INSERT INTO organizations(org_name, org_address, org_country \
                org_state, org_city, phone, email, passwd)"; 
    sql_query += f"VALUES( {organization_data['organization_name']}, {organization_data['organization_address']},"
    sql_query += f"{organization_data['organization_country']}, {organization_data['organization_state']}, "
    sql_query += f"{organization_data['organization_phone']}, {organization_data['organization_email']},"
    sql_query += f"{organization_data['organization_password']}"
    print(sql_query)
    return {'data': "Construction"}
