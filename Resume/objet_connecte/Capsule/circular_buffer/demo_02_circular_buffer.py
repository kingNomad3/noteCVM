import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
from random import randint, uniform
from math import tau, cos, sin

from circular_buffer import CircularBuffer

class BouncingBall:
    def __init__(self, x=0.0, y=0.0, vx=0.0, vy=0.0, radius=1.0, color=(0,0,0)):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color
        self.drag_line = CircularBuffer(capacity=10)

    def move(self, width, height):
        self.x += self.vx
        self.y += self.vy
        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.vx = -self.vx
        if self.y - self.radius <= 0 or self.y + self.radius  >= height:
            self.vy = -self.vy
            
        self.drag_line.push((self.x, self.y))
            
    def randomize(self, min_radius, max_radius, world_width, world_height, min_speed, max_speed):
        self.radius = uniform(min_radius, max_radius)
        self.x = uniform(self.radius, world_width - self.radius)
        self.y = uniform(self.radius, world_height - self.radius)
        speed = uniform(min_speed, max_speed)
        orientation = uniform(0.0, tau)
        self.vx = speed * cos(orientation)
        self.vy = speed * sin(orientation)
        self.color = tuple(randint(0, 255) for _ in range(3))
        
    def draw(self, surface):
        surface.ellipse([self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius], fill=self.color)
        
        for i in range(len(self.drag_line) - 1):
            start = self.drag_line[i]
            end = self.drag_line[i + 1]
            surface.line([start[0], start[1], end[0], end[1]], fill=self.color, width=3)
        
    @staticmethod
    def from_randomized(min_radius, max_radius, world_width, world_height, min_speed, max_speed):
        ball = BouncingBall()
        ball.randomize(min_radius, max_radius, world_width, world_height, min_speed, max_speed)
        return ball

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.width = 400
        self.height = 400
        self.label = tk.Label(self)
        self.label.pack()
        
        self.balls = [BouncingBall.from_randomized(5.0, 15.0, self.width, self.height, 10.0, 25.0) for _ in range(15)]
        
        self.update()

    def draw_frame(self):
        # Création d'une image de fond
        background = Image.new("RGB", (self.width, self.height), "white")
        draw = ImageDraw.Draw(background)
        
        # Dessiner chaque balle sur l'image de fond
        for ball in self.balls:
            ball.draw(draw)
        
        # Conversion de l'image Pillow en image Tkinter
        self.tk_image = ImageTk.PhotoImage(background)
        self.label.config(image=self.tk_image)

    def update(self):
        for ball in self.balls:
            ball.move(self.width, self.height)
        self.draw_frame()
        self.after(50, self.update)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
