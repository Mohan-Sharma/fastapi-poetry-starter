# @author Mohan Sharma

import os
import zipfile
from pathlib import Path

from dependency_injector.wiring import inject
from fastapi import Depends, Request
from fastapi import UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates

from com.crack.snap.make.config import CommonSettings
from com.crack.snap.make.di import container
from com.crack.snap.make.utils.utility import Utility

router = APIRouter()
templates = Jinja2Templates(directory="com/crack/snap/make/templates")


@router.get("/", response_class=HTMLResponse)
@inject
async def index(request: Request, config: CommonSettings = Depends(lambda: container.settings())):
	return templates.TemplateResponse("index.html", {
		"request": request,  # this is required by Jinja2
		"debug_mode": "on" if config.debug else "off"
	})


@router.post("/generate", response_model=dict)
@inject
async def generate_response(file: UploadFile = File(...), utility: Utility = Depends(lambda: container.utility())):
	try:
		generated_file = utility.generate_dummy_file(file)
		return {"filename": generated_file}
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))

@router.get("/download/{filename}", response_class=FileResponse)
async def download_file(filename: str):
	try:
		output_folder = f"{Path(__file__).resolve().parent.parent}/static/files"
		file_path = f"{output_folder}/{filename}"
		filename_with_extension = os.path.basename(file_path)
		filename, ext = os.path.splitext(filename_with_extension)
		zip_filename = f"{filename}.zip"
		zip_path = f"{output_folder}/{zip_filename}"
		
		with zipfile.ZipFile(zip_path, 'w') as zipf:
			zipf.write(file_path, os.path.basename(file_path))
		
		return FileResponse(zip_path, filename=zip_filename)
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))
	
