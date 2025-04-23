# from fastapi import FastAPI, Request
# app = FastAPI()
# @app.post('/')
# async def test(request: Request):
#     print((await request.body()).decode())
#     return "hello world"
from fastapi import FastAPI
from pydantic import BaseModel
class Test(BaseModel):
    name: str
    age: int
app = FastAPI()
@app.post('/')

def test(t: Test):
    return t