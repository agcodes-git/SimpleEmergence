import vmath
import pygame

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.movement = [0,0]

    # I just used manhattan distance, but of course you can try anything.
    # Tweaking this distance metric drastically changes the behavior of the system.
    def custom_distance_to(self, p):
        return abs(self.x-p.x)+abs(self.y-p.y)

    # Movement is a function of the relative positions of all other particles.
    # Movement is calculated as the euclidean-normalized sum of the euclidean-normalized difference vectors, where
    # for each difference vector (p_to_us), the sign is determined by some function of the distance.
    def calculate_movement (self, all_particles):

        interim_movement = [0,0]

        for p in all_particles:
            if p == self: continue
            p_to_us = [self.x-p.x, self.y-p.y]
            n_p_to_us = vmath.normalize( p_to_us )

            # Tweaking this logic drastically changes the behavior of the system.
            if self.custom_distance_to(p) > 200:
                interim_movement[0] -= n_p_to_us[0]
                interim_movement[1] -= n_p_to_us[1]
            elif self.custom_distance_to(p) < 100:
                interim_movement[0] += n_p_to_us[0]
                interim_movement[1] += n_p_to_us[1]

        self.movement = vmath.normalize(interim_movement)

    def apply_movement ( self ):
        self.x += self.movement[0]
        self.y += self.movement[1]

    def draw( self, s ):
        pygame.draw.rect( s, (0,255,0), (self.x,self.y,1,1), 0 )