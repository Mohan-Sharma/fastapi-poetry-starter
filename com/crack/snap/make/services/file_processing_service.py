# @author Mohan Sharma
import os
import shutil


class FileProcessingService:
	
	def __init__(self):
		pass
	
	def read_file(self, file_path):
		with open(file_path, 'r') as file:
			return file.read()
		
	def write_file(self, file, folder_to_write):
		file_location = f"{folder_to_write}/{file.filename}"
		os.makedirs(os.path.dirname(file_location), exist_ok=True)
		with open(file_location, "wb") as buffer:
			shutil.copyfileobj(file.file, buffer)
		return file_location
		
	
