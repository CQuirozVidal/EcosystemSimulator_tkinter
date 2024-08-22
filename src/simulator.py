import tkinter as tk
from PIL import Image, ImageTk
import random
import os
from src.creature import Creature
from src.plant import Plant

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CONTROL_FRAME_HEIGHT = 50
CREATURE_SIZE = 50
CREATURE_COUNT = 10
PLANT_COUNT = 20
BACKGROUND_COLOR = "#C2B280"  
LION_COUNT = 2 

class EcosystemSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de Ecosistema Interactivo")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT + CONTROL_FRAME_HEIGHT + 30}")

        self.canvas = tk.Canvas(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=BACKGROUND_COLOR)
        self.canvas.pack()

        self.control_frame = tk.Frame(self, height=CONTROL_FRAME_HEIGHT)
        self.control_frame.pack(fill=tk.X, side="bottom")

        self.lions_label = tk.Label(self.control_frame, text="Lions: 0")
        self.lions_label.pack(side="left", padx=20)

        self.deers_label = tk.Label(self.control_frame, text="Deers: 0")
        self.deers_label.pack(side="left", padx=20)

        self.plants_label = tk.Label(self.control_frame, text="Plants: 0")
        self.plants_label.pack(side="left", padx=20)

        self.start_button = tk.Button(self.control_frame, text="Iniciar Simulación", command=self.start_simulation)
        self.start_button.pack(side="left", padx=20)

        self.pause_button = tk.Button(self.control_frame, text="Pausar Simulación", command=self.pause_simulation)
        self.pause_button.pack(side="left", padx=20)

        self.stop_button = tk.Button(self.control_frame, text="Detener Simulación", command=self.stop_simulation)
        self.stop_button.pack(side="left", padx=20)

        base_dir = os.path.dirname(os.path.abspath(__file__))

        lion_image_path = os.path.join(base_dir, "../assets/images/lion.png")
        deer_image_path = os.path.join(base_dir, "../assets/images/deer.png")
        plant_image_path = os.path.join(base_dir, "../assets/images/plant.png")

        self.carnivore_img = ImageTk.PhotoImage(Image.open(lion_image_path).resize((CREATURE_SIZE, CREATURE_SIZE)))
        self.herbivore_img = ImageTk.PhotoImage(Image.open(deer_image_path).resize((CREATURE_SIZE, CREATURE_SIZE)))
        self.plant_img = ImageTk.PhotoImage(Image.open(plant_image_path).resize((int(CREATURE_SIZE // 1.5), int(CREATURE_SIZE // 1.5))))

        self.creatures = []
        self.plants = []
        self.sim_running = False
        self.paused = False

        self.create_creatures()
        self.create_plants()

    def create_creatures(self):
        lions_created = 0
        for _ in range(CREATURE_COUNT):
            x = random.randint(0, WINDOW_WIDTH - CREATURE_SIZE)
            y = random.randint(0, WINDOW_HEIGHT - CREATURE_SIZE)
            
            if lions_created < LION_COUNT:
                image = self.carnivore_img
                herbivore = False
                lions_created += 1
            else:
                image = self.herbivore_img
                herbivore = True
            
            self.creatures.append(Creature(self.canvas, x, y, image, herbivore))
        self.update_counts()

    def create_plants(self):
        for _ in range(PLANT_COUNT):
            x = random.randint(0, WINDOW_WIDTH - CREATURE_SIZE)
            y = random.randint(0, WINDOW_HEIGHT - CREATURE_SIZE)
            self.plants.append(Plant(self.canvas, x, y, self.plant_img))
        self.update_counts()

    def start_simulation(self):
        if not self.sim_running:
            self.sim_running = True
            self.paused = False
            self.update_simulation()

    def update_simulation(self):
        if self.sim_running and not self.paused:
            for creature in self.creatures:
                creature.move()
                if creature.is_herbivore():
                    creature.eat(self.plants)
                else:
                    creature.chase_prey(self.creatures)

            self.update_counts()
            self.after(100, self.update_simulation)

    def stop_simulation(self):
        self.sim_running = False
        self.creatures.clear()
        self.plants.clear()
        self.canvas.delete("all")
        self.create_creatures()
        self.create_plants()

    def pause_simulation(self):
        self.paused = not self.paused

    def update_counts(self):
        lion_count = sum(1 for creature in self.creatures if not creature.is_herbivore() and self.is_visible(creature))
        deer_count = sum(1 for creature in self.creatures if creature.is_herbivore() and self.is_visible(creature))
        plant_count = sum(1 for plant in self.plants if self.is_visible(plant))

        self.lions_label.config(text=f"Leones: {lion_count}")
        self.deers_label.config(text=f"Ciervos: {deer_count}")
        self.plants_label.config(text=f"Plantas: {plant_count}")

    def is_visible(self, entity):
        return 0 <= entity.x <= WINDOW_WIDTH - CREATURE_SIZE and 0 <= entity.y <= WINDOW_HEIGHT - CREATURE_SIZE

