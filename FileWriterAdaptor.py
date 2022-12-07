from StorageWriterBase import StorageWriterBase
import json
import os


class FileWriterAdaptor(StorageWriterBase):

	def __init__(self):
		pass	

	def store(self, webmention_collection: list[dict[str,str]], label: str) -> None :
		os.makedirs("stored_search_results")
		with open (label, 'w') as f:
			json.dump(webmention_collection, f)
