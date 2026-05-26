import csv
import hashlib
import os
import random
import subprocess
import sys
import colorama
colorama.init()

username = None
RESET = '\033[0m'
BOLD = '\033[1m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[97m'

script_dir = os.path.dirname(os.path.abspath(__file__))
users_file = os.path.join(script_dir, 'users.csv')
loggedin = False

if not os.path.exists(users_file):
    open(users_file, 'a').close()

print()
print(f'{CYAN}{BOLD}v1.0.0{RESET}')
print(f'{WHITE}Made by {CYAN}Morpheus5061{RESET}')
print(f'{WHITE}Get the most recent version on {CYAN}https://github.com/dorian123537/VoidOS{RESET}')
print()
print(f'{GREEN}────────────────────────────────────────────────────────────────────────────────{RESET}')
print()

def login():
    global username, loggedin

    username = input(f'{BOLD}{CYAN}Username{RESET}: ')
    password = input(f'{BOLD}{CYAN}Password{RESET}: ')

    login_success = False
    with open(users_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2 and row[0] == username and row[1] == hashlib.sha256(password.encode()).hexdigest():
                login_success = True
                break

    if login_success:
        loggedin = True
        print(f'{YELLOW}Welcome {username}!{RESET}')
        user_dir = os.path.join(script_dir, username)
        if not os.path.isdir(user_dir):
            os.makedirs(user_dir)
        os.chdir(user_dir)
    else:
        print(f'{RED}Invalid username or password{RESET}')
        signuprequest = input(f'{YELLOW}Do you want to sign up? (Y/n){RESET}: ')
        if signuprequest.lower() == 'y':
            new_username = input('New Username: ')
            new_password = input('New Password: ')
            new_password = hashlib.sha256(new_password.encode()).hexdigest()
            with open(users_file, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([new_username, new_password])
            print(f'{GREEN}User registered successfully!{RESET}')
            print(f'{YELLOW}Run the launcher again to sign in.{RESET}')
        else:
            print(f'{YELLOW}Goodbye!{RESET}')
        quit()

class Commands:
    def help():
        print('Available commands:')
        print('help - Show this message')
        print('who - Show your username')
        print('logout - Log out and restart start.bat')
        print('shutdown - Shut down and run shutdown.py')
        print('close - Alias for shutdown')
        print('newfile - Create a new file')
        print('rnamefile - Rename a file')
        print('delfile - Delete a file')
        print('readfile - Read a file')
        print('changefile - Change file content')
        print('newdir - Create a new directory')
        print('rnamedir - Rename a directory')
        print('deldir - Delete a directory')
        print('listdir - List files in a directory')
        print('odir - Open a directory')
        print('tictactoe - Play Tic Tac Toe against the bot')
        print('hash - Hash a string')
        print('unhash - Unhash a string')
        print('passwd - Change your password')
        print('web - Open a website')
        print('More commands coming soon!')

    def who():
        print(f'You are {username}')
    
    def shutdown():
        print(f'{YELLOW}Shutting down...{RESET}')
        subprocess.run([sys.executable, os.path.join(script_dir, 'shutdown.py')])
        quit()

    def close():
        return Commands.shutdown()

    def logout():
        print(f'{YELLOW}Logging out...{RESET}')
        subprocess.run([sys.executable, os.path.join(script_dir, 'logout.py')])
        sys.exit(100)
    
    def newfile():
        filename = input('Filename: ')
        with open(filename, 'w') as f:
            print(f'File {filename} created successfully!')
    
    def rnamefile():
        oldname = input('Old Filename: ')
        newname = input('New Filename: ')
        try:
            os.rename(oldname, newname)
            print(f'File renamed from {oldname} to {newname} successfully!')
        except FileNotFoundError:
            print(f'File {oldname} not found!')
    
    def delfile():
        filename = input('Filename: ')
        try:
            os.remove(filename)
            print(f'File {filename} deleted successfully!')
        except FileNotFoundError:
            print(f'File {filename} not found!')
    
    def readfile():
        filename = input('Filename: ')
        try:
            with open(filename, 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print(f'File {filename} not found!')
    
    def changefile():
        filename = input('Filename: ')
        try:
            with open(filename, 'w') as f:
                content = input('New Content: ')
                f.write(content)
                print(f'File {filename} updated successfully!')
        except FileNotFoundError:
            print(f'File {filename} not found!')

    def newdir():
        dirname = input('Directory Name: ')
        try:
            os.mkdir(dirname)
            print(f'Directory {dirname} created successfully!')
        except FileExistsError:
            print(f'Directory {dirname} already exists!')
    
    def rnamedir():
        oldname = input('Old Directory Name: ')
        newname = input('New Directory Name: ')
        try:
            os.rename(oldname, newname)
            print(f'Directory renamed from {oldname} to {newname} successfully!')
        except FileNotFoundError:
            print(f'Directory {oldname} not found!')
    
    def deldir():
        dirname = input('Directory Name: ')
        try:
            os.rmdir(dirname)
            print(f'Directory {dirname} deleted successfully!')
        except FileNotFoundError:
            print(f'Directory {dirname} not found!')
        except OSError:
            print(f'Directory {dirname} is not empty!')
    
    def listdir():
        dirname = input('Directory Name: ')
        try:
            files = os.listdir(dirname)
            print(f'Files in {dirname}:')
            for file in files:
                print(file)
        except FileNotFoundError:
            print(f'Directory {dirname} not found!')

    def odir():
        dirname = input('Directory Name: ')
        try:
            files = os.listdir(dirname)
            print(f'Files in {dirname}:')
            for file in files:
                print(file)
        except FileNotFoundError:
            print(f'Directory {dirname} not found!')
    
    def tictactoe():
        def print_board(board):
            print()
            print(f' {board[0]} | {board[1]} | {board[2]} ')
            print('---+---+---')
            print(f' {board[3]} | {board[4]} | {board[5]} ')
            print('---+---+---')
            print(f' {board[6]} | {board[7]} | {board[8]} ')
            print()

        def find_winner(board):
            wins = [
                (0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)
            ]
            for a, b, c in wins:
                if board[a] == board[b] == board[c] and board[a] != ' ':
                    return board[a]
            return None

        def board_full(board):
            return all(cell != ' ' for cell in board)

        def human_move(board):
            while True:
                move = input('Choose a position (1-9): ')
                if not move.isdigit():
                    print('Please enter a number between 1 and 9.')
                    continue
                idx = int(move) - 1
                if idx < 0 or idx > 8:
                    print('Please enter a number between 1 and 9.')
                elif board[idx] != ' ':
                    print('That square is already taken.')
                else:
                    return idx

        def available_moves(board):
            return [i for i, cell in enumerate(board) if cell == ' ']

        def bot_move(board, bot_mark, human_mark, difficulty):
            if difficulty == 'easy':
                return random.choice(available_moves(board))

            def try_win_or_block(marker):
                for idx in available_moves(board):
                    board[idx] = marker
                    if find_winner(board) == marker:
                        board[idx] = ' '
                        return idx
                    board[idx] = ' '
                return None

            if difficulty == 'medium':
                win_move = try_win_or_block(bot_mark)
                if win_move is not None:
                    return win_move
                block_move = try_win_or_block(human_mark)
                if block_move is not None:
                    return block_move
                return random.choice(available_moves(board))

            def minimax(board_state, current_marker):
                winner = find_winner(board_state)
                if winner == bot_mark:
                    return 1
                if winner == human_mark:
                    return -1
                if board_full(board_state):
                    return 0

                scores = []
                for idx in available_moves(board_state):
                    board_state[idx] = current_marker
                    score = minimax(board_state, human_mark if current_marker == bot_mark else bot_mark)
                    board_state[idx] = ' '
                    scores.append(score)

                return max(scores) if current_marker == bot_mark else min(scores)

            best_score = -999
            best_move = None
            for idx in available_moves(board):
                board[idx] = bot_mark
                score = minimax(board, human_mark)
                board[idx] = ' '
                if score > best_score:
                    best_score = score
                    best_move = idx
            return best_move

        print('Starting Tic Tac Toe')
        print('Pick a difficulty: easy, medium, hard')
        while True:
            difficulty = input('Difficulty: ').strip().lower()
            if difficulty in ('easy', 'medium', 'hard'):
                break
            print('Invalid difficulty. Choose easy, medium, or hard.')

        board = [' '] * 9
        human_mark = 'X'
        bot_mark = 'O'
        current_player = 'human'

        print('Board positions:')
        print(' 1 | 2 | 3 ')
        print('---+---+---')
        print(' 4 | 5 | 6 ')
        print('---+---+---')
        print(' 7 | 8 | 9 ')

        while True:
            if current_player == 'human':
                print_board(board)
                idx = human_move(board)
                board[idx] = human_mark
            else:
                idx = bot_move(board, bot_mark, human_mark, difficulty)
                board[idx] = bot_mark
                print(f'Bot chooses position {idx + 1}.')

            winner = find_winner(board)
            if winner:
                print_board(board)
                if winner == human_mark:
                    print('You win!')
                else:
                    print('Bot wins!')
                break

            if board_full(board):
                print_board(board)
                print('Draw!')
                break

            current_player = 'bot' if current_player == 'human' else 'human'
    
    def passwd():
        new_password = input('New Password: ')
        new_password_hash = hashlib.sha256(new_password.encode()).hexdigest()
        users = []
        with open(users_file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == username:
                    users.append([username, new_password_hash])
                else:
                    users.append(row)
        with open(users_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(users)
        print('Password changed successfully!')
    
    def hash():
        text = input('Text to hash: ')
        print(f'SHA-256 Hash: {hashlib.sha256(text.encode()).hexdigest()}')
    
    def unhash():
        print('Do it yourself on https://crackstation.net')
    
    def web():
        url = input('URL: ')
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        try:
            import webbrowser
            webbrowser.open(url)
            print(f'Opening {url} in your default browser...')
        except Exception as e:
            print(f'Failed to open {url}: {e}')

login()

if loggedin:
    while True:
        userinput = input(f'{CYAN}{username}〔V〕VoidOS > {RESET}')
        if userinput == 'help':
            Commands.help()
        elif userinput == 'who':
            Commands.who()
        elif userinput == 'close':
            Commands.close()
        elif userinput == 'newfile':
            Commands.newfile()
        elif userinput == 'rnamefile':
            Commands.rnamefile()
        elif userinput == 'delfile':
            Commands.delfile()
        elif userinput == 'readfile':
            Commands.readfile()
        elif userinput == 'newdir':
            Commands.newdir()
        elif userinput == 'rnamedir':
            Commands.rnamedir()
        elif userinput == 'deldir':
            Commands.deldir()
        elif userinput == 'listdir':
            Commands.listdir()
        elif userinput == 'changefile':
            Commands.changefile()
        elif userinput == 'odir':
            Commands.odir()
        elif userinput == 'tictactoe':
            Commands.tictactoe()
        elif userinput == 'passwd':
            Commands.passwd()
        elif userinput == 'hash':
            Commands.hash()
        elif userinput == 'unhash':
            Commands.unhash()
        elif userinput == 'web':
            Commands.web()
        elif userinput == 'shutdown':
            Commands.shutdown()
        elif userinput == 'close':
            Commands.close()
        else:
            print('Unknown command. Type "help" for a list of commands.')