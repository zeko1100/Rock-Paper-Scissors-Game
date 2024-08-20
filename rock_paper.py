import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Rock-Paper-Scissors Game")

        # Labels for instructions
        self.instruction_label = tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=('Arial', 14))
        self.instruction_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Buttons for user to select their choice
        self.rock_button = tk.Button(window, text="Rock", width=10, command=lambda: self.play_game("Rock"))
        self.rock_button.grid(row=1, column=0, padx=10, pady=10)

        self.paper_button = tk.Button(window, text="Paper", width=10, command=lambda: self.play_game("Paper"))
        self.paper_button.grid(row=1, column=1, padx=10, pady=10)

        self.scissors_button = tk.Button(window, text="Scissors", width=10, command=lambda: self.play_game("Scissors"))
        self.scissors_button.grid(row=1, column=2, padx=10, pady=10)

        # Labels to display choices and results
        self.result_label = tk.Label(window, text="", font=('Arial', 14))
        self.result_label.grid(row=2, column=0, columnspan=3, pady=10)

        self.score_label = tk.Label(window, text="Scores: You 0 - 0 Computer", font=('Arial', 14))
        self.score_label.grid(row=3, column=0, columnspan=3, pady=10)

        # Buttons to play again or quit
        self.play_again_button = tk.Button(window, text="Play Again", width=15, command=self.reset_game, state=tk.DISABLED)
        self.play_again_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="e")

        self.quit_button = tk.Button(window, text="Quit", width=15, command=window.quit)
        self.quit_button.grid(row=4, column=2, padx=10, pady=10, sticky="w")

        # Initialize scores
        self.user_score = 0
        self.computer_score = 0

    def play_game(self, user_choice):
        # Computer makes a random choice
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        # Determine the winner
        if user_choice == computer_choice:
            result_text = f"Both chose {user_choice}. It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result_text = f"You chose {user_choice}. Computer chose {computer_choice}. You win!"
            self.user_score += 1
        else:
            result_text = f"You chose {user_choice}. Computer chose {computer_choice}. You lose!"
            self.computer_score += 1

        # Display result
        self.result_label.config(text=result_text)
        self.update_scores()

        # Disable choice buttons and enable play again button
        self.toggle_buttons(False)

    def update_scores(self):
        self.score_label.config(text=f"Scores: You {self.user_score} - {self.computer_score} Computer")

    def reset_game(self):
        # Reset result label and re-enable choice buttons
        self.result_label.config(text="")
        self.toggle_buttons(True)

    def toggle_buttons(self, state):
        # Enable or disable choice buttons
        if state:
            self.rock_button.config(state=tk.NORMAL)
            self.paper_button.config(state=tk.NORMAL)
            self.scissors_button.config(state=tk.NORMAL)
            self.play_again_button.config(state=tk.DISABLED)
        else:
            self.rock_button.config(state=tk.DISABLED)
            self.paper_button.config(state=tk.DISABLED)
            self.scissors_button.config(state=tk.DISABLED)
            self.play_again_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
