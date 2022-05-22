import uvicorn
from fastapi import FastAPI, File, UploadFile
from FaceIdentification import FaceIdentifier as myFI

app = FastAPI()

@app.get("/knownpeople/")
async def getKnownPeople():
    myFI.LoadNewImages();

    return {"known_people": f"{myFI.KnownFaces()}"}

@app.post("/uploadphoto/")
async def uploadPhoto(name: str, photo: UploadFile = File(...)):
    contents = await photo.read()

    try:
        if myFI.AddPerson(name, contents):
            result = f"person {name} with photo {photo.filename} uploaded"
        else:
            result = "not one person"
    except:
        result = "Error!"

    return {"upload_result": result}

@app.post("/checkphoto/")
async def checkPhoto (photo: UploadFile = File(...)):
    contents = await photo.read()

    myFI.LoadNewImages()

    if len (myFI.KnownFaces()) > 0:
        try:
            result = myFI.DetectedKnownFaces(contents)
        except:
            result = "no known people in database"

    return {"check_result": f"{result}"}

        
if __name__ == "__Application__":
    uvicorn.run(app, port=8000, host="0.0.0.0")