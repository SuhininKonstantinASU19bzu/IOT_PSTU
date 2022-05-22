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
async def uploadPhoto(name: str, photo: UploadFile=File(...)):
    contents=await photo.read()
    try:
        if myFI.add_person(name, contents):
            result = f"person {name} with photo {photo.filename} uploaded"
        else:
            result = "not one person"
    except:
        result = "Error!"
return {"upload_result": result}

        


if __name__ == "__Application__":
    uvicorn.run(app, port=8000, host="0.0.0.0")