from abc import ABC, abstractmethod

class ChessPieces(ABC):
    
    @abstractmethod
    def show_move(self):
        pass
    @abstractmethod 
    def show_count_in_board(self):
        pass


class renk(ABC):
    
    @abstractmethod
    def acikrenk(self):
        pass
    
    @abstractmethod
    def kapalirenk(self):
        pass
    
    
class at(ChessPieces,renk):
    
    def show_move(self):
       print("L gider")
       
    def show_count_in_board(self):
       print("4 tane at vardir ") 

    
    def acikrenk(self):
        print("acik renk")
    
    
    def kapalirenk(self):
        print("kapali renk")

    
    
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
    
    '''
    atimiz.show_move()
    filimiz.show_count_in_board()
    vezir.show_count_in_board()
    '''
    
    atimiz.acikrenk()
       
       
       
       