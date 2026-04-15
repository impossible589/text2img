from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.websocket("/ws")   # 🔥 THIS IS REQUIRED
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        data = await ws.receive_text()
        print("Received:", data)
        await ws.send_text("Reply: " + data)
