import abc
import typing

class StorageWriterBase:

    @abc.abstractmethod
    def store(self, webmention_collection: list[dict[str,str]]):
        pass    
    