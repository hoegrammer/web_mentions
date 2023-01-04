from SearchAdaptorBase import SearchAdaptorBase
from StorageWriterBase import StorageWriterBase


class StorageAdaptorSpy(StorageWriterBase):
    stored = []

    def __init__(self):
        self.webmention_collection = None

    def store(self, webmention_collection: list[dict[str, str]]):
        self.webmention_collection = webmention_collection
        self.stored = webmention_collection


class SearchAdaptorStub(SearchAdaptorBase):
    data: list[dict[str, str]]

    def gather(self) -> list[dict[str, str]]:
        return self.data
