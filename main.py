from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import utils

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def generate_wave(
    request: Request,
    messageFrequency: float = Form(...),
    messageAmplitude: float = Form(...),
    messageWaveform: str = Form(...),
    carrierFrequency: float = Form(...),
    carrierAmplitude: float = Form(...),
    carrierWaveform: str = Form(...),
    modulationType: str = Form(...)
):
    img_path = utils.generate_modulation(
        messageFrequency,
        messageAmplitude,
        messageWaveform,
        carrierFrequency,
        carrierAmplitude,
        carrierWaveform,
        modulationType
    )
    return templates.TemplateResponse("index.html", {
        "request": request,
        "img_path": f"/static/plots/{img_path}"
    })
