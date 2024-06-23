from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket('/remote')
async def remote(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        print(data)
