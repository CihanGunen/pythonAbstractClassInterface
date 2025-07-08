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
       print("L gider")
       
    def show_count_in_board(self):
       print("4 tane at vardir ") 




class fil(ChessPieces):
    def show_move(self):
        print("Çapraz gider") 
    
    def show_count_in_board(self):
        print("4 tane fil vardir ")



class vezir(ChessPieces):
    
    def show_move(self):
        print("Çapraz ve düz sonsuz hareket eder")
        
    def show_count_in_board(self):
        print("2 tane vezir vardir ")
        



if __name__ == '__main__' :
      
      
    atimiz=at()
    filimiz=fil()
    vezirimiz=vezir()
    
    atimiz.show_move()
    filimiz.show_count_in_board()
    vezir.show_count_in_board()
       