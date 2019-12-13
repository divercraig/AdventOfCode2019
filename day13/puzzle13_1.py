from day13.game import Game, Tile

game = Game(input_file='input.txt')
game.run()

blocks = 0
for tile in game.grid.values():
    if tile == Tile.BLOCK:
        blocks += 1

print("There are {} blocks on screen".format(blocks))
