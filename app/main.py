from fastapi import FastAPI

from app.interface.api.main_router import main_router

app = FastAPI()
app.include_router(main_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


print("Hello World!")
