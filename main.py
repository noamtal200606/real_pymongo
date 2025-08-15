import uvicorn as uvicorn
from fastapi import FastAPI
from router import router

app = FastAPI()
app.include_router(router, prefix="/api")

# host should be 0.0.0.0, you know why we've been through this...
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, access_log=False)

