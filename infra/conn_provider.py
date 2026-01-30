from abc import ABC, abstractmethod


class ConnProvider(ABC):

    @abstractmethod
    def get_conn(self):
        pass