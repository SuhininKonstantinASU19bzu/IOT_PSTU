import uvicorn
from fastapi import FastAPI, File, UploadFile
from FaceIdentification import FaceIdentifier as myFI
from Functions import FaceCapture

app = FastAPI()

@app.get("/knownpeople/")
async def GetKnownPeople():
    myFI.LoadNewImages()

    return {"known_people": f"{myFI.KnownFaces()}"}

@app.post("/uploadphoto/")
async def UploadPhoto(name: str, photo: UploadFile = File(...)):
    contents = await photo.read()

    if myFI.AddPerson(name, contents):
        result = f"person {name} with photo {photo.filename} uploaded"
    else:
        result = "not one person"

    return {"upload_result": result}

@app.post("/checkphoto/")
async def CheckPhoto(photo: UploadFile = File(...)):
    contents = await photo.read()

    myFI.LoadNewImages()

    if myFI.KnownFaces():
        if myFI.DetectedKnownFaces(contents):
            result = myFI.DetectedKnownFaces(contents)
        else:
            result = "no known people in database"

    return {"check_result": f"{result}"}

@app.post("/checkcamera/")
async def CheckCamera():
    photo = FaceCapture()
    contents = await photo.read()

    myFI.LoadNewImages()

    if myFI.KnownFaces():
        if myFI.DetectedKnownFaces(contents):
            result = myFI.DetectedKnownFaces(contents)
        else:
            result = "no known people in database"

    return {"check_result": f"{result}"}

if __name__ == "__Application__":
    uvicorn.run(app, port=8000, host="0.0.0.0")