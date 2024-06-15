from concurrent.futures import ProcessPoolExecutor

import uvicorn
from fastapi import FastAPI

from api.v1.hand_strange.hand_strange import router as hand_strange_router

app = FastAPI()
app.state.executor = ProcessPoolExecutor()
app.include_router(hand_strange_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host = "0.0.0.0", port = 8000, reload=True)