from game import constants
from game.actor import Actor
from game.point import Point
import random

class Speed:
    """A limbless reptile. The responsibility of Snake is keep track of its segments. It contains methods for moving and growing among others.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The snake's body (a list of Actor instances)
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Snake): An instance of snake.
        """
        super().__init__()
        self._words = []
        self.master_word_list = constants.LIBRARY
        self.word_list = []
        for _ in range(0,5):
            self.word_list.append(self.master_word_list[random.randint(0,len(self.master_word_list))])
        

        for item in range(0,len(self.word_list)):
            self.create_new_word(self.word_list[item])
        
    def create_new_word(self,word):
        new_word = Actor()
        new_word.set_text(word)
        new_word.set_position(Point(random.randint(0,constants.MAX_X),random.randint(0,constants.MAX_Y-5)))
        new_word.set_velocity(Point(0,1))
        self._words.append(new_word)
        
        
        

    def move_words(self):
        for item in self._words:
            item.move_next()

    def check_word(self,word):
        points = len(word * 10)
        if word in self.word_list:
            index = self.word_list.index(word)
            self._words.pop(index)
            self.word_list.pop(index)
            
            new_word_text = self.master_word_list[random.randint(0,len(self.master_word_list))]
            self.word_list.append(new_word_text)
            self.create_new_word(new_word_text)
            
            return True, points
        else:
            
            return False, points

    def get_all(self):
        """Gets all the snake's segments.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            list: The snake's segments.
        """
        return self._words

    def get_body(self):
        """Gets the snake's body.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            list: The snake's body.
        """
        return self._segments[1:]

    

    def grow_tail(self):
        """Grows the snake's tail by one segment.
        
        Args:
            self (Snake): An instance of snake.
        """
        tail = self._segments[-1]
        offset = tail.get_velocity().reverse()
        text = "#"
        position = tail.get_position().add(offset)
        velocity = tail.get_velocity()
        self._add_segment(text, position, velocity)
    
    def move_head(self, direction):
        """Moves the snake in the given direction.

        Args:
            self (Snake): An instance of snake.
            direction (Point): The direction to move.
        """
        count = len(self._segments) - 1
        for n in range(count, -1, -1):
            segment = self._segments[n]
            if n > 0:
                leader = self._segments[n - 1]
                velocity = leader.get_velocity()
                segment.set_velocity(velocity)
            else:
                segment.set_velocity(direction)
            segment.move_next()

    def _add_segment(self, text, position, velocity):
        """Adds a new segment to the snake using the given text, position and velocity.

        Args:
            self (Snake): An instance of snake.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)

    def _prepare_body(self):
        """Prepares the snake body by adding segments.
        
        Args:
            self (Snake): an instance of Snake.
        """
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        for n in range(constants.SNAKE_LENGTH):
            text = "8" if n == 0 else "#"
            position = Point(x - n, y)
            velocity = Point(1, 0)
            self._add_segment(text, position, velocity)