from SearchAdaptorBase import SearchAdaptorBase
from StorageWriterBase import StorageWriterBase
import typing

class StorageAdaptorSpy(StorageWriterBase):
    stored = []

    def store(self, webmention_collection: list[dict[str,str]]):
        self.webmention_collection = webmention_collection
        self.stored = webmention_collection 

class SearchAdaptorStub(SearchAdaptorBase): 

    def gather(self) -> list[dict[str,str]] :
        return self.data