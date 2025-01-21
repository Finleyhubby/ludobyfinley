import random

class LudoGame:
    def __init__(self):
        self.players = ['Player 1', 'Player 2']
        self.positions = {player: {'piece1': 0, 'piece2': 0} for player in self.players}
        self.board_size = 52
        self.winner = None

    def roll_dice(self):
        return random.randint(1, 6)

    def move_piece(self, player, piece, steps):
        current_position = self.positions[player][piece]
        new_position = (current_position + steps) % self.board_size
        self.positions[player][piece] = new_position
        print(f"{player} moved {piece} to position {new_position}")

    def check_win(self, player):
        if self.positions[player]['piece1'] == self.board_size - 1 and self.positions[player]['piece2'] == self.board_size - 1:
            self.winner = player
            return True
        return False

    def play_turn(self, player):
        print(f"\n{player}'s turn")
        input("Press Enter to roll the dice...")
        dice_roll = self.roll_dice()
        print(f"{player} rolled a {dice_roll}")

        piece = input("Choose piece to move (piece1 or piece2): ").strip().lower()
        if piece not in ['piece1', 'piece2']:
            print("Invalid piece. Please choose 'piece1' or 'piece2'.")
            return

        self.move_piece(player, piece, dice_roll)

        if self.check_win(player):
            print(f"{player} has won the game!")
            return True
        return False

    def start_game(self):
        print("Welcome to Simple Ludo Game!")
        while not self.winner:
            for player in self.players:
                if self.play_turn(player):
                    break
            if self.winner:
                break

if __name__ == "__main__":
    game = LudoGame()
    game.start_game()
