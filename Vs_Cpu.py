import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 960, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = 65

# RGB Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# Calculate the offset for centering the board
board_width = SQUARE_SIZE * COLS
board_height = SQUARE_SIZE * ROWS
x_offset = (WIDTH - board_width) // 2
y_offset = (HEIGHT - board_height) // 2

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

# Define the piece class
class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = x_offset + SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = y_offset + SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            font = pygame.font.SysFont(None, 35)
            text = font.render('K', True, WHITE)
            win.blit(text, (self.x - text.get_width() // 2, self.y - text.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

# Define the board class
class Board:
    def __init__(self):
        self.board = []
        self.create_board()
        self.blue_left = self.red_left = 12

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (x_offset + row * SQUARE_SIZE, y_offset + col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLUE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()

    def get_piece(self, row, col):
        return self.board[row][col]

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece.color == BLUE:
                self.blue_left -= 1
            else:
                self.red_left -= 1

# Define the game class
class Game:
    def __init__(self):
        self.board = Board()
        self.turn = BLUE
        self.selected_piece = None
        self.ai_delay = False
        self.ai_start_time = 0
        self.winner = None

    def update(self):
        self.board.draw(screen)
        if self.winner:
            self.draw_winner(screen, self.winner)
        pygame.display.update()

    def reset(self):
        self.__init__()

    def select(self, row, col):
        if self.selected_piece:
            result = self._move(row, col)
            if not result:
                self.selected_piece = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected_piece = piece
            return True

        return False

    def _move(self, row, col):
        piece = self.selected_piece
        if piece and (row, col) in self.get_valid_moves(piece):
            skipped = self.get_skipped_pieces(piece, row, col)
            self.board.move(piece, row, col)
            if skipped:
                self.board.remove(skipped)  # Remove captured pieces
            self.change_turn()
            self.selected_piece = None  # Reset selected piece after move
            self.check_winner()
            return True
        return False

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))

        if piece.color == BLUE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board.get_piece(r, left)
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last
                    break
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped + last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped + last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board.get_piece(r, right)
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last
                    break
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped + last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped + last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves

    def get_skipped_pieces(self, piece, row, col):
        skipped = []
        if abs(piece.row - row) == 2:
            skipped_row = (piece.row + row) // 2
            skipped_col = (piece.col + col) // 2
            skipped_piece = self.board.get_piece(skipped_row, skipped_col)
            if skipped_piece != 0:
                skipped.append(skipped_piece)
        return skipped

    def change_turn(self):
        self.turn = RED if self.turn == BLUE else BLUE
        if self.turn == RED:
            self.ai_delay = True
            self.ai_start_time = pygame.time.get_ticks()

    def ai_move(self):
        valid_moves = []
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board.get_piece(row, col)
                if piece != 0 and piece.color == RED:
                    moves = self.get_valid_moves(piece)
                    for move, skipped in moves.items():
                        valid_moves.append((piece, move, skipped))

        if valid_moves:
            piece, move, skipped = random.choice(valid_moves)
            self.board.move(piece, move[0], move[1])
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
            self.check_winner()

    def check_winner(self):
        if self.board.blue_left == 0:
            self.winner = "Red Wins!"
        elif self.board.red_left == 0:
            self.winner = "Blue Wins!"

    def draw_winner(self, win, winner):
        colour = 0
        if self.board.blue_left == 0:
            colour = RED
        elif self.board.red_left == 0:
            colour = BLUE
        font = pygame.font.SysFont(None, 100)
        text = font.render(winner, True, colour)
        win.blit(text, ((WIDTH - text.get_width()) // 2, (HEIGHT - text.get_height()) // 2))

# Main function
def main():
    game = Game()
    running = True

    while running:
        game.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game.winner:
                    pos = pygame.mouse.get_pos()
                    row, col = (pos[1] - y_offset) // SQUARE_SIZE, (pos[0] - x_offset) // SQUARE_SIZE
                    if 0 <= row < ROWS and 0 <= col < COLS:  # Ensure the click is within the board area
                        game.select(row, col)

        if game.ai_delay and not game.winner:
            current_time = pygame.time.get_ticks()
            if current_time - game.ai_start_time >= 1000:  # 2000 ms delay
                game.ai_move()
                game.ai_delay = False

    pygame.quit()

if __name__ == "__main__":
    main()
