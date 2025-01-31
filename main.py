from fastapi import FastAPI

app = FastAPI()

@app.get('/items/{id}')
async def read(id):
    arr = [{"messege": "continuing fastapi as a ackend service"},{"Item":id}]
    return arr


@app.post('/')
async def create(data):
    return data

@app.put('/')
async def modify(data):
    return data

@app.delete('/')
async def remove(data):
    return data