from fastapi import FastAPI 
import startup
from users.index import users_router
from service_providers.index import service_providers_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 
print("############################ Server Started ######################")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(service_providers_router)

