from Logic import *


gameLogic = Logic()

gameLogic.menu()
gameLogic.create_board_and_key()

for i in range(gameLogic.board.howManyColors):
    gameLogic.boss_action(gameLogic.board.actualColor)
    gameLogic.team_action(gameLogic.board.actualColor)
    gameLogic.switch_color()

gameLogic.winner()
gameLogic.menu()
gameLogic.end_state()
