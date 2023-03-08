from fastapi import FastAPI
import uvicorn
import pathlib

app = FastAPI()


@app.get("/")
async def index():
    return {"message":"good"}

def start():
    cwd = pathlib.Path(__file__).parent.resolve()
    uvicorn.run(app, host="127.0.0.1", port=5050)
    
if __name__ == "__main__":
    start()