from pygame.image import load
from pygame.math import Vector2
import random as r
from pygame.mixer import Sound
from pygame import Color

def load_sprite(name, with_alpha=True):
    path = f"../assets/sprites/{name}.png" #creates path to an image
    loaded_sprite = load(path) # returns a surface object that represents an image

    if with_alpha:
        return loaded_sprite.convert_alpha() #with transparency value
    else:
        return loaded_sprite.convert()#without transparency but faster to load
    
def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)

def get_random_position(surface):
    return Vector2(
        r.randrange(surface.get_width()),
        r.randrange(surface.get_height()),
    )

def get_random_velocity(min_speed, max_speed):
    speed = r.randint(min_speed, max_speed)
    angle = r.randrange(0,360)
    return Vector2(speed, 0).rotate(angle)

def load_sound(name):
    path = f"../assets/Sounds/{name}.wav"
    print(path)
    return Sound(path)

def print_text(surface, text, font, color=Color("tomato")): #tomato already defined by pygame
    text_surface = font.render(text, True, color)#creates surface with text on antialiasing true

    rect = text_surface.get_rect()# gets the rectangle that represents the surface
    rect.center = Vector2(surface.get_size()) / 2

    surface.blit(text_surface, rect)#uses top left corner of rect to blit
