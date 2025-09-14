import tkinter as tk
import random

class BinarySearchGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Binary Search Game")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f8ff")

        # Sorted list
        self.data = list(range(1, 101))
        self.target = random.choice(self.data)

        # Binary search pointers
        self.low = 0
        self.high = len(self.data) - 1
        self.moves = 0

        # GUI Elements
        self.title_label = tk.Label(root, text="🔎 Binary Search Game", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="#2c3e50")
        self.title_label.pack(pady=10)

        self.info_label = tk.Label(root, text="Guess the number (between 1 and 100)!", font=("Arial", 14), bg="#f0f8ff")
        self.info_label.pack(pady=10)

        # Canvas for visualization
        self.canvas = tk.Canvas(root, width=780, height=300, bg="#ecf0f1", highlightthickness=1, highlightbackground="black")
        self.canvas.pack(pady=10)
        self.draw_bars()

        self.range_label = tk.Label(root, text=f"Search Range: {self.data[self.low]} - {self.data[self.high]}", font=("Arial", 12), bg="#f0f8ff", fg="blue")
        self.range_label.pack(pady=5)

        self.step_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff", fg="purple")
        self.step_label.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f8ff")
        self.result_label.pack(pady=15)

        self.score_label = tk.Label(root, text=f"Moves: {self.moves}", font=("Arial", 12), bg="#f0f8ff", fg="green")
        self.score_label.pack(pady=5)

        self.left_button = tk.Button(root, text="⬅ Go Left", font=("Arial", 12), bg="#ff7675", fg="white", width=12, command=self.go_left)
        self.left_button.pack(side="left", padx=30, pady=20)

        self.check_button = tk.Button(root, text="✅ Check Middle", font=("Arial", 12), bg="#55efc4", fg="black", width=15, command=self.check_middle)
        self.check_button.pack(side="left", padx=10, pady=20)

        self.right_button = tk.Button(root, text="➡ Go Right", font=("Arial", 12), bg="#74b9ff", fg="white", width=12, command=self.go_right)
        self.right_button.pack(side="left", padx=30, pady=20)

        self.restart_button = tk.Button(root, text="🔄 Restart", font=("Arial", 12), bg="#ffeaa7", fg="black", command=self.restart)
        self.restart_button.pack(pady=20)

    def draw_bars(self):
        self.canvas.delete("all")
        bar_width = 780 // len(self.data)
        for i, value in enumerate(self.data):
            height = value * 2
            x0 = i * bar_width
            y0 = 300 - height
            x1 = (i + 1) * bar_width
            y1 = 300
            color = "#3498db" if self.low <= i <= self.high else "#bdc3c7"
            if value == self.target:
                color = "#e74c3c"  # Highlight target
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
            self.canvas.create_text((x0 + x1) / 2, y0 - 10, text=str(value), font=("Arial", 8))

    def update_range(self):
        self.moves += 1
        self.score_label.config(text=f"Moves: {self.moves}")
        self.range_label.config(text=f"Search Range: {self.data[self.low]} - {self.data[self.high]}")
        self.draw_bars()

    def check_middle(self):
        if self.low > self.high:
            self.result_label.config(text="❌ Game Over! Number not found.", fg="red")
            return

        mid = (self.low + self.high) // 2
        guess = self.data[mid]
        self.step_label.config(text=f"Checking middle: {guess}")
        self.root.update()

        if guess == self.target:
            self.result_label.config(text=f"🎉 Correct! The number is {self.target} in {self.moves} moves!", fg="green")
            self.draw_bars()  # Redraw to emphasize target
        elif guess < self.target:
            self.result_label.config(text=f"⬆ Middle {guess} is too small!", fg="orange")
            self.low = mid + 1
        else:
            self.result_label.config(text=f"⬇ Middle {guess} is too big!", fg="orange")
            self.high = mid - 1
        self.update_range()

    def go_left(self):
        mid = (self.low + self.high) // 2
        self.high = mid - 1
        self.update_range()
        self.step_label.config(text=f"Moving left from middle {self.data[mid]}")

    def go_right(self):
        mid = (self.low + self.high) // 2
        self.low = mid + 1
        self.update_range()
        self.step_label.config(text=f"Moving right from middle {self.data[mid]}")

    def restart(self):
        self.low = 0
        self.high = len(self.data) - 1
        self.target = random.choice(self.data)
        self.moves = 0
        self.result_label.config(text="")
        self.step_label.config(text="")
        self.score_label.config(text=f"Moves: {self.moves}")
        self.update_range()

# Run the game
root = tk.Tk()
game = BinarySearchGame(root)
root.mainloop()