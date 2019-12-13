from day13.game import Game, Tile

game = Game(input_file='input.txt')
game.brain.memory[0] = 2
score = game.run(debug=True)

blocks = 0
for tile in game.grid.values():
    if tile == Tile.BLOCK:
        blocks += 1

print("There are {} blocks on screen".format(blocks))
print("The score is {}".format(score))


