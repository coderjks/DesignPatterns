from game import Game

if __name__ == "__main__":
    game = Game(dimension=20, no_of_dices=1, no_of_snakes=20, no_of_ladders=20, no_of_players=10)
    game.start_game()
    print('Game Finished')
