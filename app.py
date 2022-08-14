from fastapi import FastAPI 
import startup
from users.index import users_router

app = FastAPI() 
print("############################ Server Started ######################")

app.include_router(users_router)

