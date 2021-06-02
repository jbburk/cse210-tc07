from time import sleep
from game import constants
from game.word import Word
from game.score import Score
from game.speed import Speed

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        word (Word): The speed's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        speed (Speed): The player or speed.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.


        """

        self._word = Word()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._speed = Speed()


        self.current_entry = ""
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

        print("ok you won! Go away now")

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the speed.

        Args:
            self (Director): An instance of Director.
        """
        

        self.letter = self._input_service.get_letter()


    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        if self.letter == "*":
            #check the word and clear
            is_word_correct,points = self._speed.check_word(self.current_entry)
            if is_word_correct:
                self._score.add_points(points)
            else:
                self._score.subtract_points(points)
            
            self.current_entry = ""
            self._word.set_text("Word: ")

        else:
            self.current_entry += self.letter
            self._word.set_text(f"Word: {self.current_entry}")
        
        if self.letter == "-":
            if self.current_entry != "":
                self.current_entry = self.current_entry[0:-2]
                self._word.set_text(f"Word: {self.current_entry}")
        

        #self._handle_body_collision()
        #self._handle_food_collision()
        pass
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._word)
        self._output_service.draw_actors(self._speed.get_all(),type="words")
        self._output_service.draw_actor(self._score)

        self._speed.move_words()

        self._output_service.flush_buffer()

        if self._score.get_score() >= 1000:
            self._keep_playing = False



    def _handle_body_collision(self):
        """Handles collisions between the speed's head and body. Stops the game 
        if there is one.

        Args:
            self (Director): An instance of Director.
        """
        head = self._speed.get_head()
        body = self._speed.get_body()
        for segment in body:
            if head.get_position().equals(segment.get_position()):
                self._keep_playing = False
                break

    def _handle_food_collision(self):
        """Handles collisions between the speed's head and the word. Grows the 
        speed, updates the score and moves the word if there is one.

        Args:
            self (Director): An instance of Director.
        """
        head = self._speed.get_head()
        if head.get_position().equals(self._word.get_position()):
            points = self._word.get_points()
            for n in range(points):
                self._speed.grow_tail()
            self._score.add_points(points)
            self._word.reset() 