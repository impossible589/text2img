from fastapi import FastAPI, WebSocket,File ,UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
prompt = ""
infoforweb = {}

app = FastAPI()
app.mount("/static", StaticFiles(directory="."), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)



needtotalk = False
@app.get("/item")
async def get_item1():
    global prompt
    if(prompt==""):
       return {"task":"null"}
    else:
        return {

        "task": "shell", "prompt": str(prompt)

    }



@app.get("/front_handler")
async def get_item2(parcel: str):
    global infoforweb
    print("Yes")
    print("parcel__" + parcel)
    global prompt

    parcellist = parcel.split("-")
    print(parcellist)
    if parcellist[0] == "shell":
       prompt = parcellist[1]
       print(prompt)
       return {
           "info":"okay"

       }


    elif parcellist[0] == "statuscheck":
        print("statuscheck pinged"+str(infoforweb))
        treturn = infoforweb
        infoforweb = {}
        return treturn

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

@app.post("/items")
async def receive_item(data: dict):
    info = data.get("info")
    print("infooo"+info)
    global infoforweb
    if info == "diffus_completed":
        infoforweb = {"info" :"imageisready"}

    if info == "diffus_progress":
        progess = data.get("progress")
        infoforweb = {"info" :"diffus_progress","value":progess}
        print("updatedinfo4web"+str(infoforweb))


    return {"status": "no task"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global infoforweb
    # Save file in chunks (important for large files)
    with open(file.filename, "wb") as f:
        while chunk := await file.read(1024 * 1024):  # 1MB chunks
            f.write(chunk)
    infoforweb = "imageisready"
    return {"filename": file.filename, "status": "uploaded"}


@app.get("/")
async def serve_home():

    return FileResponse("index.html")
