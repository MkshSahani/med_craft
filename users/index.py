from fastapi import APIRouter 


users_router = APIRouter(
    prefix="/users", 
    tags=["users"]
)


@users_router.get("/test_connection")
async def get_connection(): 
    return {
        "status_code": 200,
        "data": [],
        "message": "SuccessFull"
    }
