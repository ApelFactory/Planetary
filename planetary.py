import requests
import random
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

API_KEY = "b14wLhkDZppo37G5Y49EpdI4GAgSHoAMVxoLC6Eu"

# DATA PLANET
planets = {
    "Mercury": "Closest planet to the Sun.",
    "Venus": "Hottest planet.",
    "Earth": "Our home planet.",
    "Mars": "Red planet.",
    "Jupiter": "Largest planet.",
    "Saturn": "Has rings.",
    "Uranus": "Rotates sideways.",
    "Neptune": "Strongest winds."
}

# === FUNCTIONS ===

def show_menu():
    clear()
    Label(root, text="Planetary App",
          bg=bg, fg="white", font=("Arial", 16, "bold")).pack(pady=20)

    Button(root, text="Explore Planets", command=explore_ui,
           bg=btn, fg="white").pack(pady=10)

    Button(root, text="Space Quiz", command=quiz_ui,
           bg=btn, fg="white").pack(pady=10)

    Button(root, text="NASA Image", command=nasa_ui,
           bg=btn, fg="white").pack(pady=10)


def explore_ui():
    clear()
    Label(root, text="Choose Planet",
          bg=bg, fg="white").pack(pady=10)

    for p in planets:
        Button(root, text=p,
               command=lambda x=p: show_planet(x),
               bg=btn, fg="white").pack(pady=5)

    back_btn()


def show_planet(name):
    clear()
    Label(root, text=f"{name}",
          bg=bg, fg="white", font=("Arial", 14)).pack(pady=10)

    Label(root, text=planets[name],
          bg=bg, fg="gray").pack(pady=10)

    back_btn()


def quiz_ui():
    clear()
    global score, question_list
    score = 0
    question_list = list(planets.items())
    random.shuffle(question_list)
    ask_question(0)


def ask_question(i):
    clear()
    if i >= 5:
        Label(root, text=f"Score: {score}/5",
              bg=bg, fg="white").pack(pady=20)
        back_btn()
        return

    name, fact = question_list[i]

    Label(root, text=f"Which planet: {fact}",
          bg=bg, fg="white", wraplength=300).pack(pady=20)

    entry = Entry(root)
    entry.pack(pady=10)

    def check():
        global score
        if entry.get().capitalize() == name:
            score += 1
        ask_question(i + 1)

    Button(root, text="Submit", command=check,
           bg=btn, fg="white").pack(pady=10)


def nasa_ui():
    clear()

    Label(root, text="NASA Image",
          bg=bg, fg="white").pack(pady=10)

    try:
        url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
        data = requests.get(url).json()

        Label(root, text=data["title"],
              bg=bg, fg="white", wraplength=300).pack(pady=5)

        img_data = requests.get(data["url"]).content
        img = Image.open(BytesIO(img_data))
        img = img.resize((300, 200))

        img_tk = ImageTk.PhotoImage(img)
        img_label = Label(root, image=img_tk, bg=bg)
        img_label.image = img_tk
        img_label.pack(pady=10)

    except:
        Label(root, text="Failed to load NASA data",
              bg=bg, fg="red").pack()

    back_btn()


def back_btn():
    Button(root, text="Back",
           command=show_menu,
           bg="#374151", fg="white").pack(pady=15)


def clear():
    for widget in root.winfo_children():
        widget.destroy()


# === UI SETUP ===
root = Tk()
root.title("Planetary App")
root.geometry("350x500")

bg = "#0f172a"
btn = "#6366f1"

root.configure(bg=bg)

show_menu()

root.mainloop()
