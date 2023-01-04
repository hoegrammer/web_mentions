from StorageWriterBase import StorageWriterBase
import json
import os

from WebMention import WebMention


class FileWriterAdaptor(StorageWriterBase):

	def __init__(self):
		pass	

	def store(self, webmention_collection: list[WebMention]) -> None :
		os.makedirs("stored_search_results")
		with open ('stored_search_results/results.json', 'w') as f:
			json.dump(webmention_collection, f)
