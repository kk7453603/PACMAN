import pygame

from objects.lives import LivesObject
from objects.pacman import PacmanObject
from objects.ghost import GhostBase


class ConsequenceObject:
    def effect_after_collision(self, collide, lives, scared):
        if collide.ghost_collision_check() and not scared.get_scared_status():
            lives.reduce_lives()
            #Ghosts move in center
        elif collide.ghost_collision_check() and scared.get_scared_status():
            pass
