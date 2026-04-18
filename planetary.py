from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from kivy.graphics import Rectangle, Color
from kivy.animation import Animation
import requests
import random

API_KEY = "b14wLhkDZppo37G5Y49EpdI4GAgSHoAMVxoLC6Eu"

planets = {
    "Mercury": {
        "desc": "The smallest and closest planet to the Sun.",
        "distance": "57.9 million km",
        "diameter": "4,879 km",
        "fact": "A year lasts 88 days.",
        "vibe": "☀️ Extreme",
        "img": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Mercury_in_true_color.jpg"
    },
    "Venus": {
        "desc": "A hot planet with thick toxic clouds.",
        "distance": "108.2 million km",
        "diameter": "12,104 km",
        "fact": "Spins backwards.",
        "vibe": "🔥 Hottest",
        "img": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Venus-real_color.jpg"
    },
    "Earth": {
        "desc": "Our home planet full of life.",
        "distance": "149.6 million km",
        "diameter": "12,742 km",
        "fact": "71% water.",
        "vibe": "🌍 Life",
        "img": "https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg"
    },
    "Mars": {
        "desc": "The Red Planet.",
        "distance": "227.9 million km",
        "diameter": "6,779 km",
        "fact": "Tallest volcano.",
        "vibe": "🔴 Future",
        "img": "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg"
    },
    "Jupiter": {
        "desc": "Largest planet with giant storms.",
        "distance": "778.5 million km",
        "diameter": "139,820 km",
        "fact": "Great Red Spot storm.",
        "vibe": "🌪️ Giant",
        "img": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Jupiter.jpg"
    },
    "Saturn": {
        "desc": "Famous for its rings.",
        "distance": "1.4 billion km",
        "diameter": "116,460 km",
        "fact": "Could float in water.",
        "vibe": "💍 Rings",
        "img": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Saturn_during_Equinox.jpg"
    },
    "Uranus": {
        "desc": "Rotates sideways.",
        "distance": "2.9 billion km",
        "diameter": "50,724 km",
        "fact": "Extreme seasons.",
        "vibe": "🧊 Sideways",
        "img": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg"
    },
    "Neptune": {
        "desc": "Strongest winds.",
        "distance": "4.5 billion km",
        "diameter": "49,244 km",
        "fact": "Fastest winds.",
        "vibe": "Stormy",
        "img": "https://upload.wikimedia.org/wikipedia/commons/5/56/Neptune_Full.jpg"
    }
}

class Gradient(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        with self.canvas.before:
            Color(0.07, 0.1, 0.2, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._u, pos=self._u)

    def _u(self, *a):
        self.rect.size = self.size
        self.rect.pos = self.pos

# === BASE SCREEN ===
class Base(Screen):
    def on_enter(self):
        self.opacity = 0
        Animation(opacity=1, duration=0.3).start(self)

def go(sm, target, direction="left"):
    sm.transition = SlideTransition(direction=direction, duration=0.25)
    sm.current = target

# === HOME ===
class Home(Base):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = Gradient(orientation='vertical', padding=20, spacing=12)

        layout.add_widget(Label(text="🌌 Astronaut Super App 🚀", font_size=22))

        for text, target in [
            ("🪐 Explore Planets", "planet"),
            ("🧠 Space Quiz", "quiz"),
            ("🌌 NASA Image", "nasa")
        ]:
            b = Button(text=text, size_hint=(1, None), height=50,
                       background_color=(0.4, 0.3, 1, 1))
            b.bind(on_press=lambda x, t=target: go(self.manager, t))
            layout.add_widget(b)

        self.add_widget(layout)

# === PLANET ===
class Planet(Base):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.layout = Gradient(orientation='vertical', padding=20, spacing=10)

        self.img = AsyncImage(size_hint=(1, 0.5))
        self.layout.add_widget(self.img)

        self.info = Label(text="Tap a planet", halign="center")
        self.layout.add_widget(self.info)

        for p in planets:
            b = Button(text=p)
            b.bind(on_press=lambda x, p=p: self.show(p))
            self.layout.add_widget(b)

        back = Button(text="⬅ Back")
        back.bind(on_press=lambda x: go(self.manager, "home", "right"))
        self.layout.add_widget(back)

        self.add_widget(self.layout)

    def show(self, name):
        data = planets[name]
        self.img.source = data["img"]

        self.info.text = (
            f"🪐 {name}\n\n"
            f"{data['desc']}\n\n"
            f"📏 {data['diameter']}\n"
            f"🌞 {data['distance']}\n\n"
            f"✨ {data['fact']}\n"
            f"{data['vibe']}"
        )

# === QUIZ ===
class Quiz(Base):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.layout = Gradient(orientation='vertical', padding=20, spacing=10)

        self.q = Label(text="")
        self.layout.add_widget(self.q)

        self.input = TextInput(hint_text="Your answer")
        self.layout.add_widget(self.input)

        btn = Button(text="Submit")
        btn.bind(on_press=self.check)
        self.layout.add_widget(btn)

        back = Button(text="⬅ Back")
        back.bind(on_press=lambda x: go(self.manager, "home", "right"))
        self.layout.add_widget(back)

        self.add_widget(self.layout)
        self.new_q()

    def new_q(self):
        self.cur = random.choice(list(planets.keys()))
        self.q.text = f"Which planet is this: {planets[self.cur]['fact']}"
        self.input.text = ""

    def check(self, *_):
        if self.input.text.capitalize() == self.cur:
            self.q.text = "✅ Correct!"
        else:
            self.q.text = f"❌ Wrong! {self.cur}"
        self.new_q()

# === NASA ===
class Nasa(Base):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.layout = Gradient(orientation='vertical', padding=20, spacing=10)

        self.title = Label(text="NASA Image")
        self.layout.add_widget(self.title)

        self.img = AsyncImage(size_hint=(1, 0.6))
        self.layout.add_widget(self.img)

        btn = Button(text="Load NASA Image")
        btn.bind(on_press=self.load)
        self.layout.add_widget(btn)

        back = Button(text="⬅ Back")
        back.bind(on_press=lambda x: go(self.manager, "home", "right"))
        self.layout.add_widget(back)

        self.add_widget(self.layout)

    def load(self, *_):
        try:
            data = requests.get(
                f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
            ).json()

            self.title.text = data["title"]
            self.img.source = data["url"]
        except:
            self.title.text = "Failed to load data"

# === APP ===
class SuperApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())

        sm.add_widget(Home(name="home"))
        sm.add_widget(Planet(name="planet"))
        sm.add_widget(Quiz(name="quiz"))
        sm.add_widget(Nasa(name="nasa"))

        return sm

SuperApp().run()
