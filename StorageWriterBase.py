import abc

from WebMention import WebMention


class StorageWriterBase:

    @abc.abstractmethod
    def store(self, webmention_collection: list[WebMention]):
        pass
