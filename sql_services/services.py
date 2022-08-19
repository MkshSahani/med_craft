from startup import sql_server 
import logger.logging as logger

## * execute sql Query 
async def execute_query(api_refrence : str = "", sql_query : str = "", commit_operation : bool = True): 
    try: 
        if sql_query == "":
            logger.log(api_refrence, "SQL Query Is Empty", sql_query)
            raise Exception("SQL Query Empty !!!")
        cursor = sql_server.cursor();
        cursor.execute(sql_query)
        if commit_operation:
            sql_server.commit()
        result = cursor.fetchall()
        logger.info(api_refrence=api_refrence, msg = "SQL Query Result", data = result)
        return result 
    except Exception as e: 
        logger.error(api_refrence, "Error While Executing SQL Query", e)
        return None # * no response given back