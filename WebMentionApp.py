import typing
from SearchAdaptorBase import SearchAdaptorBase
from StorageWriterBase import StorageWriterBase

class WebMentionApp:

    def __init__ (self, searchAdaptor: SearchAdaptorBase, storageWriter: StorageWriterBase):
        self.searchAdaptor = searchAdaptor
        self.storageWriter = storageWriter

    def gather_and_store(self):

        search_data = self.searchAdaptor.gather()
        self.storageWriter.store(search_data)

