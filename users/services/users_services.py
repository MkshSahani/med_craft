# filename: users_services.py 
from os import access
from users.user_validators import UserValidator, UserLoginValidator
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
        logger.info(api_refrence="register_user", msg = "SQL Query", data = sql_query)
        sql_service.execute_query(api_refrence="register User", sql_query=sql_query, commit_operation=True)
        return responses.send_response(msg = "account created", data = {
            'access_token': access_token
        })
    except Exception as e: 
        logger.error(api_refrence="register_user", msg = "Error in User Registration", data = e)
        raise e


async def user_login(user_login_details: UserLoginValidator):
    try: 
        username = user_login_details['username']
        password = user_login_details['password']
        sql_query = "SELECT access_token FROM `med_craft_users` "
        sql_query += f"WHERE username = '{username}' AND password = '{password}'"
        user_details = await sql_service.execute_query(api_refrence='user_login', sql_query=sql_query)
        if len(user_details) == 0:
            return responses.send_response(
                msg = "Invalid Account Details",
                status_code = 404,
                data = {}
            )
        else:
            return responses.send_response(
                msg = "SuccessFull Login",
                status_code=200,
                data =  {
                    'access_token': user_details[0][0]
                }
            )
    except Exception as e: 
        logger.error(api_refrence="user login", msg = "Eroor While user login", data = e)
        return responses.send_error(
            msg = "SomeThing Went Wrong !!!",
            status_code= 400,
            data = {}
        )