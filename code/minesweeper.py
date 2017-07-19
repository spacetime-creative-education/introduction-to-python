## Make a minesweeper
import pyglet
from pyglet.sprite import
# CONSTANTS
SCN_HEIGHT = 500
SCN_WIDTH = 500
GRID_LENGTH = 10
# Window
window = pyglet.window.Window(width=SCN_WIDTH, height=SCN_HEIGHT)
label = pyglet.text.Label('MineSweeper ' + str(window._mouse_x),
                          font_name='Arial',
                          font_size=32,
                          x=window.width // 2,
                          y=window.height // 2,
                          anchor_x='center',
                          anchor_y='center')

@window.event
def on_draw():
    window.clear()
    # label.draw()
    pyglet.graphics.draw(3, pyglet.gl.GL_POINTS,
                         ('v2i', (10, 15, 30, 35, 10, 10))
                         )
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                 [0, 1, 3, 0, 2, 3],
                                 ('v2i', (100, 100,
                                          150, 100,
                                          150, 180,
                                          100, 150))
                                 )

@window.event
def on_mouse_motion(x, y, dx, dy):
    print(x, y, dx, dy)


# Drawings
def grid():
    for x in range(0, SCN_WIDTH // GRID_LENGTH):
        for y in range(0, SCN_HEIGHT // GRID_LENGTH):



pyglet.app.run()
