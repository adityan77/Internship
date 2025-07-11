import tkinter as tk
from tkinter import messagebox
import math

# Game state
board = [" " for _ in range(9)]
buttons = []
player_score = 0
ai_score = 0
draws = 0

# Winner check
def check_winner(brd, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in win_combos:
        if all(brd[i] == player for i in combo):
            return True
    return False

def is_draw(brd):
    return " " not in brd

# Minimax algorithm
def minimax(brd, depth, is_max):
    if check_winner(brd, "O"):
        return 1
    if check_winner(brd, "X"):
        return -1
    if is_draw(brd):
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "O"
                score = minimax(brd, depth + 1, False)
                brd[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "X"
                score = minimax(brd, depth + 1, True)
                brd[i] = " "
                best = min(best, score)
        return best

# AI move
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    if move is not None:
        board[move] = "O"
        buttons[move]["text"] = "O"
        buttons[move]["fg"] = "red"
        buttons[move]["state"] = "disabled"
        check_game_over()

# On player move
def on_click(i):
    if board[i] == " ":
        board[i] = "X"
        buttons[i]["text"] = "X"
        buttons[i]["fg"] = "blue"
        buttons[i]["state"] = "disabled"
        if not check_game_over():
            window.after(400, ai_move)

# Game over check
def check_game_over():
    global player_score, ai_score, draws

    if check_winner(board, "X"):
        messagebox.showinfo("Game Over", "🎉 You Win!")
        player_score += 1
        update_score()
        disable_all_buttons()
        return True
    elif check_winner(board, "O"):
        messagebox.showinfo("Game Over", "💻 AI Wins!")
        ai_score += 1
        update_score()
        disable_all_buttons()
        return True
    elif is_draw(board):
        messagebox.showinfo("Game Over", "🤝 It's a Draw!")
        draws += 1
        update_score()
        disable_all_buttons()
        return True
    return False

def disable_all_buttons():
    for b in buttons:
        b["state"] = "disabled"

def restart():
    global board
    board = [" " for _ in range(9)]
    for i in range(9):
        buttons[i]["text"] = " "
        buttons[i]["state"] = "normal"
        buttons[i]["fg"] = "black"

def update_score():
    score_label.config(text=f"👤 You: {player_score}    💻 AI: {ai_score}    🤝 Draws: {draws}")

# UI Setup
window = tk.Tk()
window.title("Tic Tac Toe - Colorful with AI")
window.configure(bg="#f0f0f0")
window.resizable(False, False)

frame = tk.Frame(window)
frame.pack(pady=10)

for i in range(9):
    b = tk.Button(frame, text=" ", width=6, height=3, font=("Helvetica", 24, "bold"),
                  bg="#e0e0e0", command=lambda i=i: on_click(i))
    b.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(b)

# Scoreboard
score_label = tk.Label(window, text="👤 You: 0    💻 AI: 0    🤝 Draws: 0", font=("Arial", 14), bg="#f0f0f0")
score_label.pack()

# Restart Button
restart_btn = tk.Button(window, text="Restart", font=("Arial", 12), command=restart, bg="#d9ead3", width=10)
restart_btn.pack(pady=10)

# Start GUI loop
window.mainloop()