import random

class Creature:
    def __init__(self, canvas, x, y, image, herbivore):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.image = image
        self.herbivore = herbivore
        self.id = self.canvas.create_image(self.x, self.y, anchor="nw", image=self.image)
        self.energy = 100

    def move(self):
        if self.is_herbivore():
            dx = random.choice([-30, -20, 0, 20, 30])  
            dy = random.choice([-30, -20, 0, 20, 30])
        else:
            dx = random.choice([-15, -10, 0, 10, 15])  
            dy = random.choice([-15, -10, 0, 10, 15])

        self.x += dx
        self.y += dy

        if self.x < 0: self.x = 0
        if self.y < 0: self.y = 0
        if self.x > self.canvas.winfo_width() - 50: self.x = self.canvas.winfo_width() - 50
        if self.y > self.canvas.winfo_height() - 50: self.y = self.canvas.winfo_height() - 50

        self.canvas.move(self.id, dx, dy)
        self.energy -= 1

    def is_herbivore(self):
        return self.herbivore

    def eat(self, plants):
        for plant in plants:
            if abs(self.x - plant.x) < 50 and abs(self.y - plant.y) < 50:
                self.energy += 20
                self.canvas.delete(plant.id)
                plants.remove(plant)

    def chase_prey(self, creatures):
        prey = None
        min_distance = float("inf")
        for creature in creatures:
            if creature.is_herbivore():
                distance = abs(self.x - creature.x) + abs(self.y - creature.y)
                if distance < min_distance:
                    min_distance = distance
                    prey = creature

        if prey:
            dx = -10 if self.x > prey.x else 10
            dy = -10 if self.y > prey.y else 10
            self.x += dx
            self.y += dy
            self.canvas.move(self.id, dx, dy)
            
            if abs(self.x - prey.x) < 10 and abs(self.y - prey.y) < 10:
                self.canvas.delete(prey.id)
                creatures.remove(prey)
                self.energy += 50  

