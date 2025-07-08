from abc import ABC, abstractmethod

class ChessPieces(ABC):
    @abstractmethod
    def show_move(self):
        pass
    @abstractmethod 
    def show_count_in_board(self):
        pass


class at(ChessPieces):
    
    def show_move(self):
        pass 
    
    def show_count_in_board(self):
        pass



class fil(ChessPieces):
    def show_move(self):
        pass 
    
    def show_count_in_board(self):
        pass



class vezir(ChessPieces):
    
    def show_move(self):
        pass 
    
    def show_count_in_board(self):
        pass