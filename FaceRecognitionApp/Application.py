import uvicorn
from fastapi import FastAPI, File, UploadFile
#from FaceIdentification import 

app = FastAPI()
myFI = SimpleFaceRecognizer()

@app.get("/knownpeople/")
async def getKnownPeople():
myFI.load_new_images();
return {"knownPeople": f{"myFI.known_faces()}"}

@app.post("/uploadphoto/")
async def uploadPhoto(name: str, photo: UploadFile = File(...)):
    contents = await photo.read()
    try:
        if myFI.add_person(name, contents):
            result = f"person {name} with photo {photo.filename} uploaded"
        else:
            result = "not one person"
    except:
        result = "Error!"
return {"upload_result": result}

@app.post("/checkphoto/")
async def checkPhoto (photo: UploadFile = File(...)):
    contents = await photo.read()
    if len (myFI.known_faces()) > 0:
        try:
            result = myFI.detected_known_faces(contents)
        except:
            result = "no known people in database"
return {"check_result": f"{result}"}
        


if __name__ == "__Application__":
    uvicorn.run(app, port=8000, host="0.0.0.0")