# hidding internal details and showing only assestial features..
# we use this concepts with the help of absract class 
""" 
blue print of other class ,inke under implement nhi hota
example ABC module 

 """

from abc import ABC,abstractmethod

class animal(ABC): #abstract class
    @abstractmethod
    #blue prints of its child class
    def make_sound(): 
        pass
    def gave_color():    
        pass

class lion(animal):
    def make_sound(self): #implementation
        print("The sound of a lion is: roar\n")   
    def gave_color(self):
        print("These are the basic color of lion : black,brown,white\n")   
        
class cat(animal):
    def make_sound(self):
        print("The sound of a cat is: Meow\n")   
  

lion=lion() #object
lion.make_sound()    #function call
lion.gave_color()

cat=cat() #object
cat.make_sound()  #function call




