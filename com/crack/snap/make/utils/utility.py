# @author Mohan Sharma
import os
import shutil
from pathlib import Path

from dependency_injector.wiring import inject
from rich.console import Console

from com.crack.snap.make.config import CommonSettings
from com.crack.snap.make.services.file_processing_service import \
	FileProcessingService


class Utility:
	
	@inject
	def __init__(self, settings: CommonSettings, file_processing_service: FileProcessingService):
		self.console = Console()
		self.settings = settings
		self.file_processing_service = file_processing_service

	def console_rich_print(self, message, style) -> None:
		return self.console.print(message, style=style)
	
	def generate_dummy_file(self, file):
		__green = "bold green"
		output_folder = f"{Path(__file__).resolve().parent.parent}/static/files"
		self.remove_all_files_quietly(output_folder)
		
		input_file = self.file_processing_service.write_file(file, output_folder)
		filename_with_extension = os.path.basename(input_file)
		filename, ext = os.path.splitext(filename_with_extension)
		output_file_name = f"{filename}-dummy{ext}"
		output_file_path = f"{output_folder}/{output_file_name}"
		return filename_with_extension
		
	@staticmethod
	def remove_all_files_quietly(directory: str):
		for root, dirs, files in os.walk(directory):
			for file in files:
				try:
					os.remove(os.path.join(root, file))
				except Exception:
					pass  # Quietly ignore errors
			
			for dir in dirs:
				dir_path = os.path.join(root, dir)
				try:
					shutil.rmtree(dir_path)
				except Exception:
					pass  # Quietly ignore errors
