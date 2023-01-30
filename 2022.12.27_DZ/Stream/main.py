import board
import game

game.set_player_names()
# board.draw_board()
while True:
    if game.game_turn():
        break