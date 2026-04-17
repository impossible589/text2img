
from fastapi import FastAPI, WebSocket,File ,UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
app = FastAPI()





needtotalk = False
@app.get("/item")
async def get_item1():
    prompt = "hello"
    return {

        "task": "shell", "value": str(prompt)

    }



@app.get("/main_handler")
async def get_item2(parcel: str):
    print("Yes")
    print("parcel__" + parcel)
    parcellist = parcel.split("-")
    if parcellist[0] == "shell":
       prompt = parcellist[1]
       print(prompt)
    elif parcellist[0] == "statuscheck":
        pass
    elif parcellist[0] == "givefilename":
        pass

    return {
        "task": "shell","value":str(prompt)

    }
@app.get("/colab_receiver")
async def get_item3(parcel: str, price: int):
    print("parcel__"+parcel)
    parcellist = parcel.split("-")
    if parcellist[0] == "taskisready":
        pass
    elif parcellist[0] == "fileready":
        pass

@app.post("/item")
async def receive_item(data: dict):
    print("Received:", data)

    if data.get("task"):
        return {"status": "matched", "received": data}

    return {"status": "no task"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Save file in chunks (important for large files)
    with open(file.filename, "wb") as f:
        while chunk := await file.read(1024 * 1024):  # 1MB chunks
            f.write(chunk)

    return {"filename": file.filename, "status": "uploaded"}


@app.get("/")
async def serve_home():

    return FileResponse("index.html")
