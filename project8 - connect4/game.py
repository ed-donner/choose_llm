from board import Board, RED, YELLOW, EMPTY, pieces
from player import Player
from dotenv import load_dotenv

class Game:

    def __init__(self, model_red, model_yellow):
        load_dotenv(override=True)
        self.board = Board()
        self.players = {RED: Player(model_red, RED), YELLOW: Player(model_yellow, YELLOW)}

    def move(self):
        self.players[self.board.player].move(self.board)

    def is_active(self):
        return self.board.is_active()

    def thoughts(self, player):
        return self.players[player].thoughts()

    def run(self):
        while self.is_active():
            self.move()
            print(self.board)