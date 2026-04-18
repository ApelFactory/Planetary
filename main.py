import tkinter as tk
from tkinter import ttk

planets = {
    "Mercury": {"distance": "57.9 million km","diameter": "4,879 km","fact": "Closest planet to the Sun."},
    "Venus": {"distance": "108.2 million km","diameter": "12,104 km","fact": "Hottest planet."},
    "Earth": {"distance": "149.6 million km","diameter": "12,742 km","fact": "Supports life."},
    "Mars": {"distance": "227.9 million km","diameter": "6,779 km","fact": "Red planet."}
}

def show_info():
    planet = selected_planet.get()
    if planet in planets:
        data = planets[planet]
        result_label.config(text=f"{planet}\n\nDistance: {data['distance']}\nDiameter: {data['diameter']}\nFact: {data['fact']}")

root = tk.Tk()
root.title("Sky Info App")
root.geometry("300x250")

selected_planet = tk.StringVar()

dropdown = ttk.Combobox(root, textvariable=selected_planet, values=list(planets.keys()))
dropdown.pack(pady=10)

btn = tk.Button(root, text="Show Info", command=show_info)
btn.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=250)
result_label.pack(pady=10)

root.mainloop()
