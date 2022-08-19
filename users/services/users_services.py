# filename: users_services.py 
from os import access
from users.user_validators import UserValidator
import secrets
import sql_services.services as sql_service
import logger.logging as logger
import responses.responses as responses

async def register_user(user_deatils: UserValidator):
    try:
        sql_query = "INSERT INTO `med_craft_users`( ";
        sql_attributes_lst = []
        sql_values_str = "";
        sql_attributes_lst.append('username') 
        sql_values_str += f"'{user_deatils['username']}',"
        sql_attributes_lst.append('firstname')
        sql_values_str += f"'{user_deatils['firstname']}',"
        sql_attributes_lst.append('password')
        sql_values_str += f"'{user_deatils['password']}',"
        sql_attributes_lst.append('email')
        sql_values_str += f"'{user_deatils['email']}',"
        sql_attributes_lst.append('phone')
        sql_values_str += f"'{user_deatils['phone']}',"
        sql_attributes_lst.append('user_type')
        sql_values_str += f"{int(user_deatils['user_type'])},"

        if user_deatils['middle_name']: 
            sql_attributes_lst.append('middle_name')
            sql_values_str += f"'{user_deatils['middle_name']}',"
        if user_deatils['lastname']: 
            sql_attributes_lst.append('lastname')
            sql_values_str += f"'{user_deatils['lastname']}',"

        sql_attributes_lst.append("access_token")
        access_token = secrets.token_hex(35)
        sql_values_str += f"'{access_token}',"
        sql_attr_str = ",".join(sql_attributes_lst)
        # sql_values_str = sql_values_str.split(" ")
        # sql_values_str.pop()

        sql_query += sql_attr_str + ")" + " VALUES (" + sql_values_str[:-1] + " )"
        print(sql_query)
        print("***********************************")
        print(sql_values_str)
        print(sql_attr_str)
        print("*************************************")
        await sql_service.execute_query(api_refrence="register User", sql_query=sql_query, commit_operation=True)
        print("====================== sql ==========")
        return responses.send_response(msg = "account created", data = {
            'access_token': access_token
        })
    except Exception as e: 
        logger.error(api_refrence="register_user", msg = "Error in User Registration", data = e)
        raise e    