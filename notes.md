Fade(out_time, hold_time, in_time, color="#000")

Returns a transition that takes out_time seconds to fade to a screen filled with color, holds at that screen for hold_time seconds, and then takes in_time to fade to then new screen.

# Fade to black and back.
define fade = Fade(0.5, 0.0, 0.5)

# Hold at black for a bit.
define fadehold = Fade(0.5, 1.0, 0.5)

# Camera flash - quickly fades to white, then back to the scene.
define flash = Fade(0.1, 0.0, 0.5, color="#fff")


https://www.befunky.com/features/blur-image/
