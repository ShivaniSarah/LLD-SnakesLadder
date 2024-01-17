from collections import deque
from SnakesNLadder.Board import Board
from .Dice import Dice
from .Player import Player


class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.board = Board(10, 5, 4)
        self.dice = Dice(1)
        self.winner = None
        self.add_players()

    def add_players(self):
        self.players_list = list([Player("p1", 0), Player("p2", 0)])

    def start_game(self):
        while self.winner is None:
            # Check whose turn now
            player_turn = self.find_player_turn()
            # print("Player turn is:", player_turn.id, "Current position is:", player_turn.current_position)

            # Roll the dice
            dice_numbers = self.dice.roll_dice()

            # Get the new position
            player_new_position = player_turn.current_position + dice_numbers
            player_new_position = self.jump_check(player_new_position)
            player_turn.current_position = player_new_position

            print("Player turn is:", player_turn.id, "New position is:", player_new_position)

            # Check for winning condition
            if player_new_position >= len(self.board.cells) * len(self.board.cells) - 1:
                self.winner = player_turn

        print("WINNER IS:", self.winner.id)

    def find_player_turn(self):
        player_turn = self.players_list.pop(1)
        self.players_list.insert(0,player_turn)
        return player_turn

    def jump_check(self, player_new_position):
        if player_new_position > len(self.board.cells) * len(self.board.cells) - 1:
            return player_new_position

        cell = self.board.get_cell(player_new_position)
        if cell.jump is not None and cell.jump.start == player_new_position:
            jump_by = "ladder" if cell.jump.start < cell.jump.end else "snake"
            print("Jump done by:", jump_by)
            return cell.jump.end

        return player_new_position
