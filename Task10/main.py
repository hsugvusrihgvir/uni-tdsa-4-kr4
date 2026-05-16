from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from schemas import CustomExceptionModel, ItemResponse, User
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError

# задание 10.1
app = FastAPI()

class CustomExceptionA(HTTPException):
    def __init__(self, detail: str, message: str, status_code: int):
        super().__init__(status_code=status_code, detail=detail)
        self.message = message

class CustomExceptionB(HTTPException):
    def __init__(self, detail: str, message: str, status_code: int):
        super().__init__(status_code=status_code, detail=detail)
        self.message = message


@app.exception_handler(CustomExceptionA)
async def custom_exception_a_handler(request: Request, exc: CustomExceptionA):
    error = jsonable_encoder(
        CustomExceptionModel(status_code=exc.status_code, er_message=exc.message, er_details=exc.detail))
    return JSONResponse(status_code=exc.status_code, content=error)


@app.exception_handler(CustomExceptionB)
async def custom_exception_b_handler(request: Request, exc: CustomExceptionB):
    error = jsonable_encoder(
        CustomExceptionModel(status_code=exc.status_code, er_message=exc.message, er_details=exc.detail))
    return JSONResponse(status_code=exc.status_code, content=error)

@app.get("/item/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    if item_id == 1:
        raise CustomExceptionA(detail="Item not found",
                               message="You're trying to get an item that doesn't exist. Try entering a different item_id.",
                               status_code=404)
    return ItemResponse(id=item_id)

@app.get("/items")
async def get_items(c: int):
    if c % 2 == 0:
        raise CustomExceptionB(detail="Invalid parameter", message="Parameter c must be odd.", status_code=422)
    return {"message": "Success"}



# ЗАДАНИЕ 10.2

@app.exception_handler(RequestValidationError)
async def value_error_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={
            "error": "Validation failed",
            "message": exc.errors()
        }
    )

@app.post("/register")
async def register_user(user: User):
    return user