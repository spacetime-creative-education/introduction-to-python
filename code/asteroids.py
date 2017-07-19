# Recreate the famous Asteroids Atari game in Pyglets

import pyglet

# CONSTS
SCR_HEIGHT = 400
SCR_WIDTH = 300

window = pyglet.window.Window(width=SCR_WIDTH, height=SCR_HEIGHT)

if __name__ == "__main__":
    pyglet.app.run()