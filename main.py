from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def task():
    
    return {
        "slack_username": "bolex",
        "backend": True,
        "age": 21,
        "bio": 'my name is bolu, i love taking challenges and trying to provide soluctions to problems'
    }