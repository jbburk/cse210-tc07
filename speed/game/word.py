import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):
    """A nutritious substance that snake's like. The responsibility of Word is to keep track of its appearance and position. A Word can move around randomly if asked to do so. 
    
    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the word is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, set's the 
        text and moves the word to a random position within the boundary of the 
        screen.
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self.points = 50
        self.set_text("-Word: ")
        self.set_position(Point(0,constants.MAX_Y))
        
        #self.reset()
    
    def get_points(self):
        """Gets the points this word is worth.
        
        Args:
            self (Word): an instance of Word.

        Returns:
            integer: The points this word is worth.
        """
        return self._points

    def reset(self):
        """Resets the word by moving it to a random position within the boundaries of the screen and reassigning the points to a random number.
        
        Args:
            self (Word): an instance of Word.
        """
        # self._points = random.randint(1, 5)
        # x = random.randint(1, constants.MAX_X - 2)
        # y = random.randint(1, constants.MAX_Y - 2)
        position = Point(0, 20)
        # position = Point(x, y)
        self.set_position(position)
        
