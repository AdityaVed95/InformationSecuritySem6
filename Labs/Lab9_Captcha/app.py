from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home(request: Request):
    images_names_list = ["my_image1.jpg","my_image2.jpg","my_image3.jpg","my_image4.jpg","my_image5.jpg","my_image6.jpg","my_image7.jpg","my_image8.jpg","my_image9.jpg"]
    return templates.TemplateResponse("home.html",{"request":request,"images_names_list":images_names_list})
