from board import Board
from dice import Dice
from player import Player
from collections import deque


class Game:

    def __init__(self, dimension, no_of_dices, no_of_snakes, no_of_ladders, no_of_players):
        self.board = Board(1, dimension, no_of_snakes, no_of_ladders)
        self.dice = Dice(no_of_dices)
        self.players = deque(self.generate_players(no_of_players))
        self.winner = None

    def start_game(self):
        self.board.initialize()
        while not self.winner:
            player = self.find_player_turn()
            steps_to_move = self.dice.roll()
            print('Player {0} at position {1} has rolled dice and got {2}'.format(player.id, player.cur_pos+1,
                                                                                  steps_to_move))
            new_position = self.move(player.cur_pos, steps_to_move)
            if self.is_winner(new_position):
                self.winner = player

            player.cur_pos = min(new_position, self.board.dim*self.board.dim + 1)
            print('Player {0} is now at position {1}'.format(player.id, player.cur_pos+1))
        print('Winner is Player {0}'.format(self.winner.id))

    def find_player_turn(self):
        playing_player = self.players.popleft()
        self.players.append(playing_player)
        return playing_player

    def move(self, cur_pos, steps):
        new_position = cur_pos + steps
        if new_position <= (self.board.dim * self.board.dim - 1):
            cell = self.board.get_cell(new_position)

            if cell.snake_ladder and cell.snake_ladder.start == new_position:
                new_position = cell.snake_ladder.end
        return new_position

    def is_winner(self, position):
        if position >= (self.board.dim * self.board.dim - 1):
            return True
        return False

    def generate_players(self, no_of_players):
        return [Player(i+1) for i in range(no_of_players)]
