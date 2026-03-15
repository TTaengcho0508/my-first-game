import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fancy Particle Playground ✨")

clock = pygame.time.Clock()

particles = []

class Particle:
    def __init__(self, x, y):

        self.x = x
        self.y = y

        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(2, 7)

        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        self.life = random.randint(50, 100)
        self.max_life = self.life

        self.size = random.randint(3, 6)

        self.color = (
            random.randint(180,255),
            random.randint(120,255),
            random.randint(200,255)
        )

    def update(self):
        self.x += self.vx
        self.y += self.vy

        self.vy += 0.05
        self.vx *= 0.99

        self.life -= 1

    def draw(self, surf):

        alpha = int(255 * (self.life / self.max_life))

        particle_surface = pygame.Surface((50,50), pygame.SRCALPHA)

        glow_size = self.size * 4
        pygame.draw.circle(
            particle_surface,
            (*self.color, alpha//3),
            (25,25),
            glow_size
        )

        pygame.draw.circle(
            particle_surface,
            (*self.color, alpha),
            (25,25),
            self.size
        )

        surf.blit(particle_surface, (self.x-25, self.y-25))

    def alive(self):
        return self.life > 0


def draw_background(surface, t):

    for y in range(HEIGHT):
        r = int(20 + 20 * math.sin(y*0.01 + t))
        g = int(40 + 40 * math.sin(y*0.008 + t*0.8))
        b = int(70 + 50 * math.sin(y*0.005 + t*0.6))

        pygame.draw.line(surface, (r,g,b), (0,y), (WIDTH,y))


running = True
time = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()

    if buttons[0]:
        for _ in range(10):
            particles.append(Particle(mouse[0], mouse[1]))

    time += 0.02

    draw_background(screen, time)

    for p in particles:
        p.update()
        p.draw(screen)

    particles = [p for p in particles if p.alive()]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()