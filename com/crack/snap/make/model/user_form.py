# @author Mohan Sharma
from fastapi import UploadFile
from pydantic import BaseModel


class UserForm(BaseModel):
	file: UploadFile
