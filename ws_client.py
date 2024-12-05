# -*- coding: utf-8 -*-
# author: itimor

import websocket
import json

ws = websocket.WebSocket()

ws.connect("ws://localhost:8000/chat/")

msg = {
    "stream": "chatgroup",
    "payload": {
        "action": "create",
        "data": {
            "name": "aaa",
            "desc": "dadasd"
        }
    }
}

data = json.dumps(msg)

print(ws.send(data))
