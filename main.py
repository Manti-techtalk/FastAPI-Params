from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read():
    return {"messege": "continuing fastapi as a ackend service"}

@app.post('/')
async def create(data):
    return data

@app.put('/')
async def modify(data):
    return data

@app.delete('/')
async def remove(data):
    return data