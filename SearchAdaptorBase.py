import abc

from WebMention import WebMention


class SearchAdaptorBase:

    @abc.abstractmethod
    def gather(self) -> list[WebMention]:
        pass
