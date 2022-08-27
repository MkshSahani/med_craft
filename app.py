from fastapi import FastAPI 
import startup
from users.index import users_router
from service_providers.index import service_providers_router

app = FastAPI() 
print("############################ Server Started ######################")

app.include_router(users_router)
app.include_router(service_providers_router)