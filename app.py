from fastapi import FastAPI, Depends

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this WINE app."}