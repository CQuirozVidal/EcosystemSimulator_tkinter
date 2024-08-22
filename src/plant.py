class Plant:
    def __init__(self, canvas, x, y, image):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.image = image
        self.id = canvas.create_image(self.x, self.y, image=self.image)
