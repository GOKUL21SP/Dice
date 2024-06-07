import tkinter as tk
from PIL import Image, ImageTk
import random
import os

class DiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")

        # Folder containing the dice images
        self.image_folder = "Dice"  

        # Load dice images
        self.Dice = [ImageTk.PhotoImage(Image.open(os.path.join(self.image_folder, f"dice{i}.png"))) for i in range(1, 7)]

        # Label to display the dice face
        self.dice_label = tk.Label(root)
        self.dice_label.pack(pady=20)

        # Roll button
        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice, font=('Helvetica', 14))
        self.roll_button.pack(pady=20)

    def roll_dice(self):
        # Random number between 1 and 6
        dice_value = random.randint(1, 6)
        # Update the label with the corresponding dice image
        self.dice_label.config(image=self.Dice[dice_value - 1])

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceApp(root)
    root.mainloop()
