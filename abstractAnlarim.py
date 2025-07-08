from abc import ABC, abstractmethod

class ChessPieces(ABC):
    @abstractmethod
    def show_move(self):
        pass
    @abstractmethod 
    def show_count_in_board(self):
        pass