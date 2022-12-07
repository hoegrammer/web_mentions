import abc

class StorageWriterBase:

    @abc.abstractmethod
    def store(self, webmention_collection: list[dict[str,str]], label: str):
        pass    
    