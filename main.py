from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["https://localhost:-5000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers=["*"],
)

@app.get("/", status_code=status.HTTP_200_OK)
async def task():
    
    return {
        "slack_username": "bolex",
        "backend": True,
        "age": 21,
        "bio": 'my name is bolu, i love taking challenges and trying to provide soluctions to problems'
    }