![logo](../img/logo.jpg)

# Assignment - Week 8
We now know about the class structure and Object oriented programming

keywords: class, OOPs

# 1. Bank Account
*Level: Easy*

Let's warm up a bit.

If you have to create a class for handling bank accounts. What are the different `attributes` and `functions` you would create.

Explain the structure of the class definition by writing a template code.

# 2. Ball bounce
*Level: intermediate*

We want to develop a physics engine. As a first step, we want to create a ball, that bouces elastically without stopping.

1. Develop a ball class on pyprocessing and make it bounce in the center of the canvas. It should obey gravity and bounce back to the initial position (center of canvas) without any loss/
2. If we press left or right it should experience a force, that moves it right/left. Keeps on bouncing, if it encounters the left/right edge of the canvas, it treats it as walls bouncing back.

# 3. Tic Tac Toe
*Level: Hard*

Design and implement the Tic Tac Toe game, which can be played from command line.

Hint: One possible implementation uses a `list of lists` to represent the state of the game:

```python
# present state of the game
game = [[1, 2, 0],
        [1, 0, 0],
        [2, 0, 1],
        ]

```

Where 1 represents `O`, 2 represents `X` and 0 represents empty square.

Make atleast two parts:

1. A `game_core` which processes the present state and checks if any player has won or not
2. A simple command line display of the present state. Example:

```
>>>
|  X  |     |  O  |
|     |  O  |  O  |
|     |     |  X  |

Enter next move: _
```

You can make the game be played between two humans or between a computer and a human being.
