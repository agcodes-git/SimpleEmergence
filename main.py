import pygame, sys, copy
import key_input as IN
import random as r
import particle

# Configure pygame, so we can view our particles.
pygame.init()
width = height = 500
s = pygame.display.set_mode((width,height))
pclock = pygame.time.Clock()

# Generate a number of somewhat randomly distributed particles within a square.
r.seed(0)
spread = 50
num_particles = 100
particles = [ particle.Particle((r.random()-0.5)*spread + width/2,
            (r.random()-0.5)*spread + height/2) for i in range(num_particles)]

# Run until the window is closed.
while True:

    # Get input from the keyboard and parse it into something useful.
    IN.last_keys_down = copy.deepcopy( IN.keys_down )
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN: IN.keys_down[str(event.key)] = True
        elif event.type == pygame.KEYUP: IN.keys_down[str(event.key)] = False

    # Redraw the background rectangle so we don't see the old drawings adding up over time.
    pygame.draw.rect(s,(0,0,0),(0,0,width,height))

    # Calculate, move, and draw each particle.
    for p in particles: p.calculate_movement( particles )
    for p in particles: p.apply_movement()
    for p in particles: p.draw( s )

    # Update the display at ~60 Hz.
    pygame.display.flip()
    pclock.tick(60)












