Fade(out_time, hold_time, in_time, color="#000")

Returns a transition that takes out_time seconds to fade to a screen filled with color, holds at that screen for hold_time seconds, and then takes in_time to fade to then new screen.

# Fade to black and back.
define fade = Fade(0.5, 0.0, 0.5)

# Hold at black for a bit.
define fadehold = Fade(0.5, 1.0, 0.5)

# Camera flash - quickly fades to white, then back to the scene.
define flash = Fade(0.1, 0.0, 0.5, color="#fff")


https://www.befunky.com/features/blur-image/


screen disableclick(time):
    timer time action Hide("disableclick")
    key "mouseup_1" action NullAction()

label start:
    "dialogue"
    show screen disableclick(3) # pause for three seconds
    "DIALOGUE! {w=3.0}"
    "dialogue"


I only included left click because I'm lazy, but by default, left click, enter, space, and return are bound to CTC. http://www.renpy.org/doc/html/keymap.html#keymap


The characters per second tag sets the speed of text display, for text between the tag and its closing tag. If the argument begins with an asterisk, it's taken as a multiplier to the current text speed. Otherwise, the argument gives the speed to show the text at, in characters per second.

"{cps=20}Fixed Speed{/cps} {cps=*2}Double Speed{/cps}"



show letter_7 at truecenter
with dissolve

hide letter_7
with dissolve



Splash
- [ASSET] Theme song

Intro
- Class selection
- Optimistic Pessimistic increases
- [TODO] Short endings
- [TODO] Letter

Front door
- Empty house

Lounge
- Piano
  - [ASSET] Trillbird
- Window
- Chair

Library
- Gentleman's Guide to Negotiation
  - Possible mention of Marian
- Rory novel
  - [ASSET] Wedding Song
  - [ASSET] Blurred Images
  - Flashback 1
    - Rory relationship exposition and Jimmy's hidden background
    - [TODO] dialogue based on occupation
    - [TODO] travel dialogue
    - [TODO] family at wedding dialogue?
- A Noble Charade

Dining Room
- Table
- Silverware
- Picture

Patio
- Mood dialogue

Kitchen
- Cupboard
  - [TODO] Memory 2 with birthday party
- Drawer with stand mixer
- Whiskey

Upstairs hallway/Balcony
- [TODO] [ASSET] interlude music
- [TODO] [ASSET] Balcony image
- Balcony interlude

Salon
- [TODO] Painting
- Shelf

Gueuloir
  - [TODO] [ASSET] record scratch noise

Conservatory
- Pasiphae play

Study
- [TODO] Safe - OLIVER OPENS IT?!!?!?
- Mess of papers
- [TODO] Picture
  - [TODO] Memory 3 with Oliver
- Check for taricus cult
- Novel 3 relating to Marian's work

Bedroom
- Fan Mail
- Shitty ending where you don't do anything? No redistribution of assets, no publishing of unfinished works?


QUOTES:
Oliver: Do I have to take on his debt? -- he isn't super aware of the reality of death and debt, and also he potentially questions James's situation overall but thinks James generally has it made
