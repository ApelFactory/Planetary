planets = {
    "mercury": {
        "distance": "57.9 million km",
        "diameter": "4,879 km",
        "description": "The smallest planet and closest to the Sun.",
        "fact": "A year on Mercury is just 88 Earth days."
    },
    "venus": {
        "distance": "108.2 million km",
        "diameter": "12,104 km",
        "description": "A very hot planet with thick clouds.",
        "fact": "Venus spins backwards compared to most planets."
    },
    "earth": {
        "distance": "149.6 million km",
        "diameter": "12,742 km",
        "description": "Our home planet, full of life.",
        "fact": "Earth is the only known planet with liquid water on its surface."
    },
    "mars": {
        "distance": "227.9 million km",
        "diameter": "6,779 km",
        "description": "Known as the Red Planet.",
        "fact": "Mars has the tallest volcano in the solar system."
    },
    "jupiter": {
        "distance": "778.5 million km",
        "diameter": "139,820 km",
        "description": "The largest planet in the solar system.",
        "fact": "Jupiter has a giant storm called the Great Red Spot."
    },
    "saturn": {
        "distance": "1.4 billion km",
        "diameter": "116,460 km",
        "description": "Famous for its beautiful rings.",
        "fact": "Saturn could float in water because it is so light."
    },
    "uranus": {
        "distance": "2.9 billion km",
        "diameter": "50,724 km",
        "description": "An ice giant that rotates on its side.",
        "fact": "Uranus spins almost sideways compared to other planets."
    },
    "neptune": {
        "distance": "4.5 billion km",
        "diameter": "49,244 km",
        "description": "A cold and windy planet far from the Sun.",
        "fact": "Neptune has the strongest winds in the solar system."
    }
}

def show_menu():
    print("\n🌌 Solar System Explorer 🚀")
    print("Choose a planet:")
    for p in planets:
        print("-", p)

def show_planet(name):
    data = planets[name]
    print(f"\n🪐 {name.capitalize()}")
    print("Distance from Sun:", data["distance"])
    print("Diameter:", data["diameter"])
    print("Description:", data["description"])
    print("Fun Fact:", data["fact"])

while True:
    show_menu()
    choice = input("\nType planet name (or 'exit'): ").lower()

    if choice == "exit":
        print("👋 Goodbye astronaut!")
        break
    elif choice in planets:
        show_planet(choice)
    else:
        print("❌ Planet not found, try again.")
