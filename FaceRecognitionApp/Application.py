import uvicorn
from fastapi import FastAPI, File, UploadFile
#from FaceIdentification import 

app = FastAPI()


if __name__ == "__Application__":
    uvicorn.run(app, port=8000, host="0.0.0.0")