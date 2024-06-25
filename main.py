from fastapi import FastAPI, WebSocket
import pyautogui

app = FastAPI()


@app.websocket('/remote')
async def remote(websocket: WebSocket):
    tv_width = 0
    tv_height = 0

    screen_size = pyautogui.size()
    mac_width = screen_size.width
    mac_height = screen_size.height

    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        print(data)

        if data['event'] == 'register_tv_size':
            tv_width = data['payload']['x']
            tv_height = data['payload']['y']
        elif data['event'] == 'mouseMove':
            if 'payload' in data:
                x = data['payload']['x']
                y = data['payload']['y']

                actual_x = (mac_width * x) / tv_width
                actual_y = (mac_height * y) / tv_height
                pyautogui.moveTo(actual_x, actual_y, _pause=False)
