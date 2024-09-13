import tkinter as tk
from tkinter import messagebox
from model import get_cosine_similarity

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TEXT_BOX_WIDTH = 90
TEXT_BOX_HEIGHT = 15
RESULT_FONT = ("Arial", 14)

def calculate_similarity_gui():    
    text1 = text_box1.get("1.0", tk.END).strip()
    text2 = text_box2.get("1.0", tk.END).strip()

    if not text1 or not text2:
        messagebox.showwarning("Input Error", "Please enter both texts.")
        return

    similarity = get_cosine_similarity(text1, text2)

    if similarity is not None:
        result_label.config(text=f"Cosine Similarity: {similarity:.4f}")
    else:
        messagebox.showerror("Error", "Failed to compute similarity. Please try again.")

def create_label(root, text):
    label = tk.Label(root, text=text)
    label.pack()
    return label

def create_text_box(root, width, height):
    frame = tk.Frame(root)
    frame.pack(pady=5)  
    scrollbar = tk.Scrollbar(frame)
    text_box = tk.Text(frame, width=width, height=height, wrap="word", yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_box.yview)
    scrollbar.pack(side="right", fill="y")
    text_box.pack(side="left")
    return text_box

def create_button(root, text, command):
    button = tk.Button(root, text=text, command=command)
    button.pack()
    return button

def initialize_gui():
    root = tk.Tk()
    root.title("Cosine Similarity Calculator")
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    create_label(root, "Enter Text 1:")
    global text_box1
    text_box1 = create_text_box(root, TEXT_BOX_WIDTH, TEXT_BOX_HEIGHT)

    create_label(root, "Enter Text 2:")
    global text_box2
    text_box2 = create_text_box(root, TEXT_BOX_WIDTH, TEXT_BOX_HEIGHT)

    create_button(root, "Calculate Similarity", calculate_similarity_gui)

    global result_label
    result_label = tk.Label(root, text="", font=RESULT_FONT)
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    initialize_gui()
