from Logic import *


gameLogic = Logic()

gameLogic.menu()
gameLogic.create_board_and_key()

for i in range(gameLogic.board.how_many_colors):
    gameLogic.boss_action(gameLogic.board.actual_color)
    gameLogic.team_action(gameLogic.board.actual_color)
    gameLogic.switch_color()

gameLogic.winner()
gameLogic.menu()
gameLogic.end_state()
