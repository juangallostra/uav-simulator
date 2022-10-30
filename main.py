from ursina import *
from ursina.shaders import *
from controllers import DroneController
from logger import Logger

from player import DronePlayer

# create a window
app = Ursina()
# most things in ursina are Entities. An Entity is a thing you place in the world.
# you can think of them as GameObjects in Unity or Actors in Unreal.
# the first paramenter tells us the Entity's model will be a 3d-model called 'cube'.
# ursina includes some basic models like 'cube', 'sphere' and 'quad'.

EditorCamera()

Sky()
ground = Entity(model='plane', collider='box', scale=128, texture='grass', texture_scale=(4,4), name="ground")

# in ursina, positive x is right, positive y is up, and positive z is forward.
# Drone
player = DronePlayer(
    angular_speed=120,
    linear_speed=6,
    controller=DroneController,
    model='models/drone.obj',
    color=color.black,
    # model='models/pirate-ship-fat.obj', 
    # texture='models/pirate-ship-fat.mtl',
    scale_x=0.5,
    scale_y=0.5,
    scale_z=0.5,
    # position=(0,-0.1,0),
    position=(0,0.2,0),
    # collider='mesh'
    collider='box',
    shader=lit_with_shadows_shader
)


# camera.position = (15, 100, 15)
# camera.rotation = (90, 0, 0)

# test = Text(text='AAAAAAAA', x=-.85, y=.45)
logger = Logger(
    messages_to_display=20, 
    x_0=-.85,
    y_0=.45,
    dy=-.05
)

camera.position = (20, 70, -55)
camera.rotation = (45, 0, 0)

# def input(key):
#     if key == 'space':
#     elif key == 'r':

# def update():
#     for projectile in projectiles:
#         if projectile.intersects(player).hit:
#             projectile.color = color.lime
#             destroy(projectile)
#         else:
#             projectile.color = color.black

# this part will make the player move left or right based on our input.
# to check which keys are held down, we can check the held_keys dictionary.
# 0 means not pressed and 1 means pressed.
# time.dt is simply the time since the last frame. by multiplying with this, the
# player will move at the same speed regardless of how fast the game runs.


# def input(key):
#     if key == 'space':
#         player.y += 1
#         invoke(setattr, player, 'y', player.y-1, delay=.25)

# Shaders
pivot = Entity()
DirectionalLight(
    parent=pivot,
    x = 20,
    y = 70,
    z= -55,
    shadows=True,
    rotation=(45, 0, 0)
)

# start running the game
app.run()