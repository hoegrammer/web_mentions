import abc

class SearchAdaptorBase:
    
    @abc.abstractmethod
    def gather(self) -> list[dict[str,str]]:
        return

